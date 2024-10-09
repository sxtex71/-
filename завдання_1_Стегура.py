import random
from colorama import Fore, Style, init

                                    # Ініціалізація Colorama
init(autoreset=True)

                                    # Зберігаємо рахунки в словнику
accounts = {}


                                    # Створення нового рахунку
def create_account():
    account_id = str(random.randint(10000, 99999))  # Генерація унікального ідентифікатора
    name = input(Fore.YELLOW + "Введіть ім'я клієнта: ")
    initial_balance = float(input(Fore.YELLOW + "Введіть початковий баланс: "))

    accounts[account_id] = {
        "name": name,
        "balance": initial_balance,
        "transactions": []
    }

    print(Fore.GREEN + f"Рахунок створено. Номер рахунку: {account_id}")


                                    # Ф-ція поповнення рахунку
def deposit(account_id, amount):
    if account_id in accounts:
        accounts[account_id]["balance"] += amount
        accounts[account_id]["transactions"].append(f"Поповнення: {amount}")
        print(Fore.GREEN + f"Поповнено рахунок на {amount}. Новий баланс: {accounts[account_id]['balance']}")
    else:
        print(Fore.RED + "Рахунок не знайдено.")


                                    # Ф-ція зняття коштів
def withdraw(account_id, amount):
    if account_id in accounts:
        if accounts[account_id]["balance"] >= amount:
            accounts[account_id]["balance"] -= amount
            accounts[account_id]["transactions"].append(f"Зняття: {amount}")
            print(Fore.GREEN + f"Знято {amount}. Новий баланс: {accounts[account_id]['balance']}")
        else:
            print(Fore.RED + "Недостатньо коштів.")
    else:
        print(Fore.RED + "Рахунок не знайдено.")


                                    # Ф-ція переведення коштів
def transfer(sender_id, receiver_id, amount):
    if sender_id in accounts and receiver_id in accounts:
        if accounts[sender_id]["balance"] >= amount:
            accounts[sender_id]["balance"] -= amount
            accounts[receiver_id]["balance"] += amount
            accounts[sender_id]["transactions"].append(f"Переказ на рахунок {receiver_id}: {amount}")
            accounts[receiver_id]["transactions"].append(f"Переказ з рахунку {sender_id}: {amount}")
            print(Fore.GREEN + f"Переказано {amount} з рахунку {sender_id} на рахунок {receiver_id}.")
        else:
            print(Fore.RED + "Недостатньо коштів для переказу.")
    else:
        print(Fore.RED + "Один з рахунків не знайдено.")


# Функція перегляду балансу
def view_balance(account_id):
    if account_id in accounts:
        print(Fore.GREEN + f"Баланс рахунку {account_id}: {accounts[account_id]['balance']}")
    else:
        print(Fore.RED + "Рахунок не знайдено.")


# Функція перегляду історії транзакцій
def view_transactions(account_id):
    if account_id in accounts:
        print(Fore.GREEN + f"Історія транзакцій для рахунку {account_id}:")
        for transaction in accounts[account_id]["transactions"]:
            print(Fore.CYAN + transaction)
    else:
        print(Fore.RED + "Рахунок не знайдено.")


# Головне меню
def main_menu():
    while True:
        print(Fore.BLUE + "\n1. Створити новий рахунок")
        print(Fore.BLUE + "2. Поповнити рахунок")
        print(Fore.BLUE + "3. Зняти кошти")
        print(Fore.BLUE + "4. Переказати кошти")
        print(Fore.BLUE + "5. Переглянути баланс")
        print(Fore.BLUE + "6. Переглянути історію транзакцій")
        print(Fore.BLUE + "0. Вийти")

        choice = input(Fore.YELLOW + "Оберіть дію: ")

        if choice == "1":
            create_account()
        elif choice == "2":
            account_id = input(Fore.YELLOW + "Введіть номер рахунку: ")
            amount = float(input(Fore.YELLOW + "Введіть суму поповнення: "))
            deposit(account_id, amount)
        elif choice == "3":
            account_id = input(Fore.YELLOW + "Введіть номер рахунку: ")
            amount = float(input(Fore.YELLOW + "Введіть суму для зняття: "))
            withdraw(account_id, amount)
        elif choice == "4":
            sender_id = input(Fore.YELLOW + "Введіть номер рахунку відправника: ")
            receiver_id = input(Fore.YELLOW + "Введіть номер рахунку отримувача: ")
            amount = float(input(Fore.YELLOW + "Введіть суму переказу: "))
            transfer(sender_id, receiver_id, amount)
        elif choice == "5":
            account_id = input(Fore.YELLOW + "Введіть номер рахунку: ")
            view_balance(account_id)
        elif choice == "6":
            account_id = input(Fore.YELLOW + "Введіть номер рахунку: ")
            view_transactions(account_id)
        elif choice == "0":
            print(Fore.MAGENTA + "Дякуємо за використання банківської системи.")
            break
        else:
            print(Fore.RED + "Невірний вибір. Спробуйте ще раз.")


# Запуск програми
if __name__ == "__main__":
    main_menu()
