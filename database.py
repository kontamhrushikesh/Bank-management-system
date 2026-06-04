# Database Management Banking - MongoDB

from pymongo import MongoClient # type: ignore

client = MongoClient("mongodb://localhost:27017/")

db = client["bank"]

customers_collection = db["customers"]
transactions_collection = db["transactions"]


def createcustomertable():
    """
    MongoDB does not create tables.
    Collections are created automatically.
    We create indexes instead.
    """

    customers_collection.create_index(
        "username",
        unique=True
    )

    customers_collection.create_index(
        "account_number",
        unique=True
    )


def get_customer_by_username(username):

    return customers_collection.find_one(
        {"username": username}
    )


def get_customer_by_account_number(account_number):

    return customers_collection.find_one(
        {"account_number": account_number}
    )


def insert_customer(customer_data):

    return customers_collection.insert_one(
        customer_data
    )


def update_customer_balance(
        username,
        new_balance):

    return customers_collection.update_one(
        {"username": username},
        {"$set": {"balance": new_balance}}
    )


def insert_transaction(
        transaction_data):

    return transactions_collection.insert_one(
        transaction_data
    )


if __name__ == "__main__":

    createcustomertable()

    print("MongoDB Connected Successfully")