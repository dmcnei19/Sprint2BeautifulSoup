# import beautifulsoup and request here
import json
from urllib import request, response
from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup
import urllib3


app = Flask(__name__, template_folder="templates")

@app.route("/")
def displayJobDetails():
    with request.urlopen("https://raw.githubusercontent.com/dmcnei19/Sprint2BeautifulSoup/main/jobDetails.json") as result:
        raw = result.read()
        responseJSON = json.loads(raw)
    return render_template('index.html', responseJSON= responseJSON)


# function to get job list from url 'https://www.indeed.com/jobs?q={role}&l={location}'
def getJobList(role, location):
    url = 'https://www.indeed.com/jobs?q=' + role + '&l=' + location
    # Complete the missing part of this function here
    request = requests.get(url)
    job = BeautifulSoup(request.text, 'html.parser')
    job.prettify()
    jobTitle = job.find('h2', class_='jobTitle').text
    companyName = job.find('span', class_='companyName').text
    jobSnippet = job.find('div', class_='job-snippet').text
    salary = job.find('div', class_='salary-snippet-container').text
    endJob = [jobTitle, companyName, jobSnippet, salary]
    return endJob


# save data in csv file
def saveDataInJSON(job):
    # Complete the missing part of this function here
    print("Saving data to JSON")
    output = open("jobDetails.json", 'w')
    json.dump(job, output)
    output.close()


# main function
def main():
    # Write a code here to get job location and role from user e.g. role = input()
    print("Enter role you want to search")
    role = input()
    # Complete the missing part of this function here
    print("Enter location: ")
    location = input()
    print("Job role: ", role)
    print("location: ", location)
    job = getJobList(role, location)
    saveDataInJSON(job)
    displayJobDetails(job)


if __name__ == '__main__':
    app.run(host="127.0.1", port=5000, debug=True)
    displayJobDetails()
    main()
