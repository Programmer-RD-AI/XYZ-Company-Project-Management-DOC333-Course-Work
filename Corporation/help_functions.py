from Corporation import *


def menu(
    redirect: bool = False,
    to: int = None,
    name_of_the_company: str = company_name,
    msg: str = "Enter your choice: ",
) -> str:
    """This function finds the choice that should be displayed to the user next...

    Keyword arguments:
    redirect (bool) -- A boolean to know whether or not the user will be redirected
    to (int) -- The choice that user will be redirected to
    name_of_the_company (str) -- The companies name that will be displayed
    msg (str) -- The message that will be displayed to the user asking their next choice

    Return: (str) the next choice which the user has chosen...
    """
    main_menu = f"""
     {name_of_the_company}
     Main Menu
     1. Add a new project to existing projects.
     2. Remove a completed project from existing projects.
     3. Add new workers to available workers group.
     4. Updates details on ongoing projects.
     5. Project Statistics.
     6. Exit
    """.center(
        14
    )
    print(
        "Redirecting..." if redirect else main_menu
    )  # checking if the `redirect` variable is True if it is then "Redirecting..." if not then the main menu is displayed
    return (
        to if redirect else str(input(msg))
    )  # returning the variable `to` if `redirect` variable is True if it isnt then the user is asked an input with the `msg` string
