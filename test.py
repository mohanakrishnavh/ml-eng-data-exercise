import datetime
import os,json
import re
import pandas as pd
from pprint import pprint

'''
Reads the json logs to 

Input:
    'account_id' of the user
    
Output:
    Updated view of the user information
'''


def read_data():
    # to identify the json files in our directory
    path_to_json = 'json/'
    json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]
    
    data = pd.DataFrame(columns=['Account_ID', 'Event_Date', 'Account_Standing','First_Name','Last_Name', \
                                       'DOB', 'Address', 'E-Mail'])
    
    # we need both the json and an index number so use enumerate()
    for index, js in enumerate(json_files):
        with open(os.path.join(path_to_json, js)) as json_file:
            json_text = json.load(json_file)
            #.print(json_text)
            account_id = json_text['account_id']
            event_date = json_text['event_date']
            account_standing = json_text['account_standing']
            first_name = json_text['account_information']['first_name']
            last_name = json_text['account_information']['last_name']
            date_of_birth = json_text['account_information']['date_of_birth']
        
            address = json_text['account_information']['address']['street_number']+" "+json_text['account_information']['address']['street_name'] +" ,"+json_text['account_information']['address']['city']+" ,"+json_text['account_information']['address']['state'] +" -"+json_text['account_information']['address']['zip_code']
            email_address = json_text['account_information']['email_address']
        
            # Validating the data
            if(validate_date(event_date) and validate_name(first_name,last_name) and validate_email(email_address)):
                data.loc[index] = [account_id,event_date,account_standing,first_name,last_name,date_of_birth,address,email_address]
    
    data.to_csv("report.csv")     
    return data

def validate_date(event_date):
    #event_date = datetime.date(event_date)
    today = datetime.datetime.now()
    today_date = today.__str__()
    today = today_date.split()[0]
    if (today==event_date):
        return True
    return False

def validate_name(first_name,last_name):
    if (len(first_name)>0 and len(last_name)>0):
        return True
    return False

def validate_email(email_address):
    if re.match('[^@]+@[^@]+\.[^@]+', email_address) != None:
        return True
    return False
    
def fetch_info(account_id, data):
    info = data[data.Account_ID==int(account_id)]
    if info.empty == False:
        pprint(info)
        info.to_csv(""+account_id+".csv")
    else:
        print("Invalid Account ID")

def main():
    data = read_data()
    account_id = input("Enter the account id:")
    fetch_info(account_id, data)
    print("Information saved in "+str(account_id)+".csv file.")
    
    
if __name__ == "__main__":
    main()

