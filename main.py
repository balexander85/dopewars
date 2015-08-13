# Notes for DopeWars recreated
# Assign variables values
prompt = "> "
border = '-' * 50
menuOptions = ["Buy", "Sell", "Leave City", "Quit"]                        # List of menu items
drugOptions = ["weed", "coke", "heroin"]                                   # List of drugs to be bought and sold
weed_Cost = 50                                                             # Cost of weed
coke = 0
heroin = 0


def print_list(itemList):
    '''Prints item list with numbering.'''
    for k, v in enumerate(itemList, 1):
        print '{}) {}'.format(k, v)
    print border


def prompt_user_for_answer(query, options=None):
    if options:
        print_list(options)
    result = raw_input(query + prompt)
    try:
        return int(result)
    except ValueError:
        print ('Error: Please enter only the number'
               ' of your choice. {} is not a valid choice.'.format(result))
        return prompt_user_for_answer(query)


class Person(object):
    """docstring for Person"""
    def __init__(self, name):
        super(Person, self).__init__()
        self.name = name
        self.lifeBal = 100                 # Set to 100, once you hit zero, game over
        self.bankRoll = 1000              # Set to 1000, may adjust later
        self.origin_Location = 'Austin'    # Set to Austin for now
        self.drugStash = {'weed': 0, 'coke': 0, 'heroin': 0}

    def current_stats(self):
        '''Prints Players stats in list form.'''
        player_Stats = ["Player", "Health", "Bank", "Location",
                        "Drug Stash"]
        stats = [self.name, self.lifeBal, self.bankRoll,
                 self.origin_Location, self.drugStash]
        print border
        for k, stat in enumerate(player_Stats):
            print '{} : {}'.format(stat, stats[k])
        print border

    def bank_roll_debit(self, amount):
        if amount <= self.bankRoll:
            self.bankRoll -= amount
            return True
        else:
            print "You do not have enough money!"

    def drug_stash_debit(self, drugType, amount):
        if amount <= self.drugStash[drugType]:
            self.drugStash[drugType] -= amount
            return True
        else:
            print "You do not have enough drugs to sell!"

    def bank_roll_credit(self, amount):
        self.bankRoll += amount

    def drug_stash_credit(self, drugType, amount):
        self.drugStash[drugType] += amount

    def bad_choice(self):
        self.lifeBal -= 25


# ||||||||||||||||||||BEGINNING OF FUNCTIONS||||||||||||||||||||||||||||||
def game_over():
    print "-------GAME OVER-------"


def dead():
    print "------YOU'RE DEAD------"
    # Return 4 to the main function to end while loop
    return 4


def buy(player):
    choice = prompt_user_for_answer('What would you like to buy?\n', options=drugOptions)
    if choice == 1:
        buy_drug(player, 'weed')
    else:
        print "You chose incorrectly, try again!"


def sell(player):
    choice = prompt_user_for_answer('What would you like to sell?\n', options=drugOptions)
    if choice == 1:
        sell_drug(player, 'weed')
    else:
        print "You chose incorrectly, try again!"


def buy_drug(player, drugType):
    drugAmount = prompt_user_for_answer('How much would you like to buy?\n')
    drugCost = drugAmount * weed_Cost
    if player.bank_roll_debit(drugCost):
        print "Cool deal!"
        player.drug_stash_credit(drugType, drugAmount)


def sell_drug(player, drugType):
    drugAmount = prompt_user_for_answer('How much would you like to sell?\n')
    drugCost = drugAmount * weed_Cost
    if player.drug_stash_debit(drugType, drugAmount):
        print "Cool deal!"
        player.bank_roll_credit(drugCost)


if __name__ == "__main__":
    # name = raw_input("What's your name?\n" + prompt)
    name = 'Brian'
    player = Person(name)
    choice = 0

    while choice != 4:
        if player.lifeBal <= 0:
            choice = dead()
            game_over()
        else:
            player.current_stats()
            choice = prompt_user_for_answer('What would you like to do?\n', options=menuOptions)

            if choice == 1:
                buy(player)
            elif choice == 2:
                sell(player)
            elif choice == 3:
                print ('Not possible to leave the city yet. '
                       'Enjoy {} while you\'re there!'.format(player.origin_Location))
            elif choice == 4:
                game_over()
            else:
                print "You chose incorrectly, try again!"
                player.bad_choice()
