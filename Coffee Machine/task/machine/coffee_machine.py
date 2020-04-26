class CoffeeMachine:
    drinks = {"1": {"water": 250, "milk": 0, "beans": 16, 'cups': 1, "money": 4},
              "2": {"water": 350, "milk": 75, "beans": 20, 'cups': 1, "money": 7},
              "3": {"water": 200, "milk": 100, "beans": 12, 'cups': 1, "money": 6}}
    filling = {'Filling water': ['ml of water', 'water', 'Filling milk'],
               'Filling milk': ['ml of milk', 'milk', 'Filling beans'],
               'Filling beans': ['grams of coffee beans', 'beans', 'Filling cups'],
               'Filling cups': ['disposable cups of coffee', 'cups', 'Waiting']}

    def __init__(self):
        self.supply = {'water': 400,
                       'milk': 540,
                       'beans': 120,
                       'cups': 9}
        self.money = 550
        self.state = 'Waiting'

    def work(self, inp):
        if self.state is 'Waiting':
            if 'buy' in inp:
                print('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:')
                self.state = 'Drink to buy'
                return True
            elif 'fill' in inp:
                self.state = 'Filling water'
                print('Write how many ml of water do you want to add:')
                return True
            elif 'take' in inp:
                print('I gave you $' + str(machine.money))
                machine.take()
                return True
            elif 'remaining' in inp:
                machine.info()
                return True
            elif 'exit' in inp:
                return False

        if self.state is 'Drink to buy':
            if 'back' not in inp and machine.check(inp):
                print('I have enough resources, making you a coffee!')
                machine.buy(inp)
            self.state = 'Waiting'
            return True

        if 'Filling' in self.state:
            self.fill(CoffeeMachine.filling[self.state][1], inp)
            self.state = CoffeeMachine.filling[self.state][2]
            if self.state is not 'Waiting':
                print('Write how many', CoffeeMachine.filling[self.state][0], 'do you want to add:')
            return True

    def buy(self, drink):
        drink_ = CoffeeMachine.drinks[drink]
        for i in self.supply:
            self.supply[i] -= drink_[i]
        self.money += drink_['money']

    def fill(self, supply, inp):
        self.supply[supply] += int(inp)

    def take(self):
        self.money = 0

    def check(self, drink):
        drink_ = CoffeeMachine.drinks[drink]
        not_enough = ''
        for i in self.supply:
            if self.supply[i] - drink_[i] < 0:
                not_enough = i
        if not_enough:
            print('Sorry, not enough %s!'.format(not_enough))
            return False
        return True

    def info(self):
        print("The coffee machine has:")
        for i in self.supply:
            print(self.supply[i], 'of', i)
        print(self.money, 'of money')


isWorking = True
machine = CoffeeMachine()
while isWorking:
    if machine.state is 'Waiting':
        print('\nWrite action (buy, fill, take, remaining, exit):')
    inp = input().strip("> ")
    isWorking = machine.work(inp)
