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
Y = tf.placeholder(tf.float32, name='Price')
Z = tf.placeholder(tf.float32, name='Avg_Area_Number_of_rooms')

# Step 3: create weight and bias, initialized to 0
w2 = tf.Variable(0.0, name='weights2')
b2 = tf.Variable(0.0, name='bias2')

# Step 4: build model to predict Y
Y_predicted2 = Z * w2 + b2

# Step 5: use the square error as the loss function
loss2 = tf.square(Y - Y_predicted2, name='loss2')

# Step 6: using gradient descent with learning rate of 0.01 to minimize loss
optimizer2 = tf.train.GradientDescentOptimizer(learning_rate=0.0001).minimize(loss2)


with tf.Session() as sess2:
    # Step 7: initialize the necessary variables, in this case, w and b
    sess2.run(tf.global_variables_initializer())

    writer2 = tf.summary.FileWriter('./graphs/linear_reg', sess2.graph)

    # Step 8: train the model
    for i in range(2):  # train the model 50 epochs
        total_loss = 0
        for _, _, z, _, _, y,_ in data:
            # print(x,y)
            # Session runs train_op and fetch values of loss
            _, l = sess2.run([optimizer2, loss2], feed_dict={Z: z, Y: y})
            total_loss += l
        print('Epoch {0}: {1}'.format(i, total_loss / n_samples))

    # close the writer when you're done using it
    writer2.close()

    # Step 9: output the values of w and b
    w2, b2 = sess2.run([w2, b2])

print("w2 = ", w2, "b = ", b2)

# plot the results
Z, Y = np.float32(data.T[2]), np.float32(data.T[5])
print(Z)
plt.figure(2)
plt.plot(Z, Y, 'bo', label='Real data')
plt.plot(Z, Z * w2 + b2, 'r', label='Predicted data')
plt.legend()
plt.title("Avg. Area Number of Rooms vs. Price")
plt.xlabel('Avg. Area Number of Rooms')
plt.ylabel('Price')
plt.show()