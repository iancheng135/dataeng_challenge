# dataeng_challenge

## Objectives
A data file will be provided alongside this test. The dataset is a CSV which contains publicly available data about New York Police Dept. (NYPD) Arrest Data in 2018 first 6 six months. 

### Actions
1. Load the data file, process and output the data in the forms specified
2. Read in, process and present the data as specified in the requirements section
3. Demonstrate usage of list comprehension for at least one of the tasks
4. Allow user input to run all of your script, or specific sections


## Requirements
1. Read in the attached file
  - Produce a dictionary count records group by `OFNS_DESC` in descending order
  - Obtain the first 10 items from the resultant list and output to the console

2. Obtain the count of arrests grouped by age group and PD_CD. 
   Find the 4th greatest number of arrests by PD_CD for each age group and output to the console.


3. Export to a csv file containing user specified `OFNS_DESC`. For example, a user can specify full or part of an offence - 'ASSAULT' or 'ASSAULT 3' or 'ASSAULT 3 & RELATED'. Export the result to a csv file.

  
4. Instantiate a sqlite db and insert all records from the original csv into it.



## Code_Owner 
Name: Ian Cheng \
Email: chengqian135@gmail.com
