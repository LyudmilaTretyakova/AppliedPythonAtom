#!/usr/bin/env python
# coding: utf-8

class TEventStats:
    FIVE_MIN = 300

    def __init__(self):
        # TODO: реализовать метод
        self.reg_events = dict()
        self.deq = []
        self.count = 0

    def register_event(self, user_id, time):

        if user_id in self.reg_events.keys():
            self.reg_events[user_id].append(time)

        else:
            self.reg_events[user_id] = [time]
            count = 0
        # TODO: реализовать метод

    def query(self, count, time):
        itog = 0
        count1 = 0
        # TODO: реализовать метод
        time1 = time-self.FIVE_MIN
        for i in self.reg_events.keys():
            if len(self.reg_events[i]) == count:
                for ii in self.reg_events[i]:
                    if ii > time1 and ii < time:
                        count1 += 1
            else:
                count1 = -1
            if count1 == count:
                itog += 1
            count1 = 0
        return itog
