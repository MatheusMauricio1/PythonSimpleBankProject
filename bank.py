from typing import List
from time import sleep
from models.client import Client
from models.account import Account


accounts: List = []


def main() -> None:
    menu()


def menu():
    print('=======================================================')
    print('===================== BANKBANK! =======================')
    print("============ You're welcom' Space Cowboy! =============")
    print("=======================================================\n")

    print("BANKBANK is the bank that is goin' to spank your skank debts and keeps yer mon' swanky! Yeeeee Hawwww!")
    print("Feel free to navigate among the given options Space Cowboy!:\n")
    print('Option 1 - Create Account')
    print('Option 2 - List Accounts')
    print('Option 3 - Deposit money')
    print('Option 4 - Withdraw money')
    print('Option 5 - Transfer money')
    print('Option 6 - Exit\n')

    client_opt: int = int(input("Please, select an option. You must type the number of the option: "))
    print('')
    if client_opt == 1:
        create_account()

    elif client_opt == 2:
        list_accounts()

    elif client_opt == 3:
        deposit_money()

    elif client_opt == 4:
        withdraw_money()

    elif client_opt == 5:
        transfer_money()

    elif client_opt == 6:
        print("See ya Space Cowboy! Feel free to com' back! And always REMEMBER! GOD BLESS 'MERICA!\n")
        print("""                |* * * * * * * * * * OOOOOOOOOOOOOOOOOOOOOOOOO|
                | * * * * * * * * *  :::::::::::::::::::::::::|        .---.        .----------- 
                |* * * * * * * * * * OOOOOOOOOOOOOOOOOOOOOOOOO|       /     \  __  /    ------ 
                | * * * * * * * * *  :::::::::::::::::::::::::|      / /     \(  )/    -----
                |* * * * * * * * * * OOOOOOOOOOOOOOOOOOOOOOOOO|     //////   ' \/ `   ---
                | * * * * * * * * *  ::::::::::::::::::::;::::|    //// / // :    : ---
                |* * * * * * * * * * OOOOOOOOOOOOOOOOOOOOOOOOO|   // /   /  /`    '--
                |:::::::::::::::::::::::::::::::::::::::::::::|  //          //..\\
                |OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO|         ====UU====UU==== 
                |:::::::::::::::::::::::::::::::::::::::::::::|              '//||\\`
                |OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO|                ''``
                |:::::::::::::::::::::::::::::::::::::::::::::|
                |OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO|  
                                      ,-.    ,-.  ,-. ,----. ,----.,-. ,----.   ,-.   
                                      |  `.  \  `.|  \\  .--`\ \"L \\ \\ .-._\  |  `.     
                                      | |. `. \ \ ` L \\  __\ \ .  < \ \\ \  __ | |. `.
                                      | .--. `.\ \`-'\ \\ `---.\ \L `.\ \\ `-` \| .--. `.  
                                      `-'   `--``'    `-'`----' `-'`-' `' `----'`-'   `--'           
                """)

        sleep(2)
        exit(0)
    else:
        print("Seems like you've typed an invalid option Space Cowboy!")
        print("I take ya back to the main menu! Please wait right there!.\n")
        sleep(7)
        menu()


def create_account():
    print("Please type the client's informations : ")

    name: str = input("Client's Name: ")
    email: str = input("Client's email: ")
    cpf: str = input("Client's CPF: ")
    birthday: str = input("Client's birthday: ")

    client: Client = Client(name, email, cpf, birthday)
    account = Account(client)

    accounts.append(account)
    print('-----------------------------')
    print('The account has been successfully created!')
    print('-----------------------------')
    print('Account informations: ')
    print('')
    print(account)
    print('')
    sleep(2)
    menu()


def withdraw_money():
    if len(accounts) > 0:
        account_number: int = int(input('Please, inform your account number: '))
        account: Account = search_account_by_number(account_number)

        if account:
            value:  float = float(input("How much mon' do ye want to withdraw Space Cowboy?: "))
            account.withdraw(value)
        else:
            print(f"The account you've informed is not valid Space Cowboy!: {account_number}")
            print(f"Please create an account or try to access again!")
            sleep(2)
            menu()
    else:
        print('There are no registered accounts yet!')
    sleep(2)
    menu()


def deposit_money():
    if len(accounts) > 0:
        account_number: int = int(input('Please, inform your account number: '))
        account: Account = search_account_by_number(account_number)

        if account:
            value:  float = float(input("How much mon' do ye want to deposit Space Cowboy?: "))
            account.deposit(value)
        else:
            print(f"The account you've informed is not a valid one Space Cowboy!: Account: {account_number}")
            print(f"Please create an account or try to access again!")
            print(f'')
            sleep(2)
            menu()

    else:
        print('There are no registered accounts yet!')
    sleep(2)
    menu()


def transfer_money():
    if len(accounts) > 0:
        account_number: int = int(input('Please, inform your account number: '))
        o_account: Account = search_account_by_number(account_number)

        if o_account:
            d_acc_number: int = int(input('Please inform the destination account number: '))
            d_account: Account = search_account_by_number(d_acc_number)

            if d_account:
                value: float = float(input("Please inform how much money do you want to transfer: "))
                o_account.transfer(d_account, value)
            else:
                print(f"The account {d_acc_number} that you've informed could not found")
                print("Please Try again.")
                sleep(2)
                menu()

        else:
            print(f"The account you've informed is not a valid onde Space Cowboy!: Account {account_number}")
            print(f"Please create an account or try to access again!")
            print(f'')
            sleep(2)
            menu()
    else:
        print('There are no registered accounts yet!')
    sleep(2)
    menu()


def list_accounts() -> None:
    if len(accounts) > 0:
        print('Account Listing:')

        for account in accounts:
            print(f'{account}\n----------------------')
        print('')
        sleep(2)
        menu()
    else:
        print('There are no registered accounts yet!')
        sleep(2)
        menu()


def search_account_by_number(num: int) -> Account:
    c: Account = None

    if len(accounts) > 0:
        for account in accounts:
            if account.number == num:
                c = account

    return c


if __name__ == '__main__':
    main()

