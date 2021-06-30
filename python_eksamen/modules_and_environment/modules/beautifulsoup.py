#Vi importerer requests fra pip, som er det module vi bruger til http requests
import requests
from pprint import pprint as pp
from bs4 import BeautifulSoup
#with these two lines, we've actually scraped the webpage, using request module.
URL = 'https://www.it-jobbank.dk/job/software-webudvikling/storkoebenhavn'
page = requests.get(URL)

# pprint, får pages content til at se en smule pænere ud. 
#pp(page.content)

# Creating af beautiful soup object:
# When instantiating a bs objecjt, you'll have to give the correct parser along as an argument
soup = BeautifulSoup(page.content, 'html.parser')

# Ved at inspecte siden, kan vi se at id=result_list_box indeholder alle job opslagne
results = soup.find(id='result_list_box')
#print(results.prettify())

# Hvert jobopslag findes i et div-element hvor klassen = 'jobsearch-result, vi kan derfor vha. bs4,
# loope over hvert jobopslag og printe dem ud med 4 mellemrum, det tynder lidt ud i koden.
job_elems = results.find_all('div', class_='jobsearch-result')

for job_elem in job_elems:

    title_elem = job_elem.find('h3', class_='job-title')
    place_elem = job_elem.find('span', class_='job-location')
    company_elem = job_elem.find('div', class_='job-company')
    description_elem = job_elem.find('p')
    
    print('Jobtitel:\n', title_elem.text, '\n')
    print('Lokation:\n', place_elem.text, '\n')
    print('Firmanavn:\n', company_elem.text, '\n')
    print('Jobeskrivelse:\n', description_elem.text, '\n')
    print('\n'*4)




