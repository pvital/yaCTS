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

class YactsTrack:
    """yaCTS Track Class
    """

    def __init__(self):
        self.track_name = None
        self.morning = {"12:00PM": "Lunch"}
        self.morning_slots = 36
        self.remaining_morning_slots = 36
        self.afternoon = {"05:00PM": "Networking Event"}
        self.afternoon_slots = 48
        self.remaining_afternoon_slots = 48

    def schedule_talk(self, talk):
        if not isinstance(talk, tuple):
            print("ERROR: invalid talk")

        # Check if there's available slots for this talk in morning
        if self.remaining_morning_slots < talk.get_time_slot():
            # If not remaining_morning_slots, then check afternoon
            if self.remaining_afternoon_slots < talk.get_time_slot():
                # there's not time slots for this track
                print("No available time to this track")
            # Schedule in the afternoon
            self.afternoon[self._get_next_time()] = talk.get_title()
            self.remaining_afternoon_slots -= talk.get_time_slot()
        # Schedule in the morning
        self.morning[self._get_next_time()] = talk.get_title()
        self.remaining_morning_slots -= talk.get_time_slot()

    def _get_next_time(self, shift):
        """
            Return the next free time of the given shift
        """
        for sessions in sorted(shift.keys()):

if __name__ == "__main__":
    track = YactsTrack()
    print track.morning
    print track.afternoon
