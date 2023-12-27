from Corporation import *


def date_verification(msg: str) -> str:
    """A function that uses recursion to make sure that the entered date is in a correct format...
    Keyword arguments:
    msg (str) -- the message that should be displayed...
    Return: A string which contains a correct date format...
    """
    try:
        date = input(msg)  # asking the user for an input
        splitted_date = date.split(
            date[2] if len(date) > 3 else " "
        )  # splitting the data with the second element (starting from 0) the string
        if (
            len(splitted_date) != 3
        ):  # checking if there is 3 elements in the list of the splitting string
            print("Enter a valid format of the date..!")
            return date_verification(msg)
        month, date, _ = splitted_date  # splitting the list into month, date, and yrs
        if int(month) > 12:  # checking if the months are bigger than 12
            print("Enter a valid month..!")
            return date_verification(msg)
        if int(date) > 31:  # checking if the date is higher than 31
            print("Enter a valid date..!")
            return date_verification(msg)
        return date
    except:
        print("An error occured please enter the value again..!")
        return date_verification(msg)


def project_status_verification(
    msg: str = "Project Status (ongoing/completed/on hold) : ",
    update_status: bool = False,
) -> (str, list, int):
    """An function that uses recursion to make sure that an input is enter as required
    Keyword arguments:
    msg -- The message that should be displayed to the user to get the project status input
    update_status -- Whether to update the status count
    Return: Tuple[The state enter by the user,
                    the statistic list used to track the project status count,
                    the index of the enter state
                ]
    """
    project_state = (
        str(input(msg)).replace(" ", "").lower()
    )  # asking the user for the project_status and then replacing " " with "" and lowering the entire string
    if (
        project_state not in possible_inputs
    ):  # checking if the project_state is not in the possible_inputs
        print("The entered project status is incorrect...")
        return (
            project_status_verification()
        )  # Calls the project_status_verification() function (itself)
    if update_status:  # checking if the `update_status` boolean is True
        statistics_list[
            possible_inputs.index(project_state)
        ] += 1  # update the statistics_list
    return (
        project_state,
        statistics_list,
        possible_inputs.index(project_state),
    )  # returning (project_state,statistics_list,index)


def project_code_verification(msg: str, project_codes: list) -> str:
    """Project Code Verification function with the use of recursion...
    Keyword arguments:
    msg (str) -- The message that is displayed and ask the user to enter the project code
    project_codes (list) -- The list of project codes that already exists
    Return: (str) of a project code that doesnt already exist...
    """
    project_code = str(input(msg))  # asking the user for an project_code input
    if (
        project_code in project_codes
    ):  # checking if the project code in `project_codes` list
        print("Project Code already exists..!")
        return project_code_verification(
            msg, project_codes
        )  # return the same function (recursion)
    return project_code  # return the project_code


def check_if_int(msg) -> int:
    try:
        return int(input(msg))  # ask the user an input by displaying the `msg` variable
    except:
        print("The msg entered was not an integer")
        return check_if_int(msg)  # if an error is caused by trying to turn the input
