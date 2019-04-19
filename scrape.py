from bs4 import BeautifulSoup
import requests
import csv

page = requests.get(
    'https://apps.carleton.edu/student/orgs/#CulturalIntercultural')

soup = BeautifulSoup(page.text, 'html.parser')

# listOfOrgs = soup.find(id_='orgsList')
subheadings = soup.find_all(class_='orgContainer')
titles = soup.find_all(class_='careerField')
intercultural = titles[2]
# orgsSet = listOfOrgs.find_all('careerField')
# print(intercultural)

# print(type(subheadings))
# print(len(subheadings))
# print(type(listOfOrgs))
# print(type(orgsSet))
# print(orgsSet)



# print(intercultural.find_next_siblings("div"))


orgs = []
# 74 - 111 is OIIL
count = 1
for org in subheadings:
    info = {}
    
    if count in range(74,112):
        info['Organization Name'] = org.h4.contents[0]

        if org.div.p == None:
            member = 'Not listed'

        elif org.div.p == 'Visit our':
            member = 'Not listed'
        else:
            member = org.div.p.contents[0].strip('Contact:(')
            # print(org.div.p.contents[1])
            contact = org.div.p.contents[1]['href'].strip('mailto:')
            # print(contact)
            info['Board Members'] = member
            info['Contact'] = contact

        orgs.append(info)
    
    count += 1

# print(orgs)

with open('data.csv', mode='w') as csv_file:
    fieldnames = ['Organization Name', 'Board Members', 'Contact']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(orgs)
    # print(org.div.p.contents[0].strip('('))
