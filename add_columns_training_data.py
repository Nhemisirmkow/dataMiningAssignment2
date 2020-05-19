import pandas as pd
import numpy
import random
from datetime import timedelta, datetime
from collections import OrderedDict, defaultdict

percentage = 0.08
train_data_fraction = 0.75

NUMERIC_COLUMNS = [
                   'visitor_hist_starrating',
                   'visitor_hist_adr_usd',
                   'prop_starrating',
                   'prop_review_score',
                   'prop_location_score1',
                   'prop_location_score2',
                   'prop_log_historical_price',
                   'price_usd',
                   'srch_length_of_stay',
                   'srch_booking_window',
                   'srch_adults_count',
                   'srch_children_count',
                   'srch_room_count',
                   'srch_query_affinity_score',
                   'orig_destination_distance',
                   'comp1_rate_percent_diff',
                   'comp2_rate_percent_diff',
                   'comp3_rate_percent_diff',
                   'comp4_rate_percent_diff',
                   'comp5_rate_percent_diff',
                   'comp6_rate_percent_diff',
                   'comp7_rate_percent_diff',
                   'comp8_rate_percent_diff',
                   'comp1_rate',
                   'comp2_rate',
                   'comp3_rate',
                   'comp4_rate',
                   'comp5_rate',
                   'comp6_rate',
                   'comp7_rate',
                   'comp8_rate',
                   'comp1_inv',
                   'comp2_inv',
                   'comp3_inv',
                   'comp4_inv',
                   'comp5_inv',
                   'comp6_inv',
                   'comp7_inv',
                   'comp8_inv',
                   ]
MEAN_NUMERIC_COLUMNS = ['visitor_hist_starrating',
                        'visitor_hist_adr_usd',
                        'prop_location_score1',
                        'prop_location_score2',
                        'srch_query_affinity_score',
                        'orig_destination_distance',
                        'comp1_rate_percent_diff',
                        'comp2_rate_percent_diff',
                        'comp3_rate_percent_diff',
                        'comp4_rate_percent_diff',
                        'comp5_rate_percent_diff',
                        'comp6_rate_percent_diff',
                        'comp7_rate_percent_diff',
                        'comp8_rate_percent_diff',
                        ]
MEDIAN_NUMERIC_COLUMNS = [
                          'prop_review_score',
                          'comp1_rate',
                          'comp1_inv',
                          'comp2_rate',
                          'comp2_inv',
                          'comp3_rate',
                          'comp3_inv',
                          'comp4_rate',
                          'comp4_inv',
                          'comp5_rate',
                          'comp5_inv',
                          'comp6_rate',
                          'comp6_inv',
                          'comp7_rate',
                          'comp7_inv',
                          'comp8_rate',
                          'comp8_inv',
                          ]


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
    data_path = "./datasets_preprocessed/training_set_VU_DM_without_nan.csv"
    global_statistic_path = "./datasets_preprocessed/global_statistic.csv"
    local_statistic_path = "./datasets_preprocessed/local_statistic.csv"


    data = pd.read_csv(data_path)
    print("Train dataset loaded")

    global_statistic = pd.read_csv(global_statistic_path)
    print("Global statistic loaded")

    local_statistic = pd.read_csv(local_statistic_path)
    local_statistic.set_index(["prop_id"])
    print("Local statistic loaded")

    local_statistic_dict = local_statistic.set_index("prop_id").to_dict('index')
    print("Local statistic transformed to dict.")

    for name in MEAN_NUMERIC_COLUMNS:
        if name in NOT_IMPORTANT_COLUMNS:
            continue
        data["mean_"+name] = [ local_statistic_dict[prop_id]["mean_"+name] for prop_id in data['prop_id']]
        data["std_dev_"+name] = [ local_statistic_dict[prop_id]["std_dev_"+name] for prop_id in data['prop_id']]
        print(name, " added")
    for name in MEDIAN_NUMERIC_COLUMNS:
        if name in NOT_IMPORTANT_COLUMNS:
            continue
        data["median_"+name] = [ local_statistic_dict[prop_id]["median_"+name] for prop_id in data['prop_id']]
        data["std_dev_"+name] = [ local_statistic_dict[prop_id]["std_dev_"+name] for prop_id in data['prop_id']]
        print(name, " added")
    for name in NUMERIC_COLUMNS:
        if name in MEDIAN_NUMERIC_COLUMNS or name in MEAN_NUMERIC_COLUMNS:
            continue
        if name in NOT_IMPORTANT_COLUMNS:
            continue
        data["mean_"+name] = [ local_statistic_dict[prop_id]["mean_"+name] for prop_id in data['prop_id']]
        data["median_"+name] = [ local_statistic_dict[prop_id]["median_"+name] for prop_id in data['prop_id']]
        data["std_dev_"+name] = [ local_statistic_dict[prop_id]["std_dev_"+name] for prop_id in data['prop_id']]
        print(name, " added")

    data.to_csv("./datasets_preprocessed/training_set_VU_DM_added_columns.csv", index = False)
    print("Preprocessed dataset saved.")
