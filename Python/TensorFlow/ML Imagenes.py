import tensorflow as tf
from keras import datasets, layers, models
import matplotlib.pyplot as plt
import numpy as np
from keras.applications import ResNet50

# Cargar el conjunto de datos CIFAR-10, o 10 categorías de imágenes.
# fuente de datos: https://www.cs.toronto.edu/~kriz/cifar-10-python.tar.gz
(train_images, train_labels), (test_images, test_labels) = datasets.cifar10.load_data()

# Normalizar los valores de los píxeles (0-255) a un rango de 0-1
train_images, test_images = train_images / 255.0, test_images / 255.0

# tf.keras.preprocessing.image_dataset_from_directory para cargar imágenes personalizadas.

# Clasificaciones del modelo:
class_names = ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']

# Muestreo de imágenes:
plt.figure(figsize=(10,10))
for i in range(25):
    plt.subplot(5,5,i+1)
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    plt.imshow(train_images[i], cmap=plt.cm.binary)
    plt.xlabel(class_names[train_labels[i][0]])
plt.show()

# Arquitectura de Red Neuronal Convolucional, o CNN:
model = models.Sequential()

# Primera capa de convolución seguida de una capa de pooling
model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)))
model.add(layers.MaxPooling2D((2, 2)))

# Segunda capa de convolución seguida de otra capa de pooling
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))

# Tercera capa de convolución seguida de otra capa de pooling
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))

# Aplanamiento y capas densas
model.add(layers.Flatten())
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dense(10))  # 10 clases en CIFAR-10

# Compilar el modelo definiendo el optimizador, la función de pérdida y las métricas:
model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

# Aumento de datos (para mejorar la precisión):
datagen = tf.keras.preprocessing.image.ImageDataGenerator(
    rotation_range=15,
    width_shift_range=0.1,
    height_shift_range=0.1,
    horizontal_flip=True
)

# Entrenamiento:
history = model.fit(datagen.flow(train_images, train_labels, batch_size=64), 
                    epochs=10, 
                    validation_data=(test_images, test_labels))

# Evaluar el rendimiento del modelo en el conjunto de pruebas:
test_loss, test_acc = model.evaluate(test_images, test_labels, verbose=2)
print(f'\nPrecisión en el conjunto de pruebas: {test_acc}')

# Uso de Transfer Learning para mejorar la precisión, usando ResNet50:
# Cargar el modelo preentrenado sin la última capa
base_model = ResNet50(weights='imagenet', include_top=False, input_shape=(32, 32, 3))

# Congelar las capas del modelo preentrenado
base_model.trainable = False

# Crear una nueva cabeza de clasificación
model = models.Sequential([
    base_model,
    layers.GlobalAveragePooling2D(),
    layers.Dense(128, activation='relu'),
    layers.Dense(10)  # 10 clases
])

# Compilar y entrenar el modelo como antes
# Fuente de datos: https://storage.googleapis.com/tensorflow/keras-applications/resnet/resnet50_weights_tf_dim_ordering_tf_kernels_notop.h5
model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

history = model.fit(train_images, train_labels, epochs=10, validation_data=(test_images, test_labels))

# Muestreo de datos en forma de gráfica.
plt.plot(history.history['accuracy'], label='Precisión en el entrenamiento')
plt.plot(history.history['val_accuracy'], label='Precisión en la validación')
plt.xlabel('Época')
plt.ylabel('Precisión')
plt.legend(loc='lower right')
plt.show()

# La primera vez que se ejecutó este código:
#   La sección sin ResNet alcanzó una precisión de 11.5%.
#   La sección con ResNet alcanzó una precisión de 38%.
#   Ambas secciones poseían 10 épocas cada una. Para aumentar la precisión, se pueden usar más épocas.