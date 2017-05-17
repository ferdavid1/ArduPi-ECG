import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
rng = np.random

values = pd.read_table('../Real_Values.txt')
# Parameters
learning_rate = 0.01
training_epochs = 3000
display_step = 50

# Training Data
train_size = int(len(values)*0.5) 
test_size = len(values) - train_size

train_X = values[0:(train_size -10)]
train_Y = values[train_size:(len(values)-11)]

n_samples = train_X.shape[0]

# tf Graph Input
X = tf.placeholder("float")
Y = tf.placeholder("float")

# Set model weights
W = tf.Variable(rng.randn(), name="weight")
b = tf.Variable(rng.randn(), name="bias")

# Construct a linear model
pred = tf.add(tf.multiply(X, W), b)

# Mean squared error
cost = tf.reduce_sum(tf.pow(pred-Y, 2))/(2*n_samples)

# Gradient descent
#  Note, minimize() knows to modify W and b because Variable objects are trainable=True by default
optimizer = tf.train.GradientDescentOptimizer(learning_rate).minimize(cost)

# Initializing the variables
init = tf.global_variables_initializer()

# Launch the graph
with tf.Session() as sess:
    sess.run(init)

    # Fit all training data
    for epoch in range(training_epochs):
        for (x, y) in zip(train_X, train_Y):
            sess.run(optimizer, feed_dict={X: x, Y: y})

        # Display logs per epoch step
        if (epoch+1) % display_step == 0:
            c = sess.run(cost, feed_dict={X: train_X, Y:train_Y})
            print("Epoch:", '%04d' % (epoch+1), "cost=", "{:.9f}".format(c), \
                "W=", sess.run(W), "b=", sess.run(b))

    print("Optimization Finished!")
    training_cost = sess.run(cost, feed_dict={X: train_X, Y: train_Y})
    print("Training cost=", training_cost, "W=", sess.run(W), "b=", sess.run(b), '\n')
    predicted = sess.run(W) * train_X + sess.run(b)
    # Graphic display
    plt.plot(train_X, train_Y, 'ro', label='Original data')
    plt.plot(train_X, predicted, label='Fitted line')
    plt.ylabel('BPM')
    plt.xlabel('Sample')
    plt.title('Neural Net Regression - Predicted over Training')
    plt.legend()
    plt.savefig('NN_LR_train.png')
    plt.show()

    # Testing 
    test_X = values[(train_size -10):train_size]
    test_Y = values[(len(values)-10): len(values)]  

    print("Testing... (Mean square loss Comparison)")
    testing_cost = sess.run(
        tf.reduce_sum(tf.pow(pred - Y, 2)) / (2 * test_X.shape[0]),
        feed_dict={X: test_X, Y: test_Y})  # same function as cost above
    print("Testing cost=", testing_cost)
    print("Absolute mean square loss difference:", abs(
        training_cost - testing_cost))

    plt.plot(test_X, test_Y, 'bo', label='Testing data')
    plt.plot(train_X, sess.run(W) * train_X + sess.run(b), label='Fitted line')
    plt.ylabel('BPM')
    plt.xlabel('Sample')
    plt.title('Neural Net Regression - Predicted over Test')
    plt.savefig('NN_LR_test.png')
    plt.legend()
    plt.show()
    with open('PredValues.txt', 'w') as pred:
        for line in predicted.get_values():
            pred.write(str(line).strip('[ ]') + '\n')