# **Reproducible Data and ML Pipeline using DVC - Live Demo**


## Step by step Explaination:

<a href="http://www.youtube.com/watch?feature=player_embedded&v=0fZsYTGoH0A" target="_blank"><img src="http://img.youtube.com/vi/0fZsYTGoH0A/0.jpg" 
alt="MLFlow Live Demo" width="500" height="315" border="10" /></a>

**Source Code Credit: `wget https://code.dvc.org/get-started/code.zip`. It is used to explain how to create DVC data and ML pipeline and run reproducible pipelines.**

### 1. Create Conda environment

1. `conda create -n mlops python=3.9 ipykernel` 
it will create a conda env named mlops and install python version 3.9 and a ipykernel inside this environment

2. Activate the environment
`conda activate mlops`

3. add newly created environment to the notebook as kernel
`python -m ipykernel install --user --name=mlops` 

4. install notebook inside the environment
`pip install notebook`

5. Now install all required dependencies to run this notebook

   * clone this repository and then use requirements.txt file to install the dependencies or you can install independently like below:

* `pip install dvclive>=3.0`
* `pip install pandas`
* `pip install pyaml`
* `pip install scikit-learn>=1.3`
* `pip install scipy`
* `pip install matplotlib`
* `pip install dvc-gs`

Now open the notebook using below command:

`jupyter notebook`

#### Open Text Classification notebook and go thorugh the code. `text_classification.ipynb`
This code is what we as a data scientist write in the notebook. But this can not go to the production as it is. So from here onwards we are going to convert this code in pipeline way so that we can deploy this pipeline and reproduce it whenever required.

### Now time to switch from Jupyter notebook to a proper IDE. you can use VS code or PyCharm.
So, clone this repository and go to Data and ML Pipline folder (as there are different folder at parent level explaining different features of DVC)
Activate conda environment from within the vs code terminal. conda env you have already created, if not then please create like described above and install all the dependencies using `pip install -r src/requirements.txt` file

At this stage the folder structure at your machine should look like as below:

![image](https://github.com/user-attachments/assets/26811fc7-1b98-412a-a727-20e369269d43)

Now our initial project structure is ready. Inside src folder it is the same code base which you have seen in the text_classification notebook but in more structured way.
you can refer the video to understand more about it.

Now it is time to stack all py files as a pipeline steps.
To run them as a pipeline and reproduce them whenever required, it is desired to pass all parameters including hyper-parameter values via a yaml file you can name it as a `params.yaml`
So the idea is if you want to update any parameter just update in the paramsyaml and reproduce the pipeline output. then it will execute only that particular step of the pipeline which is affected by this parameter change and other steps will be skipped which saves the resource cost significantly.

So now if you have done above things then lets run some command to put together everything in pipeline.

### Pipeline Creation

#### **Command 1**
From inside the project folder run below commands.
* `git init` #initialize the git repo
* `dvc init` #initialize the dvc repo to version data and also for pipeline stuff
* `dvc remote add myremote <remote directory path ex. gs://gs_bucket_name/>`

<a href="http://www.youtube.com/watch?feature=player_embedded&v=kAg4TO03slA" target="_blank"><img src="http://img.youtube.com/vi/kAg4TO03slA/0.jpg" 
alt="MLFlow Live Demo" width="500" height="315" border="10" /></a>

#### **Command 2**
* `dvc add data/data.xml`
#### **Command 3**
* `git add --all`
* `git commit -m "initial commit"`
#### **Command 4**
`dvc stage add -n prepare \
                -p prepare.seed,prepare.split \
                -d src/prepare.py -d data/data.xml \
                -o data/prepared \
                python src/prepare.py data/data.xml`
                
This will create the first stage named prepare in the pipeline and will put parameters seed and split ratio to the dvc.yaml file and create a folder named prepared inside data folder. While executing this will accept arguement data/data.xml file. [For detailed explaination please refer the video link mentioned at the top]

#### **Command 5**
`dvc stage add -n featurize \
                -p featurize.max_features,featurize.ngrams \
                -d src/featurization.py -d data/prepared \
                -o data/features \
                python src/featurization.py data/prepared data/features`

 Similar to the above command it will create next stage as featurize and output the genrated features in the new folder featured created inside data folder.

#### **Command 6**
`dvc stage add -n train \
                -p train.seed,train.n_est,train.min_split \
                -d src/train.py -d data/features \
                -o model.pkl \
                python src/train.py data/features model.pkl`

This command will create the train stage in the pipeline and once pipeline executes it will create model.pkl file.

#### **Command 7**
* `git add .--all`
* `git commit -m "pipeline defined"`\

## Reproducing
#### **Command 8**

`dvc repro`

#### **command 9**
* `git add dvc.lock`
* `git commit -m "first pipeline repro"`


### Next Steps, 
as explained in the video tutoria, change some of the parameters value in the `params.yaml` file and re run the `dvc repro` command and observe the output at terminal.

