import pandas as pd
import numpy as np
import random
from datetime import timedelta, datetime
import statsmodels.api as sm
from sklearn.linear_model import RidgeCV, LassoCV, Ridge, Lasso


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

TO_DELETE_COLUMNS = [
                    "prop_review_score",
                    "site_id", # ?????
                    "std_dev_comp5_rate_percent_diff",
                    "median_srch_booking_window",
                    "orig_destination_distance", # :(
                    "comp8_inv", # :(
                    "comp5_rate_percent_diff", # :(
                    "std_dev_srch_length_of_stay",
                    "prop_log_historical_price",
                    "price_usd",
                    "std_dev_prop_location_score2",
                    "median_comp8_rate",
                    "mean_srch_adults_count",
                    "median_comp3_inv",
                    "median_srch_length_of_stay",
                    "std_dev_comp8_rate",
                    "comp5_inv",
                    "comp2_inv",
                    "std_dev_comp5_rate",
                    "std_dev_prop_starrating",
                    "std_dev_srch_children_count",
                    "std_dev_price_usd",
                    "std_dev_comp3_rate",
                    "median_comp2_inv",
                    "mean_comp5_rate_percent_diff",
                    "mean_price_usd",
                    "mean_prop_location_score2",
                    "srch_saturday_night_bool",
                    "comp2_rate",
                    "mean_orig_destination_distance",
                    "median_comp3_rate",
                    "std_dev_comp3_inv",
                    "median_srch_children_count",
                    "visitor_location_country_id", # ????
                    "srch_destination_id",  # ????
                    "std_dev_prop_log_historical_price",
                    "std_dev_comp2_rate",
                    "median_srch_room_count",
                    "std_dev_prop_review_score",
                    "std_dev_srch_room_count",
                    "std_dev_orig_destination_distance",
                    "srch_adults_count",
                    "std_dev_comp8_inv",
                    "median_comp2_rate",
                    "median_comp5_inv",
                    "median_prop_log_historical_price",
                    "mean_prop_starrating",
                    "std_dev_prop_location_score1",
                    ]

if __name__ == "__main__":
    data_path = "./datasets_preprocessed/test_set_VU_DM_added_columns.csv"


    data = pd.read_csv(data_path)
    print("Main dataset loaded.")

    for name in TO_DELETE_COLUMNS:
        data.pop(name)

    data.to_csv("./datasets_preprocessed/test_set_VU_DM_feature_selection.csv", index=False)
