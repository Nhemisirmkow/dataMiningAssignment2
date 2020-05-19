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
                         "srch_query_affinity_score",  # ?
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
                         "comp7_rate_percent_diff",  # ?
                         "comp8_rate_percent_diff",
                         "date_time",]

TO_DELETE_COLUMNS = [
                    # "date_time",
                    # "srch_id",
                    # "prop_id",
                    # "comp3_rate_percent_diff",
                    # "comp6_inv",
                    # "comp6_rate",
                    # "comp8_rate_percent_diff",
                    # "comp1_rate_percent_diff",
                    # "comp4_rate",
                    # "orig_destination_distance", # :(
                    # "comp7_inv",
                    # "comp2_rate_percent_diff",
                    # "comp8_inv", # :(
                    # "comp5_rate_percent_diff", # :(
                    # "visitor_hist_starrating",
                    # "comp4_rate_percent_diff",
                    # "site_id", # ?
                    # "visitor_location_country_id", # ?
                    # "visitor_hist_adr_usd",
                    # "srch_saturday_night_bool", # :(
                    # "comp1_inv",
                    # "comp6_rate_percent_diff",
                    # "comp5_inv", # :(
                    # "srch_destination_id",  # ?
                    # "comp4_inv",
                    # "comp1_rate",
                    # "comp3_inv", # :(
                    # "comp3_rate", # :(
                    # "prop_brand_bool", # :(
                    # "comp2_inv", # :(
                    # "srch_booking_window", # :(
                    # #
                    # "srch_adults_count",
                    # "srch_room_count",
                    # "comp2_rate",
                    # "comp5_rate",
                    # "comp7_rate",
                    # "comp8_rate",
                    ]

TO_DELETE_COLUMNS = [
                    # "date_time",
                    # "srch_id",
                    # "prop_id",
                    "prop_review_score",
                    # "site_id", # ?????
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
                    # "visitor_location_country_id", # ????
                    # "srch_destination_id",  # ????
                    "std_dev_prop_log_historical_price",
                    "std_dev_comp2_rate",
                    "median_srch_room_count",
                    "std_dev_prop_review_score",
                    "std_dev_srch_room_count",
                    "std_dev_orig_destination_distance",
                    "srch_adults_count",
                    "std_dev_comp8_inv",
                    "median_comp2_rate",
                    "median_comp5_inv",  # B
                    "median_prop_log_historical_price", # B
                    "mean_prop_starrating",
                    "std_dev_prop_location_score1",
                    # "mean_prop_log_historical_price",
                    #
                    # "comp3_inv", # B
                    # "std_dev_prop_location_score1", # B
                    # "std_dev_comp2_inv", # B
                    # "std_dev_comp5_inv", # B
                    # "median_comp8_inv", # B
                    # "median_srch_adults_count", # B
                    # "std_dev_srch_adults_count", # B
                    # "mean_srch_children_count", # B
                    # "mean_srch_room_count", # B

                    #

                    # "prop_starrating",
                    # "prop_brand_bool",
                    # "prop_location_score1",
                    # "prop_location_score2",
                    # "promotion_flag",
                    # "srch_length_of_stay",
                    # "srch_children_count",
                    # "srch_room_count",
                    # "random_bool",
                    # "comp3_rate",
                    # "comp5_rate",
                    # "comp8_rate",
                    # "mean_prop_location_score1",
                    # "median_prop_review_score",
                    # "median_comp5_rate",
                    # "mean_prop_starrating",
                    # "median_prop_starrating",
                    # "mean_srch_length_of_stay",
                    #
                    # "comp3_inv",
                    # "std_dev_prop_location_score1",
                    # "std_dev_comp2_inv",
                    # "median_comp5_inv",
                    # "std_dev_comp5_inv",
                    # "median_comp8_inv",
                    # "median_prop_log_historical_price",
                    # "median_srch_adults_count",
                    # "std_dev_srch_adults_count",
                    # "mean_srch_children_count",
                    # "mean_srch_room_count",
                    # "comp3_rate", # :(
                    # "prop_brand_bool", # :(
                    # "srch_booking_window", # :(
                    ]


                    # "price_usd",
                    # "comp2_inv",
                    # "orig_destination_distance",
                    # "comp5_rate_percent_diff",
                    # "comp8_inv",

if __name__ == "__main__":
    data_path = "./datasets_preprocessed/extracted_training_dataset.csv"


    data = pd.read_csv(data_path)
    print("Main dataset loaded.")

    # print(data["rank_score"].corr(data["visitor_hist_adr_usd"]))
    # for name in NUMERIC_COLUMNS:
    #     if name in NOT_IMPORTANT_COLUMNS:
    #         continue
    #     print(name)
    #     print(data["rank_score"].corr(data[name]))

    for name in TO_DELETE_COLUMNS:
        data.pop(name)

    y = data.pop("rank_score")

    X_1 = sm.add_constant(data)
    model = sm.OLS(y,X_1).fit()
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', None)
    print(model.pvalues)


    reg = LassoCV()
    reg.fit(data, y)
    print("Best alpha using built-in LassoCV: %f" % reg.alpha_)
    print("Best score using built-in LassoCV: %f" %reg.score(data,y))
    coef = pd.Series(reg.coef_, index = data.columns)
    print(coef == 0)
