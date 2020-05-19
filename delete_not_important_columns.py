import pandas as pd
import numpy as np
import random
from datetime import timedelta, datetime

NOT_IMPORTANT_COLUMNS = ["visitor_hist_starrating",
                         "visitor_hist_adr_usd",
                         "srch_query_affinity_score",
                         "comp1_rate",
                         "comp1_inv",
                         "comp1_rate_percent_diff",
                         "comp2_rate_percent_diff",
                         "comp3_rate_percent_diff",
                         "comp4_rate",
                         "comp4_inv",
                         "comp4_rate_percent_diff",
                         "comp6_rate",
                         "comp6_inv",
                         "comp6_rate_percent_diff",
                         "comp7_rate",
                         "comp7_inv",
                         "comp7_rate_percent_diff",
                         "comp8_rate_percent_diff",
                         "date_time",]


if __name__ == "__main__":
    # data_path = "datasets_raw/training_set_VU_DM.csv"
    data_path = "./datasets_raw/test_set_VU_DM.csv"


    data = pd.read_csv(data_path, parse_dates=['date_time'])
    print("Train dataset loaded")

    for name in NOT_IMPORTANT_COLUMNS:
        data.pop(name)

    data.to_csv("./datasets_preprocessed/test_removed_non_important_columns.csv", index = False)
