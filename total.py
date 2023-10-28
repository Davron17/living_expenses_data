import json

def total_expenses(file_path: str) -> float:
    """
    get total expenses from json file
    
    Args:
        file_path (str): path to json file

    Returns:
        float: total expenses
    """
    f=open(file_path).read()
    d=json.loads(f)
    t=0.0
    for i in d:
        t+=d[i]
    return t
# test
file_path = "data.json"
total = total_expenses(file_path)
print(total)
