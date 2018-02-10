# Import the numpy module
import numpy as np

def main():
    # Create a random variable of 10x10 matrix
    a = 10*np.random.random((10,10))

    # For ease rounding the random float value upto hundredth decimal
    a = np.round(a,2)
    print(a)

    # Find the minimum value of the array
    min_val = a.min(axis=1)
    print('min value: ', min_val)

    # Find the maximum value of the array
    max_val = a.max(axis=1)
    print('max value: ', max_val)

if __name__ == "__main__":
    main()

