'''A mudule or script dealing prime numbers'''

def prime_list(input_n):
    '''Return all the prime number u<= n as a list'''
    a=list(range(1,input_n+1))
    j=1
    while j <= len(a):
        A=a.copy()
        for i in range(len(a[j+1:])):
            if a[i+j+1] % a[j] == 0:
                A.remove(a[i+j+1])
        a = A
        j+=1
    a.remove(1)
    return a

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('integers', metavar='N', type=int, nargs='+', \
                        help='an integer for the accumulator')

    args = parser.parse_args()
    n = args.integers[0]
    print(prime_list(n))
    print(f'{len(prime_list(n))} prime number(s) in total')
