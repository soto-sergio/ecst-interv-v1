1
# Automating Interventions with Selenium and Python
***

This program will let you automate the process for documenting interventions in ecst on the current day of your class intervention.   
***

## Steps:

1. Download ChromeDriver if using Google Chrome as web browser. [Link](https://chromedriver.chromium.org/downloads) 
- Install and keep `chromedriver.exe` in the project's folder.  

2. In the `private/` folder you will see the two scripts for sensitive information:  
`credentials.py` for teacher's login info.  `homeroom_roster.py` for homeroom roster. Data is expected to be stored as a dictionary. ID:"First Name"  

3. Run the script `ecst_api.py`  

4. You will be propted to select between `reading` or `math` intervention.  

5. Then you will be asked to take the attendance of your homeroom class.  
   Choose between `y` or `n` if the student is present.  

6. Wait and see! 


## NOTES:

> * Amount of minutes of each intervention entry is set to 30. Changing it seems to produce an error.
>
> * Please test the program with ONLY ONE student the first time since I can't confirm that the links that appear to select Math or Reading Intervention appear in the same order than it did for me.


