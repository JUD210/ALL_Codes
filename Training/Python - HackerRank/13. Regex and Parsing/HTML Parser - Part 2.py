# https://www.hackerrank.com/challenges/html-parser-part-2/problem


from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        if data.count("\n") >= 1:
            print(f">>> Multi-line Comment\n{data}")
        else:
            print(f">>> Single-line Comment\n{data}")

    def handle_data(self, data):
        if data != "\n":
            print(f">>> Data\n{data}")


html = "\n".join([input() for _ in range(int(input()))])
# 4

# <!--[if IE 9]>IE9-specific content
# <![endif]-->
# <div> Welcome to HackerRank</div>
# <!--[if IE 9]>IE9-specific content<![endif]-->

parser = MyHTMLParser()
parser.feed(html)
parser.close()
# >>> Multi-line Comment
# [if IE 9]>IE9-specific content
# <![endif]
# >>> Data
#  Welcome to HackerRank
# >>> Single-line Comment
# [if IE 9]>IE9-specific content<![endif]
