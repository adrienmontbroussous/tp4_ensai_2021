from PyInquirer import Separator, prompt

from view.abstract_view import AbstractView
from view.session import Session


class StartView(AbstractView):

    def __init__(self):
        self.__questions = [
            {
                'type': 'list',
                'name': 'choix',
                'message': 'Bonjour '+str(Session().user_name),
                'choices': [
                    'Next'
                    , 'Pokemon List'
                    , 'Attack List'
                    , 'Sign In example'

                ]
            }
        ]

    def display_info(self):
        print('welcolme')

    def make_choice(self):
        reponse = prompt(self.__questions)
        if reponse['choix'] == 'Next':
            pass
        elif reponse['choix'] == 'Pokemon List':
            from view.pokemon_list_view import PokemonListView
            return PokemonListView()
        elif reponse['choix'] == 'Attack List':
            from view.attack_list_view import AttackListView
            return AttackListView()
        elif reponse['choix'] == 'Sign In example':
            from view.sign_in_example import SignInExample
            return SignInExample()


