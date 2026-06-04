# User Registration Signin Signup - MongoDB Version

from customer import Customer
from bank import Bank
from database import customers_collection
import random


def SignUp():
    username = input("Create Username: ")

    temp = customers_collection.find_one(
        {"username": username}
    )

    if temp:
        print("Username Already Exists")
        SignUp()

    else:
        print("Username is Available Please Proceed")

        password = input("Enter Your Password: ")
        name = input("Enter Your Name: ")
        age = input("Enter Your Age: ")
        city = input("Enter Your City: ")

        while True:
            account_number = random.randint(10000000, 99999999)

            temp = customers_collection.find_one(
                {"account_number": account_number}
            )

            if temp:
                continue

            else:
                print("Your Account Number", account_number)
                break

        cobj = Customer(username, password, name, age, city, account_number)
        cobj.createuser()

        bobj = Bank(username, account_number)
        bobj.create_transaction_table()


def SignIn():
    username = input("Enter Username: ")

    temp = customers_collection.find_one(
        {"username": username}
    )

    if temp:
        while True:
            password = input(
                f"Welcome {username.capitalize()} Enter Password: "
            )

            if temp["password"] == password:
                print("Sign IN Successfully")
                return username

            else:
                print("Wrong Password Try Again")
                continue

    else:
        print("Enter Correct Username")
        return SignIn()