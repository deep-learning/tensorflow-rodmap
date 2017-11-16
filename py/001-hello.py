import tensorflow as tf

node1 = tf.constant(1, dtype=tf.float32)
node2 = tf.constant(2.0)
print(node1, node2)
add = tf.add(node1, node2)
print(add)

# A placeholder is a promise to provide a value later
a = tf.placeholder(tf.float32)
b = tf.placeholder(tf.float32)
adder_node = a + b # shortcut for tf.add(a, b)
sess = tf.Session()
print(sess.run(node1))
print(sess.run(add))
print(sess.run(adder_node, {a: 3, b: 4.5}))
print(sess.run(adder_node, {a: [1, 3], b: [2, 4]}))

add_and_triple = adder_node * 3
print(sess.run(add_and_triple, {a: 3, b: 4.5}))