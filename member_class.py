class Member_Setup():
    def __init__(self):

        self.members = [
        ]

    def setting(self, name, age, gender):

        entry = {name:
            [
                age, gender
            ]
        }

        self.members.append(entry)

    def input_member(self):
        _name= input("Please tell me your name : ")
        _age= input("Please tell me your age: ")
        _gender= input("Please tell me your gender: ")

        self.setting(_name, _age, _gender)
