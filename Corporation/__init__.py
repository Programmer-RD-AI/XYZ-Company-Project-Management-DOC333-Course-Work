import datetime
from typing import Tuple

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

from Corporation.help_functions import *
from Corporation.verification import *
from Corporation.project_management import *
