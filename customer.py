# Customer Details

from database import insert_customer


class Customer:

    def __init__(
        self,
        username,
        password,
        name,
        age,
        city,
        account_number
    ):

        self.__username = username
        self.__password = password
        self.__name = name
        self.__age = age
        self.__city = city
        self.__account_number = account_number

    def createuser(self):

        customer_data = {
            "username": self.__username,
            "password": self.__password,
            "name": self.__name,
            "age": self.__age,
            "city": self.__city,
            "balance": 0,
            "account_number": self.__account_number,
            "status": 1
        }

        insert_customer(customer_data)