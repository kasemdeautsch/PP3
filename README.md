
# Students Grades CMD. 
  Wellcome to my **worksheet students project**. \
  This is Python command line program that runs using Code Institute mock terminal on Heroku\
  It looks like the image below:

  ![](/media/project-image.png)

## Wireframing
**Lucid Flowcharts**
- I designed a flowchart  using **Lucid app** to record the steps of the program \
  to make it easy later on when writing the functions.

  ![](/media/flowchart.png)

## Features

**Existing Features**

- The Starting message
  - the program starts with a message to introduce itself and descripes what it does like it receives subject
    name as anumber and then displays the name of subjects and waits the user to enter his choice.

![](/media/starting.png)

- Enter grades
  - It prompts user to choose a subject name and input grades and gives a sample example.

    ![](/media/enter-grades.png)

- Progress
  * It shows the program progress.

    ![](/media/progress.png)
- Results

  * It calculates the average and max value of the grades in a subject choosen from user
    and print it out to the terminal

    ![](/media/calculations.png)

+ Continue possibility

  + It gives the user possibility to continue the program to update another worksheet and prints the results
  
      ![](/media/continue.png)

- Terminate the program
  - It terminates the program when user finished updating all subjects saying(bye!)

    ![](/media/terminate.png)

- Input validation and error checking

  - It validates all user inputs and displayes the relevant message

     ![](/media/checknumber.png)
  + You cann't enter a string where an integer number expected
    
     ![](/media/validate-numbers.png)
    
- Grades Validation

  * It does not accepts negative grades
    
     ![](/media/negative.png) 

  + You cann't enter grades out of range (0-100)

    ![](/media/outofrange.png) 

**Features Left to Implement**
- I would expand the project to accept more students and subjects.
+ 
## Testing
  - The game works on different web browsers like Chrome, Firefox and Edge.
  - The results are always correct.
  - The web site is responsive and looks good on standard screen sizes using devtools device toolbar.
  - The header, instructions, options, results, and footer text is readable and easy to understand.
  
  
  - All Images have the **alt** attribute for the purpose of impared visual users.
  - All Buttons have the **Aria-label** attribute.
  - I included **mete tags** with **keywords** and **description** attribute to enable more
    SEO improvement.
  - The fonts and colors chosen are clear and easy to understand and accessible by running it 
     in the lighthouse in DevTools.
  - I chosed  a color that is almost light brown for both header and footer
     with a color that is close to it on the body also.  


     ![](/assets/images/readme/testing/testing.png)
     
     

**Bugs**
  - When I deployed my project to github, I noticed that the  links to (css, js) were broken, \
    the reason was that i used the absolute file path:\
    `<link rel="stylesheet" href="/assets/css/style.css">`
  - To fix that I removed the / from the starting.


**Unfixed Bugs**
  - No unfixed bugs.

  
**Validator Testing**
  - HTML
    - I tested the website and no errors were returned when passing through the official W3C validator
    ![](/assets/images/readme/testing/html-validator.png)
    - Also 404.html page tested and no errors found.
    ![](/assets/images/readme/testing/errorpage.png)
    
  - CSS 
    <p>
       <a href="http://jigsaw.w3.org/css-validator/check/referer">
        <img style="border:0;width:88px;height:31px"
            src="http://jigsaw.w3.org/css-validator/images/vcss"
            alt="Valid CSS!" />
       </a>
    </p>
    
    - No errors were found when passing through the official (Jigsaw) validator
      ![](/assets/images/readme/testing/css-validator.png)
  - Accesibility
    - Colors and fonts are accesible and readable using lighthouse in devtools.
      ![](/assets/images/readme/testing/testing.png)
 - JavaScript
   - I tested the code and found only one warning about for loop.
    ![](/assets/images/readme/testing/Js.png)
## Deployment

  - The site was deployed to GitHub pages. The steps to deploy are as follows:
    - In the GitHub repository, navigate to the Settings tab.
    - Navigate to **Pages** tab in the left menue.
    - From the source section drop-down menu choose **Deploy from branch**.
    - Select the relevent branch (*main* in my case).
    - Make sure the /(root) directory is selected and klick **Save**.
    - Once the branch has been selected, the page provides the link to the deployed project.
    - The live link can be found [here](https://github.com/kasemdeautsch/pp2).
    - in the repository on the right menue under **Deplpyments** click on** github-pages**.

## Credits
- Content
  - The page design and Project idea was taken from **Portfolio Project Scope** module in our course.
  - Some functions idea ware taken from **Love Maths** project
  - The following websites ware used for problem solving.
    - **https://www.diffchecker.com/**.
    - **https://stackoverflow.com/**.
    - **https://www.w3schools.com/**.
    - **https://www.perplexity.ai/**.
    - **https://www.pexels.com/**.
    - **https://tinypng.com/**.
    -  **https://balsamiq.com/**.

- Media
  - I found the images for the (Rock Paper Scissors) in Google.
  