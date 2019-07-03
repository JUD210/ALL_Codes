# https://www.hackerrank.com/challenges/html-parser-part-1/problem


"""
from html.parser import HTMLParser

# Create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Found a start tag  :" + tag)

    def handle_endtag(self, tag):
        print("Found an end tag   :" + tag)

    def handle_startendtag(self, tag, attrs):
        print("Found an empty tag :" + tag)


# The attrs argument is a list of (name, value) pairs containing the attributes found inside the tag's <> brackets.


# Instantiate the parser and feed it some HTML
parser = MyHTMLParser()
parser.feed(
    "<html><head><title>HTML Parser - I</title></head>"
    + "<body><h1>HackerRank</h1><br /></body></html>"
)

# Found a start tag  : html
# Found a start tag  : head
# Found a start tag  : title
# Found an end tag   : title
# Found an end tag   : head
# Found a start tag  : body
# Found a start tag  : h1
# Found an end tag   : h1
# Found an empty tag : br
# Found an end tag   : body
# Found an end tag   : html

"""

from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(f"Start : {tag}")
        for attr in attrs:
            print(f"-> {attr[0]} > {attr[1]}")

    def handle_endtag(self, tag):
        print(f"End   : {tag}")

    def handle_startendtag(self, tag, attrs):
        print(f"Empty : {tag}")
        for attr in attrs:
            print(f"-> {attr[0]} > {attr[1]}")


html = "\n".join([input() for _ in range(int(input()))])
# 2

# <html><head><title>HTML Parser - I</title></head>
# <body data-modal-target class='1'><h1>HackerRank</h1><br /></body></html>

parser = MyHTMLParser()
parser.feed(html)
parser.close()
# Start : html
# Start : head
# Start : title
# End   : title
# End   : head
# Start : body
# -> data-modal-target > None
# -> class > 1
# Start : h1
# End   : h1
# Empty : br
# End   : body
# End   : html
