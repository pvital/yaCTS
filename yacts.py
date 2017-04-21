#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2017 Paulo Vital
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os
import sys

from yacts.yacts_io import YactsIO
from yacts.yacts_talk import YactsTalk

def usage():
    print("usage: yacts [-h] input_file ")

def main(argv):
    if len(argv) < 2:
        usage()
        sys.exit(2)

    if argv[1] == "-h":
        usage()
        sys.exit(0)

    # For each argument from argv, check if it's a regular file to then read
    # the content
    files = []
    for arg in argv[1:]:
        if not os.path.isfile(arg):
            print("IO ERROR: file %s is not a regular file." % arg)
            continue
        files.append(YactsIO(arg))

    tracks = []
    for file in files:
        talks = []
        for line in file.content:
            talks.append(YactsTalk(line[0], line[1]))

        for talk in talks:
            print "%s - %s - %s" % (talk.get_title(), talk.get_duration(),
                                    talk.get_time_slot())
            tracks.append()


if __name__ == "__main__":
    main(sys.argv)
    sys.exit(0)
