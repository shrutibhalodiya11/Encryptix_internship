import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    
    pwd = ''.join(random.choice(characters) for i in range(length))
    
    return pwd

def main():
    try:
        length = int(input("Enter the desired length of your password: "))
    except ValueError:
        print("Length should be a positive integer.")
        return
    
    pwd = generate_password(length)
    
    print("Your generated password is:", pwd)

if __name__ == "__main__":
    main()
