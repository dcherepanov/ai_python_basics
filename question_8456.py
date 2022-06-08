
__author__ = 'Черепанов Дмитрий Евгеньевич'

''' 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А
также класс «Оргтехника», который будет базовым для классов-наследников. Эти классы —
конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определите
параметры, общие для приведённых типов. В классах-наследниках реализуйте параметры,
уникальные для каждого типа оргтехники.'''

''' Вместо склада я решил сделать примитивное представление работы брокерского счета*.
Депозитарий - аналог склада в данной задаче. Вместо оргтехники - ценные бумаги (в рамках
моего решения у них есть тип, название, средняя цена приобретения, и, в зависимости от типа,
иные атрибуты вроде истории дивидендной доходности или накопленного купонного дохода).'''

''' 5. Продолжить работу над первым заданием. Разработайте методы, которые отвечают за приём
оргтехники на склад и передачу в определённое подразделение компании. Для хранения
данных о наименовании и количестве единиц оргтехники, а также других данных, можно
использовать любую подходящую структуру (например, словарь).'''

''' В рамках моей задачи реализуются методы приобретения и продажи ценных бумаг клиентом, погашение
обязательств.'''

''' 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых
пользователем данных. Например, для указания количества принтеров, отправленных на
склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь реализовать в проекте «Склад оргтехники» максимум возможностей,
изученных на уроках по ООП.

*у меня нет экономического образования, поэтому реализуется сугубо мое личное представление
с огромными упрощениями'''  

import json


class BuyError(Exception):
    def __init__(self, text):
        self.txt = text


class SellError(Exception):
    def __init__(self, text):
        self.txt = text


class DifferentTypesError(Exception):
    def __init__(self, text):
        self.txt = text


class Stock:
    '''
    Атрибуты:
    stock_type - тип ценной бумаги ("share" - акция, "bond" - облигация с фиксированной 
    процентной ставкой, "currency" - валюта);
    ticker - биржевой тикер (например, "ALRS");
    average_price - средняя цена приобретения;
    base_currency - тикер базовой валюты (например, "RUB");
    amount - количество;
    Методы:
    is_same_types_and_tickers - проверка двух экземпляров класса на идентичность типов и тикеров;
    buy - покупка по цене purchase_price в количестве amount;
    sell - продажа по цене purchase_price в количестве amount;
    '''
    def __init__(self, stock_type, ticker, base_currency, average_price, amount):
        self.stock_type = stock_type
        self.ticker = ticker
        self.base_currency = base_currency
        self.average_price = average_price
        self.amount = amount


    @staticmethod
    def is_same_types_and_tickers(obj1, obj2):
        if obj1.stock_type != obj2.stock_type:
            raise DifferentTypesError('Операции с разными типами ценных бумаг не позволены')
        if obj1.ticker != obj2.ticker:
            raise DifferentTypesError('Операции с разными ценными бумагами не позволены')
        return True 


    def buy(self, purchase_price, amount):
        sum_price = self.amount * self.average_price + purchase_price * amount
        self.amount += amount
        self.average_price = sum_price / self.amount
        

    def sell(self, sell_price, amount):
        if amount > self.amount:
            raise SellError('Попытка продать больше того, что имеется')
        sum_price = self.amount * self.average_price - sell_price * amount
        self.amount -= amount
        if self.amount != 0:
            self.average_price = sum_price / self.amount
        else:
            self.average_price = 0

    
    def __str__(self):
        return '{:<12}|\t{:<12}|\t{:<12} {}|\t{:<12} {}'.format(self.ticker, 
            self.amount, round(self.average_price, 2), self.base_currency, 
            self.average_price * self.amount, self.base_currency)


class Currency(Stock):
    '''
    Валюта;
    Базовый класс - Stock;
    Методы:
    get_current_price - получение текущего курса к RUB (я не стал реализовывать настоящий запрос,
    сделана искусственная затычка);
    Перегружены методы сложения и вычитания для удобства рассчетов по сделкам.
    '''
    def __init__(self, ticker, base_currency, amount=0, average_price=0):
        super().__init__('currency', ticker, base_currency, average_price, amount)
        if ticker == base_currency:
            self.average_price = 1


    def get_current_price(self):
        self.average_price = 70 #предположим, здесь реализуется запрос текущего курса
        if self.ticker == self.base_currency:
            self.average_price = 1


    def __add__(self, other):
        if self.is_same_types_and_tickers(self, other):
            return Currency(self.ticker, self.base_currency, self.amount + other.amount, self.average_price)
    

    def __sub__(self, other):
        if self.is_same_types_and_tickers(self, other):
            if other.amount > self.amount:
                raise SellError('Недостаточно средств')
            return Currency(self.ticker, self.base_currency, self.amount - other.amount, self.average_price)


class Share(Stock):
    '''
    Акция;
    Базовый класс - Stock;
    Атрибуты:
    payed_divident  - выплаченный дивидендный доход;
    Методы:
    divident - метод выплаты дивидендного дохода по акции;
    перегружен __str__ для удобного вывода информации по акции.
    '''
    def __init__(self, ticker, base_currency, average_price=0, amount=0, payed_divident=0):
        super().__init__('share', ticker, base_currency, average_price, amount)
        self.payed_divident = payed_divident


    def divident(self, account, quantity):
        income = quantity * self.amount
        self.payed_divident += income
        currencies = account.stocks['currency']
        if account.is_stock_in_balance('currency', self.base_currency):     
            currencies[self.base_currency] += Currency(self.base_currency, 
                currencies[self.base_currency].base_currency, income)
        else:
            currency = Currency(self.base_currency, 'RUB', income)
            currency.get_current_price()
            currencies.append(currency)
            currencies[self.base_currency] = currency


    def __str__(self):
        return '{:<12}|\t{:<12}|\t{:<12} {}|\t{:<12} {}|\t Divident: {} {}'.format(self.ticker, 
            self.amount, round(self.average_price, 2), self.base_currency, 
            self.average_price * self.amount, self.base_currency, 
            self.payed_divident, self.base_currency)


class Bond(Stock):
    '''
    Облигация;
    Базовый класс - Stock;
    Атрибуты:
    income - выплаченный купонный доход;
    Методы:
    accrued_interest - метод выплаты накопленного купонного дохода;
    matured - метод погашения облигации.
    перегружен __str__ для удобного вывода информации по облигации;
    Погашение облигации заключается в выплате номинальной стоимости (1000).
    '''
    def __init__(self, ticker, base_currency, average_price=0, amount=0, income=0):
        super().__init__('bond', ticker, base_currency, average_price, amount)
        self.income = income


    def accrued_interest(self, account, rate):
        income = rate * 1000 * self.amount
        self.income += income
        currencies = account.stocks['currency']
        if account.is_stock_in_balance('currency', self.base_currency):     
            currencies[self.base_currency] += Currency(self.base_currency, 
                currencies[self.base_currency].base_currency, income)
        else:
            currency = Currency(self.base_currency, 'RUB', income)
            currency.get_current_price()
            currencies.append(currency)
            currencies[self.base_currency] = currency


    def matured(self, account):
        income = 1000 * self.amount
        currencies = account.stocks['currency']
        if account.is_stock_in_balance('currency', self.base_currency):     
            currencies[self.base_currency] += Currency(self.base_currency, 
                currencies[self.base_currency].base_currency, income)
        else:
            currency = Currency(self.base_currency, 'RUB', income)
            currency.get_current_price()
            currencies.append(currency)
            currencies[self.base_currency] = currency

    
    def __str__(self):
        return '{:<12}|\t{:<12}|\t{:<12} {}|\t{:<12} {}|\t Payed AI: {} {}'.format(self.ticker, 
            self.amount, round(self.average_price, 2), self.base_currency, 
            self.average_price * self.amount, self.base_currency, 
            self.income, self.base_currency)
    

class CustodianBankAccount:
    '''
    Класс аккаунт;
    Атрибуты:
    owner_id - id клиента;
    stocks - словарь с активами
    class_dict - словарь для удобного вызова нудных классов при операциями с активами
    Методы:
    pay_divident - метод выплаты дивидендов;
    pay_ai - метод выплаты накопленного купонного дохода;
    bond_matured - метод погашения облигации;
    dump, load - сохранение и подгрузка состояния аккаунта;
    is_stock_in_balance - проверка наличия ценной бумаги на счете;
    is_numeric_data - проверка вводимых данных (числа ли они);
    перегружен __str__ для удобного вывода выписки.
    '''
    def __init__(self, owner_id, initial_balance):
        self.owner_id = owner_id
        self.stocks = {'currency': {'RUB': Currency('RUB', 'RUB', amount=initial_balance)}, 
            'share':{}, 'bond': {}}
        self.class_dict = {'currency': Currency, 'share': Share, 'bond': Bond}


    def is_stock_in_balance(self, stock_type, ticker):
        return True if ticker in self.stocks[stock_type].keys() else False


    def buy_stock(self, stock_type, ticker, base_currency, amount, price):
        if not self.is_numeric_data(amount, price):
            raise ValueError('amount и price должны быть числами')
        if self.is_stock_in_balance('currency', base_currency):
            currencies = self.stocks['currency']
            try:
                currencies[base_currency] -= Currency(base_currency, 
                    currencies[base_currency].base_currency, price * amount)
                stocks = self.stocks[stock_type]
            except Exception as e:
                print(e)
                return False
            if self.is_stock_in_balance(stock_type, ticker):
                stocks[ticker].buy(price, amount)
            else:
                stocks[ticker] = self.class_dict[stock_type](ticker, base_currency)
                stocks[ticker].buy(price, amount)
            self.dump()
            return True
        else:
            return False


    def sell_stock(self, stock_type, ticker, amount, price):
        if not self.is_numeric_data(amount, price):
            raise ValueError('amount и price должны быть числами')
        if self.is_stock_in_balance(stock_type, ticker):
            stocks = self.stocks[stock_type]            
            try:
                stocks[ticker].sell(price, amount)
                stock_base_currency = stocks[ticker].base_currency
                if stocks[ticker].amount == 0:
                    stocks.pop(ticker)
            except Exception as e:
                print(e)
                return False
            currencies = self.stocks['currency']
            if self.is_stock_in_balance('currency', stock_base_currency):
                currencies[stock_base_currency] += Currency(stock_base_currency, 
                    currencies[stock_base_currency].base_currency, price * amount)
            else:
                currency = Currency(stock_base_currency, 'RUB', price * amount)
                currency.get_current_price()
                currencies[stock_base_currency] = currency
            self.dump()
            return True
        else:
            return False


    def pay_divident(self, ticker, amount):
        if not self.is_numeric_data(amount):
            raise ValueError('amount должнен быть числом')
        if self.is_stock_in_balance('share', ticker):
            self.stocks['share'][ticker].divident(self, amount)
            self.dump()
    

    def pay_ai(self, ticker, rate):
        if not self.is_numeric_data(rate):
            raise ValueError('rate должнен быть числом')
        if self.is_stock_in_balance('bond', ticker):
            self.stocks['bond'][ticker].accrued_interest(self, rate)
            self.dump()


    def bond_matured(self, ticker):
        if self.is_stock_in_balance('bond', ticker):
            self.stocks['bond'][ticker].matured(self)
            self.stocks['bond'].pop(ticker)
            self.dump()


    @staticmethod
    def is_numeric_data(*data):
        bool_data = [True if type(d) is float or type(d) is int else False for d in data]
        return all(bool_data)


    def __str__(self):
        info_head = '{:<12}|\t{:<12}|\t{:<16}|\t{:<16}|\t {}'.format('ticker', 'amount', 'price', 'sum', 'income')
        divider = '-' * 75
        return '\n'.join(['\n'.join([divider, f'{key}:', divider, info_head, 
                '\n'.join(map(str, item.values()))]) for key, item in self.stocks.items()])       


    def dump(self):
        with open(f'{self.owner_id}.json', 'w', encoding='utf-8') as f:
            stocks = {stock_type: {key: data.__dict__ for key, data in 
                value_dict.items()} for stock_type, value_dict in self.stocks.items()}
            json.dump(stocks, f)


    @classmethod
    def load(cls, owner_id):
        with open(f'{owner_id}.json', 'r', encoding='utf-8') as f:
            stocks = json.load(f)
            acc = CustodianBankAccount(owner_id, 0)
            stocks = {stock_type: {key: acc.class_dict[data[list(data.keys())[0]]](**{k: data[k] for k in 
                list(data.keys())[1:]}) for key, data in value_dict.items()} for stock_type, value_dict in stocks.items()}
            acc.stocks = stocks
            return acc


if __name__ == '__main__':
    'Проверка основного функционала:'
    owner_id = 11122344
    account = CustodianBankAccount(11122344, 1000000)
    account.buy_stock('share', 'ALRS', 'RUB', 20, 800)
    account.buy_stock('share', 'ALRS', 'RUB', 20, 600)
    account.buy_stock('share', 'SBER', 'RUB', 20, 100)
    account.buy_stock('share', 'GAZP', 'RUB', 100, 250)
    account.buy_stock('currency', 'USD', 'RUB', 5000, 60)
    account.buy_stock('share', 'KO', 'USD', 10, 60)
    account.buy_stock('bond', 'OFZ FD', 'RUB', 25, 950)
    account.buy_stock('bond', 'SHY', 'USD', 3, 980)
    print('-' * 75 + '\nПокупка:\n' + '-' * 75)
    print(account)
    account.sell_stock('share', 'ALRS', 8, 1000)
    account.sell_stock('bond', 'SHY', 3, 1000)
    print('-' * 75 + '\nПродажа:\n' + '-' * 75)
    print(account)
    print('-' * 75 + '\nВыплата доходности:\n' + '-' * 75)
    account.pay_divident('ALRS', 200)
    account.pay_divident('KO', 5)
    account.pay_ai('OFZ FD', 0.03)
    print(account)
    print('-' * 75 + '\nУдаление и подгрузка текущего состояния из файла:\n' + '-' * 75)
    del(account)
    acc = CustodianBankAccount.load(11122344)
    print(acc)
    print('-' * 75 + '\nПродажа всех активов и погашение обязательств:\n' + '-' * 75)
    acc.sell_stock('share', 'ALRS', 32, 1200)
    acc.sell_stock('share', 'SBER', 20, 110)
    acc.sell_stock('share', 'GAZP', 100, 300)
    acc.sell_stock('share', 'KO', 10, 75)
    acc.sell_stock('currency', 'USD', 5260, 70)
    acc.bond_matured('OFZ FD')
    print(acc)
