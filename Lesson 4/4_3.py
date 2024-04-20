import openpyxl
from openpyxl import Workbook

class ATM:
    def __init__(self):
        self.balance = 0
        self.operation_count = 0
        self.transactions = []

    def wealth_tax(self):
        if self.balance > 5000000:  # Превышение суммы в 5 млн у.е.
            self.balance *= 0.9  # Вычитание 10% налога на богатство

    def deposit(self, amount):
        self.wealth_tax()
        if amount % 50 == 0:
            self.balance += amount
            self.operation_count += 1
            self.transactions.append(('Пополнение', amount, self.balance))
            self.interest_bonus()
        else:
            print("Сумма пополнения должна быть кратной 50 у.е.")
        print(f"Текущий баланс: {self.balance:.2f}")

    def withdraw(self, amount):
        self.wealth_tax()
        if amount % 50 == 0:
            fee = max(30, min(600, 0.015 * amount))
            total_withdraw = amount + fee
            if total_withdraw <= self.balance:
                self.balance -= total_withdraw
                self.operation_count += 1
                self.transactions.append(('Снятие', amount, self.balance))
                self.interest_bonus()
            else:
                print("Недостаточно средств для снятия.")
        else:
            print("Сумма снятия должна быть кратной 50 у.е.")
        print(f"Текущий баланс: {self.balance:.2f}")

    def interest_bonus(self):
        if self.operation_count % 3 == 0:
            self.balance *= 1.03
            self.transactions.append(('Бонус процентов', "3%", self.balance))

    def save_transactions_to_excel(self):
        workbook = Workbook()
        sheet = workbook.active
        sheet.title = 'Транзакции'
        sheet.append(('Тип операции', 'Сумма', 'Баланс после операции'))

        for transaction in self.transactions:
            sheet.append(transaction)

        workbook.save('transactions.xlsx')
        print("Транзакции сохранены в файл 'transactions.xlsx'.")

    def run(self):
        while True:
            print("\nДоступные операции: пополнить, снять, выйти")
            action = input("Введите действие: ").strip().lower()
            if action == "выйти":
                self.save_transactions_to_excel()
                print(f"Окончательный баланс: {self.balance:.2f}")
                break
            elif action in ["пополнить", "снять"]:
                amount = input("Введите сумму: ")
                if amount.isdigit():
                    amount = int(amount)
                    if action == "пополнить":
                        self.deposit(amount)
                    elif action == "снять":
                        self.withdraw(amount)
                else:
                    print("Введите корректную сумму.")
            else:
                print("Неверное действие. Повторите ввод.")

if __name__ == '__main__':
    atm_machine = ATM()
    atm_machine.run()