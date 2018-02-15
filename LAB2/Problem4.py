# import the numpy module
import numpy as np

def main():
    # Create the numpy array of random integer of size 15 between 0-20
    random_integer = np.random.randint(20, size=15)
    print(random_integer)

    # Finds the unique data sets and it's number of repetition
    # Set return_counts to True return the number of counts for unique data entries
    unique_data, repetition = np.unique(random_integer, return_counts=True)

    # Create the dictionary of the unique data and its repetition
    # zip function is used for array comprehension by making pair of two or more entries
    dict_integer = dict(zip(unique_data, repetition))
    print(dict_integer)

    # Loop through all the items of dictionary
    for k, v in dict_integer.items():
        # Check if the value of each item is equal to the max value of the dictionary
        if v == max(dict_integer.values()):
            # Print the max key value pair
            print('max value: ', k, ':',v)

if __name__ == '__main__':
    main()