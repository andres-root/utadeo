#!/usr/bin/env python3


class Student:
    def __init__(self, id=0, first_name, last_name, degree=None, courses=[]):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.last_name = last_name
        self.fullname = '{0} {1}'.format(self.first_name, self.last_name)
        self.degree = degree
        self.courses = courses
    
    def set_course(self, course):
        self.courses.append(course)
        return self.courses

    def __repr__(self):
        return 'Student: {}'.format(self.fullname)
    
    def __str__(self):
        return 'Student: {}'.format(self.fullname)
