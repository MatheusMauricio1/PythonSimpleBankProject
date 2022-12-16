from datetime import date
from useful.helper import date_to_str, str_to_date


class Client:
    counter: int = 200

    def __init__(self: object, name: str, cpf: str, email: str, birthday: str) -> None:
        self.__code: int = Client.counter
        self.__name: str = name
        self.__cpf: str = cpf
        self.__email: str = email
        self.__birthday: date = str_to_date(birthday)
        self.__register_date: date = date.today()
        Client.counter += 1

    @property
    def code(self: object) -> int:
        return self.__code

    @property
    def name(self: object) -> str:
        return self.__name

    @property
    def cpf(self: object) -> str:
        return self.__cpf

    @property
    def email(self: object) -> str:
        return self.__email

    @property
    def birthday(self: object) -> date:
        return self.__birthday

    @property
    def register_date(self: object) -> str:
        return date_to_str(self.__register_date)

    def __str__(self: object) -> str:
        return f"Client's code: {self.code}\nName: {self.name}\nBirthday: {self.birthday}\n" \
               f"Date of registration: {self.register_date}"




