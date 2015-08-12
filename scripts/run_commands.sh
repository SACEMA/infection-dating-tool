 #!/bin/bash
BASE_DIR="`dirname \"$0\"`/.."
cd $BASE_DIR

ROOT=$(pwd)
cd ${ROOT}

SRC=${ROOT}/cephia
SITE_PATH=${SRC}                                                                                                                                                            
VENV=${ROOT}/venv

echo "activate virtualenv"
cd ${VENV}
. ./bin/activate
if [ $? != 0 ]; then
    echo "failed to activate virtualenv at ${VENV}: ABORTING"
    exit 1
fi
cd -

cd ${SITE_PATH}
python manage.py import_pending_files --settings=cephia.management_settings
python manage.py process_imported_files --settings=cephia.management_settings
python manage.py associate_subject_visit --settings=cephia.management_settings
python manage.py associate_specimen_visit --settings=cephia.management_settings