import tensorflow as tf

model = tf.saved_model.load('./', tags=None)

class_names = ['Disease', 'Normal']
predict_dataset = tf.convert_to_tensor([
[0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.000100010001916,0.000200010006665,0.000100010001916,0.000600059982389,0.000600030063652,0.000800160050858,0.0035002399236,0.00540042994544,0.00840090028942,0.0148015199229,0.0207023099065,0.0306030828506,0.040604352951,0.0594057627022,0.0660072863102,0.0846078470349,0.0879089385271,0.093909278512,0.0967091023922,0.0839086174965,0.0770079419017,0.0624061636627,0.0513050407171,0.038703661412,0.0271027591079,0.0192018318921,0.0128011703491,0.00720079941675,0.00290037994273,0.00150016008411,0.000600050028879,0.00040005997289,0.000100010001916,2.00020000563e-08,9.99999993923e-09,0.0,1.00000001686e-16,1.00000004904e-20,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0
],
[0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,1.00000004904e-20,0.0,0.0,0.0,0.0,0.0,1.00000001954e-24,0.0,1.00000001686e-16,9.99999993923e-09,0.0,1.00009994028e-16,9.99999993923e-09,1.00009995944e-12,0.000100020006357,0.000200010006665,0.000199999994948,0.000100010001916,0.000200049995328,0.000400029995944,0.00010005000513,0.000500090012792,0.000800090027042,0.000800110050477,0.0012001299765,0.00140016002115,0.00270034000278,0.00340038002469,0.00510036991909,0.00600059982389,0.00730071030557,0.00770067004487,0.00820085033774,0.0108010005206,0.0111011201516,0.0136013394222,0.0151017196476,0.0181020200253,0.0208019502461,0.02280206047,0.0263024102896,0.0285031311214,0.0302028693259,0.0311030205339,0.0351033993065,0.0373036116362,0.0394036881626,0.0396036207676,0.0418043322861,0.0405038297176,0.0403037890792,0.0349043719471,0.0367038398981,0.0342035293579,0.0360036119819,0.032403498888,0.0309032406658,0.0280030220747,0.027402639389,0.0266025215387,0.0239024311304,0.0212021302432,0.0200017392635,0.0178016908467,0.0137012908235,0.0125012202188,0.0113010006025,0.0104010300711,0.00560068991035,0.0051005599089,0.0069005205296,0.00340042007156,0.00200029998086,0.0025002299808,0.00170021003578,0.00150012993254,0.00170018000063,0.000500099966303,0.000400120014092,0.000300000014249,0.00040005001938,0.000600020051934,0.000400040007662,0.000100030003523
]
])

predictions = model(predict_dataset, training=False)

for i, logits in enumerate(predictions):
  class_idx = tf.argmax(logits).numpy()
  p = tf.nn.softmax(logits)[class_idx] #probability
  name = class_names[class_idx]
  print("Example {} prediction: {} ({:4.3f}%)".format(i, name, 100*p))
