'''
    Date: Feb 1, 2018
    Author: Paras Maharjan
    Class: Pyhton and Deep Learning
    Lab Assignment: 1
    Problem: 3

    Given a list of n number, write a Python program to find triplets in the list which gives the sum of zero.

'''

def main():
    print('Program started...')
    print('Program to find the triplet that sums to zero\n\r')

    # Input the size of the number user want to enter
    length = int(input('Enter the number of list you want as input: '))

    # Close the program if the input size of list is less than 3
    if length < 3:
        print('The size of list must be greater than or equal to 3')
        return

    # Create empty list
    n_list = []

    for i in range(1, length+1):
        dummy = int(input('Enter number: '))
        # Create the list by appending the number to the above created list
        n_list.append(dummy)

    # make the unique list of the above number = no repetition
    n_set = set(sorted(n_list))

    # Sort the list from lower to higher just for ease to the user
    number = sorted(n_set)

    # Display the uniquely ordered number
    #print(number)

    # find the possible triplets that sums to zero
    triplet(number)

def test():
    print('Test program started...')

    # Make the list of predefined number
    n_list = [1, 3, 6, 2, -1, 2, 8, -2, -4]

    # make the unique list of the above number = no repetition
    n_set = set(sorted(n_list))

    # Sort the list from lower to higher just for ease to the user
    number = sorted(n_set)

    # Display the uniquely ordered number
    #print(number)

    # Find the possible triplets that sums to zero
    triplet(number)

# This function makes the set of all the possible triplets and then finds if sum of all the element of triple is zero
def triplet(n):
    length = len(n)

    # The three loop here iterates through every element of the list to make the possible triples
    for i in range(0, length):
        for j in range(i+1, length):
            for k in range(j+1, length):
                # Display all the possible triplets
                # print(i+1,',',j+1,',',k+1)

                # Sum the elements
                t_sum = n[i] + n[j] + n[k]

                # Check if the sum is zero
                if t_sum == 0:
                    # Display the triplets that sums to zero
                    print('Triplets sum to zero found: [', n[i], ',', n[j], ',', n[k], ']')

if __name__ == "__main__":
    main()
    #test()