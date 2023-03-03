class student:

    def __init__(self, name, major, gpa):
        self.name = name
        self.major = major
        self.gpa = gpa


    def on_honor_roll(self):
        if self.gpa >= 2.5:
            return True
        else:
            return False


