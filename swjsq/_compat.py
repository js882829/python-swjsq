from __future__ import absolute_import

import functools
import itertools
import sys


PY2 = sys.version_info[0] == 2
PY3 = sys.version_info[0] == 3

if PY2:
    text_type = unicode
    binary_type = str

    iterbytes = functools.partial(itertools.imap, ord)
else:
    text_type = str
    binary_type = bytes

    iterbytes = iter