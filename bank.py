# Bank Services - MongoDB Version

from database import customers_collection, transactions_collection
import datetime


class Bank:
    def __init__(self, username, account_number):
        self.__username = username
        self.__account_number = account_number

    def create_transaction_table(self):
        """
        MongoDB does not need separate transaction tables.
        We use one transactions collection for all users.
        """
        transactions_collection.create_index("username")
        transactions_collection.create_index("account_number")

    def balanceequiry(self):
        customer = customers_collection.find_one(
            {"username": self.__username}
        )

        if customer:
            print(f"{self.__username} Balance is {customer['balance']}")
        else:
            print("Customer not found")

    def deposit(self, amount):
        customer = customers_collection.find_one(
            {"username": self.__username}
        )

        if not customer:
            print("Customer not found")
            return

        new_balance = customer["balance"] + amount

        customers_collection.update_one(
            {"username": self.__username},
            {"$set": {"balance": new_balance}}
        )

        self.balanceequiry()

        transactions_collection.insert_one({
            "timedate": datetime.datetime.now(),
            "username": self.__username,
            "account_number": self.__account_number,
            "remarks": "Amount Deposit",
            "amount": amount
        })

        print(
            f"{self.__username} Amount is Successfully Deposited into Your Account {self.__account_number}"
        )

    def withdraw(self, amount):
        customer = customers_collection.find_one(
            {"username": self.__username}
        )

        if not customer:
            print("Customer not found")
            return

        current_balance = customer["balance"]

        if amount > current_balance:
            print("Insufficient Balance Please Deposit Money")

        else:
            new_balance = current_balance - amount

            customers_collection.update_one(
                {"username": self.__username},
                {"$set": {"balance": new_balance}}
            )

            self.balanceequiry()

            transactions_collection.insert_one({
                "timedate": datetime.datetime.now(),
                "username": self.__username,
                "account_number": self.__account_number,
                "remarks": "Amount Withdraw",
                "amount": amount
            })

            print(
                f"{self.__username} Amount is Successfully Withdrawn from Your Account {self.__account_number}"
            )

    def fundtransfer(self, receive, amount):
        sender = customers_collection.find_one(
            {"username": self.__username}
        )

        if not sender:
            print("Sender account not found")
            return

        if amount > sender["balance"]:
            print("Insufficient Balance Please Deposit Money")
            return

        receiver = customers_collection.find_one(
            {"account_number": receive}
        )

        if not receiver:
            print("Account Number Does not Exist")
            return

        sender_new_balance = sender["balance"] - amount
        receiver_new_balance = receiver["balance"] + amount

        customers_collection.update_one(
            {"username": self.__username},
            {"$set": {"balance": sender_new_balance}}
        )

        customers_collection.update_one(
            {"account_number": receive},
            {"$set": {"balance": receiver_new_balance}}
        )

        receiver_username = receiver["username"]

        self.balanceequiry()

        transactions_collection.insert_one({
            "timedate": datetime.datetime.now(),
            "username": receiver_username,
            "account_number": receive,
            "remarks": f"Fund Transfer From {self.__account_number}",
            "amount": amount
        })

        transactions_collection.insert_one({
            "timedate": datetime.datetime.now(),
            "username": self.__username,
            "account_number": self.__account_number,
            "remarks": f"Fund Transfer -> {receive}",
            "amount": amount
        })

        print(
            f"{self.__username} Amount is Successfully Transferred from Your Account {self.__account_number}"
        )