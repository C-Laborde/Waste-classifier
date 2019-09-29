import numpy as np
import matplotlib.pyplot as plt
from utils.load_data import load_data

import tensorflow as tf
from tensorflow import keras

train_imgs, train_labels = load_data("train")
val_imgs, val_labels = load_data("valid")
test_imgs, test_labels = load_data("test")