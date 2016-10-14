import tensorflow as tf

hello = tf.Variable("Hello, f**k")
init = tf.initialize_all_variables()

sess = tf.Session()
sess.run(init)
print sess.run(hello)

sess.close()