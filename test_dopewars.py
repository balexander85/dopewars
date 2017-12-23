from main import Player

PLAYER_NAME = "Brian"
PLAYER_CASH_START = 2000


class BaseTest:

    def setup(self):
        self.player = Player(PLAYER_NAME)


class TestPlayer(BaseTest):

    def test_name(self):
        assert self.player.name == PLAYER_NAME

    def test_add_cash(self):
        added_cash = 200
        new_cash_balance = added_cash + PLAYER_CASH_START
        assert self.player.cash == PLAYER_CASH_START
        output = self.player.cash_credit(added_cash)
        print(output)
        assert self.player.cash == new_cash_balance

    def test_debit_cash(self):
        debited_cash = 200
        new_cash_balance = PLAYER_CASH_START - debited_cash
        assert self.player.cash == PLAYER_CASH_START
        self.player.cash_debit(debited_cash)
        assert self.player.cash == new_cash_balance

    def test_buy_weed(self):
        added_stash = 20
        weed_start_balance = 0
        new_weed_balance = added_stash + self.player.drug_stash["Weed"]
        assert self.player.drug_stash["Weed"] == weed_start_balance
        assert self.player.bag_size == 100
        self.player.stash_credit("Weed", added_stash)
        assert self.player.drug_stash["Weed"] == new_weed_balance
        assert self.player.bag_size == 80

    def test_sell_weed(self):
        self.player.drug_stash["Weed"] = 40
        self.player.bag_size = 60
        assert self.player.drug_stash["Weed"] == 40
        assert self.player.bag_size == 60
        debited_stash = 20
        new_weed_balance = self.player.drug_stash["Weed"] - debited_stash
        self.player.stash_debit("Weed", debited_stash)
        assert self.player.drug_stash["Weed"] == new_weed_balance
        assert self.player.bag_size == 80


