# DVC Demo

This project demonstrates the use of DVC for data version control. Follow the instructions below to set up and run the project.

## First-Time Setup

If you are setting up the project for the first time, you'll need to create a virtual environment and install the required dependencies. Execute the following commands in your terminal:

```bash
git init
dvc init
python -m venv dvcvenv
.\dvcvenv\Scripts\activate
pip install -r .\src\requirements.txt
dvc remote add -d myremote s3://dvc-test-alroy/data
```

## Steps to Run if you Cloned

If you've cloned the project and want to run it, follow these steps:

```bash
python -m venv dvcvenv
.\dvcvenv\Scripts\activate
python -m pip install --upgrade pip 
pip install -r .\src\requirements.txt
git checkout test
dvc pull
```