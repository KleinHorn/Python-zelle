# A simple program illustrating chaotic behavior.


def main():
    print("This program illustrates a chaotic function")
    x = eval(input("Enter a number between 0 and 1: "))
    num_of_rand = eval(input("How many numbers would you like to receive back?: "))
    for i in range(num_of_rand):
        x = 3.0 * x * (1 - x)
        print(x)


main()
