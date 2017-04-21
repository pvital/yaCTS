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

class YactsTalk:
    """yaCTS Talk Class
    """

    def __init__(self, title=None, duration=5):
        self.title = title
        self.duration = duration
        self.time_slots = duration/5

    def set_title(self, title):
        self.title = title

    def get_title(self):
        return self.title

    def set_duration(self, duration):
        self.duration = duration
        self.time_slots = duration/5

    def get_duration(self):
        return self.duration

    def get_time_slot(self):
        return self.time_slots

if __name__ == "__main__":
    lunch = YactsTalk()
    lunch.set_title("Lunch")
    lunch.set_duration(60)
    networking = YactsTalk("Networking Event", 60)
