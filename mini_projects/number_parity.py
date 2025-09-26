def main():
    x = int(input('Write a number: '))
    if is_even(x):
        print(f'{x} is an even number')
    else:
        print(f'{x} is an odd number')

def is_even(n):
   return n % 2 == 0

main()