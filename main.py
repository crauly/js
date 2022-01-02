import pandas as pd
from member_class import Member_Setup



def inputMember(name, age, gender):
  member = dict(name=name,
              age=age,
              gender=gender)
  return member
  
def stockData(member: dict, df: pd.DataFrame) -> pd.DataFrame:
  df.append(member)
  return df

member_lists = Member_Setup()




member_of_numbers = 10

for i in range(member_of_numbers):
  member_lists.input_member()