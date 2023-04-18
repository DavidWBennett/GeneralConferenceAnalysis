import requests
import json

# Replace these variables with the URL of the repository and your GitHub API token
repo_url = "https://raw.githubusercontent.com/cgood92/general-conference-stats/master/case2/output/1971-04.json"

# Specify the starting and ending years
start_year = 1971
end_year = 2022

# Specify the two months General Conference is held
months_list = ["04","10"]

# Create a list of consecutive years
years_list = list(range(start_year, end_year + 1))

repo_urls = []
for i in years_list:
    for j in months_list:
        repo_urls.append(f"https://raw.githubusercontent.com/cgood92/general-conference-stats/master/case2/output/{str(i)}-{j}.json")


contents = [requests.get(url).json() for url in repo_urls]

def speaker_list(speaker = "Russell M. Nelson", date = "04-2018"):
    filtered_list = []
    for i in range(0,len(contents)):
        #If possible, check if the speaker spoke during the session. Currently, this is returning every session.
        filtered_list.append([d for d in contents[i] if d.get('speaker') == speaker])

    speaker_list = list(filter(lambda x: x != [], filtered_list))
    return speaker_list

#speaker_list("Russell M. Nelson", "10-1974")