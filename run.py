import gspread
from google.oauth2.service_account import Credentials
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
    Get grades from user.
    use a while loop that ends only when grades are 5 long,
    and all the grades are (numbers) rather than something else.
    accepts grades only from 0-100.
    """
    while True:
        print("Please enter the Grades for students")
        print("Enter 5 grades separated by commma(,)")
        print("Example: 60,76,48,90,54\n")
        grade_str = input("Enter here:\n")

        grades = grade_str.split(',')
        if validate_grades(grades):
            print("Data is valid!.\n")
            break
    # print(grades)
    # values = [int(value) for value in grades]
    # update_math_worksheet(values)
    return grades


def validate_grades(grades):
    """
    convert string values to integers(within try).
    raise ValueError if can not convert the string to integer,
    or the grades not exactly 5 values.
    added acondition to check if its from 0-100
    """
    try:
        [int(num) for num in grades]
        for num in grades:
            if int(num) not in range(101):
                raise ValueError("grade must be between 0-100")
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
    print(f"{worksheet} worksheet updated successfully!.\n")


def get_subject_grades(worksheet):
    """
    Gets the grades of particular worksheet for all students
    and return it as list of lists.
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
    Receives grades for all stdudens is a suubject and the woorksheet.
    calculate the average grades for all students,
    in particular subject and return it in a list.
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


def return_average_result(data, worksheet):
    """
    Recieves the average list for students.
    return the average value of particular worksheet
    for all students as dictionary.
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
    Receives grades for all stdudens is a suubject and the woorksheet.
    calculate the max grade for all students,
    in particular subject and return it in a list.
    """

    print(f"\nCalculating Max value of {worksheet} starting...\n")
    new_data = []
    for column in data:
        int_column = [int(num) for num in column]
        max_grade = max(int_column)
        new_data.append(max_grade)
    return new_data


def return_max_result(data, worksheet):
    """
    Recieves the max value list for students and the worksheet.
    return the max value of particular worksheet
    for all students as dictionary
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
    """
    Use while loop to:
    Ask user to choose the subject name by entering a number from 1-3.
    and checks if the entry in only number(1-3).
    return it when it meets the conditions
    the loop here is infinite, 
    ends only when condition True using break statement.
    """
    while True:
        print("Please enter a subject to start!")

        print("you should enter only number (1 / 2 / 3).\n")
        print("1.Math   2.Science   3.Biology")
        option = input("Enter here:\n")
        # validate_number(option)
        if validate_number(option):
            break
    return option


def validate_number(number):
    """
    Receives a number and  within(try):
    converts number to integer.
    checks if it is from 1-3.
    raise ValueError if can not convert the string to integer, with customised message
    """
    try:
        int(number)
        if int(number) not in [1, 2, 3]:
            raise ValueError("Expected integer number between 1-3")
    except ValueError as error:
        print(f"Invalid data!: {error}, please try again.")
        return False
    return True


def update_result(grades, subject):
    """
    Receives the grades converted to numbers(as list) and the subject name
    then cals the rest of functions, rather than calling from main
    to save repetitive tasks.
    """
    update_worksheet(grades, subject)
    subject_columns = get_subject_grades(subject)
    average_data = calculate_average(subject_columns, subject)
    average_result = return_average_result(average_data, subject)
    print(f"Average grades results of {subject}:")
    print("-------------------------------")
    for key in average_result:
        print(f"{key}: {average_result[key]}")
    max_grade_data = calculate_max_grade(subject_columns, subject)
    max_result = return_max_result(max_grade_data, subject)
    print(f"Max grades results of {subject}:")
    print("-------------------------------")
    for key in max_result:
        print(f"{key}: {max_result[key]}")


def validate_continue_answer():
    """
    Using while loop and prompts user to keep entering the answer.
    it will not exit if user don't enter the character y or n.
    """
    while True:
        answer = input("\nDo you want to continue? (y/n): \n")
        if answer.lower() == "n":
            return False
        elif answer.lower() == "y":
            return True
        else:
            print(f"Invalid input ({answer}), please enter (y/n)")


def main():
    """
    call all program functions
    """
    while True:
        print("\nThis program accepts a list of grades for 5 students,\n"
              "and a choosen(subject), then insert the grades in a worksheet.\n"
              "the worksheet contains 3 subjects (Math, Science, Biology),\n"
              "and hosted in Google Sheets.\n")
        subject = read_subject_name()
        values = get_grades()
        grades = [int(value) for value in values]
        if int(subject) == 1:
            update_result(grades, 'math')
        elif int(subject) == 2:
            update_result(grades, 'science')
        elif int(subject) == 3:
            update_result(grades, 'biology')
        # answer = input("\nDo you want to continue? (y/n): \n")
        if not validate_continue_answer():
            print("I am sad to see you exit, Bye!")
            print("------------------")
            break


print("\nStaring the program!")
print("------------------")
main()
