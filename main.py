
# lancer dans un terminal qui est à la racine de l'application la commande python -m main

from view.start_view import StartView

# This script is the entry point of your application

if __name__ == '__main__':
    # run the StartView
    current_view = StartView()

    # while current_view is not none, the application is still running
    while current_view:
        # a border between view
        with open('graphical_assets/border.txt', 'r', encoding="utf-8") as asset:
            print(asset.read())
        # Display the info of the view
        current_view.display_info()
        # ask user for a choice
        current_view = current_view.make_choice()

    with open('graphical_assets/suprised_pikachu.txt', 'r', encoding="utf-8") as asset:
        print(asset.read())


