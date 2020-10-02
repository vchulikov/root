import os
import matplotlib.pyplot as plt
import tensorflow as tf
import numpy

tf.enable_eager_execution() 

#names that corresponds to color name
class_names = ['Disease', 'Normal']

#0 - disease, 1 - normal

def get_dataset(file_path, **kwargs):
  column_names = []
  for i in range(100):
   column_names.append("bin_" + str(i+1))
  column_names.append("sp")
  print(column_names)
  label_name = column_names[-1]
  dataset = tf.data.experimental.make_csv_dataset(
      file_path,
      batch_size=50, #120 works worst
      column_names=column_names,
      label_name=label_name,
      na_value="?",
      num_epochs=1,
      ignore_errors=True, 
      **kwargs)
  return dataset

#raw_train_data = get_dataset("./dataset/peak_training.csv") #old sample 75 events
#raw_train_data = get_dataset("./dataset/data_classifier.csv")

#infarct
raw_train_data = get_dataset("./datasets/train_inf.csv")


#show features of data-sample
#is just a standard tf operation to show what data class contains
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
print("Loss test: {}".format(l))

#calculate gradient to model optimize
def grad(model, inputs, targets):
  with tf.GradientTape() as tape:
    loss_value = loss(model, inputs, targets, training=True)
  return loss_value, tape.gradient(loss_value, model.trainable_variables)

#choose optimizer and learning rate
#optimizer = tf.keras.optimizers.Adam(learning_rate=0.06)#0.06
optimizer = tf.keras.optimizers.SGD(learning_rate=0.1)#0.06 #Stohastic gradient descent

loss_value, grads = grad(model, features, labels)


#train loop begins
train_loss_results = []
train_accuracy_results = []

num_epochs = 501 #1001 #301

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
    print("Epoch {:03d}: Loss: {:.3f}, Accuracy: {:.3%}".format(epoch,
                                                                epoch_loss_avg.result(),
                                                                epoch_accuracy.result()))

#train loop ends

#show learning results
fig, axes = plt.subplots(2, sharex=True, figsize=(12, 8))
fig.suptitle('Training Metrics')

axes[0].set_ylabel("Loss", fontsize=14)
axes[0].plot(train_loss_results)

axes[1].set_ylabel("Accuracy", fontsize=14)
axes[1].set_xlabel("Epoch", fontsize=14)
axes[1].plot(train_accuracy_results)
plt.show()

#predict here:

#1. dis
#2. norm
predict_dataset = tf.convert_to_tensor([
[0.,0.000750000006519,0.00104999996256,0.001200000057,0.00124999997206,0.00170000002254,0.00209999992512,0.00224999990314,0.00310000008903,0.00325000006706,0.00334999989718,0.00365000008605,0.00480000022799,0.00554999988526,0.00570000009611,0.00689999992028,0.00865000020713,0.00784999970347,0.00920000020415,0.00985000003129,0.0109000001103,0.0109000001103,0.0137999998406,0.0127499997616,0.0144999995828,0.0142999999225,0.0156999994069,0.0170000009239,0.0167500004172,0.0173000004143,0.019999999553,0.0194499995559,0.0202500000596,0.0190500002354,0.0193000007421,0.0190999992192,0.0214499998838,0.019999999553,0.0188500005752,0.0183499995619,0.0184000004083,0.0173000004143,0.0167500004172,0.0173000004143,0.0153500000015,0.0150499995798,0.0147000001743,0.0122999995947,0.0137999998406,0.0129500003532,0.0124000003561,0.0114500001073,0.0117499995977,0.00960000045598,0.0082499999553,0.00980000011623,0.0103000001982,0.00829999987036,0.00910000037402,0.00829999987036,0.0093999998644,0.00735000008717,0.00810000021011,0.00875000003725,0.00875000003725,0.00889999978244,0.00930000003427,0.00884999986738,0.010150000453,0.00910000037402,0.0109000001103,0.00920000020415,0.010150000453,0.00985000003129,0.0111999996006,0.011250000447,0.0111499996856,0.0114500001073,0.0103000001982,0.0104999998584,0.0103500001132,0.00934999994934,0.00975000020117,0.00860000029206,0.00899999961257,0.00860000029206,0.00755000021309,0.00650000013411,0.00689999992028,0.00820000004023,0.00710000004619,0.00625000009313,0.00474999984726,0.00524999992922,0.00430000014603,0.00449999980628,0.00295000011101,0.00304999994114,0.00289999996312,0.00245000002906],
[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,6.24999996202E-10,0.,0.,0.,0.,1.56249999376E-14,2.49999993684E-05,2.50012490142E-05,7.50006292947E-05,1.2499999924E-09,2.50012490142E-05,4.99999987369E-05,0.000125003120047,0.000150007501361,7.50037506805E-05,0.000250004377449,0.000325007480569,0.000250011245953,0.000625019369181,0.000700027507264,0.00112502195407,0.00147503812332,0.0013500462519,0.00272506871261,0.00330009195022,0.00407509226352,0.00477513112128,0.0068501457572,0.00815020594746,0.0088002178818,0.0103002637625,0.0126752713695,0.0146753201261,0.0159503929317,0.0181504432112,0.0187004506588,0.0194755233824,0.0214505251497,0.0224005486816,0.0226755831391,0.024075621739,0.0239756032825,0.0236005820334,0.0226505752653,0.0224505588412,0.0205505378544,0.0182255096734,0.0167754422873,0.0165503956378,0.0152753600851,0.0129503235221,0.0111002810299,0.00955024920404,0.008500196971,0.00710016256198,0.00540011981502,0.00477510737255,0.00360010308214,0.00225007487461,0.00200005294755,0.00177505495958,0.00145003572106,0.00117502571084,0.000500012480188,0.00065001565963,0.000550008087885,0.000200005000806,0.000275003752904,0.000150002510054,5.00025016663E-05,7.50000035623E-05,2.50012490142E-05,3.90634777658E-19,2.44140629771E-28,3.90625006587E-19,1.56249999376E-14,0.,6.24999996202E-10,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.]
])

predictions = model(predict_dataset, training=False)
print("predictions")
print(predictions)

for i, logits in enumerate(predictions):
  class_idx = tf.argmax(logits).numpy() #color type "0", "1", "2"
  p = tf.nn.softmax(logits)[class_idx] #probability
  name = class_names[class_idx] #get name from class_names array
  print("Example {} prediction: {} ({:4.3f}%)".format(i, name, 100*p))

#random prediction from csv-file
#predictions from another dataset
test_dataset = get_dataset("./datasets/test_inf.csv")
test_dataset = test_dataset.map(pack_features_vector)
test_accuracy = tf.keras.metrics.Accuracy()

for (x, y) in test_dataset:
  logits = model(x, training=False)
  prediction = tf.argmax(logits, axis=1, output_type=tf.int32)
  test_accuracy(prediction, y)

print("Test set accuracy: {:.3%}".format(test_accuracy.result()))
print(tf.stack([y,prediction],axis=1))

tf.saved_model.save(model, './')
