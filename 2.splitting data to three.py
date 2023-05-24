import json
import os
import random


def split_dataset_into_splits(path_to_dataset):
    with open(path_to_dataset, 'r') as f:
        dataset = json.load(f)

    # shuffle the keys of the dictionary
    keys = list(dataset.keys())
    random.shuffle(keys)

    # calculate the number of samples for each split
    num_samples = len(dataset)
    num_train = int(num_samples * 0.8)
    num_val = int(num_samples * 0.1)

    # create three new dictionaries for training, validation, and testing
    train_dict = dict()
    val_dict = dict()
    test_dict = dict()

    # iterate over the shuffled keys and add each key-value pair to the appropriate dictionary
    for i, key in enumerate(keys):
        if i < num_train:
            train_dict[key] = dataset[key]
        elif i < num_train + num_val:
            val_dict[key] = dataset[key]
        else:
            test_dict[key] = dataset[key]

    os.makedirs("features", exist_ok=True)

    # save the resulting dictionaries
    with open("features/ALC_features_lld_train.json", mode="w", encoding="utf8") as f:
        json.dump(train_dict, f)
    with open("features/ALC_features_lld_valid.json", mode="w", encoding="utf8") as f:
        json.dump(val_dict, f)
    with open("features/ALC_features_lld_test.json", mode="w", encoding="utf8") as f:
        json.dump(test_dict, f)

#split_dataset_into_splits('opensmile_lld_features.json')
split_dataset_into_splits('ALC_lld_features.json')