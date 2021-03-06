from file_handler import FileHandler
from handler_imports import *
import logging
from lib import log_exception

logger = logging.getLogger(__name__)

class IDEV3FileHandler(FileHandler):
    upload_file = None

    def __init__(self, upload_file):
        super(IDEV3FileHandler, self).__init__(upload_file)

        self.registered_columns = [
            'specimen_label',
            'assay',
            'laboratory',
            'test_date',
            'operator',
            'assay_kit_lot',
            'plate_identifier',
            'specimen_purpose',
            'exclusion',
            'interpretation', 
            'test_mode',
            'well_tm',
            'well_v3',
            'tm_OD',
            'v3_OD',
            'tm_ratio_reported',
            'v3_ratio_reported',
            'tm_ratio',
            'v3_ratio',
            'intermediaire_reported',
            'intermediaire',
            'conclusion_reported',
            'conclusion',
            
        ]

    def parse(self):
        from assay.models import IDEV3ResultRow

        rows_inserted = 0
        rows_failed = 0
        

        for row_num in range(self.num_rows):
            try:
                if row_num >= 1:
                    self.header = [ x.strip() for x in self.header ]
                    row_dict = dict(zip(self.header, self.file_rows[row_num]))

                    ide_result_row = IDEV3ResultRow.objects.create(
                        specimen_label = row_dict['specimen_label'],
                        assay = row_dict['assay'],
                        laboratory = row_dict['laboratory'],
                        test_date = row_dict['test_date'],
                        operator = row_dict['operator'],
                        assay_kit_lot = row_dict['assay_kit_lot'],
                        plate_identifier = row_dict['plate_identifier'],
                        specimen_purpose = row_dict['specimen_purpose'],
                        exclusion = row_dict['exclusion'],
                        interpretation = row_dict['interpretation'],
                        test_mode = row_dict['test_mode'],
                        well_tm = row_dict['well_tm'],
                        well_v3 = row_dict['well_v3'],
                        tm_OD = row_dict['tm_OD'],
                        v3_OD = row_dict['v3_OD'],
                        tm_ratio_reported = row_dict['tm_ratio_reported'],
                        v3_ratio_reported = row_dict['v3_ratio_reported'],
                        tm_ratio = row_dict['tm_ratio'],
                        v3_ratio = row_dict['v3_ratio'],
                        intermediaire_reported = row_dict['intermediaire_reported'],
                        intermediaire = row_dict['intermediaire'],
                        conclusion_reported = row_dict['conclusion_reported'],
                        conclusion = row_dict['conclusion'],
                        state='pending',
                        fileinfo=self.upload_file
                    )

                    rows_inserted += 1
            except Exception, e:
                self.upload_file.message = "row " + str(row_num) + ": " + log_exception(e, logger)
                self.upload_file.save()
                return 0, 1

        if rows_failed > 0:
            self.upload_file.state = 'row_error'
        else:
            self.upload_file.state = 'imported'
        fail_msg = 'Failed to import ' + str(rows_failed) + ' rows.'
        success_msg = 'Successfully imported ' + str(rows_inserted) + ' rows.'

        self.upload_file.message += fail_msg + '\n' + success_msg + '\n'
        self.upload_file.save()

    def validate(self, panel_id):
        from cephia.models import Specimen, Panel, Assay
        from assay.models import IDEV3ResultRow, IDEV3Result, PanelMembership

        rows_validated = 0
        rows_failed = 0

        for ide_result_row in IDEV3ResultRow.objects.filter(fileinfo=self.upload_file, state='pending'):
            try:
                error_msg = ''
                # might only need to be used in the future
                panel = Panel.objects.get(pk=panel_id)
                panel_memberships = PanelMembership.objects.filter(panel=panel)
                assay = Assay.objects.get(name=ide_result_row.assay)

                try:
                    Specimen.objects.get(
                        specimen_label=ide_result_row.specimen_label,
                        specimen_type=panel.specimen_type,
                        parent_label__isnull=False
                    )
                except Specimen.DoesNotExist:
                    if ide_result_row.specimen_purpose == 'panel_specimen':
                        error_msg += "Specimen not recognised.\n"

                # if specimen.visit.id not in [ membership.id for membership in panel_memberhsips ]:
                #     error_msg += "Specimen does not belong to any panel membership.\n"

                if error_msg:
                    raise Exception(error_msg)

                ide_result_row.state = 'validated'
                ide_result_row.error_message = ''
                rows_validated += 1
                ide_result_row.save()
            except Exception, e:
                logger.exception(e)
                ide_result_row.state = 'error'
                ide_result_row.error_message = e.message
                rows_failed += 1
                ide_result_row.save()
                continue

        if rows_failed > 0:
            self.upload_file.state = 'row_error'
        else:
            self.upload_file.state = 'validated'
        fail_msg = 'Failed to validate ' + str(rows_failed) + ' rows.'
        success_msg = 'Successfully validated ' + str(rows_validated) + ' rows.'

        self.upload_file.message += fail_msg + '\n' + success_msg + '\n'
        self.upload_file.save()

    def process(self, panel_id, assay_run):
        from cephia.models import Specimen, Laboratory, Assay, Panel
        from assay.models import IDEV3ResultRow, IDEV3Result

        rows_inserted = 0
        rows_failed = 0

        for ide_result_row in IDEV3ResultRow.objects.filter(fileinfo=self.upload_file, state='validated'):
            
            try:
                with transaction.atomic():
                    assay = assay_run.assay
                    panel = Panel.objects.get(pk=panel_id)
                    specimen = Specimen.objects.get(
                        specimen_label=ide_result_row.specimen_label,
                        specimen_type=panel.specimen_type,
                        parent_label__isnull=False
                    )


                    ide_result = IDEV3Result.objects.create(
                        specimen=specimen,
                        assay=assay,
                        laboratory=assay_run.laboratory,
                        test_date=datetime.strptime(ide_result_row.test_date, '%Y-%m-%d').date(),
                        operator=ide_result_row.operator,
                        assay_kit_lot=ide_result_row.assay_kit_lot,
                        plate_identifier=ide_result_row.plate_identifier,
                        test_mode=ide_result_row.test_mode,
                        specimen_purpose=ide_result_row.specimen_purpose,
                        assay_run=assay_run,
                        
                        well_tm=ide_result_row.well_tm,
                        well_v3=ide_result_row.well_v3,
                        tm_OD=ide_result_row.tm_OD,
                        v3_OD=ide_result_row.v3_OD,
                        tm_ratio_reported=ide_result_row.tm_ratio_reported,
                        v3_ratio_reported=ide_result_row.v3_ratio_reported,
                        tm_ratio=ide_result_row.tm_ratio,
                        v3_ratio=ide_result_row.v3_ratio,
                        intermediaire_reported=ide_result_row.intermediaire_reported,
                        intermediaire=ide_result_row.intermediaire,
                        conclusion_reported=ide_result_row.conclusion_reported,
                        conclusion=ide_result_row.conclusion,
                        
                    )

                    IDEV3Result.objects.get(pk=ide_result.pk).calculate_and_save()

                    ide_result_row.state = 'processed'
                    ide_result_row.date_processed = timezone.now()
                    ide_result_row.error_message = ''
                    ide_result_row.idev3_result = ide_result
                    ide_result_row.save()
                    rows_inserted += 1

            except Exception, e:
                ide_result_row.state = 'error'
                ide_result_row.error_message = log_exception(e, logger)
                ide_result_row.save()
                rows_failed += 1
                continue

        if rows_failed > 0:
            self.upload_file.state = 'row_error'
        else:
            self.upload_file.state = 'processed'
        fail_msg = 'Failed to process ' + str(rows_failed) + ' rows.'
        success_msg = 'Successfully processed ' + str(rows_inserted) + ' rows.'

        self.upload_file.message += fail_msg + '\n' + success_msg + '\n'
        self.upload_file.save()
