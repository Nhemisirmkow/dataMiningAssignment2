import pandas as pd
import numpy
import random
from datetime import timedelta

data_fraction = 0.2

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
    data_path_result_1 = "./test_chunk_1_dataset_result.csv"
    data_path_result_2 = "./test_chunk_2_dataset_result.csv"
    data_path_result_3 = "./test_chunk_3_dataset_result.csv"
    data_path_result_4 = "./test_chunk_4_dataset_result.csv"
    data_path_result_5 = "./test_chunk_5_dataset_result.csv"

    data_result_1 = pd.read_csv(data_path_result_1)
    data_result_2 = pd.read_csv(data_path_result_2)
    data_result_3 = pd.read_csv(data_path_result_3)
    data_result_4 = pd.read_csv(data_path_result_4)
    data_result_5 = pd.read_csv(data_path_result_5)
    print("Datasets loaded.")
    data_result_1 = data_result_1.append(data_result_2, ignore_index=True)
    data_result_1 = data_result_1.append(data_result_3, ignore_index=True)
    data_result_1 = data_result_1.append(data_result_4, ignore_index=True)
    data_result_1 = data_result_1.append(data_result_5, ignore_index=True)
    print("Datasets merged.")
    data_result_1 = data_result_1.sort_values(by=['srch_id', "predicted_ranking"], ascending=[True,False])
    print("Dataset sorted.")
    data_result_1 = data_result_1[['srch_id', 'prop_id']]
    print("'srch_id' and 'prop_id' column extracted.")

    data_result_1.to_csv("./result.csv", index=False)
