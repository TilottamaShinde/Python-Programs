from bs4 import BeautifulSoup
html_doc = """
<html>
    <body>
        <div class = "job">
            <h2 class  = "title">Python Developer</h2>
            <span class = "company">Tech Corp</span>
            <span class = "location">Remote</span>
        </div>
        <div class = "job">
            <h2 class = "title">Data Analyst</h2>
            <span class = "company">DataWiz</span>
            <span class = "location">New York</span>
        </div>
        <div class = "job">
        <h2 class = "title">Backend Engineer</h2>
        <span class = "company">CodeWorks</span>
        <span class = "location">San Francisco</span>
        </div>
    </body>
</html>
"""

soup = BeautifulSoup(html_doc, "html.parser")

jobs = soup.find_all('div', class_ = 'job')

for job in jobs:
    title = job.find('h2', class_ = 'title').text
    company = job.find('span', class_ = 'company').text
    location = job.find('span', class_ = 'location').text
    print(f"{title} at {company} ({location})")

"""
Output 
Python Developer at Tech Corp (Remote)
Data Analyst at DataWiz (New York)
Backend Engineer at CodeWorks (San Francisco)
"""
