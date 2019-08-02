#!/usr/bin/env python3


import Course
import Student
import Teacher

objects = {
    'course': {
        'object': Course,
        'types': ['Calculus', 'Programming', 'Artificial Intelligence'],
    },
    'student': Course,
    'teacher': Teacher,
}

def factory(object_name, **kwargs):
    try:
        obj = objects[object_name]
    except KeyError:
        raise 'Object not found.'

    for , index in enumerate(available_courses):
        courses[course] = Course(
            code=index,
            name=course,
            classroom=(100 + index)
            teacher=casir
        )



andres = Student(
    id='1234567890'
    first_name='Andres'
    last_name='Lujan'
    degree='Systems Engineering'
    courses = 
)

casir = Student(
    id='1230987456'
    first_name='Casir'
    last_name='Gonzales'
    salary=10000000 
)


available_courses = ['Calculus', 'Programming', 'Artificial Intelligence']
courses = {}

for course, index in enumerate(available_courses):
    courses[course] = Course(
        code=index,
        name=course,
        classroom=(100 + index)
        teacher=casir
    )

