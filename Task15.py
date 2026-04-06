# import tensorflow as tf
# from tensorflow.keras import datasets, layers, models

# 1. Load and normalize data
# (train_images, train_labels), (test_images, test_labels) = datasets.cifar10.load_data()
# train_images, test_images = train_images / 255.0, test_images / 255.0

# 2. Build the CNN Architecture
# model = models.Sequential([
    # Convolutional Base
    # layers.Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)),
    # layers.MaxPooling2D((2, 2)),
    # layers.Conv2D(64, (3, 3), activation='relu'),
    # layers.MaxPooling2D((2, 2)),
    
    # Dense Layers (The "Head")
    # layers.Flatten(),
    # layers.Dense(64, activation='relu'),
    # layers.Dense(10) # 10 classes in CIFAR-10
# ])

# 3. Compile and Train
# model.compile(optimizer='adam',
            #   loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
            #   metrics=['accuracy'])

# model.fit(train_images, train_labels, epochs=10, validation_data=(test_images, test_labels))