def main():
    print('Program started...')
    l = int(input('Enter the number of list you want as input: '))
    n_list = []
    for i in range(1,l+1):
        dummy = int(input('Enter number: '))
        n_list.append(dummy)
    n_set = set(sorted(n_list))
    number = sorted(n_set)
    print(number)
    # find the possible triplets that sums to zero
    triplet(number)

def triplet(n):
    l = len(n)
    t = []
    for i in range(0, l):
        for j in range(i+1, l):
            for k in range(j+1, l):
                #print(i+1,',',j+1,',',k+1)
                t_sum = n[i] + n[j] + n[k]
                if t_sum == 0:
                    print('Triplets sum to zero found: [',n[i],',', n[j],',', n[k],']')
def test():
    print('Test program started...')

    n_list = [1,3,6,2,-1,2,8,-2,-4]
    # make tg=he unique list of the above number
    n_set = set(sorted(n_list))
    number = sorted(n_set)
    print(number)
    #find the possible triplets that sums to zero
    triplet(number)

if __name__ == "__main__":
    main()
    #test()