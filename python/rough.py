class Quiz:
    def __init__(self, title, li):
        self.title = title
        self._answers = li


class Course:
    def __init__(self, courseCode, list):
        self.courseCode = courseCode
        self._listQ = list
        self._quizCount = len(list)
        list = []
        for quiz in self._listQ:
            list.append(courseCode+quiz.title)
        self._quizcodes = list

col100q1=Quiz("quiz1",["a","b"])
col100q2=Quiz("quiz2",["a","b"])
print(Course("COL100",[col100q1,col100q2])._quizcodes[1])