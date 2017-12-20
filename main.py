"""Notes for DopeWars recreated"""

import os


PROMPT = "> "
BORDER = '-' * 50
MENU_OPTIONS = ["Buy", "Sell", "Leave City", "Quit"]


def print_list(item_list):
    """Prints item list with numbering."""
    for number, item in enumerate(item_list, 1):
        print(f'{number}) {item}')
    print(BORDER)


def prompt_user_for_answer(query, options=None):
    """
    Takes a question and possible list of options
    and returns an integer.
    """
    if options:
        print_list(options)
    result = input(query + PROMPT)
    try:
        result = int(result)
    except ValueError:
        print('Error: Please enter only an integer of your choice.'
              f' "{result}" is not a valid choice.')
        return prompt_user_for_answer(query, options)
    return result


class Drugs:
    """docstring for Drugs"""

    def __init__(self, drug_type=None):
        super(Drugs, self).__init__()
        self.drug_type = drug_type
        self.drug_options = {1: Weed(), 2: Coke(), 3: Heroin()}
        # self.drug_options = dict(Weed=Weed(),
        #                          Coke=Coke(),
        #                          Heroin=Heroin())

    def get_drug_class(self):
        """Get the int value for the drug type."""
        return self.drug_options.get(self.drug_type)

    def get_drug_option_names(self):
        """Returns the str names for the drugs."""
        return [name.drug_type for name in self.drug_options.values()]

    def buy(self, player):
        """A player determines what kind of drug they should buy."""
        choice = prompt_user_for_answer(
            'What would you like to buy?\n',
            options=self.get_drug_option_names()
        )
        buy_drug(player, Drugs(choice).get_drug_class())

    def sell(self, player):
        """A player determines what kind of drug they should sell."""
        choice = prompt_user_for_answer(
            'What would you like to sell?\n',
            options=self.get_drug_option_names()
        )
        sell_drug(player, Drugs(choice).get_drug_class())


class Transaction:
    """docstring for Transaction"""

    def __init__(self, arg):
        self.arg = arg


class Drug:
    """doctsring for Drug"""

    def __init__(self):
        super(Drug, self).__init__()
        self.classification = ""
        self.legal_name = ""
        self.street_value = ""
        self.street_name = ""

    def __str__(self) -> str:
        """Print(NewDrug)"""
        return f"{self.street_name}"

    def __repr__(self):
        """Name and Classification"""
        return f"{self.street_name} Classification: {self.classification}"

    def get_drug_total_cost(self, quantity):
        """Multiply value by quantity to get total cost of drug."""
        return quantity * self.street_value


class Weed(Drug):
    """docstring for Weed"""

    def __init__(self):
        super(Weed, self).__init__()
        self.drug_type = "Weed"
        self.street_value = 50
        self.street_name = "Grass"
        self.classification = "II"


class Coke(Drug):
    """docstring for Weed"""

    def __init__(self):
        super(Coke, self).__init__()
        self.drug_type = "Coke"
        self.street_value = 300
        self.street_name = "Snow"
        self.classification = "I"


class Heroin(Drug):
    """docstring for Weed"""

    def __init__(self):
        super(Heroin, self).__init__()
        self.drug_type = "Heroin"
        self.street_value = 500
        self.street_name = "H"
        self.classification = "I"


class Player:
    """docstring for Player"""

    def __init__(self, name):
        super(Player, self).__init__()
        self.name = name
        self.health = 100
        self.cash = 2000
        self.guns = 0
        self.bank = 0
        self.debt = 5500
        self.bag_size = 100
        self.origin_location = 'Austin'     # Set to Austin for now
        self.current_location = 'Austin'
        self.drug_stash = {'Weed': 0, 'Coke': 0, 'Heroin': 0}

    def bank_roll_debit(self, amount):
        """Debit amount from bank_roll if player has enough money."""
        if amount <= self.cash:
            self.cash -= amount
            return True
        else:
            print("You do not have enough money!")

    def drug_stash_debit(self, drug_type, amount):
        """Subtract drugs from stash if player has enough drugs."""
        if amount <= self.drug_stash[drug_type]:
            self.drug_stash[drug_type] -= amount
            return True
        else:
            print("You do not have enough drugs to sell!")

    def bad_choice(self):
        """Temp method, probably will delete."""
        self.health -= 25


class Stats:
    """Player Stats displayed"""

    def __init__(self, player_stats: Player):
        self.cash = player_stats.cash
        self.guns = player_stats.guns
        self.health = player_stats.health
        self.bank = player_stats.bank
        self.debt = player_stats.debt

    def __str__(self):
        return(
            "************STATS****************\n"
            f"*     Cash:   {self.cash:>12}      *\n"
            f"*     Guns:   {self.guns:>12}      *\n"
            f"*     Health: {self.health:>12}      *\n"
            f"*     Bank:   {self.bank:>12}      *\n"
            f"*     Debt:   {self.debt:>12}      *\n"
            "*********************************"
        )


class Stash:
    """Player Stash displayed"""

    def __init__(self, player_stats: Player):
        self.drugs = player_stats.drug_stash

    def __str__(self):
        return(
            "************STASH***************************\n"
            "*  {}     *\n"
            "********************************************".format(self.drugs)
        )


# ||||||||||||||||||||BEGINNING OF FUNCTIONS||||||||||||||||||||||||||||||
def game_over():
    """Simple print statement, probably should deconstruct player class."""
    # os.system('cls' if os.name == 'nt' else 'clear')
    exit("-------GAME OVER-------")


def dead():
    """Return 4 to the main function to end while loop"""
    exit("------YOU'RE DEAD------")


def buy_drug(player, drug):
    """A player determines how much of what drug they should buy."""
    potential_amount = int(player.cash / drug.street_value)
    desired_quantity = prompt_user_for_answer(
        "How much would you like to buy?\n"
        f"You can afford {potential_amount}, "
        f"and you can carry {player.bag_size}\n"
    )
    drug_cost = drug.get_drug_total_cost(desired_quantity)
    if player.bank_roll_debit(drug_cost):
        print("Cool deal!")
        player.drug_stash[drug.drug_type] += desired_quantity
        player.bag_size -= desired_quantity


def sell_drug(player, drug):
    """A player determines how much of what drug they should sell."""
    desired_quantity = prompt_user_for_answer(
        "How much would you like to sell?\n"
        f"You have {player.drug_stash.get(drug.drug_type)}\n"
    )
    drug_cost = drug.get_drug_total_cost(desired_quantity)
    if player.drug_stash_debit(drug.drug_type, desired_quantity):
        print("Cool deal!")
        player.cash += drug_cost
        player.bag_size += desired_quantity


if __name__ == "__main__":
    NAME = 'B-Axe'
    menu_selection = 0
    # NAME = raw_input("What's your name?\n" + PROMPT)
    print(BORDER)
    print('********Welcome to DopeWars!*************')
    player = Player(NAME)

    while menu_selection != 4:
        if player.health <= 0:
            dead()
        else:
            print(Stats(player))
            print(Stash(player))
            menu_selection = prompt_user_for_answer(
                'What would you like to do?\n',
                options=MENU_OPTIONS
            )

            if menu_selection == 1:
                Drugs().buy(player)
            elif menu_selection == 2:
                Drugs().sell(player)
            elif menu_selection == 3:
                print(f'Not possible to leave the city yet. '
                      f'Enjoy {player.current_location}'
                      f' while you are there!')
            elif menu_selection == 4:
                game_over()
            else:
                print("You chose incorrectly, try again!")
                player.bad_choice()
