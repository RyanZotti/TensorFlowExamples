import tensorflow as tf

#define a variable to hold normal random values
normal_rv = tf.Variable( tf.truncated_normal([2,3],stddev = 0.1))

#initialize the variable
init_op = tf.initialize_all_variables()

#run the graph
with tf.Session() as sess:
    sess.run(init_op) #execute init_op
    #print the random values that we sample
    print (sess.run(normal_rv))

'''
prints:

[[ 0.03907356 -0.07167048 -0.11734595]
 [ 0.08760806 -0.16870497 -0.0474607 ]]

'''