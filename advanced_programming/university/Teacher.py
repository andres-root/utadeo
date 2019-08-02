#!/usr/bin/env python3


class Student:
    def __init__(self, id=0, first_name, last_name, salary=0):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.fullname = '{0} {1}'.format(self.first_name, self.last_name)
        self.salary = salary

    def __repr__(self):
        return 'Student: {}'.format(self.fullname)
    
    def __str__(self):
        return 'Student: {}'.format(self.fullname)
