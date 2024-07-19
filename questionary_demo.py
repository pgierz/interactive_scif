#!/usr/bin/env python3
import questionary
from questionary import Style

custom_style_dope = Style(
    [
        ("separator", "fg:#6C6C6C"),
        ("qmark", "fg:#FF9D00 bold"),
        ("question", ""),
        ("selected", "fg:#5F819D"),
        ("pointer", "fg:#FF9D00 bold"),
        ("answer", "fg:#5F819D bold"),
    ]
)


def main():
    questionary.text("What's your first name").ask()
    questionary.password("What's your secret?").ask()
    questionary.confirm("Are you amazed?").ask()
    questionary.select(
        "What do you want to do?",
        choices=["Order a pizza", "Make a reservation", "Ask for opening hours"],
    ).ask()
    questionary.rawselect(
        "What do you want to do?",
        choices=["Order a pizza", "Make a reservation", "Ask for opening hours"],
    ).ask()
    questionary.checkbox(
        "Select toppings", choices=["foo", "bar", "bazz"], style=custom_style_dope
    ).ask()
    questionary.path("Path to the projects version file").ask()


if __name__ == "__main__":
    main()
