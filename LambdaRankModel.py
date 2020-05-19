import pandas as pd
import numpy as np
import random
from datetime import timedelta, datetime
import lightgbm as lgb
from sklearn.model_selection import train_test_split

if __name__ == "__main__":
    data_path_train = "./datasets_preprocessed/extracted_training_dataset.csv"
    # data_path_test = "./datasets_preprocessed/extracted_test_dataset.csv"
    data_path_test = "./datasets_preprocessed/test_set_VU_DM_added_columns.csv"
    data_path_val = "./datasets_preprocessed/extracted_val_dataset.csv"

    data_train = pd.read_csv(data_path_train)
    print("Training dataset loaded.")

    y_train = data_train.pop("rank_score")
    X_train = data_train

    gbm = lgb.LGBMRanker()

    srch_ids_train = X_train.srch_id.unique()

    query_train_temp = {}
    for i in srch_ids_train:
        query_train_temp[i] = X_train.loc[X_train['srch_id'] == i].shape[0]
        # query_train.append(X_train.loc[X_train['srch_id'] == i].shape[0])
    query_train = list(query_train_temp.items())
    query_train.sort()
    query_train = [x for (_, x) in query_train]

    print("Training dataset prepared.")


    data_test = pd.read_csv(data_path_test)
    print("Test dataset loaded.")

    # y_test = data_test.pop("rank_score")
    X_test = data_test

    srch_ids_test = X_test.srch_id.unique()

    # query_test = []
    # query_test_temp = {}
    # count = 0
    # last_progress = -5
    # for i in srch_ids_test:
    #     query_test_temp[i] = X_test.loc[X_test['srch_id'] == i].shape[0]
    #     # query_test.append(X_test.loc[X_test['srch_id'] == i].shape[0])
    #     count += 1
    #     progress = round(count / len(srch_ids_test) * 100, 2)
    #     if int(progress * 100) % 500 == 0 and progress > last_progress + 4:
    #         last_progress = progress
    #         print(progress, "%")
    # query_test = list(query_test_temp.items())
    # query_test.sort()
    # query_test = [x for (_, x) in query_test]

    # query_test_pandas = pd.Series(query_test)
    # query_test_pandas.to_csv("./datasets_preprocessed/test_set_VU_DM_added_columns_group_sizes.csv")
    query_test_pandas = pd.read_csv("./datasets_preprocessed/test_set_VU_DM_added_columns_group_sizes.csv")['0']
    query_test = list(query_test_pandas)

    print("Test dataset prepared.")


    data_val = pd.read_csv(data_path_val)
    print("Val dataset loaded.")

    y_val = data_val.pop("rank_score")
    X_val = data_val

    srch_ids_val = X_val.srch_id.unique()

    query_val_temp = {}
    for i in srch_ids_val:
        query_val_temp[i] = X_val.loc[X_val['srch_id'] == i].shape[0]
        # query_val.append(X_val.loc[X_val['srch_id'] == i].shape[0])
    query_val = list(query_val_temp.items())
    query_val.sort()
    query_val = [x for (_, x) in query_val]

    print("Val dataset prepared.")



    gbm.fit(X_train, y_train, group=query_train,
        eval_set=[(X_val, y_val)], eval_group=[query_val],
        eval_at=[5], early_stopping_rounds=50)

    print("Model fit.")

    test_pred = gbm.predict(X_test, group=query_test)

    print("Model predicted.")

    X_test["predicted_ranking"] = test_pred
    print("Added predictions.")
    X_predictions = X_test[['srch_id', 'prop_id', 'predicted_ranking']]
    X_predictions = X_predictions.sort_values(by=['srch_id', "predicted_ranking"], ascending=[True,False])
    print("Sorted predictions.")
    X_predictions = X_predictions[['srch_id', 'prop_id']]
    print("Extracted predictions.")
    # result = pd.DataFrame(columns=['srch_id', 'prop_id'])
    # count = 0
    # for i in srch_ids_test:
    #     X_predictions = X_test.loc[X_test['srch_id'] == i].sort_values(by=["predicted_ranking"], ascending=False)
    #     X_predictions = X_predictions[['srch_id', 'prop_id']]
    #     result = result.append(X_predictions)
    #     count += 1
    #     progress = round(count / len(srch_ids_test) * 100, 2)
    #     if int(progress * 100) % 500 == 0:
    #         print(round(count / len(srch_ids_test) * 100, 2), "%")

    print(X_predictions)
    X_predictions.to_csv("./result.csv", index=False)
