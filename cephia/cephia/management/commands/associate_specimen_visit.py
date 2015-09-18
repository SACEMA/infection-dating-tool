from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone
from cephia.models import Specimen, Visit
import logging

logger = logging.getLogger(__name__)

class Command(BaseCommand):
    help = 'Associate specimen with visits'

    def handle(self, *args, **options):
        num_associations = 0

        for specimen in Specimen.objects.filter(visit=None):
            try:
                visit = Visit.objects.get(subject=specimen.subject, visit_date=specimen.reported_draw_date)
                specimen.visit = visit
                #specimen.source_study = visit.source_study
                specimen.visit_linkage = 'confirmed'
                specimen.save()
            except Visit.DoesNotExist:
                continue

            num_associations = num_associations + 1

        logger.info('Successfully associated "%s" visits with subjects' % num_associations)
