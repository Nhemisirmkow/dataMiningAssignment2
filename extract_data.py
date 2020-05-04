import pandas as pd
import numpy
import random
from datetime import timedelta

percentage = 0.08
train_data_fraction = 0.75

if __name__ == "__main__":
    data_path = "./datasets_raw/training_set_VU_DM.csv"

    data = pd.read_csv(data_path, parse _dates=['date_time'])
    data.set_index(["srch_id"])

    srch_ids = list(set(data['srch_id']))

    random_sample_srch_ids = list(random.sample(srch_ids, int(len(srch_ids) * percentage)))
    extracted_train_srch_ids = list(random.sample(random_sample_srch_ids, int(len(srch_ids) * percentage * train_data_fraction)))
    extracted_test_srch_ids = list(set(random_sample_srch_ids) - set(extracted_train_srch_ids))
    print("sampled")
    extracted_test_srch_ids.sort()
    extracted_train_srch_ids.sort()

    extracted_train_dataset = pd.DataFrame()
    extracted_test_dataset = pd.DataFrame()

    extracted_test_dataset =data.loc[data['srch_id'].isin(extracted_test_srch_ids)]
    print("Extracted test data set.")
    extracted_train_dataset =data.loc[data['srch_id'].isin(extracted_train_srch_ids)]
    print("Extracted train data set.")
    extracted_train_dataset.to_csv("./datasets_preprocessed/extracted_training_dataset.csv")
    extracted_test_dataset.to_csv("./datasets_preprocessed/extracted_test_dataset.csv")
