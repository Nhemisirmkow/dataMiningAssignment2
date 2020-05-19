import pandas as pd
import numpy as np
import random
from datetime import timedelta, datetime

if __name__ == "__main__":
    data_path = "datasets_raw/training_set_VU_DM.csv"
    data_path2 = "./datasets_preprocessed/training_important_rows.csv"
    data_path3 = "./datasets_preprocessed/training_booking_rows.csv"


    data = pd.read_csv(data_path)
    print("Main dataset loaded.")
    data2 = pd.read_csv(data_path2)
    print("Important_rows dataset loaded.")
    data3 = pd.read_csv(data_path3)
    print("Booking dataset loaded.")

    srch_ids = list(data.srch_id.unique())
    prop_ids = list(data.prop_id.unique())
    srch_ids2 = list(data2.srch_id.unique())
    prop_ids2 = list(data2.prop_id.unique())
    srch_ids3 = list(data3.srch_id.unique())
    prop_ids3 = list(data3.prop_id.unique())

    print("Number of rows:")
    print(data.shape[0])
    print(data2.shape[0])
    print(round(data2.shape[0] / data.shape[0] * 100, 2), "%")
    print(data3.shape[0])
    print(round(data3.shape[0] / data.shape[0] * 100, 2), "%")
    print("###############")

    print("Srch_ids: ")
    print(len(srch_ids))
    print(len(srch_ids2))
    print(round((len(srch_ids2) / len(srch_ids) * 100), 2), "%")
    print(len(srch_ids3))
    print(round((len(srch_ids3) / len(srch_ids) * 100), 2), "%")
    print("###############")

    print("Prop_ids: ")
    print(len(prop_ids))
    print(len(prop_ids2))
    print(round((len(prop_ids2) / len(prop_ids) * 100), 2), "%")
    print(len(prop_ids3))
    print(round((len(prop_ids3) / len(prop_ids) * 100), 2), "%")
    print("###############")
