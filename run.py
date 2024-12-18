import gspread
from google.oauth2.service_account import Credentials
from pprint import pprint
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('students_grades')


def get_grades():
    """
    Get grades from user
    Use a while loop that ends only when grades are 5 long
    and all the grades numbers rather than something else.
    """
    while True:
        print("Please enter the Grades for students")
        print("Enter 5 grades separated by commma(,)")
        print("Example: 60,76,48,90,54\n")
        grade_str = input("Enter the here:\n")

        grades = grade_str.split(',')
        if validate_grades(grades):
            print("Data is valid!.")
            break
    # print(grades)
    # values = [int(value) for value in grades]
    # update_math_worksheet(values)
    return grades


def validate_grades(grades):
    """
    convert string values to integers(within try).
    raise ValueError if can not convert the string to integer,
    or the grades not exactly 5.
    """
    try:
        [int(num) for num in grades]
        if len(grades) != 5:
            raise ValueError(
                f"Expected 5 values. you provided ({len(grades)})")
    except ValueError as error:
        print(f"Invalid data!: {error}, please try again.")
        return False
    return True


def update_worksheet(grades, worksheet):
    """
    receives the grades(list of integers)
    insert the grades in the relevent worksheet
    """
    print(f"Updating grades in {worksheet} worksheet...\n")
    worksheet_to_update = SHEET.worksheet(worksheet)
    worksheet_to_update.append_row(grades)
    print(f"{worksheet} worksheet updated successfully.\n")


def get_subject_grades(worksheet):
    """
    Gets the grades of particular worksheet
    """
    subject_worksheet = SHEET.worksheet(worksheet)
    columns = []
    for ind in range(1, 6):
        column = subject_worksheet.col_values(ind)
        columns.append(column[1:])
    # pprint(columns)
    # calculate_average(columns, worksheet)
    return columns


def calculate_average(data, worksheet):
    """
    calculate the average grades for all students
    in particular subject
    """
    print(f"Calculating Average value of {worksheet} starting...\n")
    new_data = []
    for column in data:
        int_column = [int(num) for num in column]
        average = sum(int_column)/len(int_column)
        new_data.append(round(average))
    return new_data
    # math = SHEET.worksheet('math').get_all_values()
    # pprint(math[-1])


def print_average_result(data, worksheet):
    """
    prints out  the average value of particular worksheet
    for all students
    """
    result = {}
    worksheet_heading = SHEET.worksheet(worksheet).get_all_values()[0]
    # pprint(worksheet_heading)
    for ind in range(5):
        result[worksheet_heading[ind]] = data[ind]
        # pprint(columns)
        # calculate_average(columns, worksheet)
        # return columns
    return result


def calculate_max_grade(data, worksheet):
    """
    calculate the maximum grades for all students
    in particular subject
    """
    print(f"Calculating Max value of {worksheet} starting...\n")
    new_data = []
    for column in data:
        int_column = [int(num) for num in column]
        max_grade = max(int_column)
        new_data.append(max_grade)
    return new_data


def print_max_result(data, worksheet):
    """
     prints out  the maximum value of particular worksheet
    for all students
    """
    result = {}
    worksheet_heading = SHEET.worksheet(worksheet).get_all_values()[0]
    # pprint(worksheet_heading)
    for ind in range(5):
        result[worksheet_heading[ind]] = data[ind]
        # pprint(columns)
        # calculate_average(columns, worksheet)
        # return columns
    return result


def read_subject_name():

    while True:
        print("Please enter which subject to update.")
        print("you should enter only number (1/2/3).")
        print("1.Math   2.Science   3.Biology")
        option = input("Enter here!\n")
        validate_number(option)
        if validate_number(option):
            break
    return option


def validate_number(number):
    # print("xf")
    try:
        int(number)
    except ValueError:
        print("enter number please")
        return False
    return True


def main():
    """
    call all program functions
    """

    values = get_grades()
    grades = [int(value) for value in values]

    subject = read_subject_name()
    print(subject)
    if int(subject) == 1:
        print('math')
        update_worksheet(grades, 'math')
    elif int(subject) == 2:
        update_worksheet(grades, 'science')
    elif int(subject) == 3:
        update_worksheet(grades, 'biology')

    """
    subject_columns = get_subject_grades('math')
    pprint(subject_columns)

    average_data = calculate_average(subject_columns, 'math')
    print(average_data)

    average_result = print_average_result(average_data, 'math')
    print(average_result)

    max_grade_data = calculate_max_grade(subject_columns, 'math')
    print(max_grade_data)
    max_result = print_max_result(max_grade_data, 'math')
    print(max_result)
    """


print("\nStaring the program.")
print("------------------")
main()

# subject = read_subject_name()
# print(subject)
# update_worksheet(grades, 'math')


"""
subject_columns = get_subject_grades('math')
pprint(subject_columns)

average_data = calculate_average(subject_columns, 'math')
print(average_data)

average_result = print_average_result(average_data, 'math')
print(average_result)

max_grade_data = calculate_max_grade(subject_columns, 'math')
print(max_grade_data)
max_result = print_max_result(max_grade_data, 'math')
print(max_result)
"""
# res = print_average_result(average_data, 'math')
# student = SHEET.worksheet('math')
# data = student.get_all_values()
