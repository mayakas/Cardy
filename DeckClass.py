from random import shuffle, choice


class Deck:

    def __init__(self, cards, players, number_of_cards):
        self.number_of_players = players
        self.number_of_cards = number_of_cards
        self.cards = cards
        self.shuffled_cards = []
        self.shuffle()
        self.player_decks = []
        self.remaining_cards = []
        self.decks_creation()
        self.the_starting_card = {}
        self.picking_cards = []
        self.starting_card()

    def __repr__(self):
        print([f'{card["name"]} of {card["type"]}' for card in self.cards])

    def __len__(self):
        return len(self.cards)

    def __iter__(self):
        return iter(self.cards)

    def shuffle(self):
        shuffled_cards = self.cards[:]
        shuffle(shuffled_cards)
        self.shuffled_cards = shuffled_cards

    @classmethod
    def length(cls, deck):
        return len(deck)

    def starting_card(self):
        non_start_cards = ['K', 'Q', 'J', '8', '3', '2', 'A']
        # print(len(self.remaining_cards))
        self.the_starting_card = choice(
            [card for card in self.remaining_cards if card['name'] not in non_start_cards])

        self.picking_cards = [
            card for card in self.remaining_cards if card != self.the_starting_card]

    def issue_cards(self, number, picking_cards):
        cards_issued = [
            card for card in picking_cards if picking_cards.index(card) < number]
        return cards_issued, picking_cards[number:]

    @classmethod
    def next_card(cls, played_card, player_deck):
        possible_cards = [card for card in player_deck if card['name']
                          == played_card['name'] or card['type'] == played_card['type']]
        grouped_possible_cards = {
            'same_name': [card for card in possible_cards if played_card['name'] == card['name']],
            'same_type': [card for card in possible_cards if played_card['type'] == card['type']]}

    # CREATION OF PLAYER DECKS

    def decks_creation(self):
        rotation_list = list(range(1, self.number_of_players + 1))
        shuffle(rotation_list)

        for player in range(self.number_of_players):
            self.player_decks.append(
                {'player': player, 'deck': [], 'rotation_number': rotation_list[player]})

        number_of_cards = self.number_of_players * self.number_of_cards
        for deck in self.player_decks:
            deck['deck'] = self.shuffled_cards[deck['player']:number_of_cards:self.number_of_players]

        self.remaining_cards = self.shuffled_cards[number_of_cards:]
