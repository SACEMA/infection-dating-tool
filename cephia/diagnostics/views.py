from cephia.models import Subject
from diagnostics.models import DiagnosticTestHistory
import logging
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.forms.models import model_to_dict
from collections import OrderedDict
from django.utils import timezone
from django.conf import settings
from diagnostics.forms import SubjectEDDIFilterForm, SubjectEDDIStatusForm
from django.views.decorators.csrf import csrf_exempt
import json
from django.forms import modelformset_factory
from django.core.management import call_command
from pylab import figure, axes, pie, title
from matplotlib.backends.backend_agg import FigureCanvasAgg
import matplotlib


@login_required
def eddi_report(request, template="diagnostics/eddi_report.html"):
    context = {}
    subjects = Subject.objects.all()

    form = SubjectEDDIFilterForm(request.GET or None)
    if form.is_valid():
        subjects = form.filter(subjects)

    context['subjects'] = subjects
    context['form'] = form
    
    return render_to_response(template, context, context_instance=RequestContext(request))

def subject_test_timeline(request, subject_id=None, template="cephia/subject_test_timeline.html"):
    context = {}
    context['subject_id'] = subject_id
    return render_to_response(template, context, context_instance=RequestContext(request))

def subject_timeline_data(request, subject_id=None, template="diagnostics/timeline_data.json"):
    context = {}
    context['tests'] = DiagnosticTestHistory.objects.filter(subject__id=subject_id, ignore=False)
    context['subject'] = Subject.objects.get(pk=subject_id)
    response = render_to_response(template, context, context_instance=RequestContext(request))
    return HttpResponse(json.dumps({'response': response.content}))

@csrf_exempt
@login_required
def eddi_report_detail(request, subject_id=None, template="diagnostics/eddi_report_detail_modal.html"):
    context = {}
    TestHistoryModelFormset = modelformset_factory(DiagnosticTestHistory, fields=('ignore',))
    tests = DiagnosticTestHistory.objects.filter(subject__id=subject_id).order_by('test_date')
    status_form = SubjectEDDIStatusForm(request.POST or None)
    history_formset = TestHistoryModelFormset(request.POST or None, queryset=tests)
    subject = Subject.objects.get(pk=subject_id)

    if request.method == 'POST':
        if status_form.is_valid():
            subject_eddi_status = status_form.save()
            subject.subject_eddi_status = subject_eddi_status
            subject.save()

        if history_formset.is_valid():
            history_formset.save()
            subject.subject_eddi.recalculate = True
            subject.subject_eddi.save()
            
        data = {
            'success': True,
        }
        json_data = json.dumps(data)
        return HttpResponse(json_data, content_type='application/json')
    elif request.method == 'GET':
        if subject.subject_eddi_status:
            status_form = SubjectEDDIStatusForm(initial=subject.subject_eddi_status.model_to_dict())
        
        context['tests'] = tests
        context['status_form'] = status_form
        context['history_formset'] = history_formset
        context['subject'] = subject

    response = render_to_response(template, context, context_instance=RequestContext(request))
    return HttpResponse(json.dumps({'response': response.content}))


def recalculate_eddi(request):
    call_command('eddi_update')
    return HttpResponseRedirect(reverse('diagnostics:eddi_report'))


def test_matplotlib(request):
    f = figure(figsize=(6,6))
    ax = axes([0.1, 0.1, 0.8, 0.8])
    labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
    fracs = [15,30,45, 10]
    explode=(0, 0.05, 0, 0)
    pie(fracs, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True)
    title('Raining Hogs and Dogs', bbox={'facecolor':'0.8', 'pad':5})

    canvas = FigureCanvasAgg(f)    
    response = HttpResponse(content_type='image/png')
    matplotlib.pyplot.close(f)
    canvas.print_png(response)
    return response
