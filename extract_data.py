import pandas as pd
import numpy
import random
from datetime import timedelta

percentage = 0.2
train_data_fraction = 0.6
percentage = 1
train_data_fraction = 0.7
val_data_fraction = (1 - train_data_fraction) / 5

def saveQueryDataset(name, data):
    srch_ids = data.srch_id.unique()

    query_temp = {}
    count = 0
    last_progress = -5
    data_srch_id = data[['srch_id']]
    for i in srch_ids:
        query_temp[i] = data_srch_id.loc[data_srch_id['srch_id'] == i].shape[0]
        count += 1
        progress = round(count / len(srch_ids) * 100, 2)
        if int(progress * 100) % 500 == 0 and progress > last_progress + 4:
            last_progress = progress
            print(progress, "%")
    query_train = list(query_temp.items())
    query_train.sort()
    query_train = [x for (_, x) in query_train]
    query_train_pandas = pd.Series(query_train)
    query_train_pandas.to_csv("./datasets_preprocessed/"+name+"_group_size.csv")
    print("Finished SaveQueryDataset: " + name)

if __name__ == "__main__":
    # data_path = "./datasets_preprocessed/training_set_VU_DM_without_nan.csv"
    # data_path = "./Baptiste_datasets/2/training_data_2.csv"
    data_path = "./Baptiste_datasets/3/training_set_3.csv"

    # data = pd.read_csv(data_path, parse_dates=['date_time'])
    data = pd.read_csv(data_path)
    print("Dataset loaded.")
    # data.set_index(["srch_id"])

    srch_ids = list(set(data['srch_id']))

    print("Sampling...")
    random_sample_srch_ids = list(random.sample(srch_ids, int(len(srch_ids) * percentage)))

    extracted_val_1_srch_ids = list(random.sample(random_sample_srch_ids, int(len(random_sample_srch_ids) * val_data_fraction)))
    extracted_train_srch_ids = list(set(random_sample_srch_ids) - set(extracted_val_1_srch_ids))

    extracted_val_2_srch_ids = list(random.sample(extracted_train_srch_ids, int(len(random_sample_srch_ids) * val_data_fraction)))
    extracted_train_srch_ids = list(set(extracted_train_srch_ids) - set(extracted_val_2_srch_ids))

    extracted_val_3_srch_ids = list(random.sample(extracted_train_srch_ids, int(len(random_sample_srch_ids) * val_data_fraction)))
    extracted_train_srch_ids = list(set(extracted_train_srch_ids) - set(extracted_val_3_srch_ids))

    extracted_val_4_srch_ids = list(random.sample(extracted_train_srch_ids, int(len(random_sample_srch_ids) * val_data_fraction)))
    extracted_train_srch_ids = list(set(extracted_train_srch_ids) - set(extracted_val_4_srch_ids))

    extracted_val_5_srch_ids = list(random.sample(extracted_train_srch_ids, int(len(random_sample_srch_ids) * val_data_fraction)))
    extracted_train_srch_ids = list(set(extracted_train_srch_ids) - set(extracted_val_5_srch_ids))
    print("sampled")

    print("sorting:")
    # extracted_test_srch_ids.sort()
    # print("test set finished")
    extracted_train_srch_ids.sort()
    print("train set finished")
    extracted_val_1_srch_ids.sort()
    print("Val 1 set finished")
    extracted_val_2_srch_ids.sort()
    print("Val 2 set finished")
    extracted_val_3_srch_ids.sort()
    print("Val 3 set finished")
    extracted_val_4_srch_ids.sort()
    print("Val 4 set finished")
    extracted_val_5_srch_ids.sort()
    print("Val 5 set finished")
    print("sorted")

    extracted_train_dataset = pd.DataFrame()
    extracted_val_1_dataset = pd.DataFrame()
    extracted_val_2_dataset = pd.DataFrame()
    extracted_val_3_dataset = pd.DataFrame()
    extracted_val_4_dataset = pd.DataFrame()
    extracted_val_5_dataset = pd.DataFrame()

    extracted_train_dataset =data.loc[data['srch_id'].isin(extracted_train_srch_ids)]
    print("Extracted train data set.")
    extracted_val_1_dataset =data.loc[data['srch_id'].isin(extracted_val_1_srch_ids)]
    print("Extracted val data set.")
    extracted_val_2_dataset =data.loc[data['srch_id'].isin(extracted_val_2_srch_ids)]
    print("Extracted val data set.")
    extracted_val_3_dataset =data.loc[data['srch_id'].isin(extracted_val_3_srch_ids)]
    print("Extracted val data set.")
    extracted_val_4_dataset =data.loc[data['srch_id'].isin(extracted_val_4_srch_ids)]
    print("Extracted val data set.")
    extracted_val_5_dataset =data.loc[data['srch_id'].isin(extracted_val_5_srch_ids)]
    print("Extracted val data set.")


    extracted_train_dataset.to_csv("./datasets_preprocessed/extracted_training_dataset.csv", index=False)
    print("Saved train data set.")
    extracted_val_1_dataset.to_csv("./datasets_preprocessed/extracted_val_1_dataset.csv", index=False)
    print("Saved val 1 data set.")
    extracted_val_2_dataset.to_csv("./datasets_preprocessed/extracted_val_2_dataset.csv", index=False)
    print("Saved val 2 data set.")
    extracted_val_3_dataset.to_csv("./datasets_preprocessed/extracted_val_3_dataset.csv", index=False)
    print("Saved val 3 data set.")
    extracted_val_4_dataset.to_csv("./datasets_preprocessed/extracted_val_4_dataset.csv", index=False)
    print("Saved val 4 data set.")
    extracted_val_5_dataset.to_csv("./datasets_preprocessed/extracted_val_5_dataset.csv", index=False)
    print("Saved val 5 data set.")

    saveQueryDataset("extracted_training_dataset", extracted_train_dataset)
    saveQueryDataset("extracted_val_1_dataset", extracted_val_1_dataset)
    saveQueryDataset("extracted_val_2_dataset", extracted_val_2_dataset)
    saveQueryDataset("extracted_val_3_dataset", extracted_val_3_dataset)
    saveQueryDataset("extracted_val_4_dataset", extracted_val_4_dataset)
    saveQueryDataset("extracted_val_5_dataset", extracted_val_5_dataset)
