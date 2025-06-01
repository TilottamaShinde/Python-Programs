from bs4 import BeautifulSoup

html_doc = """
<html>
    <body>
        <h2>Welcome</h2>
        <h2>About Us</h2>
        <h2>Contact</h2>
    </body>
</html>
"""

soup = BeautifulSoup(html_doc, 'html.parser')
for tag in soup.find_all('h2'):
    print(tag.text)
