import os
import tensorflow as tf
import numpy as np

#GRAPHICS
import Imports
import ROOT
import matplotlib.pyplot as plt



#names that corresponds to data-types
class_names = ['Disease', 'Normal']

#0 - disease, 1 - normal
def get_dataset(file_path, **kwargs):
    column_names = []
    for i in range(100):
        column_names.append('bin_' + str(i+1))
    column_names.append('sp')
    label_name = column_names[-1]
    dataset = tf.data.experimental.make_csv_dataset(
        file_path,
        batch_size=50, #120 works worst
        column_names=column_names,
        label_name=label_name,
        na_value='?',
        num_epochs=1,
        ignore_errors=True, 
        **kwargs)
    return dataset

#get data
raw_train_data = get_dataset('./files/all_data.csv')

#show features of data-sample
#its just a standard tf operation to show what data class contains
features, labels = next(iter(raw_train_data))

#pack features to array
def pack_features_vector(features, labels):
    features = tf.stack(list(features.values()), axis=1)
    return features, labels

raw_train_data = raw_train_data.map(pack_features_vector)
features, labels = next(iter(raw_train_data))

#create model

model = tf.keras.Sequential([
  tf.keras.layers.Dense(10, activation=tf.nn.relu, input_shape=(100,)),  # input shape
  tf.keras.layers.Dense(10, activation=tf.nn.relu), #tf.nn.relu - activ.function
  tf.keras.layers.Dense(2)
])

#its just predictions
predictions = model(features)

#loss function for minimizing
loss_object = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)

def loss(model, x, y, training):
   y_ = model(x, training=training)
   return loss_object(y_true=y, y_pred=y_)

l = loss(model, features, labels, training=False)

#calculate gradient to model optimize
def grad(model, inputs, targets):
    with tf.GradientTape() as tape:
        loss_value = loss(model, inputs, targets, training=True)
    return loss_value, tape.gradient(loss_value, model.trainable_variables)

#choose optimizer and learning rate
#optimizer = tf.keras.optimizers.Adam(learning_rate=0.06)#0.06
optimizer = tf.keras.optimizers.SGD(learning_rate=0.015)#0.06 #Stohastic gradient descent

loss_value, grads = grad(model, features, labels)

#train loop begins
train_loss_results = []
train_accuracy_results = []

num_epochs = 21 #1001 #301

for epoch in range(num_epochs):
    epoch_loss_avg = tf.keras.metrics.Mean()
    epoch_accuracy = tf.keras.metrics.SparseCategoricalAccuracy()

  # Training loop - using batches of 32
    for x, y in raw_train_data:
    # Optimize the model
        loss_value, grads = grad(model, x, y)
        optimizer.apply_gradients(zip(grads, model.trainable_variables))

    # Track progress
        epoch_loss_avg.update_state(loss_value)  # Add current batch loss
        epoch_accuracy.update_state(y, model(x, training=True))

  # End epoch
    train_loss_results.append(epoch_loss_avg.result())
    train_accuracy_results.append(epoch_accuracy.result())

    if epoch % 2 == 0:
        print('Epoch {:03d}: Loss: {:.3f}, Accuracy: {:.3%}'.format(epoch,
                                                                epoch_loss_avg.result(),
                                                                epoch_accuracy.result()))

#TRAINING METRICS
train_arr = []
accur_arr = []

#COST FUNCTION
for i in range(len(train_loss_results)):
    train_arr.append(train_loss_results[i].numpy())

#ACCURACY
for i in range(len(train_loss_results)):
    accur_arr.append(train_accuracy_results[i].numpy())

#save result of trains
np.savez('learning_info', tr = train_arr, ac = accur_arr)


#PREDICTIONS
print('\nPREDICTIONS:')

for i, logits in enumerate(predictions):
    class_idx = tf.argmax(logits).numpy() #type "0", "1"
    p = tf.nn.softmax(logits)[class_idx] #probability
    name = class_names[class_idx] #get name from class_names array
    #CLASS CORRESPONDANCE
    #print('LOGITS:')
    #print(tf.nn.softmax(logits)[0])
    #print(tf.nn.softmax(logits)[1])
    #print(logits)
    #PRINT RESULTS
    print('Example {} prediction: {} ({:4.3f}%)'.format(i, name, 100*p))

#predictions from another dataset
print('\nPREDICTIONS BY SAMPLE-DATASET')

test_dataset = get_dataset('./datasets/test_sample_1.csv')
test_dataset = test_dataset.map(pack_features_vector)
test_accuracy = tf.keras.metrics.Accuracy()

for (x, y) in test_dataset:
    logits = model(x, training=False)
    prediction = tf.argmax(logits, axis=1, output_type=tf.int32)
    test_accuracy(prediction, y)

print('Test set accuracy: {:.3%}'.format(test_accuracy.result()))
print(tf.stack([y,prediction],axis=1))


#SAVE MODEL
tf.saved_model.save(model, './saved_model')

