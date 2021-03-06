from file_handler import FileHandler
from handler_imports import *
import logging

logger = logging.getLogger(__name__)

class LSVitrosDiluentFileHandler(FileHandler):
    upload_file = None

    def __init__(self, upload_file):
        super(LSVitrosDiluentFileHandler, self).__init__(upload_file)

        self.registered_columns = ["specimen_label",
                                   "assay",
                                   "laboratory",
                                   "test_date",
                                   "operator",
                                   "assay_kit_lot",
                                   "plate_identifier",
                                   "well",
                                   "test_mode",
                                   "specimen_purpose",
                                   "SCO",
                                   "panel"]

        self.assay_name = 'LSVitros-Diluent'


    def parse(self):
        from assay.models import LSVitrosDiluentResultRow

        rows_inserted = 0
        rows_failed = 0

        self.header = [ x.strip() for x in self.header ]

        for row_num in range(self.num_rows):
            try:
                if row_num >= 1:
                    row_dict = dict(zip(self.header, self.file_rows[row_num]))

                    lsvitros_result_row = LSVitrosDiluentResultRow.objects.create(specimen_label=row_dict['specimen_label'],
                                                                                  assay=row_dict['assay'],
                                                                                  laboratory=row_dict['laboratory'],
                                                                                  test_date=row_dict['test_date'],
                                                                                  operator=row_dict['operator'],
                                                                                  assay_kit_lot=row_dict['assay_kit_lot'],
                                                                                  plate_identifier=row_dict['plate_identifier'],
                                                                                  well=row_dict['well'],
                                                                                  test_mode=row_dict['test_mode'],
                                                                                  specimen_purpose=row_dict['specimen_purpose'],
                                                                                  SCO=row_dict['SCO'],
                                                                                  state='pending',
                                                                                  fileinfo=self.upload_file)



                    rows_inserted += 1
            except Exception, e:
                logger.exception(e)
                self.upload_file.message = "row " + str(row_num) + ": " + e.message
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
        from assay.models import LSVitrosDiluentResultRow, LSVitrosDiluentResult, PanelMembership

        rows_validated = 0
        rows_failed = 0

        for lsvitros_result_row in LSVitrosDiluentResultRow.objects.filter(fileinfo=self.upload_file, state='pending'):
            try:
                error_msg = ''
                panel = Panel.objects.get(pk=panel_id)

                try:
                    specimen = Specimen.objects.get(specimen_label=lsvitros_result_row.specimen_label,
                                                    specimen_type=panel.specimen_type,
                                                    parent_label__isnull=False)
                except Specimen.DoesNotExist:
                    if lsvitros_result_row.specimen_purpose == 'panel_specimen':
                        error_msg += "Specimen not recognised.\n"

                if error_msg:
                    raise Exception(error_msg)

                lsvitros_result_row.state = 'validated'
                lsvitros_result_row.error_message = ''
                rows_validated += 1
                lsvitros_result_row.save()
            except Exception, e:
                logger.exception(e)
                lsvitros_result_row.state = 'error'
                lsvitros_result_row.error_message = e.message
                rows_failed += 1
                lsvitros_result_row.save()
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
        from assay.models import (LSVitrosDiluentResultRow, LSVitrosDiluentResult,
                                  AssayResult, PanelMembership)

        rows_inserted = 0
        rows_failed = 0

        assay = Assay.objects.get(name=self.assay_name)
        panel = Panel.objects.get(pk=panel_id)
        panel_memberhsips = PanelMembership.objects.filter(panel=panel)
        panel_memberhsip_ids = [ membership.id for membership in panel_memberhsips ]

        for lsvitros_result_row in LSVitrosDiluentResultRow.objects.filter(fileinfo=self.upload_file, state='validated'):
            try:
                warning_msg = ''

                with transaction.atomic():
                    specimen = None
                    try:
                        specimen = Specimen.objects.get(specimen_label=lsvitros_result_row.specimen_label,
                                                        specimen_type=panel.specimen_type,
                                                        parent_label__isnull=False)
                    except Specimen.DoesNotExist:
                        warning_msg += "Specimen not recognised.\n"

                    # if specimen.visit.id not in panel_memberhsip_ids:
                    #     warning_msg += "Specimen does not belong to any panel membership.\n"

                    lsvitros_result = LSVitrosDiluentResult.objects.create(specimen=specimen,
                                                                           assay=assay,
                                                                           laboratory=Laboratory.objects.get(name=lsvitros_result_row.laboratory),
                                                                           test_date=datetime.strptime(lsvitros_result_row.test_date, '%Y-%m-%d').date(),
                                                                           operator=lsvitros_result_row.operator,
                                                                           assay_kit_lot=lsvitros_result_row.assay_kit_lot,
                                                                           plate_identifier=lsvitros_result_row.plate_identifier,
                                                                           test_mode=lsvitros_result_row.test_mode,
                                                                           well=lsvitros_result_row.well,
                                                                           specimen_purpose=lsvitros_result_row.specimen_purpose,
                                                                           SCO=lsvitros_result_row.SCO,
                                                                           assay_run=assay_run)

                    lsvitros_result_row.state = 'processed'
                    lsvitros_result_row.date_processed = timezone.now()
                    lsvitros_result_row.error_message = ''
                    lsvitros_result_row.lsvitros_diluent_result = lsvitros_result
                    lsvitros_result_row.save()
                    rows_inserted += 1

            except Exception, e:
                logger.exception(e)
                lsvitros_result_row.state = 'error'
                lsvitros_result_row.error_message = e.message
                lsvitros_result_row.save()
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
