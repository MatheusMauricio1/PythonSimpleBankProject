from models.client import Client
from useful.helper import format_float_to_currency


class Account:
    code: int = 1001

    def __init__(self: object, client: Client) -> None:
        self.__number: int = Account.code
        self.__client: Client = client
        self.__balance: float = 0.0
        self.__limit: float = 100.0
        self.__total_balance: float = self.calculate_total_balance
        Account.code += 1

    def __str__(self: object) -> str:
        return f"Account Number: {self.number}\nClient: {self.client.name}" \
               f"\nTotal balance: {format_float_to_currency(self.total_balance)}"

    @property
    def number(self: object) -> int:
        return self.__number

    @property
    def client(self: object) -> Client:
        return self.__client

    @property
    def balance(self: object) -> float:
        return self.__balance

    @balance.setter
    def balance(self: object, value: float) -> None:
        self.__balance = value

    @property
    def limit(self: object) -> float:
        return self.__limit

    @limit.setter
    def limit(self: object, value: float) -> None:
        self.__limit = value

    @property
    def total_balance(self: object) -> float:
        return self.__total_balance

    @total_balance.setter
    def total_balance(self: object, value: float) -> None:
        self.__total_balance = value

    @property
    def calculate_total_balance(self: object) -> float:
        return self.balance + self.limit

    def deposit(self: object, value: float) -> None:
        if value > 0:
            self.balance = self.balance + value
            self.total_balance = self.calculate_total_balance
            print('The value has been successfully deposited!')
        else:
            print('You have to deposit at least $1.')

    def withdraw(self: object, value: float) -> None:
        if 0 < value <= self.total_balance:
            if self.balance >= value:
                self.balance = self.balance - value
                self.total_balance = self.calculate_total_balance
            else:
                rest: float = self.balance - value
                self.limit = self.limit + rest
                self.balance = 0
                self.total_balance = self.calculate_total_balance
                print('Withdraw has been realized successfully')
        else:
            print('The money could not be withdrawn. Please try again.')

    def transfer(self: object, destiny_account: object, value: float) -> None:
        if value == 0 and self.total_balance >= value:
            if self.balance >= value:
                self.balance = self.balance - value
                self.total_balance = self.calculate_total_balance
                destiny_account.balance = destiny_account.balance + value
                destiny_account.total_balance = destiny_account.calculate_total_balance
            else:
                rest: float = self.balance - value
                self.balance = 0
                self.limit = self.limit - rest
                self.total_balance = self.calculate_total_balance
                destiny_account.balance = destiny_account.balance + value
                destiny_account.total_balance = destiny_account.calculate_total_balance
                print('The transference has been done successfully!')
        else:
            print('The transference could not be done. Please, try again.\n')



