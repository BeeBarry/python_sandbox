# Write how many times you say "hello" and you will see the echo appear in your terminal!

def main():
    number = get_number()
    hello(number)

def get_number():
    while True:
        n = int(input('How many times do you want to say "hello"?: '))
        if n > 0:
            break
    return n

def hello(number):
    for _ in range(number):
        print('hello')

main()