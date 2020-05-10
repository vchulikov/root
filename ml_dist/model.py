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
raw_train_data = get_dataset("./dataset/data_classifier.csv")

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
  tf.keras.layers.Dense(10, activation=tf.nn.relu),
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
optimizer = tf.keras.optimizers.SGD(learning_rate=0.06)#0.06

loss_value, grads = grad(model, features, labels)


#train loop begins
train_loss_results = []
train_accuracy_results = []

num_epochs = 101 #1001 #301

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
#plt.show()

#predict here:
predict_dataset = tf.convert_to_tensor([
[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,4.99999987369E-05,0.,0.000150000007125,9.99999974738E-05,0.000300000014249,0.000750000006519,0.000950000016019,0.00170000002254,0.00215000007302,0.00435000006109,0.00425000023097,0.00735000008717,0.0111999996006,0.0162000004202,0.0199500005692,0.0228499993682,0.0305499993265,0.0377000011504,0.0443000011146,0.0520000010729,0.0524999983609,0.059050001204,0.0628999993205,0.0662499964237,0.0671000033617,0.0650499984622,0.0634500011802,0.0540000014007,0.0489999987185,0.0428000018001,0.0370500013232,0.0302499998361,0.0252999998629,0.0189999993891,0.0159000009298,0.0100499996915,0.00800000037998,0.00609999988228,0.0035500000231,0.00224999990314,0.00130000000354,0.00089999998454,0.00044999999227,0.000399999989895,0.000300000014249,4.99999987369E-05,0.000150000007125,4.99999987369E-05,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.],
[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,4.99999987369E-05,0.,0.000150000007125,9.99999974738E-05,0.000300000014249,0.000750000006519,0.000950000016019,0.00170000002254,0.00215000007302,0.00435000006109,0.00425000023097,0.00735000008717,0.0111999996006,0.0162000004202,0.0199500005692,0.0228499993682,0.0305499993265,0.0377000011504,0.0443000011146,0.0520000010729,0.0524999983609,0.059050001204,0.0628999993205,0.0662499964237,0.0671000033617,0.0650499984622,0.0634500011802,0.0540000014007,0.0489999987185,0.0428000018001,0.0370500013232,0.0302499998361,0.0252999998629,0.0189999993891,0.0159000009298,0.0100499996915,0.00800000037998,0.00609999988228,0.0035500000231,0.00224999990314,0.00130000000354,0.00089999998454,0.00044999999227,0.000399999989895,0.000300000014249,4.99999987369E-05,0.000150000007125,4.99999987369E-05,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.],
[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,2.49974996258E-09,0.,0.,0.,6.24874982189E-18,0.,2.49974996258E-09,1.24981242803E-13,2.49987497369E-09,9.99949988909E-05,5.00025016663E-05,4.99974994455E-05,0.000100015000498,0.000200007503736,0.000500012480188,0.000749982544221,0.00074999750359,0.00109999999404,0.00194999505766,0.00279999012128,0.00374998501502,0.00440004235134,0.00535003235564,0.00779997231439,0.00914998538792,0.0119999898598,0.0155499046668,0.0181499551982,0.020550088957,0.0252999607474,0.0286499708891,0.0318001359701,0.0378998816013,0.0385500453413,0.0427999980748,0.0456499196589,0.0458501279354,0.0469501055777,0.0490499846637,0.0502498932183,0.0487000197172,0.0476999878883,0.0438001416624,0.0443498045206,0.0375000610948,0.0364000499249,0.032100006938,0.029699973762,0.025099972263,0.0225998982787,0.0179499778897,0.0142999943346,0.0114500345662,0.00965000316501,0.00720005482435,0.00629999022931,0.00494999531657,0.00365002732724,0.00309997238219,0.00145003758371,0.00135003752075,0.0010500025237,0.000749982544221,0.000299999985145,0.000349989975803,0.000150002495502,5.00075002492E-05,0.000149997504195,4.99999987369E-05,4.68617212439E-26,4.99999987369E-05,1.24981242803E-13,3.12421886542E-22,3.12421886542E-22,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.],
[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,2.40974996258E-09,0.,0.,0.,6.24874982189E-18,0.,2.49974996258E-09,1.24981242803E-13,2.49987497369E-09,9.99949988909E-05,5.00025016663E-05,4.99974994455E-05,0.000100015000498,0.000200007503736,0.000500012480188,0.000749982544221,0.00074999750359,0.00109999999404,0.00194999505766,0.00279999012128,0.00374998501502,0.00440004235134,0.00535003235564,0.00779997231439,0.00914998538792,0.0119999898598,0.0155499046668,0.0181499551982,0.020550088957,0.0252999607474,0.0286499708891,0.0318001359701,0.0378998816013,0.0385500453413,0.0427999980748,0.0456499196589,0.0458501279354,0.0469501055777,0.0490499846637,0.0502498932183,0.0487000197172,0.0476999878883,0.0438001416624,0.0443498045206,0.0375000610948,0.0364000499249,0.032100006938,0.029699973762,0.025099972263,0.0225998982787,0.0179499778897,0.0142999943346,0.0114500345662,0.00965000316501,0.00720005482435,0.00629999022931,0.00494999531657,0.00365002732724,0.00309997238219,0.00145003758371,0.00135003752075,0.0010500025237,0.000749982544221,0.000299999985145,0.000349989975803,0.000150002495502,5.00075002492E-05,0.000149997504195,4.99999987369E-05,4.68617212439E-26,4.99999987369E-05,1.24981242803E-13,3.12421886542E-22,3.12421886542E-22,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.],
[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,4.99999987369E-05,0.,0.000150000007125,4.99999987369E-05,9.99999974738E-05,0.00054999999702,0.000600000028498,0.00079999997979,0.001200000057,0.00150000001304,0.00270000007004,0.00334999989718,0.00430000014603,0.00499999988824,0.00784999970347,0.00980000011623,0.0136000001803,0.0137000000104,0.0168999992311,0.0186999998987,0.0251499991864,0.029149999842,0.0333999991417,0.0355999991298,0.036850001663,0.0446499995887,0.0454499982297,0.0478500016034,0.0487499982119,0.0515000000596,0.0511500015855,0.0485499985516,0.0473500005901,0.0470499992371,0.0419499985874,0.0394500009716,0.0359000004828,0.032049998641,0.0277999993414,0.0248000007123,0.0204000007361,0.0191500000656,0.0138499997556,0.0123500004411,0.00980000011623,0.00765000004321,0.00559999980032,0.00439999997616,0.00329999998212,0.00300000002608,0.00155000004452,0.00109999999404,0.000750000006519,0.00079999997979,0.000399999989895,0.00034999998752,0.,9.99999974738E-05,0.,9.99999974738E-05,0.,0.,0.,4.99999987369E-05,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.],#norma
[0.,0.,0.,0.,0.,0.,0.,1.56203118215E-26,0.,0.,0.,3.12437512299E-22,2.49974996258E-09,4.99999987369E-05,4.99974994455E-05,0.000100002500403,0.000149999992573,0.000249990000157,0.000550005002879,0.000899997539818,0.00105003244244,0.00210002018139,0.00330003490672,0.00515001500025,0.0069000152871,0.0107499854639,0.0148499552161,0.0196499526501,0.0244001112878,0.0304999761283,0.0358000807464,0.0433000028133,0.052549764514,0.0564001351595,0.0619000606239,0.0628501027822,0.0650499463081,0.0674498230219,0.0646999999881,0.063049890101,0.0568500123918,0.0493000894785,0.0436999052763,0.0360000170767,0.0313999913633,0.0229501184076,0.0193000212312,0.013199955225,0.0106999929994,0.00690004508942,0.00545000005513,0.00369995762594,0.0027499999851,0.00145001499914,0.00114999245852,0.000649992492981,0.000300002488075,0.00010000000475,0.000249997508945,0.000149992498336,2.49974996258E-09,1.2498750407E-13,1.56203118215E-26,2.49974996258E-09,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.]#disease
])

predictions = model(predict_dataset, training=False)
print("predictions")
print(predictions)

for i, logits in enumerate(predictions):
  class_idx = tf.argmax(logits).numpy() #color type "0", "1", "2"
  p = tf.nn.softmax(logits)[class_idx] #probability
  name = class_names[class_idx] #get name from class_names array
  print("Example {} prediction: {} ({:4.1f}%)".format(i, name, 100*p))

#random prediction from csv-file
#predictions from another dataset
test_dataset = get_dataset("./dataset/data_classifier_test.csv")
test_dataset = test_dataset.map(pack_features_vector)
test_accuracy = tf.keras.metrics.Accuracy()

for (x, y) in test_dataset:
  logits = model(x, training=False)
  prediction = tf.argmax(logits, axis=1, output_type=tf.int32)
  test_accuracy(prediction, y)

print("Test set accuracy: {:.3%}".format(test_accuracy.result()))
print(tf.stack([y,prediction],axis=1))
