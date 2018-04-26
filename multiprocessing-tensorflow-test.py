import tensorflow as tf
# Creates a graph.
with tf.device('/cpu:0'):  
"""We can run it on a gpu if it is configured for gpu Now only available device is cpu:0 """ 
	a = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], name='a')
	b = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], name='b') 
	c = tf.add(a,b)
# Creates a session with log_device_placement set to True.
sess = tf.Session(config=tf.ConfigProto(log_device_placement=True))
# Runs the op.
print (sess.run(c))
