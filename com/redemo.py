import re
from aip import AipOcr
import cv

line = 'boysoe'
regex_str = '.*(b.{1}b).*'
# regex_str = '^.*sy.*$'
if re.match(regex_str, line):
    print(True)
else:
    print(False)
