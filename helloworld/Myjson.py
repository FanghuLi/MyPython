import json


class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score


def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }


s = Student('lifanghu', 18, 99)
print(json.dumps(s, default=student2dict))
print(json.dumps(s, default=lambda obj: obj.__dict__))
def dic2student(d):
    return Student(d['name'],d['age'],d['score'])

json_str = '{"age": 18, "score": 99, "name": "lifanghu"}'
print (json.loads(json_str,object_hook=dic2student))