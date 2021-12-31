import pandas as pd

def inputMember(name, age, gender):
  member = dict(name=name,
              age=age,
              gender=gender)
  return member
  
def stockData(member: dict, df: pd.DataFrame) -> pd.DataFrame:
  df.append(member)
  return df