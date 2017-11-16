import tensorflow as tf 
import sys

# model parameters 
W = tf.Variable([.3], tf.float32)
b = tf.Variable([-.3], tf.float32)

# model input & output
x = tf.placeholder(tf.float32)
linear_mode = W * x + b
y = tf.placeholder(tf.float32)

# loss
loss = tf.reduce_sum(tf.square(linear_mode - y)) # sum of the squares

# optimizer
optimizer = tf.train.GradientDescentOptimizer(0.01)
train = optimizer.minimize(loss)

# train data
x_train = [1, 2, 3, 4]
y_train = [0, -1, -2, -3]

# train loop
init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)
for i in range(1000):
    sess.run(train, {x: x_train, y: y_train})

# evaluate training accuracy
print(sess.run([W, b]))
cur_W, cur_b, cur_loss = sess.run([W, b, loss], {x: x_train, y: y_train})
print("W: %s, b: %s, loss: %s" % (cur_W, cur_b, cur_loss))
sys.exit(0)

# snippets...
print(sess.run(linear_mode, {x: [1, 2, 3, 4]}))
print(sess.run(loss, {x: [1, 2, 3, 4], y: [0, -1, -2, -3]}))

sess.run(init) # reset to default
fixW = tf.assign(W, [-1.])
fixb = tf.assign(b, [1.])
sess.run([fixW, fixb])
print(sess.run(loss, {x: [1, 2, 3, 4], y: [0, -1, -2, -3]}))


