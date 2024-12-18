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


def get_grades(sheet):
    print("Please enter the Grades for students")
    print("Enter 5 grades separated by commma(,)")
    print("Example: 60,76,48,90,54\n")
    grade = input("Enter the here: ")
    print(f'the Grades provided is {grade}')


get_grades('math')


# student = SHEET.worksheet('math')
# data = student.get_all_values()
# print(data)
