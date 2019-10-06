import numpy as np
import matplotlib.pyplot as plt
from utils.load_data import load_data

import tensorflow as tf
from tensorflow import keras

train_imgs, train_labels = load_data("train")
val_imgs, val_labels = load_data("valid")
test_imgs, test_labels = load_data("test")

class_names = ["cardboard", "glass", "plastic", "metal", "paper", "trash"]

model = keras.Sequential([
    keras.layers.Flatten(input_shape=(384, 512, 3)),
    keras.layers.Dense(128, activation=tf.nn.relu),
    keras.layers.Dense(6, activation=tf.nn.softmax)
])

model.compile(optimizer="adam",
              loss="sparse_categorical_crossentropy",
              metrics=["accuracy"]
)

model.fit(train_imgs, train_labels, epochs=5)

test_loss, test_acc = model.evaluate(test_imgs, test_labels)
print("Test accuracy: ", test_acc)

predictions = model.predict(test_imgs)
print("predictions: ", predictions[0])
print("highest probability: ", np.argmax(predictions[0]))
print("actual label: ", test_labels[0])