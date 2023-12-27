from Corporation import *


def remove_completed_projects(
    code_of_project: str,
    every_project: list,
    workers_tot: int,
    stats_list: list,
    complete_projects: list,
    possible_stats: list,
) -> (bool, str):
    """Remove completed projects
    Keyword arguments:
    code_of_project (str) -- The code of the project that will be removed
    every_project (list) -- A list which contains all the projects which haven't been removed
    workers_tot (int) -- The number of workers
    stats_list (list) -- The list that tracks the statistics for choice (5)
    complete_projects (list) -- The list which contains all removed completed projects
    possible_stats (list) -- All the possible status
    Return: Tuple[A boolean which states whether or not the operation was successful, A string which has an output msg regarding the operation if it was successful or not.]
    """
    try:
        index_of_project = project_names.index(
            code_of_project
        )  # geting the index of the project
        actual_end_date = datetime.datetime.now().strftime(
            "%m/%d/%Y"
        )  # getting the current date
        (
            code_of_project,
            clients_name,
            start_date,
            expected_end_date,
            number_of_workers,
            old_project_status,
            index,
        ) = every_project[
            index_of_project
        ]  # assigning the details from the project_details
        completed_project_details = [
            code_of_project,
            clients_name,
            start_date,
            expected_end_date,
            number_of_workers,
            actual_end_date,
        ]  # create a new data structure which contains the details for an completed project
        if old_project_status == "ongoing":
            workers_tot += number_of_workers  # if the old project status is ongoing then the workers in the project are added back to the `workers_tot` variable
        stats_list[index] -= 1  # subtracting 1 from the old_status index
        stats_list[
            possible_stats.index("completed")
        ] += 1  # adding 1 for the completed statistics
        complete_projects.append(
            completed_project_details
        )  # append the `completed_project_details` list to the main complete_projects list
        del every_project[
            index_of_project
        ]  # delete the project from `every_project` list
        del project_names[
            index_of_project
        ]  # delete the project_code from the `project_names` list
        return (
            True,
            "Successfully removed completed projects.",
            workers_tot,
            status_list,
            completed_projects,
            every_project,
            project_names,
        )
    except Exception as e:
        return (
            False,
            e,
            workers_tot,
            status_list,
            completed_projects,
            every_project,
            project_names,
        )
    # return the (execution status, response message, workers_tot, status_list, completed_projects, every_project, project_names)


def create_project(
    status_list: list,
    index: int,
    code_of_project: str,
    clients_name: str,
    start_date: str,
    expected_end_date: str,
    number_of_workers: str,
    project_status: str,
    workers_tot: int,
    project_names: list,
    all_projects: list,
) -> (bool, str):
    """This function creates a new project
    Keyword arguments:
    status_list (list) -- The list that is used for project statistics
    index (index) -- The index of the project status in the status list
    code_of_project (str) -- The code of the project
    clients_name (str) -- The project's clients name
    start_date (str) -- The start date of the project
    expected_end_date (str) -- The expected end date of the project
    number_of_workers (str) -- The number of workers required for the project
    project_status (str) -- The status of the project out of (ongoing,on hold, completed)
    workers_tot (int) -- total number of workers in the organization
    project_names (list) -- a list that contains all the project codes
    all_projects (list) -- a list that contains all the projects
    Return: Tuple[
        A boolean which shows if the function successfully executed or not,
        The message which will be displayed to the user
    ]
    """
    try:
        status_list[index] += 1  # add 1 to the statistics list that tracks the entire
        project_data = [
            code_of_project,
            clients_name,
            start_date,
            expected_end_date,
            number_of_workers,
            project_status,
            index,
        ]  # create a list with the details that are required
        if project_status == "ongoing" and (
            number_of_workers > workers_tot
        ):  # checking if the project status is "ongoing" and if `number_of_workers` is greater than `workers_tot` variable
            return (
                False,
                "There is not enough workers",
                workers_tot,
                all_projects,
                project_names,
            )
        if project_status == "ongoing":  # checking if the project status is "ongoing"
            workers_tot -= number_of_workers  # subtracting the workers that were entered by the user by the total workers available
        project_names.append(
            code_of_project
        )  # appending the project code to the `project_names` list
        all_projects.append(
            project_data
        )  # appending the project date to the `all_projects` list
        return (
            True,
            "Successfully created a new project",
            workers_tot,
            all_projects,
            project_names,
        )
    except Exception as e:
        return (False, e, workers_tot, all_projects, project_names)
    # return the (execution status, response message, workers_tot,all_projects, project_names)


def update_project_details(
    status_list: list,
    index: int,
    previous_index: int,
    code_of_project: str,
    clients_name: str,
    start_date: str,
    expected_end_date: str,
    number_of_workers: str,
    project_status: str,
    current_workers: int,
    workers_tot: int,
    previous_project_status: str,
) -> (bool, str):
    """An function that updates the project details
    Keyword arguments:
    status_list (list) -- The list that is used for project statistics
    index (int) -- The index of the new project status in the status_list
    previous_index (int) -- The index of the previous project status in the status_list
    code_of_project (str) -- The project code of the project
    clients_name (str) -- The (updated / usual) client name
    start_date (str) -- The (updated / usual) start date
    expected_end_date (str) -- The (updated / usual) end date
    number_of_workers (str) -- The (updated / usual) number of workers
    project_status (str) -- The (updated / usual) project status
    current_workers (int) -- The number of workers before the project was updated
    workers_tot (int) -- The total number of workers
    previous_project_status (str) -- The previous project status
    Return: Tuple[
        A boolean which shows if the function successfully executed or not,
        The message which will be displayed to the user
    ]
    """
    try:
        if (
            number_of_workers
            > workers_tot
            + (current_workers if previous_project_status == "ongoing" else 0)
            and project_status == "ongoing"
        ):  # checking if there is enough workers if the project_status is "ongoing" to make sure that workers are going to be assigned, and then we check if the there is enough workers to add a project
            return (False, "Workers chosen are too much", workers_tot)
        if project_status == "ongoing":  # checking if the project status is "ongoing"
            workers_tot -= number_of_workers  # subtracting the number_of_workers from the workers total
        if (
            previous_project_status == "ongoing"
        ):  # checking if the project status is "ongoing"
            workers_tot += (
                current_workers  # adding the current_workers from the workers total
            )
        status_list[index] += 1  # updating the statistics_list of the new status
        status_list[
            previous_index
        ] -= 1  # updating the statistics metrics of the old status
        project_data = [
            code_of_project,
            clients_name,
            start_date,
            expected_end_date,
            number_of_workers,
            project_status,
            index,
        ]  # create an project_data list which contains all the data
        index = project_names.index(
            code_of_project
        )  # finding the index of the project_code
        all_projects[
            index
        ] = project_data  # reassign the all_projects index to the project_data list
        return (True, "Project details updated successfully", workers_tot)
    except Exception as e:
        return (False, e, workers_tot)
    # return the (execution status, response message, workers_tot)
