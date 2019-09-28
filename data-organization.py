# data is organized under ImageNet convention

import os
from utils.split_indices import split_indices
from utils.get_names import get_names
from utils.move_files import move_files


subsets = ["train", "valid"]
material = ["cardboard", "glass", "metal", "paper", "plastic", "trash"]

for subset in subsets:
    for waste_type in material:
        folder = os.path.join("data", subset, waste_type)
        if not os.path.exists(folder):
            os.makedirs(folder)

if not os.path.exists(os.path.join("data", "test")):
    os.makedirs(os.path.join("data", "test"))

for waste_type in material:
    source_folder = os.path.join("dataset-resized", waste_type)
    train_ind, valid_ind, test_ind = split_indices(source_folder, 1, 1)

    train_names = get_names(waste_type, train_ind)
    train_source_files = [os.path.join(source_folder, name) for name in train_names]
    train_dest = "data/train/" + waste_type
    move_files(train_source_files, train_dest)

    valid_names = get_names(waste_type, valid_ind)
    valid_source_files = [os.path.join(source_folder, name) for name in valid_names]
    valid_dest = "data/valid/" + waste_type
    move_files(valid_source_files, valid_dest)

    test_names = get_names(waste_type, test_ind)
    test_source_files = [os.path.join(source_folder, name) for name in test_names]
    test_dest = "data/test/" + waste_type
    move_files(test_source_files, "data/test")