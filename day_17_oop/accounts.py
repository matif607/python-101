from datetime import datetime, timezone


class Account:

    @staticmethod
    def _current_time():
        return datetime.now(timezone.utc)

    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance
        self._transaction_list = []
        print(f"Account created for {self.name} with {self.__balance}")

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self.show_balance()
            self._transaction_list.append((Account._current_time(), amount))

    def withdraw(self, amount):
        if 0 < amount < self.__balance:
            self.__balance -= amount
            self._transaction_list.append((Account._current_time(), -amount))
        else:
            print(f"Not enough balance. Your current balance is {self.__balance}")

    def show_balance(self):
        print(f" The balance is {self.__balance}")

    def show_transaction(self):
        for date, amount in self._transaction_list:
            if amount > 0:
                tran_type = "Deposited"
            else:
                tran_type = "Withdrawal"
                amount *= -1
            print(f"{amount}, {tran_type}, on {date} (local time was {date.astimezone()})")


if __name__ == '__main__':
    atif = Account("atif", 0)
    atif.show_balance()
    atif.deposit(1000)
    # atif.show_balance()
    atif.withdraw(500)
    # atif.show_balance()
    atif.withdraw(1000)
    atif.show_transaction()

    sana = Account("sana", 500)
    sana.deposit(100)
    sana.withdraw(200)
    sana.__balance = 0  # this will not affect th output
    sana.show_balance()
    sana.show_transaction()
    sana.__Account__balance = 50  # this will affect the output by setting the balance as 50
    sana.show_balance()
