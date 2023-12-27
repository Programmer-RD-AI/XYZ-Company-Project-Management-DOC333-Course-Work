# import libraries / packages
from Corporation import *
import datetime

# initialize variables
company_name = "XYZ Company"
workers = 0
choice = 0
all_projects = []
completed_projects = []
execute = True
project_names = []
possible_inputs = ["ongoing", "completed", "onhold"]
statistics_list = [0] * len(possible_inputs)
redirect_choice = False
redirect_to = None


while execute:
    choice = menu(redirect=redirect_choice, to=redirect_to)  # call the menu() function
    redirect_choice, redirect_to = False, None
    if choice == "1":  # checking if the message entered is "1"
        print(
            f"""
            {company_name}
            Add a new project
          """.center(
                14
            )
        )
        code_of_project = project_code_verification(
            "Project Code : ", project_names
        )  # ask the user for the project code
        if code_of_project == "0":  # checking if the project_code entered is "0"
            continue
        clients_name = str(
            input("Clients Name : ")
        )  # ask the user for the clients_name
        start_date = date_verification(
            "Start Date (MM/DD/YYYY) : "
        )  # ask the user for the start date
        expected_end_date = date_verification(
            "Expected end date (MM/DD/YYYY) : "
        )  # ask the user for the start_date
        number_of_workers = check_if_int(
            "Numbers of Workers : "
        )  # ask the user for the number_of_workers
        (
            project_status,
            status_list,
            index,
        ) = project_status_verification()  # ask the user for the project_status
        save = str(
            input("Do you want to save the project(Yes/No)? ")
        )  # ask the user if they wanna save the project
        if save.upper() == "YES":
            (
                execution_status,
                response_msg,
                workers,
                all_projects,
                project_names,
            ) = create_project(
                status_list,
                index,
                code_of_project,
                clients_name,
                start_date,
                expected_end_date,
                number_of_workers,
                project_status,
                workers,
                project_names,
                all_projects,
            )  # calling the `create_project()` function
            print(
                f"{response_msg} ({execution_status})"
            )  # print out the response_msg and execution_status
        else:
            print("The project was *not* saved ..!")

    elif choice == "2":  # checking if the entered choice is "2"
        print(
            f"""
      {company_name}
      Remove Completed Project
    """.center(
                14
            )
        )
        code_of_project = str(
            input("Project Code : ")
        )  # asking the user for the project_code
        if (
            code_of_project not in project_names
        ):  # checking if the project_code is not already in the project_names list
            print("The project does not exist")
            continue
        save = str(
            input("Do you want to remove the project (Yes/ No)? ")
        )  # asking the user if they wanna remove the project
        if save.upper() == "YES":
            (
                execution_status,
                response_msg,
                workers,
                status_list,
                completed_projects,
                every_project,
                project_names,
            ) = remove_completed_projects(
                code_of_project,
                all_projects,
                workers,
                statistics_list,
                completed_projects,
                possible_inputs,
            )  # calling the `remove_completed_projects()`
            print(f"{response_msg} ({execution_status})")
        else:
            print(
                "The project was not removed..!"
            )  # print out the response_msg and execution_status

    elif choice == "3":  # if the user enters "3"
        print(
            f"""
      {company_name}
      Add new Workers
    """.center(
                14
            )
        )
        new_no_of_workers = check_if_int(
            "Number Workers to Add : "
        )  # asking the user for the number of workers to add
        if new_no_of_workers < 0:  # making sure that there is more than zero worker
            print("Workers must be more than 0..!")
            continue
        save = str(
            input("Do you want to add ? (Yes / No) ")
        )  # asking the user if they wanna add the the project
        if save.upper() == "YES":  # checking if the user entered "YES"
            workers += new_no_of_workers  # adding the number of workers to the total available worker list
            print("Workers added successfully..!")
        else:
            print("Workers were not added..!")

    elif choice == "4":  # check if the user entered is "4"
        print(
            f"""
      {company_name}
      Update Project Details
    """.center(
                14
            )
        )
        code_of_project = str(input("Project Code : "))  # enter the project code
        if (
            code_of_project not in project_names
        ):  # checking if the project_code is in the project_names list
            print("There isn't a project with the mentioned project code..!")
            continue
        if (
            code_of_project.replace(" ", "") == "0"
        ):  # checking if the project_code is zero
            continue
        clients_name = str(
            input("Clients Name : ")
        )  # asking the user for the clients name
        start_date = date_verification(
            "Start Date (MM/DD/YYYY) : "
        )  # asking the user for the start date
        expected_end_date = date_verification(
            "Expected end date (MM/DD/YYYY) : "
        )  # asking the user for the expected end date
        number_of_workers = check_if_int(
            "Numbers of Workers : "
        )  # asking the user for the number of workers
        (
            project_status,
            status_list,
            index,
        ) = project_status_verification()  # asking the user for the project status
        save = str(
            input("Do you want to update the project details (Yes/No)?")
        )  # asking the user if they wanna update the project_details
        if save.upper() == "YES":
            (
                current_workers,
                previous_project_status,
                previous_index,
            ) = all_projects[project_names.index(code_of_project)][
                4:
            ]  # assigning the current_workers, previous_project_status, previous_index to the [4:]
            execution_status, response_msg, workers = update_project_details(
                status_list,
                index,
                previous_index,
                code_of_project,
                clients_name,
                start_date,
                expected_end_date,
                number_of_workers,
                project_status,
                current_workers,
                workers,
                previous_project_status,
            )  # call the `update_project_details` method
            print(
                f"{response_msg} ({execution_status})"
            )  # printing out the response msg and the execution status
        else:
            print("The project was not updated")

    # When user choice is 5
    elif choice == "5":  # checking if the user entered "5"
        print(
            f"""
      {company_name}
      Project Statistics
    """.center(
                14
            )
        )
        for idx, item in enumerate(
            possible_inputs
        ):  # iterating the possible_inputs using `enumerate` function
            print(f"Number of {item} projects : {statistics_list[idx]}")
        print(f"Number of available workers : {workers}")
        add_project = str(
            input("Do you want to add the project (Yes/No)?")
        )  # asking the user if they wanna add the project
        if (
            add_project.upper() == "YES"
        ):  # checking if the user says they wanna add the project
            redirect_choice, redirect_to = (
                True,
                "1",
            )  # setting variables so that they can change redirect the user to the "1" choice

    elif choice == "6":  # checking if the user entered "6"
        print("Exiting Program...")
        execute = False  # setting execute to False so the program stops

    else:
        print("Please enter a valid choice..!")
