# https://www.hackerrank.com/challenges/detect-html-links/problem


""" Note some comments

I don't think this task teaches responsible use of regex.

HTML literally can't be parsed this way - not unless you give up completely on matching opening and closing tags. Even if you can get away with it this time (let's assume links never get nested, and never contain additional markup), it's bad practice.

Teaching people to use regular expressions for this is responsible for the majority of bad parsing code on the web.


All these questions that encourage the use of regex for parsing HTML are teaching poor programming practices.

"""


import re


# Inputs
standard_input = """2
# <li class="interwiki-da"><a href="//da.wikipedia.org/wiki/" title="" lang="da" hreflang="da"><b>Dansk</b></a></li>
# <li class="interwiki-sr"><a href="//sr.wikipedia.org/wiki/" title="" lang="sr" hreflang="sr"> / srpski</a></li>"""

for _ in range(int(input())):

    line = input()

    pattern = r"<a href=\"(.*?)\".*?>([\w ,./]*)(?=</)"

    result = re.findall(pattern, line)

    link: str
    title: str
    for link, title in result:
        print(link, title.strip(), sep=",")

# //da.wikipedia.org/wiki/,Dansk
# //sr.wikipedia.org/wiki/,/ srpski
