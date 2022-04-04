#import beautifulsoup and request here
import requests

url = "https://www.indeed.com/jobs?q=Software Developer&l=Charlotte"

payload={}
headers = {
  'Cookie': 'CTK=1fvrdvh93ptuu800; INDEED_CSRF_TOKEN=T2ABBZ0uBzuSmcrgE1JgfpDyxQUzUoyJ; JSESSIONID=CE9A0B60F4BFD0F9EB880E945E6B7977; PREF="TM=1649114334507:L=Charlotte"; RQ="q=Software+Developer&l=Charlotte&ts=1649114334532"; UD="LA=1649114334:CV=1649114334:TS=1649114334:SG=af77ddcf45faa77487636e0b17cca30c"; ctkgen=1; indeed_rcc=""; jaSerpCount=1'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)

#function to get job list from url 'https://www.indeed.com/jobs?q={role}&l={location}'
def getJobList():
    url = 'https://www.indeed.com/jobs?q={role}&l={location}'
    # Complete the missing part of this function here 

#save data in csv file
def saveDataInCSV():
    #Complete the missing part of this function here
    print("Saving data to csv")

#main function
def main():
    # Write a code here to get job location and role from user e.g. role = input()
    print("Unnecessary change")
    print("Enter role you want to search")
    role = input()
    # Complete the missing part of this function here
    print("Enter location: ")
    location = input()
    print("Job role: ", role)
    print("location: ", location)
    getJobList(role,location)



if __name__ == '__main__':
    main()
