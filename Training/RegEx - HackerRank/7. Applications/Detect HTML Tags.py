# https://www.hackerrank.com/challenges/detect-html-tags/problem


import re


# Inputs
standard_input = """2
<p><a href="http://www.quackit.com/html/tutorial/html_links.cfm">Example Link</a></p
<div class="more-info"><a href="http://www.quackit.com/html/examples/html_links_examples.cfm">More Link Examples...</a></div>"""

result = set()  # type: ignore
for _ in range(int(input())):
    line = input()
    result = result | set(re.findall(r"<(\w+).*?>", line))

print(*sorted(result), sep=";")
# a;div;p
