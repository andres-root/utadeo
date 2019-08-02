#!/usr/bin/env python3


class Course:
    def __init__(self, code=0, name, classroom=None, teacher):
        self.code = code
        self.name = name
        self.classroom = classroom
        self.teacher = teacher
    
    def set_teacher(self, teacher):
        self.teacher = teacher
        return self.teacher
    
    def get_teacher(self):
        return 'Teacher: {}'.format(self.teacher.fullname)

    def __repr__(self):
        return 'Course: {}'.format(self.name)
    
    def __str__(self):
        return 'Course: {}'.format(self.name)
