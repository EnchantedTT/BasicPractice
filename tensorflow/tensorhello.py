import tensorflow as tf

hello = tf.Variable("Hello, tensorflow!")
init = tf.global_variables_initializer()

sess = tf.Session()
sess.run(init)
print sess.run(hello)

sess.close()
