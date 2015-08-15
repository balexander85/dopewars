'''Notes for DopeWars recreated'''

PROMPT = "> "
BORDER = '-' * 50
MENUOPTIONS = ["Buy", "Sell", "Leave City", "Quit"]


def print_list(item_list):
    '''Prints item list with numbering.'''
    for number, item in enumerate(item_list, 1):
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


class Drugs(object):
    """docstring for Drugs"""
    def __init__(self, drug_type):
        super(Drugs, self).__init__()
        self.drug_type = drug_type
        self.drug_options = {1: Weed(), 2: Coke(), 3: Heroin()}

    def get_drug_class(self):
        '''Get the int value for the drug type.'''
        return self.drug_options[self.drug_type]

    def get_drug_option_names(self):
        '''Returns the str names for the drugs.'''
        return [name.drug_type for name in self.drug_options.values()]

    def get_drug_class_from_string(self):
        '''Get the string value name of the drug type.'''
        return [drug for drug in self.drug_options.values()
                if drug.drug_type == self.drug_type]

    def get_street_values_of_all_drugs(self):
        '''probably will delete but list of drug prices only.'''
        return [drug.street_value for drug in self.drug_options.values()]


class Drug(object):
    '''docstring for Drug'''
    def __init__(self, drug, quantity):
        super(Drug, self).__init__()
        self.drug_type = drug.drug_type
        self.street_value = drug.street_value
        self.drug_amount = quantity

    def get_drug_total_cost(self):
        '''Multiply value by quantity to get total cost of drug.'''
        return self.drug_amount * self.street_value

    def function(self):
        '''Need to update with something useful.'''
        pass


class Weed(object):
    '''docstring for Weed'''
    def __init__(self):
        self.drug_type = 'Weed'
        self.street_value = 50

    def return_drug_name(self):
        '''Return drug type name.'''
        return self.drug_type

    def return_drug_value(self):
        '''Return drug value.'''
        return self.street_value


class Coke(object):
    '''docstring for Coke'''
    def __init__(self):
        self.drug_type = 'Coke'
        self.street_value = 300

    def return_drug_name(self):
        '''Return drug type name.'''
        return self.drug_type

    def return_drug_value(self):
        '''Return drug value.'''
        return self.street_value


class Heroin(object):
    '''docstring for Heroin'''
    def __init__(self):
        self.drug_type = 'Heroin'
        self.street_value = 500

    def return_drug_name(self):
        '''Return drug type name.'''
        return self.drug_type

    def return_drug_value(self):
        '''Return drug value.'''
        return self.street_value


class Player(object):
    '''docstring for Player'''
    def __init__(self, name):
        super(Player, self).__init__()
        self.name = name
        self.life_bal = 100                 # Set to 100, once you hit zero, game over
        self.bank_roll = 1000               # Set to 1000, may adjust later
        self.origin_location = 'Austin'     # Set to Austin for now
        self.current_location = 'Austin'
        self.drug_stash = {'Weed': 0, 'Coke': 0, 'Heroin': 0}
        self.menu_selection = 0

    def player_stats(self):
        '''Prints Player's stats.'''
        stats = {'Player': self.name, 'Health': self.life_bal,
                 'Bank': self.bank_roll, 'Location': self.current_location,
                 'Drug Stash': self.drug_stash}
        print BORDER
        for key, value in stats.iteritems():
            print '{} : {}'.format(key, value)
        print BORDER

    def bank_roll_debit(self, amount):
        '''Debit amount from bank_roll if player has enough money.'''
        if amount <= self.bank_roll:
            self.bank_roll -= amount
            return True
        else:
            print "You do not have enough money!"

    def drug_stash_debit(self, drug_type, amount):
        '''Subtract drugs from stash if player has enough drugs.'''
        if amount <= self.drug_stash[drug_type]:
            self.drug_stash[drug_type] -= amount
            return True
        else:
            print "You do not have enough drugs to sell!"

    def bank_roll_credit(self, amount):
        '''Credit to bank_roll.'''
        self.bank_roll += amount

    def drug_stash_credit(self, drug_type, amount):
        '''Add drugs to stash.'''
        self.drug_stash[drug_type] += amount

    def bad_choice(self):
        '''Temp method, probably will delete.'''
        self.life_bal -= 25


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
    choice = prompt_user_for_answer('What would you like to buy?\n',
                                    options=Drugs(1).get_drug_option_names())
    buy_drug(player, Drugs(choice).get_drug_class())


def sell(player):
    '''A player determines what kind of drug they should sell.'''
    choice = prompt_user_for_answer('What would you like to sell?\n',
                                    options=Drugs(1).get_drug_option_names())
    sell_drug(player, Drugs(choice).get_drug_class())


def buy_drug(player, drug):
    '''A player determines how much of what drug they should buy.'''
    desired_quantity = prompt_user_for_answer('How much would you like to buy?\n')
    drug_cost = Drug(drug, desired_quantity).get_drug_total_cost()
    if player.bank_roll_debit(drug_cost):
        print "Cool deal!"
        player.drug_stash_credit(drug.drug_type, desired_quantity)


def sell_drug(player, drug):
    '''A player determines how much of what drug they should sell.'''
    desired_quantity = prompt_user_for_answer('How much would you like to sell?\n')
    drug_cost = Drug(drug, desired_quantity).get_drug_total_cost()
    if player.drug_stash_debit(drug.drug_type, desired_quantity):
        print "Cool deal!"
        player.bank_roll_credit(drug_cost)


if __name__ == "__main__":
    NAME = 'B-Axe'
    # NAME = raw_input("What's your name?\n" + PROMPT)
    print BORDER
    print '********Welcome to DopeWars!*************'
    PLAYER_INSTANCE = Player(NAME)

    while PLAYER_INSTANCE.menu_selection != 4:
        if PLAYER_INSTANCE.life_bal <= 0:
            PLAYER_INSTANCE.menu_selection = dead()
            game_over()
        else:
            PLAYER_INSTANCE.player_stats()
            PLAYER_INSTANCE.menu_selection = prompt_user_for_answer('What would you like to do?\n',
                                                                    options=MENUOPTIONS)

            if PLAYER_INSTANCE.menu_selection == 1:
                buy(PLAYER_INSTANCE)
            elif PLAYER_INSTANCE.menu_selection == 2:
                sell(PLAYER_INSTANCE)
            elif PLAYER_INSTANCE.menu_selection == 3:
                print ('Not possible to leave the city yet. '
                       'Enjoy {} while you are there!'.format(PLAYER_INSTANCE.current_location))
            elif PLAYER_INSTANCE.menu_selection == 4:
                game_over()
            else:
                print "You chose incorrectly, try again!"
                PLAYER_INSTANCE.bad_choice()
