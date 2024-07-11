def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero"

def main():
    print("Welcome to Simple Calculator!")

    while True:
        print("\nOperations:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice in ('1', '2', '3', '4'):
            try:
                n1 = float(input("Enter first number: "))
                n2 = float(input("Enter second number: "))

                if choice == '1':
                    print(f"{n1} + {n2} = {add(n1, n2)}")
                elif choice == '2':
                    print(f"{n1} - {n2} = {sub(n1, n2)}")
                elif choice == '3':
                    print(f"{n1} * {n2} = {mul(n1, n2)}")
                elif choice == '4':
                    print(f"{n1} / {n2} = {div(n1, n2)}")

            except ValueError:
                print("Invalid input. Please enter valid numbers.")
        
        elif choice == '5':
            print("Exiting...")
            break
        
        else:
            print("Invalid input. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    main()
