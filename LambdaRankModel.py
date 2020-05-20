import pandas as pd
import numpy as np
import random
from datetime import timedelta, datetime
import lightgbm as lgb
from sklearn.model_selection import train_test_split

forbidden_columns = []

if __name__ == "__main__":
    data_path_train = "./datasets_preprocessed/extracted_training_dataset.csv"

    # data_path_test = "./datasets_preprocessed/extracted_test_dataset.csv"
    data_path_test = "./datasets_preprocessed/test_set_VU_DM_added_columns.csv"
    # data_path_test = "./Baptiste_datasets/2/test_data_2.csv"

    data_path_val_1 = "./datasets_preprocessed/extracted_val_1_dataset.csv"
    data_path_val_2 = "./datasets_preprocessed/extracted_val_2_dataset.csv"
    data_path_val_3 = "./datasets_preprocessed/extracted_val_3_dataset.csv"
    data_path_val_4 = "./datasets_preprocessed/extracted_val_4_dataset.csv"
    data_path_val_5 = "./datasets_preprocessed/extracted_val_5_dataset.csv"

    gbm = lgb.LGBMRanker(learning_rate=0.13,
                         n_estimators=300,
                         num_leaves = 31,
                         min_child_weight = 0.1,
                         reg_alpha = 2,
                         reg_lambda = 5,
                         subsample = 0.855,
                         colsample_bytree=0.9234,
                         boosting_type="goss",
                         min_child_samples=399,
                         importance_type="gain",
                         )

    data_train = pd.read_csv(data_path_train, index_col=False)
    print(data_train.shape[0])
    print("Training dataset loaded.")


    if 'rank_score' in data_train.columns:
        y_train = data_train.pop("rank_score")
    if 'label' in data_train.columns:
        y_train = data_train.pop("label")
    if ('Unnamed: 0' in data_train.columns):
        data_train.pop('Unnamed: 0')
    if "date_time" in data_train.columns:
        data_train.pop("date_time")
    if "position" in data_train.columns:
        data_train.pop("position")
    for name in forbidden_columns:
        if name in data_train.columns:
            data_train.pop(name)
    X_train = data_train

    query_train_pandas = pd.read_csv("./datasets_preprocessed/extracted_training_dataset_group_size.csv")['0']
    query_train = list(query_train_pandas)

    print("Training dataset prepared.")


    data_val_1 = pd.read_csv(data_path_val_1, index_col=False)
    print("Val 1 dataset loaded.")


    if 'rank_score' in data_val_1.columns:
        y_val_1 = data_val_1.pop("rank_score")
    if 'label' in data_val_1.columns:
        y_val_1 = data_val_1.pop("label")
    if ('Unnamed: 0' in data_val_1.columns):
        data_val_1.pop('Unnamed: 0')
    if "date_time" in data_val_1.columns:
        data_val_1.pop("date_time")
    if "position" in data_val_1.columns:
        data_val_1.pop("position")
    for name in forbidden_columns:
        if name in data_val_1.columns:
            data_val_1.pop(name)
    X_val_1 = data_val_1

    query_val_1_pandas = pd.read_csv("./datasets_preprocessed/extracted_val_1_dataset_group_size.csv")['0']
    query_val_1 = list(query_val_1_pandas)

    print("Val 1 dataset prepared.")


    data_val_2 = pd.read_csv(data_path_val_2, index_col=False)
    print("Val 2 dataset loaded.")

    if 'rank_score' in data_val_2.columns:
        y_val_2 = data_val_2.pop("rank_score")
    if 'label' in data_val_2.columns:
        y_val_2 = data_val_2.pop("label")
    if ('Unnamed: 0' in data_val_2.columns):
        data_val_2.pop('Unnamed: 0')
    if "date_time" in data_val_2.columns:
        data_val_2.pop("date_time")
    if "position" in data_val_2.columns:
        data_val_2.pop("position")
    for name in forbidden_columns:
        if name in data_val_2.columns:
            data_val_2.pop(name)
    X_val_2 = data_val_2

    query_val_2_pandas = pd.read_csv("./datasets_preprocessed/extracted_val_2_dataset_group_size.csv")['0']
    query_val_2 = list(query_val_2_pandas)

    print("Val 2 dataset prepared.")


    data_val_3 = pd.read_csv(data_path_val_3, index_col=False)
    print("Val 3 dataset loaded.")

    if 'rank_score' in data_val_3.columns:
        y_val_3 = data_val_3.pop("rank_score")
    if 'label' in data_val_3.columns:
        y_val_3 = data_val_3.pop("label")
    if ('Unnamed: 0' in data_val_3.columns):
        data_val_3.pop('Unnamed: 0')
    if "date_time" in data_val_3.columns:
        data_val_3.pop("date_time")
    if "position" in data_val_3.columns:
        data_val_3.pop("position")
    for name in forbidden_columns:
        if name in data_val_3.columns:
            data_val_3.pop(name)
    X_val_3 = data_val_3

    query_val_3_pandas = pd.read_csv("./datasets_preprocessed/extracted_val_3_dataset_group_size.csv")['0']
    query_val_3 = list(query_val_3_pandas)

    print("Val 3 dataset prepared.")


    data_val_4 = pd.read_csv(data_path_val_4, index_col=False)
    print("Val 4 dataset loaded.")

    if 'rank_score' in data_val_4.columns:
        y_val_4 = data_val_4.pop("rank_score")
    if 'label' in data_val_4.columns:
        y_val_4 = data_val_4.pop("label")
    if ('Unnamed: 0' in data_val_4.columns):
        data_val_4.pop('Unnamed: 0')
    if "date_time" in data_val_4.columns:
        data_val_4.pop("date_time")
    if "position" in data_val_4.columns:
        data_val_4.pop("position")
    for name in forbidden_columns:
        if name in data_val_4.columns:
            data_val_4.pop(name)
    X_val_4 = data_val_4

    query_val_4_pandas = pd.read_csv("./datasets_preprocessed/extracted_val_4_dataset_group_size.csv")['0']
    query_val_4 = list(query_val_4_pandas)

    print("Val 4 dataset prepared.")


    data_val_5 = pd.read_csv(data_path_val_5, index_col=False)
    print("Val 5 dataset loaded.")

    if 'rank_score' in data_val_5.columns:
        y_val_5 = data_val_5.pop("rank_score")
    if 'label' in data_val_5.columns:
        y_val_5 = data_val_5.pop("label")
    if ('Unnamed: 0' in data_val_5.columns):
        data_val_5.pop('Unnamed: 0')
    if "date_time" in data_val_5.columns:
        data_val_5.pop("date_time")
    if "position" in data_val_5.columns:
        data_val_5.pop("position")
    for name in forbidden_columns:
        if name in data_val_5.columns:
            data_val_5.pop(name)
    X_val_5 = data_val_5

    query_val_5_pandas = pd.read_csv("./datasets_preprocessed/extracted_val_5_dataset_group_size.csv")['0']
    query_val_5 = list(query_val_5_pandas)

    print("Val 5 dataset prepared.")

    gbm.fit(X_train, y_train, group=query_train,
        eval_set=[(X_val_1, y_val_1),
                  (X_val_2, y_val_2),
                  (X_val_3, y_val_3),
                  (X_val_4, y_val_4),
                  (X_val_5, y_val_5)],
        eval_group=[query_val_1,
                    query_val_2,
                    query_val_3,
                    query_val_4,
                    query_val_5],
        eval_at=[5], early_stopping_rounds=50)
    print("Model fit.")

    # data_test = pd.read_csv(data_path_test)
    # print("Test dataset loaded.")
    #
    # # y_test = data_test.pop("rank_score")
    # # y_test = data_test.pop("label")
    # if ('Unnamed: 0' in data_test.columns):
    #     data_test.pop('Unnamed: 0')
    # if "date_time" in data_test.columns:
    #     data_test.pop("date_time")
    # for name in forbidden_columns:
    #     if name in data_test.columns:
    #         left_data[name] = data_test.pop(name)
    # X_test = data_test
    #
    # query_test_pandas = pd.read_csv("./datasets_preprocessed/test_set_VU_DM_group_sizes_original.csv")['0']
    # query_test = list(query_test_pandas)
    #
    # print("Test dataset prepared.")
    #
    # test_pred = gbm.predict(X_test, group=query_test)
    # print("Model predicted.")
    #
    # X_test["predicted_ranking"] = test_pred
    # for name in forbidden_columns:
    #     X_test['prop_id'] = left_data[name]
    # print("Added predictions.")
    #
    # X_predictions = X_test[['srch_id', 'prop_id', 'predicted_ranking']]
    # X_predictions = X_predictions.sort_values(by=['srch_id', "predicted_ranking"], ascending=[True,False])
    # print("Sorted predictions.")
    #
    # X_predictions = X_predictions[['srch_id', 'prop_id']]
    # print("Extracted predictions.")
    #
    #
    # print(X_predictions)
    # X_predictions.to_csv("./result.csv", index=False)
