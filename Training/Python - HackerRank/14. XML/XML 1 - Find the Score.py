# https://www.hackerrank.com/challenges/xml-1-find-the-score/problem


import sys
import xml.etree.ElementTree as etree


def get_attr_number(node):
    """ For Understanding """
    # print(f"\n{node} -> {node.getchildren()}")
    # print(f"{node.attrib}")
    # print(f"{len(node.attrib)}")

    """ get_attr_number(node) """
    #
    # <Element 'feed' at 0x7f1cdd3ff0e8> -> [<Element 'title' at 0x7f1cdd2a94a8>, <Element 'subtitle' at 0x7f1cdd283368>, <Element 'link' at 0x7f1cdd2839f8>, <Element 'updated' at 0x7f1cdd292b88>]
    # {'{http://www.w3.org/XML/1998/namespace}lang': 'en'}
    # 1

    """ [get_attr_number(child) for child in node] """
    #
    # <Element 'title' at 0x7f1cdd2a94a8> -> []
    # {}
    # 0
    #
    # <Element 'subtitle' at 0x7f1cdd283368> -> []
    # {'lang': 'en'}
    # 1
    #
    # <Element 'link' at 0x7f1cdd2833b8> -> []
    # {'rel': 'alternate', 'type': 'text/html', 'href': 'http://hackerrank.com/'}
    # 3
    #
    # <Element 'updated' at 0x7f1cdd292b88> -> []
    # {}
    # 0
    return len(node.attrib) + sum(get_attr_number(child) for child in node)


if __name__ == "__main__":
    sys.stdin.readline()
    # 6

    xml = sys.stdin.read()
    # <feed xml:lang='en'>
    #     <title>HackerRank</title>
    #     <subtitle lang='en'>Programming challenges</subtitle>
    #     <link rel='alternate' type='text/html' href='http://hackerrank.com/'/>
    #     <updated>2013-12-25T12:00:00</updated>
    # </feed>

    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))
    # 5
