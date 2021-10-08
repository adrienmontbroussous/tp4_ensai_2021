"""
* Checkbox question example
* run example by typing `python example/checkbox.py` in your console
From : https://github.com/CITGuru/PyInquirer/blob/master/examples/checkbox.py
"""
from pprint import pprint

from PyInquirer import prompt, Separator

from prompt_toolkit.validation import Validator, ValidationError
from view.abstract_view import AbstractView
from view.session import Session
from client.pokemon_client import PokemonClient



class CheckBoxExampleView(AbstractView):
    def __init__(self):
        client = PokemonClient()
        pokemons = client.get_all_pokemon()
        print(pokemons)
        self.__questions = [
            {
                'type': 'checkbox',
                'qmark': '🐹',
                'message': 'Select your Pokemon Team',
                'name': 'pokemons',
                'choices': [ 
                    Separator('🔥Fire Starter')
                    ,{'name':'Charmander'}
                    ,{'name':'Cyndaquil'}
                    ,{'name':'Torchic'}
                    ,{'name':'Chimchar'}
                    ,{'name':'Oshawott'}
                    ,Separator('🚿Water starter')
                    ,{'name':'Squirtle'}
                    ,{'name':'Totodile'}
                    ,{'name':'Mudkip'}
                    ,{'name':'Turtwig'}
                    ,{'name':'Tepig'}
                    ,Separator('🌱Grass starter')
                    ,{'name':'Bulbasaur'}
                    ,{'name':'Chikorita'}
                    ,{'name':'Treecko'}
                    ,{'name':'Piplup'}
                    ,{'name':'Snivy'}
                ],
            }
        ]

    def display_info(self):
        print("Hello "+ str(Session().user_name) +", please choose some pokemon")

    def make_choice(self):
        answers = prompt(self.__questions)
        pprint(answers)
        from view.start_view import StartView
        return StartView()
