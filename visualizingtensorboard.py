import tensorflow as tf

x = tf.constant(5, name='x')

y = tf.constant(6, name='y')

s = tf.add(x,y, name='sum')

with tf.Session() as sess:
	
	writer = tf.summary.FileWriter('./graphs',sess.graph)

	print(sess.run(s))

writer.close()
