import pandas as pd
import numpy
import random
from datetime import timedelta, datetime

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


if __name__ == "__main__":
    # data_path = "datasets_raw/training_set_VU_DM.csv"
    # data_path2 = "./datasets_raw/test_set_VU_DM.csv"
    data_path = "./datasets_preprocessed/extracted_test_dataset.csv"
    data_path2 = "./datasets_preprocessed/extracted_training_dataset.csv"


    data = pd.read_csv(data_path, parse_dates=['date_time'])
    data.set_index(["prop_id"])
    print("Train dataset loaded")
    data2 = pd.read_csv(data_path2, parse_dates=['date_time'])
    data2.set_index(["prop_id"])
    print("Test dataset loaded")

    prop_ids = list(set(list(set(data['prop_id'])) + list(set(data2['prop_id']))))

    print("prop_ids computed")

    values = {}
    values['global'] = {}

    for name in NUMERIC_COLUMNS:
        x = pd.concat([data[name].dropna(), data2[name].dropna()], ignore_index=True)
        if len(x) > 0:
            values['global']['mean_'+name] = numpy.mean(x)
            values['global']['std_dev_'+name] = numpy.std(x)
            values['global']['median_'+name] = numpy.median(x)
        else:
            values['global']['mean_'+name] = 0.0
            values['global']['std_dev_'+name] = 0.0
            values['global']['median_'+name] = 0.0
        print(name)

    result = []
    result.append(values['global'])
    df = pd.DataFrame(result)
    df.to_csv("./MarcinTemp/global_statistic_temp.csv", index = False)

    #
    # random_sample_srch_ids = list(random.sample(srch_ids, int(len(srch_ids) * percentage)))
    # extracted_train_srch_ids = list(random.sample(random_sample_srch_ids, int(len(srch_ids) * percentage * train_data_fraction)))
    # extracted_test_srch_ids = list(set(random_sample_srch_ids) - set(extracted_train_srch_ids))
    # print("sampled")
    # extracted_test_srch_ids.sort()
    # extracted_train_srch_ids.sort()
    #
    # extracted_train_dataset = pd.DataFrame()
    # extracted_test_dataset = pd.DataFrame()
    #
    # extracted_test_dataset =data.loc[data['srch_id'].isin(extracted_test_srch_ids)]
    # print("Extracted test data set.")
    # extracted_train_dataset =data.loc[data['srch_id'].isin(extracted_train_srch_ids)]
    # print("Extracted train data set.")
    # extracted_train_dataset.to_csv("./datasets_preprocessed/extracted_training_dataset.csv", na_rep=0)
    # extracted_test_dataset.to_csv("./datasets_preprocessed/extracted_test_dataset.csv", na_rep=0)
