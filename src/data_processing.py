import pandas as pd
from sklearn.model_selection import train_test_split
import yaml
import os

def data_processing(data_path):
    data = pd.read_csv(data_path)
    processed_Data = data.dropna()
    
    #write your data processing logic which includes data cleaning, feature engineering code
    return processed_Data

if __name__ =="__main__":
    # args = argparse.ArgumentParser()
    # args.add_argument("--param_yaml",default="params.yaml")
    # parsed_args = args.parse_args()
    # data = data_split(param_yaml_path = parsed_args.param_yaml)
    param_yaml_path = "params.yaml"
    with open(param_yaml_path) as yaml_file:
        param_yaml = yaml.safe_load(yaml_file)
    
    train_data_path = os.path.join(param_yaml["split"]["dir"], param_yaml["split"]["train_file"])
    final_train_data = data_processing(data_path = train_data_path)

    os.makedirs(param_yaml["process"]["dir"], exist_ok=True)
    final_train_data_path = os.path.join(param_yaml["process"]["dir"], param_yaml["process"]["train_file"])
    final_train_data.to_csv(final_train_data_path, index=False)

    test_data_path = os.path.join(param_yaml["split"]["dir"], param_yaml["split"]["test_file"])
    final_test_data = data_processing(data_path = test_data_path)
    final_test_data_path = os.path.join(param_yaml["process"]["dir"], param_yaml["process"]["test_file"])
    final_test_data.to_csv(final_test_data_path, index=False)