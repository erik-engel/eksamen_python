import requests
from markdownify import markdownify

URL = 'https://clbokea.github.io/exam/assignment_2.html'
page = requests.get(URL)

print(page.content)

markdown = markdownify(page.content)

print(markdown)