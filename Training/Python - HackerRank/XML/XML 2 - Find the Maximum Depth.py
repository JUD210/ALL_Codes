# https://www.hackerrank.com/challenges/xml2-find-the-maximum-depth/problem


import xml.etree.ElementTree as etree


maxdepth = -1


def depth(elem, level):
    global maxdepth
    if level == maxdepth:
        maxdepth += 1

    for child in elem:
        depth(child, level + 1)


if __name__ == "__main__":
    n = int(input())
    # 6

    xml = ""
    for i in range(n):
        xml = xml + input() + "\n"
    # <feed xml:lang='en'>
    #     <title>HackerRank</title>
    #     <subtitle lang='en'>Programming challenges</subtitle>
    #     <link rel='alternate' type='text/html' href='http://hackerrank.com/'/>
    #     <updated>2013-12-25T12:00:00</updated>
    # </feed>

    tree = etree.ElementTree(etree.fromstring(xml))
    depth(tree.getroot(), -1)
    print(maxdepth)
    # 1
