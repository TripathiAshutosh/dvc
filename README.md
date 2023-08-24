DVC demo

- python -m venv dvcvenv
- .\dvcvenv\Scripts\activate
- pip install -r .\src\requirements.txt
- dvc remote add -d myremote s3://dvc-test-alroy/data

- change in exp
- dvc repro
- dvc status -c
