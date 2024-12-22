
# Students Grades CMD. 
  Wellcome to my **worksheet students project**. \
  This is a Python command line program that runs using Code Institute mock terminal on Heroku\
  It looks like the image below:

  ![](/media/project-image.png)

## Wireframing
**Lucid Flowcharts**
- I designed a flowchart  using **Lucid app** to record the steps of the program,\
  to make it easy later on when writing the functions.

  ![](/media/flowchart2.png)

## Features

**Existing Features**

- The Starting message
  - The program starts with a message to introduce itself and descripes what it does,\
    like it receives subject name as a number and then displays the name of subjects
     and waits the user to enter his choice.

![](/media/starting.png)

- Enter grades
  - It prompts user to choose a subject name and input grades and gives a sample example.

    ![](/media/enter-grades.png)

- Progress
  * It shows the program progress.

    ![](/media/progress.png)
- Results

  * It calculates the average and max value of the grades in a subject chosen from user
    and print it out to the terminal.

    ![](/media/calculations.png)

+ Continue possibility

  + It gives the user possibility to continue the program to update another worksheet\
     and prints the results.
  
      ![](/media/continue.png)

- Terminate the program
  - It terminates the program when user finished updating all subjects saying(bye!).

    ![](/media/terminate.png)

- Input validation and error checking

  - It validates all user inputs and displayes the relevant message.

     ![](/media/checknumber.png)
  + You cann't enter a string where an integer number expected.
    
     ![](/media/validate-numbers.png)
    
- Grades Validation

  * It does not accepts negative grades.
    
     ![](/media/negative.png) 

  + You cann't enter grades out of range (0-100).

    ![](/media/outofrange.png) 

**Features Left to Implement**
- I would like to expand the project to accept more students and subjects.
+ I would like to add more functions like altering worksheets.

## Data Modeling
- I used Gspread from **Google Sheets** defining my **Scope** as **Google Drive** and **Spreadsheets**
- I used **APIs** to connect to Google Cloud spread sheets
- I used  creds.json file with the APIs and credentials installed.
- The link to the sheet that this program uses is below:

    [Click here to view the worksheet!](https://docs.google.com/spreadsheets/d/1X_Yz5qgYQ4rsQ_-7Uyb2vto13UbZAlNe4hHJwRMQPHY/edit?gid=178928932#gid=178928932) 

## Testing
   I tested the program manualy by doing the following:

   - I passed the code to PEP8 linter and confirmed that the code is clear and has
      no errors.

      ![](/media/testing.png)

   - Give invalid inputs (strings) where numbers are expected (out of range) inputs
     (negative grades).
   - Tested in workspace terminal and Heroku terminal as well.

**Bugs**

  - When I deployed my project to github, I had indexing problem with lists as coloumns in worksheets\
    starting from(1), and fixed that by adding 1 where needed.
  - The code was broken when passing huge number as a grade, i fixed that by adding a feature to function\
    to accept only a range (1-100).
  - One main bug will arrise when the sheet is not clean, so please clean the sheet before proceeding,\
    I fixed that by ensuring no letters or characters such (a, z, $, %, ' , ...).\
     or null values in the sheet.

**Unfixed Bugs**
  - No unfixed bugs.

  
**Validator Testing**

  - PEP8
    - No errors where returned when passing to **pep8ci.herokuapp.com**
     ![](/assets/images/readme/testing/errorpage.png)
    

## Deployment

  - The site was deployed on **Heroku** using Code Institute mock Terminal for Heroku.

    - The steps to deploy are as follows:
      + Clone or fork the repository.
      + Create a Heroku App.
      + Set buildbacks to **python** and **NodeJs** in this order.
      + Add new **Config Var** (The key is PORT and the value is 8000).
      + Use creds.json file content as a key(CREDS) and add its content.\
        you need the content to use its credentials to connect to the API in order to let\
        Heroku connect to spreadsheets.\
        more details about deploying [here](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+PE_PAGPPF+2021_Q2/courseware/b3378fc1159e43e3b70916fdefdfae51/605f34e006594dc4ae19f5e60ec75e2e/)
      + choose deploy.
      + The live link can be found [here](https://studens-grades-8dd6d57a22e7.herokuapp.com/)
## Credits
- Code
  - Code Institue for the deployment terminal
  - The Project idea was taken from **Love Sandiches Project**.
  - Some functions idea ware taken from the same source.
  - The steps to create project and APIs in Google Spreadsheets\
     followed from the same source.
  - The following websites ware used for problem solving.
    - **https://www.diffchecker.com/**.
    - **https://stackoverflow.com/**.
    - **https://www.w3schools.com/**.
    - **https://www.perplexity.ai/**.
- Flowchart
  - The flowchart made using **lucidchart**
    - https://www.lucidchart.com

  