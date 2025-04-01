import json


def extract_even_numbers(my_list):
    result_list = []

    for number in my_list:
        if number % 2 == 0:
            result_list.append(number)

    return result_list


def extract_odd_numbers(my_list):
    result_list = []

    for number in my_list:
        # check if number is even
        if not number % 2 == 0:
            result_list.append(number)

    return result_list


def build_dict(my_list):
    # creates a dictionary with two keys: "odd" and "even" that  contains all the odd and even numbers from my_list and returns it

    odd_numbers = extract_odd_numbers(my_list)
    even_numbers = extract_even_numbers(my_list)

    result = {
        "odd": odd_numbers,
        "even": even_numbers
    }
    return result


def save_dict_to_json(my_dict, file_name):
    with open(file_name, "w") as file:
        json.dump(my_dict, file)

class Dog:

    weight = "4kg"

    def __init__(self, name, legs, age):
        self.name = name
        self.legs = legs
        self.age = age

    def __str__(self):
        return "Dog - {name}, {legs} legs, {age} years of age.".format(name=self.name, legs=self.legs, age=self.age)

    def to_string(self):
        return "This dog's name is {name}, it has {legs} legs, and is of {age} years of age.".format(name=self.name, legs=self.legs, age=self.age)

    @classmethod
    def bark(cls):
        return "Woof Woof!"

    @classmethod
    def from_string(cls, dog_string):
        name, legs, age = dog_string.split("-")
        return cls(name, int(legs), int(age))

    @staticmethod
    def is_adult(age):
        if age > 4:
            return True
        else:
            return False

class Heap:
    def __init__(self):
        self.__heap = []

    def push(self, e):
        self.__heap.append(e)

    def pop(self):
        return self.__heap.pop()

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.__heap[-1]

    def size(self):
        return len(self.__heap)

    def is_empty(self):
        return len(self.__heap) == 0



class BankAccount:

    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        if amount > 0:
            self.balance = self.balance + amount
        else:
            print("Amount must be greater than 0!")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance = self.balance - amount
        else:
            print("Amount is too great to withdraw from account!")


class Bank:
    def __init__(self):
        self.name = "ING"
        self.account = BankAccount()
        self.savings_account = BankAccount()

    def deposit(self, amount):
        self.account.deposit(amount)

    def withdraw(self, amount):
        self.account.withdraw(amount)

    def deposit_savings(self, amount):
        self.savings_account.deposit(amount)

    def withdraw_savings(self, amount):
        self.savings_account.withdraw(amount)

    def get_total_amount(self):
        return self.account.balance + self.savings_account.balance