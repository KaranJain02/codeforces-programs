class Slot:
    def __init__(self, day, start, end):
        self.day = day
        self.start = start
        self.end = end
    def duration(self):
        return self.end - self.start

class Course:
    def __init__(self, code, title, lectures, tutorials, labs):
        self.code = code
        self.title = title
        self.lectures = lectures.copy()
        self.tutorials = tutorials.copy()
        self.labs = labs.copy()
    def lectureHours(self):
        lh = 0
        for l in self.lectures:
            lh += l.duration()
        return lh
    # similarly, you could define tutorialHours(), labHours()

col100 = Course(
    "COL100",
    "Introduction to Computer Science",
    [Slot("Mon", 9.5, 11), Slot("Thu", 9.5, 11)],
    [],
    [Slot("Wed", 13, 15)])
ell101 = Course(
    "ELL101",
    "Introduction to Electrical Engineering",
    [Slot("Tue", 10, 11), Slot("Wed", 10, 11), Slot("Fri", 10, 11)],
    [Slot("Mon", 13, 14)],
    [])
mtl100 = Course(
    "MTL100",
    "Calculus",
    [Slot("Tue", 9, 10), Slot("Wed", 9, 10), Slot("Fri", 9, 10)],
    [Slot("Mon", 14, 15)],
    [])
nin100 = Course(
    "NIN100",
    "Introduction to Engineering",
    [],
    [],
    [Slot("Tue", 17, 18.5)])
nln100 = Course(
    "NLN100",
    "Language and Writing Skills",
    [],
    [],
    [Slot("Tue", 11, 13)])
pyl101 = Course(
    "PYL101",
    "Electromagnetic Waves and Quantum Mechanics",
    [Slot("Mon", 8, 9.5), Slot("Thu", 8, 9.5)],
    [Slot("Mon", 15, 16)],
    [])

tt = [col100, ell101, mtl100, nin100, nln100, pyl101]
print(tt[0].lectures[-1].day)
