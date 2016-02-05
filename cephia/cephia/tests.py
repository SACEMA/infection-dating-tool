import logging
from cephia.test_helper.test_base import TestBase
from cephia.models import *
from django.core.management import call_command

logger = logging.getLogger(__name__)

class TestCase001(TestBase):
    def setUp(self):
        super(TestCase001, self).setUp()
        
        self.subjects = self.create_fileinfo('subject.xlsx', 'test_case_001')
        self.visits = self.create_fileinfo('visit.xlsx', 'test_case_001')
        self.transfer_ins = self.create_fileinfo('transfer_in.xlsx', 'test_case_001')
        self.aliquots = self.create_fileinfo('aliquot.xlsx', 'test_case_001')
        self.transfer_outs = self.create_fileinfo('transfer_out.xlsx', 'test_case_001')

        
    def test_case_001(self):
        self.subjects.get_handler().parse()
        self.assertEqual(1, SubjectRow.objects.filter(fileinfo=self.subjects, state='pending').count())

        self.subjects.get_handler().validate()
        self.assertEqual(1, SubjectRow.objects.filter(fileinfo=self.subjects, state='validated').count())

        self.subjects.get_handler().process()
        self.assertEqual(1, SubjectRow.objects.filter(fileinfo=self.subjects, state='processed').count())
        self.assertEqual(1, Subject.objects.all().count())

        self.visits.get_handler().parse()
        self.assertEqual(2, VisitRow.objects.filter(fileinfo=self.visits, state='pending').count())

        self.visits.get_handler().validate()
        self.assertEqual(2, VisitRow.objects.filter(fileinfo=self.visits, state='validated').count())

        self.visits.get_handler().process()
        self.assertEqual(2, VisitRow.objects.filter(fileinfo=self.visits, state='processed').count())
        self.assertEqual(2, Visit.objects.all().count())

        call_command('associate_subject_visit')
        self.assertEqual(Visit.objects.all().count(), Visit.objects.filter(subject__isnull=False).count())
        
        self.transfer_ins.get_handler().parse()
        self.assertEqual(2, TransferInRow.objects.filter(fileinfo=self.transfer_ins, state='pending').count())

        self.transfer_ins.get_handler().validate()
        self.assertEqual(2, TransferInRow.objects.filter(fileinfo=self.transfer_ins, state='validated').count())

        self.transfer_ins.get_handler().process()
        self.assertEqual(2, TransferInRow.objects.filter(fileinfo=self.transfer_ins, state='processed').count())
        self.assertEqual(2, Specimen.objects.all().count())

        call_command('associate_specimen_subject')
        self.assertEqual(Specimen.objects.all().count(), Specimen.objects.filter(subject__isnull=False).count())
        
        call_command('associate_specimen_visit')
        self.assertEqual(Specimen.objects.all().count(), Specimen.objects.filter(visit__isnull=False).count())

        self.aliquots.get_handler().parse()
        self.assertEqual(7, AliquotRow.objects.filter(fileinfo=self.aliquots, state='pending').count())

        self.aliquots.get_handler().validate()
        self.assertEqual(7, AliquotRow.objects.filter(fileinfo=self.aliquots, state='validated').count())

        self.aliquots.get_handler().process()
        self.assertEqual(7, AliquotRow.objects.filter(fileinfo=self.aliquots, state='processed').count())
        self.assertEqual(7, Specimen.objects.all().count())

        call_command('parent_child_inheritance')
        self.assertEqual(Specimen.objects.all().count(), Specimen.objects.filter(visit__isnull=False).count())
        
        self.transfer_outs.get_handler().parse()
        self.assertEqual(5, TransferOutRow.objects.filter(fileinfo=self.transfer_outs, state='pending').count())

        self.transfer_outs.get_handler().validate()
        self.assertEqual(5, TransferOutRow.objects.filter(fileinfo=self.transfer_outs, state='validated').count())

        self.transfer_outs.get_handler().process()
        self.assertEqual(5, TransferOutRow.objects.filter(fileinfo=self.transfer_outs, state='processed').count())
        self.assertEqual(7, Specimen.objects.all().count())

        self.assertEqual(5, Specimen.objects.filter(shipped_to__isnull=False).count())

        self.assertEqual(6, Specimen.objects.filter(is_available=False).count())


class TestCase002(TestBase):
    def setUp(self):
        super(TestCase002, self).setUp()

        self.subjects = self.create_fileinfo('subject.docx', 'test_case_002')

    def test_case_002(self):
        try:
            handler = self.subjects.get_handler()
        except Exception, e:
            self.assertEqual("Invalid file type. Only .csv and .xls/x are supported.", e.message)


class TestCase003(TestBase):
    def setUp(self):
        super(TestCase003, self).setUp()

        self.subjects = self.create_fileinfo('subject.xlsx', 'test_case_003')
        self.visits = self.create_fileinfo('visit.xlsx', 'test_case_003')

    def test_case_003(self):
        self.subjects.get_handler().parse()
        self.subjects.get_handler().validate()
        self.subjects.get_handler().process()
        self.visits.get_handler().parse()
        self.visits.get_handler().validate()
        self.visits.get_handler().process()

        call_command('associate_subject_visit')

        self.assertEqual(1, Visit.objects.filter(subject__isnull=False).count())
        self.assertEqual(1, Visit.objects.filter(subject__isnull=True).count())

class TestSpecimenVisitExactMatch(TestBase):
    def setUp(self):
        super(TestSpecimenVisitExactMatch, self).setUp()

        self.subjects = self.create_fileinfo('subject.xlsx', 'test_case_004')
        self.visits = self.create_fileinfo('visit.xlsx', 'test_case_004')
        self.transfer_ins = self.create_fileinfo('transfer_in.xlsx', 'test_case_004')

    def test_exact_matches(self):
        self.subjects.get_handler().parse()
        self.subjects.get_handler().validate()
        self.subjects.get_handler().process()
        self.visits.get_handler().parse()
        self.visits.get_handler().validate()
        self.visits.get_handler().process()
        self.transfer_ins.get_handler().parse()
        self.transfer_ins.get_handler().validate()
        self.transfer_ins.get_handler().process()

        call_command('associate_subject_visit')
        call_command('associate_specimen_subject')
        call_command('associate_specimen_visit')

        self.assertEqual(2, Specimen.objects.filter(subject__isnull=False).count())
        self.assertEqual(1, Specimen.objects.filter(visit__isnull=False).count())
        self.assertEqual(1, Specimen.objects.filter(specimen_label='AS10-10544', visit__isnull=False).count())
        self.assertEqual(1, Specimen.objects.filter(specimen_label='AS11-08365', visit__isnull=True).count())


class TestSpecimenVisitApproximateMatch(TestBase):
    def setUp(self):
        super(TestSpecimenVisitApproximateMatch, self).setUp()

        self.subjects = self.create_fileinfo('subject.xlsx', 'test_case_005')
        self.visits = self.create_fileinfo('visit.xlsx', 'test_case_005')
        self.transfer_ins = self.create_fileinfo('transfer_in.xlsx', 'test_case_005')
        
    def test_approximate_matches(self):
        self.subjects.get_handler().parse()
        self.subjects.get_handler().validate()
        self.subjects.get_handler().process()
        self.visits.get_handler().parse()
        self.visits.get_handler().validate()
        self.visits.get_handler().process()
        self.transfer_ins.get_handler().parse()
        self.transfer_ins.get_handler().validate()
        self.transfer_ins.get_handler().process()
        
        call_command('associate_subject_visit')
        call_command('associate_specimen_subject')
        call_command('associate_specimen_visit')

        self.assertEqual(Visit.objects.get(visit_date='2014-11-10').pk, Specimen.objects.get(specimen_label='AS10-10544').visit.pk)
        self.assertEqual(Visit.objects.get(visit_date='2014-12-01').pk, Specimen.objects.get(specimen_label='AS11-08365').visit.pk)
        self.assertEqual(Visit.objects.get(visit_date='2014-12-01').pk, Specimen.objects.get(specimen_label='AS11-08366').visit.pk)
        self.assertEqual(Visit.objects.get(visit_date='2014-07-01').pk, Specimen.objects.get(specimen_label='AS11-08367').visit.pk)

class TestVolumeArithmetic(TestBase):
    def setUp(self):
        super(TestVolumeArithmetic, self).setUp()

        self.transfer_ins = self.create_fileinfo('transfer_in.xlsx', 'test_case_006')
        self.aliquots = self.create_fileinfo('aliquot.xlsx', 'test_case_006')

    def test_transferin_volume_rollup(self):
        self.transfer_ins.get_handler().parse()
        self.transfer_ins.get_handler().validate()
        self.transfer_ins.get_handler().process()

        self.assertEqual(1, Specimen.objects.filter(specimen_label='AS10-10544').count())
        self.assertEqual(4, Specimen.objects.get(specimen_label='AS10-10544').number_of_containers)
        self.assertEqual(10000, Specimen.objects.get(specimen_label='AS10-10544').initial_claimed_volume)

    def test_transferin_multicontainer_volume(self):
        self.transfer_ins.get_handler().parse()
        self.transfer_ins.get_handler().validate()
        self.transfer_ins.get_handler().process()

        self.assertEqual(1, Specimen.objects.filter(specimen_label='AS10-10545').count())
        self.assertEqual(4, Specimen.objects.get(specimen_label='AS10-10545').number_of_containers)
        self.assertEqual(4000, Specimen.objects.get(specimen_label='AS10-10545').initial_claimed_volume)

    def test_transferin_rollup_and_multicontainer_volume(self):
        self.transfer_ins.get_handler().parse()
        self.transfer_ins.get_handler().validate()
        self.transfer_ins.get_handler().process()

        self.assertEqual(1, Specimen.objects.filter(specimen_label='AS10-10546').count())
        self.assertEqual(5, Specimen.objects.get(specimen_label='AS10-10546').number_of_containers)
        self.assertEqual(4600, Specimen.objects.get(specimen_label='AS10-10546').initial_claimed_volume)

    def test_aliquot_volume_update(self):
        self.transfer_ins.get_handler().parse()
        self.transfer_ins.get_handler().validate()
        self.transfer_ins.get_handler().process()
        self.aliquots.get_handler().parse()
        self.aliquots.get_handler().validate()
        self.aliquots.get_handler().process()

        self.assertEqual(1, Specimen.objects.filter(specimen_label='AS10-10544').count())
        self.assertEqual(10000, Specimen.objects.get(specimen_label='AS10-10544').initial_claimed_volume)
        self.assertEqual(8500, Specimen.objects.get(specimen_label='AS10-10544').volume)
        self.assertEqual(250, Specimen.objects.get(specimen_label='1234-01').volume)

        #import pdb; pdb.set_trace()

class TestEDDICalculation(TestBase):
    
    def setUp(self):
        super(TestEDDICalculation, self).setUp()
        
        #import pdb; pdb.set_trace()

        self.subjects = self.create_fileinfo('subject.xlsx', 'test_case_008_eddi')
        self.visits = self.create_fileinfo('visit.xlsx', 'test_case_008_eddi')
        self.diagnostic_test = self.create_fileinfo('diagnostic_tests.xlsx','test_case_008_eddi')
        self.test_property = self.create_fileinfo('tests_properties.xlsx','test_case_008_eddi')
        self.protocol_lookup = self.create_fileinfo('lookup.xlsx','test_case_008_eddi')
        self.test_history =  self.create_fileinfo('test_history.xlsx','test_case_008_eddi')

        #import pdb; pdb.set_trace()

    def test_case_001(self):
        self.subjects.get_handler().parse()
        self.subjects.get_handler().validate()
        self.subjects.get_handler().process()

        self.visits.get_handler().parse()
        self.visits.get_handler().validate()
        self.visits.get_handler().process()
        
        self.assertEqual(1, Subject.objects.all().count())
        self.assertEqual(2, Visit.objects.all().count())

        call_command('associate_subject_visit')
        self.assertEqual(Visit.objects.all().count(), Visit.objects.filter(subject__isnull=False).count())
        #import pdb; pdb.set_trace()


        self.diagnostic_test.get_handler().process()
        self.assertEqual(5, DiagnosticTest.objects.all().count())
        
        self.test_property.get_handler().process()
        self.assertEqual(8, TestPropertyEstimate.objects.all().count())

        self.protocol_lookup.get_handler().process()
        self.assertEqual(6, ProtocolLookup.objects.all().count())
        
        self.test_history.get_handler().parse()
        self.assertEqual(6, DiagnosticTestHistoryRow.objects.all().count())
        self.assertEqual(6, DiagnosticTestHistoryRow.objects.filter(fileinfo=self.test_history, state='pending').count())

        self.test_history.get_handler().validate()
        self.assertEqual(6, DiagnosticTestHistoryRow.objects.filter(fileinfo=self.test_history, state='validated').count())

        self.test_history.get_handler().process()
        self.assertEqual(6, DiagnosticTestHistoryRow.objects.filter(fileinfo=self.test_history, state='processed').count())
        self.assertEqual(6, DiagnosticTestHistory.objects.all().count())

                
        call_command('eddi_update')
        self.assertEqual(1, SubjectEDDI.objects.all().count())
        self.assertEqual(1, Subject.objects.filter(subject_eddi__isnull=False).count())
        self.assertEqual(2, VisitEDDI.objects.all().count())
        self.assertEqual(2, Visit.objects.filter(visit_eddi__isnull=False).count())
        
        # add check that dates are correct
        # add check that VDW size is correct
        
