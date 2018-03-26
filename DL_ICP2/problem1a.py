import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
import xlrd

DATA_FILE = 'USA_Housing.xls'

# Step 1: read in data from the .xls file
book = xlrd.open_workbook(DATA_FILE, encoding_override="utf-8")
sheet = book.sheet_by_index(0)
n_samples = sheet.nrows - 1
data = np.asarray([sheet.row_values(i) for i in range(1, sheet.nrows)])

# Step 2: create placeholders for input X (number of fire) and label Y (number of theft)
X = tf.placeholder(tf.float32, name='Avg_Area_House_Age')
Y = tf.placeholder(tf.float32, name='Price')
Z = tf.placeholder(tf.float32, name='Avg_Area_Number_of_rooms')

# Step 3: create weight and bias, initialized to 0
w1 = tf.Variable(0.0, name='weights1')
b1 = tf.Variable(0.0, name='bias1')
w2 = tf.Variable(0.0, name='weights2')
b2 = tf.Variable(0.0, name='bias2')

# Step 4: build model to predict Y
Y_predicted1 = X * w1 + b1
Y_predicted2 = Z * w2 + b2

# Step 5: use the square error as the loss function
loss1 = tf.square(Y - Y_predicted1, name='loss1')
loss2 = tf.square(Y - Y_predicted2, name='loss2')
# Step 6: using gradient descent with learning rate of 0.01 to minimize loss
optimizer1 = tf.train.GradientDescentOptimizer(learning_rate=0.0001).minimize(loss1)
optimizer2 = tf.train.GradientDescentOptimizer(learning_rate=0.0001).minimize(loss2)

with tf.Session() as sess1:
    # Step 7: initialize the necessary variables, in this case, w and b
    sess1.run(tf.global_variables_initializer())

    writer1 = tf.summary.FileWriter('./graphs/linear_reg', sess1.graph)

    # Step 8: train the model
    for i in range(2):  # train the model 50 epochs
        total_loss = 0
        for _, x, _, _, _, y,_ in data:
            # print(x,y)
            # Session runs train_op and fetch values of loss
            _, l = sess1.run([optimizer1, loss1], feed_dict={X: x, Y: y})
            total_loss += l
        print('Epoch {0}: {1}'.format(i, total_loss / n_samples))

    # close the writer when you're done using it
    writer1.close()

    # Step 9: output the values of w and b
    w1, b1 = sess1.run([w1, b1])

print("w1 = ", w1, "b = ", b1)

# plot the results
X, Y = np.float32(data.T[1]), np.float32(data.T[5])
print(X)
plt.figure(1)
plt.plot(X, Y, 'bo', label='Real data')
plt.plot(X, X * w1 + b1, 'r', label='Predicted data')
plt.legend()
plt.title("Avg. Area House Age vs. Price")
plt.xlabel('Avg. Area House Age')
plt.ylabel('Price')
plt.show()