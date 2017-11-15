import tensorflow as tf

node1 = tf.constant(1, dtype=tf.float32)
node2 = tf.constant(2.0)
print(node1, node2)
add = tf.add(node1, node2)
sess = tf.Session()
print(add)
print(sess.run(add))