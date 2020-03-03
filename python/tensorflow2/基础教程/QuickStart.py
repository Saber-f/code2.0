import tensorflow as tf
import tensorflow.keras.layers as layers

model = tf.keras.Sequential()
model.add(layers.Dense(32, activation='relu'))
model.add(layers.Dense(32, activation='relu'))
model.add(layers.Dense(10, activation='softmax'))
model.compile(optimizer=tf.keras.optimizers.Adam(0.001),
                loss=tf.keras.losses.categorical_crossentropy,
                metrics=[tf.keras.metrics.categorical_accuracy])

