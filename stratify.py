from sklearn.model_selection import StratifiedShuffleSplit

def stratify(housing):
    split = StratifiedShuffleSplit(n_splits = 1, test_size = 0.2, random_state =42)
    for train_index, test_index in split.split(housing, housing["income_cat"]):
        strat_train_set = housing.loc[train_index]
        strat_test_set = housing.loc[test_index]
    return strat_train_set, strat_test_set