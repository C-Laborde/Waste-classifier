import os
import random


def split_indices(material, seed1, seed2):
    n = len(os.listdir(material))
    full_set = list(range(1, n+1))

    # train_indices
    random.seed(seed1)
    train = random.sample(list(range(1, n+1)), int(.5*n))

    ## temp
    remain = list(set(full_set) - set(train))

    ## separate remaining into validation and test
    random.seed(seed2)
    valid = random.sample(remain, int(.5*len(remain)))
    test = list(set(remain) - set(valid))

    return(train, valid, test)