import pandas as pd
import numpy
import random
from datetime import timedelta

percentage = 0.20
train_data_fraction = 0.9
val_data_fraction = 0.2

if __name__ == "__main__":
    data_path = "./datasets_preprocessed/training_set_VU_DM_added_columns.csv"

    # data = pd.read_csv(data_path, parse_dates=['date_time'])
    data = pd.read_csv(data_path)
    data.set_index(["srch_id"])

    srch_ids = list(set(data['srch_id']))

    random_sample_srch_ids = list(random.sample(srch_ids, int(len(srch_ids) * percentage)))
    extracted_train_srch_ids = list(random.sample(random_sample_srch_ids, int(len(srch_ids) * percentage * train_data_fraction)))
    extracted_test_srch_ids = list(set(random_sample_srch_ids) - set(extracted_train_srch_ids))

    extracted_val_srch_ids = list(random.sample(extracted_train_srch_ids, int(len(extracted_train_srch_ids) * val_data_fraction)))
    extracted_train_srch_ids = list(set(extracted_train_srch_ids) - set(extracted_val_srch_ids))
    print("sampled")

    extracted_test_srch_ids.sort()
    extracted_train_srch_ids.sort()
    extracted_val_srch_ids.sort()

    extracted_train_dataset = pd.DataFrame()
    extracted_test_dataset = pd.DataFrame()
    extracted_val_dataset = pd.DataFrame()

    extracted_test_dataset =data.loc[data['srch_id'].isin(extracted_test_srch_ids)]
    print("Extracted test data set.")
    extracted_train_dataset =data.loc[data['srch_id'].isin(extracted_train_srch_ids)]
    print("Extracted train data set.")
    extracted_val_dataset =data.loc[data['srch_id'].isin(extracted_val_srch_ids)]
    print("Extracted val data set.")
    extracted_train_dataset.to_csv("./datasets_preprocessed/extracted_training_dataset.csv", index=False)
    print("Saved train data set.")
    extracted_test_dataset.to_csv("./datasets_preprocessed/extracted_test_dataset.csv", index=False)
    print("Saved test data set.")
    extracted_val_dataset.to_csv("./datasets_preprocessed/extracted_val_dataset.csv", index=False)
    print("Saved val data set.")
