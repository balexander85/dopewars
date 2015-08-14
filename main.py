'''Notes for DopeWars recreated'''
# Assign variables values
PROMPT = "> "
BORDER = '-' * 50
MENUOPTIONS = ["Buy", "Sell", "Leave City", "Quit"]                        # List of menu items
DRUGOPTIONS = {1: 'Weed', 2: 'Coke', 3: 'Heroin'}


def print_list(itemList):
    '''Prints item list with numbering.'''
    for number, item in enumerate(itemList, 1):
        print '{}) {}'.format(number, item)
    print BORDER


def prompt_user_for_answer(query, options=None):
    '''
    Takes a question and possible list of options
    and returns an integer.
    '''
    if options:
        print_list(options)
    result = raw_input(query + PROMPT)
    try:
        result = int(result)
    except ValueError:
        print ('Error: Please enter only an integer'
               ' of your choice. "{}" is not a valid choice.'.format(result))
        return prompt_user_for_answer(query, options)
    return result


class Drug(object):
    '''docstring for Drug'''
    def __init__(self, drug, quantity):
        super(Drug, self).__init__()
        self.drugType = drug.drugType
        self.streetValue = drug.streetValue
        self.drugAmount = quantity

    def get_drug_total_cost(self):
        '''Multiply value by quantity.'''
        return self.drugAmount * self.streetValue


class Weed:
    '''docstring for Weed'''
    def __init__(self):
        self.drugType = 'Weed'
        self.streetValue = 50

    def return_drug_name(self):
        '''Return drug type name.'''
        return self.drugType


class Coke:
    '''docstring for Coke'''
    def __init__(self):
        self.drugType = 'Coke'
        self.streetValue = 300


class Heroin:
    '''docstring for Heroin'''
    def __init__(self):
        self.drugType = 'Heroin'
        self.streetValue = 500


class Player(object):
    '''docstring for Player'''
    def __init__(self, name):
        super(Player, self).__init__()
        self.name = name
        self.lifeBal = 100                 # Set to 100, once you hit zero, game over
        self.bankRoll = 1000               # Set to 1000, may adjust later
        self.originLocation = 'Austin'     # Set to Austin for now
        self.currentLoction = 'Austin'
        self.drugStash = {'Weed': 0, 'Coke': 0, 'Heroin': 0}

    def player_stats(self):
        '''Prints Player's stats.'''
        stats = {'Player': self.name, 'Health': self.lifeBal,
                 'Bank': self.bankRoll, 'Location': self.currentLoction,
                 'Drug Stash': self.drugStash}
        print BORDER
        for k, v in stats.iteritems():
            print '{} : {}'.format(k, v)
        print BORDER

    def bank_roll_debit(self, amount):
        '''Debit amount from bankRoll if player has enough money.'''
        if amount <= self.bankRoll:
            self.bankRoll -= amount
            return True
        else:
            print "You do not have enough money!"

    def drug_stash_debit(self, drugType, amount):
        '''Subtract drugs from stash if player has enough drugs.'''
        if amount <= self.drugStash[drugType]:
            self.drugStash[drugType] -= amount
            return True
        else:
            print "You do not have enough drugs to sell!"

    def bank_roll_credit(self, amount):
        '''Credit to bankRoll.'''
        self.bankRoll += amount

    def drug_stash_credit(self, drugType, amount):
        '''Add drugs to stash.'''
        self.drugStash[drugType] += amount

    def bad_choice(self):
        '''Temp method, probably will delete.'''
        self.lifeBal -= 25


# ||||||||||||||||||||BEGINNING OF FUNCTIONS||||||||||||||||||||||||||||||
def game_over():
    '''Simple print statement, probably should deconstruct player class.'''
    print "-------GAME OVER-------"


def dead():
    '''Return 4 to the main function to end while loop'''
    print "------YOU'RE DEAD------"
    return 4


def buy(player):
    '''A player determines what kind of drug they should buy.'''
    choice = prompt_user_for_answer('What would you like to buy?\n', options=DRUGOPTIONS.values())
    buy_drug(player, eval(DRUGOPTIONS.get(choice)))


def sell(player):
    '''A player determines what kind of drug they should sell.'''
    choice = prompt_user_for_answer('What would you like to sell?\n', options=DRUGOPTIONS.values())
    sell_drug(player, eval(DRUGOPTIONS.get(choice)))


def buy_drug(player, drug):
    '''A player determines how much of what drug they should buy.'''
    desiredQuantity = prompt_user_for_answer('How much would you like to buy?\n')
    drugCost = Drug(drug(), desiredQuantity).get_drug_total_cost()
    if player.bank_roll_debit(drugCost):
        print "Cool deal!"
        player.drug_stash_credit(drug().drugType, desiredQuantity)


def sell_drug(player, drug):
    '''A player determines how much of what drug they should sell.'''
    desiredQuantity = prompt_user_for_answer('How much would you like to sell?\n')
    drugCost = Drug(drug(), desiredQuantity).get_drug_total_cost()
    if player.drug_stash_debit(drug().drugType, desiredQuantity):
        print "Cool deal!"
        player.bank_roll_credit(drugCost)


if __name__ == "__main__":
    name = raw_input("What's your name?\n" + PROMPT)
    print BORDER
    print '********Welcome to DopeWars!*************'
    player = Player(name)
    choice = 0

    while choice != 4:
        if player.lifeBal <= 0:
            choice = dead()
            game_over()
        else:
            player.player_stats()
            choice = prompt_user_for_answer('What would you like to do?\n', options=MENUOPTIONS)

            if choice == 1:
                buy(player)
            elif choice == 2:
                sell(player)
            elif choice == 3:
                print ('Not possible to leave the city yet. '
                       'Enjoy {} while you are there!'.format(player.originLocation))
            elif choice == 4:
                game_over()
            else:
                print "You chose incorrectly, try again!"
                player.bad_choice()
