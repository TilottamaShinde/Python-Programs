from bs4 import BeautifulSoup

html_doc = """
<html>
    <body>
        <h1>Favorite Site</h1>
        <ul>
            <li><a href = "https://www.google.com">Google</a></li>
            <li><a href = "https://www.github.com">GitHub</a></li>
            <li><a href  = "https://stackoverflow.com">Stack Overflow</a></li>
        </ul>
    </body>
</html>
"""
soup = BeautifulSoup(html_doc, "html.parser")

#Extract all links and print their text and URLs
for link in soup.find_all('a'):
    text = link.get_text()
    href = link.get('href')
    print(f"Text: {link.text} | URL: {link['href']}")
