import os
import matplotlib.pyplot as plt
import tensorflow as tf
import numpy

tf.enable_eager_execution() 

print("Tensorflow version {}".format(tf.__version__))

#download a dataset

#train_dataset_url = "https://storage.googleapis.com/download.tensorflow.org/data/iris_training.csv"

#train_dataset_fp = tf.keras.utils.get_file(fname=os.path.basename(train_dataset_url),                                           origin=train_dataset_url)

#print("Local copy of the dataset file: {}".format(train_dataset_fp))

#

# column order in CSV file
column_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']

#all symbols to last
feature_names = column_names[:-1]
#the same
label_name = column_names[-1]

print("Features: {}".format(feature_names))
print("Label: {}".format(label_name))

#names that corresponds to each line (variants)
class_names = ['Iris setosa', 'Iris versicolor', 'Iris virginica']

batch_size = 32

#train_dataset = tf.data.experimental.make_csv_dataset("/home/croissant/.keras/datasets/iris_training.csv", 32, column_names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species'], label_name=column_names[-1], num_epochs=1,shuffle=True, shuffle_buffer_size=10000, sloppy=False)
#print(train_dataset)

def get_dataset(file_path, **kwargs):
  dataset = tf.data.experimental.make_csv_dataset(
      file_path,
      batch_size=50, 
      column_names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species'],
      label_name=label_name,
      na_value="?",
      num_epochs=1,
      ignore_errors=True, 
      **kwargs)
  return dataset

raw_train_data = get_dataset("/home/croissant/.keras/datasets/iris_training.csv")

print("#############################################")

#show features of data-sample
#is just a standard tf operation to show what data class contains
features, labels = next(iter(raw_train_data))
print(features)
#lists by each parameter
print("#############################################")

plt.scatter(features['petal_length'],
            features['sepal_length'],
            c=labels,
            cmap='viridis')
#we can also plot the width's distribution

plt.xlabel("Petal length")
plt.ylabel("Sepal length")
#if you want to plot (this stuff is optional, i prefer to turn on it)
#plt.show()

#pack features to array
def pack_features_vector(features, labels):
  features = tf.stack(list(features.values()), axis=1)
  return features, labels

raw_train_data = raw_train_data.map(pack_features_vector)
features, labels = next(iter(raw_train_data))
print(features[:5])
#print(labels[:5])#also we can show the label value for each feature string

#create model

model = tf.keras.Sequential([
  tf.keras.layers.Dense(10, activation=tf.nn.relu, input_shape=(4,)),  # input shape required
  tf.keras.layers.Dense(10, activation=tf.nn.relu),
  tf.keras.layers.Dense(3)
])

#its just predictions
predictions = model(features)
print(predictions[:5])
#or their probabilities
print(tf.nn.softmax(predictions[:5]))
#we create the model, but it's not trained, we can check its results:
print("Prediction: {}".format(tf.argmax(predictions, axis=1)))
print("    Labels: {}".format(labels))
