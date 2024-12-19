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


def get_grades(sheet):
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


def update_math_worksheet(grades):
    """
    update math worksheet add new row with the list data provided.
    """
    print("Updating grades in math sheet...\n")
    math_sheet = SHEET.worksheet('math')
    math_sheet.append_row(grades)
    print("Math worksheet updated successfully.\n")


def calculate_average(sheet):
    """
    calculate the average og grades for all students
    """
    print("Calculating Average value starting...\n")
    math = SHEET.worksheet('math').get_all_values()
    pprint(math[-1])


def main():
    """
    call all program functions
    """
    values = get_grades('math')
    grades = [int(value) for value in values]
    update_math_worksheet(grades)
    calculate_average(grades)
    # print(grades)


print("Staring the program.")
print("------------------")
main()

# student = SHEET.worksheet('math')
# data = student.get_all_values()
