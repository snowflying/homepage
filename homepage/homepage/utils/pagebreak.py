# coding: utf-8
import re

RE = re.compile("<!-- \s*pagebreak \s*-->", re.I)


def get_pagebreak(content):
    tmp = RE.search(content)
    if tmp:
        rtn = content[:tmp.start()]
    else:
        rtn = content
    return rtn
