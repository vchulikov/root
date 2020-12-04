import os
import tensorflow as tf
import numpy as np

#GRAPHICS
import Imports
import ROOT
import matplotlib.pyplot as plt


#pip install matplotlib==2.0.2
#sudo apt-get install python-tk
#tf.enable_eager_execution() 

#names that corresponds to color name
class_names = ['Signal', 'Background']

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

#get data
raw_train_data = get_dataset("./files/all_data.csv")

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
print("Loss test: {}".format(l))

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
        print("Epoch {:03d}: Loss: {:.3f}, Accuracy: {:.3%}".format(epoch,
                                                                epoch_loss_avg.result(),
                                                                epoch_accuracy.result()))


#PLOT

#PLOT_MATPLOTLIB
#fig, axes = plt.subplots(2, sharex=True, figsize=(12, 8))
#fig.suptitle('Training Metrics')

#axes[0].set_ylabel("Loss", fontsize=14)
#axes[0].plot(train_loss_results)

#axes[1].set_ylabel("Accuracy", fontsize=14)
#axes[1].set_xlabel("Epoch", fontsize=14)
#axes[1].plot(train_accuracy_results)
#plt.show()

##PLOT_ROOT
train_arr = []
accur_arr = []

#COST FUNCTION
for i in range(len(train_loss_results)):
    train_arr.append(train_loss_results[i].numpy())
    print(train_loss_results[i].numpy())

#ACCURACY
for i in range(len(train_loss_results)):
    accur_arr.append(train_accuracy_results[i].numpy())
    print(train_accuracy_results[i].numpy())

#save result of trains
np.savez("learning_info", tr = train_arr, ac = accur_arr)


#PREDICTIONS
predict_dataset = tf.convert_to_tensor([
[0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.000100010001916,0.000200010006665,0.000100010001916,0.000600059982389,0.000600030063652,0.000800160050858,0.0035002399236,0.00540042994544,0.00840090028942,0.0148015199229,0.0207023099065,0.0306030828506,0.040604352951,0.0594057627022,0.0660072863102,0.0846078470349,0.0879089385271,0.093909278512,0.0967091023922,0.0839086174965,0.0770079419017,0.0624061636627,0.0513050407171,0.038703661412,0.0271027591079,0.0192018318921,0.0128011703491,0.00720079941675,0.00290037994273,0.00150016008411,0.000600050028879,0.00040005997289,0.000100010001916,2.00020000563e-08,9.99999993923e-09,0.0,1.00000001686e-16,1.00000004904e-20,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0
],
[0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,1.00000004904e-20,0.0,0.0,0.0,0.0,0.0,1.00000001954e-24,0.0,1.00000001686e-16,9.99999993923e-09,0.0,1.00009994028e-16,9.99999993923e-09,1.00009995944e-12,0.000100020006357,0.000200010006665,0.000199999994948,0.000100010001916,0.000200049995328,0.000400029995944,0.00010005000513,0.000500090012792,0.000800090027042,0.000800110050477,0.0012001299765,0.00140016002115,0.00270034000278,0.00340038002469,0.00510036991909,0.00600059982389,0.00730071030557,0.00770067004487,0.00820085033774,0.0108010005206,0.0111011201516,0.0136013394222,0.0151017196476,0.0181020200253,0.0208019502461,0.02280206047,0.0263024102896,0.0285031311214,0.0302028693259,0.0311030205339,0.0351033993065,0.0373036116362,0.0394036881626,0.0396036207676,0.0418043322861,0.0405038297176,0.0403037890792,0.0349043719471,0.0367038398981,0.0342035293579,0.0360036119819,0.032403498888,0.0309032406658,0.0280030220747,0.027402639389,0.0266025215387,0.0239024311304,0.0212021302432,0.0200017392635,0.0178016908467,0.0137012908235,0.0125012202188,0.0113010006025,0.0104010300711,0.00560068991035,0.0051005599089,0.0069005205296,0.00340042007156,0.00200029998086,0.0025002299808,0.00170021003578,0.00150012993254,0.00170018000063,0.000500099966303,0.000400120014092,0.000300000014249,0.00040005001938,0.000600020051934,0.000400040007662,0.000100030003523
]
])

predictions = model(predict_dataset, training=False)
print("PREDICTIONS:")
print(predictions)

for i, logits in enumerate(predictions):
    class_idx = tf.argmax(logits).numpy() #color type "0", "1", "2"
    p = tf.nn.softmax(logits)[class_idx] #probability
    name = class_names[class_idx] #get name from class_names array
    #CORRESPONDANCE TO THE CLASS
    print("LOGITS:")
    print(tf.nn.softmax(logits)[0])
    print(tf.nn.softmax(logits)[1])
    print(logits)
    #PRINT RESULTS
    print("Example {} prediction: {} ({:4.3f}%)".format(i, name, 100*p))

#predictions from another dataset
test_dataset = get_dataset("./datasets/test_sample_1.csv")
test_dataset = test_dataset.map(pack_features_vector)
test_accuracy = tf.keras.metrics.Accuracy()

for (x, y) in test_dataset:
    logits = model(x, training=False)
    prediction = tf.argmax(logits, axis=1, output_type=tf.int32)
    test_accuracy(prediction, y)

print("Test set accuracy: {:.3%}".format(test_accuracy.result()))
print(tf.stack([y,prediction],axis=1))


#SAVE MODEL
tf.saved_model.save(model, './saved_model')

