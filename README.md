# Automating Interventions with Selenium and Python
***

This program will let you automate the process for documenting interventions in ecst on the current day of your class intervention.   
***

## Quickstart (Windows)

a. Open Windows Command Prompt and Install Git using `winget install --id Git.Git -e --source winget`  

b. Create folder to download Git Repository and initialize git with `git init` in the CMD 

c. Pull repo with ` git pull https://github.com/soto-sergio/ecst_intrv.git`  

d. Install miniconda using  `winget install -e --id Anaconda.Miniconda3`  

e. Create environment variables  

> conda env create -f environment.yml  
> conda activate eduenv  

## Steps

1. Download ChromeDriver if using Google Chrome as web browser. [Link](https://chromedriver.chromium.org/downloads) 
- Install and keep `chromedriver.exe` in the project's folder. [Not required. Driver already included]

2. In the `private/` folder you will see the two scripts for sensitive information:  
`credentials.py` for teacher's login info. Here, you must type your E number. Password will be asked everytime the python script is run.     
`homeroom_roster.py` for homeroom roster. Data is expected to be stored as a dictionary. ID:"First Name". Populate your homeroom roster before running the python script.  

3. Run the script `ecst_api.py`  

4. You will be asked to type your password. 

5. Then you will be propted to select between `reading` or `math` intervention.  

6. Then you will be asked to take the attendance of your homeroom class.  
   Choose between `y` or `n` if the student is present.  

7. Wait and see! 


## NOTES
>
> * IMPORTANT: Make sure the Reading intervention was created before the Math one. You can always change the date to make it appear first. 
> * Amount of minutes of each intervention entry is set to 30. Changing it seems to produce an error.
> * To cancel the script use `Ctrl + C`


