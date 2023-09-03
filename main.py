#import the required modules 
import csv
import sqlite3
from collections import Counter
from operator import itemgetter
import sqlite3
#Read in the attached file
def read_csv(filename):
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        data = [row for row in reader]
    return data


#Count records grouped by OFNS_DESC
def count_by_ofns_desc(data):
    counter = Counter([row['OFNS_DESC'] for row in data])
    sorted_counter = {k: v for k, v in sorted(counter.items(), key=itemgetter(1), reverse=True)}
    return sorted_counter

#Count of arrests grouped by AGE_GROUP and PD_CD
def count_by_age_and_pdcd(data):
    counter = Counter((row['AGE_GROUP'], row['PD_CD']) for row in data)
    # Process to get 4th greatest for each age group
    sorted_counter = {}
    for age, pdcd in counter.keys():
        sorted_counter.setdefault(age, []).append((pdcd, counter[(age, pdcd)]))
    for age in sorted_counter.keys():
        sorted_counter[age] = sorted(sorted_counter[age], key=itemgetter(1), reverse=True)
        sorted_counter[age] = sorted_counter[age][3] if len(sorted_counter[age]) > 3 else None
    return sorted_counter


#Export to a CSV file
def export_to_csv(data, ofns_desc, filename):
    with open(filename, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys())
        writer.writeheader()
        for row in data:
            if ofns_desc.lower() in row['OFNS_DESC'].lower():
                writer.writerow(row)


def exportToSQLite(CSVLocation):
    conn = sqlite3.connect('nypd-arrest-data-2018-1.db')
    curs = conn.cursor()
    with open(CSVLocation, 'r') as f:
        headers = f.readline().strip().split(',')
        curs.execute(f'CREATE TABLE IF NOT EXISTS nypd_arrests ({", ".join(headers)})')
        for line in f:
            values = line.strip().split(',')
            if len(values) == len(headers):
                values = [f"'{i}'" for i in values]
                curs.execute(f'INSERT INTO nypd_arrests VALUES ({", ".join(values)})')
    

if __name__ == '__main__':
    program = True
    """
    1 - Read in the attached file
        Produce a dictionary count records group by OFNS_DESC in descending order
        Obtain the first 10 items from the resultant list and output to the console
    2 - Obtain the count of arrests grouped by age group and PD_CD. Find the 4th greatest number of arrests by PD_CD for each age group and output to the console.

    3 - Export to a csv file containing user specified OFNS_DESC. For example, a user can specify full or part of an offence - 'ASSAULT' or 'ASSAULT 3' or 'ASSAULT 3 & RELATED'. Export the result to a csv file.

    4 - Instantiate a sqlite db and insert all records from the original csv into it.
    """
    while(program):
        print("#"*50)
        print('Please select an option:')
        print('1 - Read in the attached file(Obtain top 10 OFNS_DESC)')
        print('2 - Obtain the count of arrests grouped by age group and PD_CD')
        print('3 - Export to a csv file containing user specified OFNS_DESC')
        print('4 - Instantiate a sqlite db and insert all records from the original csv into it')
        print('5 - Exit')
        print("#"*50)
        option = input('Enter your option: ')
        data = read_csv('nypd-arrest-data-2018-1.csv')
        if option == '1':
            counts = count_by_ofns_desc(data)
            # print(counts)
            first_10 = list(counts.items())[:10]
            for i in range(10):
                print(f"\"{first_10[i][0]}\": {first_10[i][1]}")
        elif option == '2':
            counts_by_age_and_pdcd = count_by_age_and_pdcd(data)
            for age, pdcd in counts_by_age_and_pdcd.items():
                print(f"{age}: {pdcd}")
        elif option == '3':
            # print('')
            ofns_desc = input("Enter OFNS_DESC: ")
            export_to_csv(data, ofns_desc, f'filtered_{ofns_desc}.csv')
        elif option == '4':
            exportToSQLite('nypd-arrest-data-2018-1.csv')
        elif option == '5':
            print('Goodbye!')
            break
        else:
            print('Wrong option! Please try again.')
        
        print("\nContinue? (y/n)")
        if input() == 'n':
            program = False
            print('Goodbye!')

