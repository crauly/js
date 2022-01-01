class Member_Setup():
    def __init__(self):
        self.name = str()
        self.age = int()
        self.gender = int()
        self.askInfo()

    def inputName(self, name: str):
        self.name = name

    def inputAge(self, age: int):
        self.age = age

    def inputGender(self, gender: int):
        self.gender = gender

    def setting(self, name, age, gender):
        self.inputName(name)
        self.inputAge(age)
        self.inputGender(gender)

    def askInfo(self):
        _name = input("Please tell me your name : ")
        _age = input("Please tell me your age: ")
        _gender = input("Please tell me your gender: ")

        self.setting(_name, _age, _gender)
