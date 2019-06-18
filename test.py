import tensorflow as tf

flags = tf.flags
FLAGS = flags.FLAGS

flags.DEFINE_integer(
    "number", 10,
    "The config json file corresponding to the pre-trained BERT model. "
    "This specifies the model architecture.")
print(FLAGS.number)