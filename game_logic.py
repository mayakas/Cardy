from random import random, choice, shuffle
from DeckClass import Deck
from databank import cards
from player import Player
from Inputs import *
from output import *

# Function that calls all the other logic functions


def main():
    players = Inputs.number_of_players()
    no_of_cards = Inputs.number_of_cards()
    deck = Deck(cards, players, no_of_cards)
    player_decks = deck.player_decks
    starting_card = deck.the_starting_card
    picking_cards = deck.picking_cards
    players_with_decks = []

    display_starting_card(starting_card)

    for deck in player_decks:
        specific_deck = deck['deck']
        player_ = Player(specific_deck)
        players_with_decks.append(player_)

    for player in players_with_decks:
        print(f"PLAYER ID : {player.player_id}")
        display_10_option(player.player_deck)
        print("*"*30)

    print_len_of('picking cards', picking_cards)


# Calling the main Function to Initiate the Logic
main()
