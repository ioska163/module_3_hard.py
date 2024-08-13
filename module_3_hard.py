def calculate_structure_sum(data):
    summ = 0
    

    if isinstance(data,int):
        return data
    elif isinstance(data,str):
        return len(data)
    elif isinstance(data, (list,tuple,set)):
        for i in data:
            summ += calculate_structure_sum(i)
    elif isinstance(data,dict):
        for key, value in data.items():
            summ += calculate_structure_sum(key)
            summ += calculate_structure_sum(value)
    return summ








data_structure = [[1, 2, 3], {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}),"Hello",((), [{(2, 'Urban', ('Urban2', 35))}])]

result = calculate_structure_sum(data_structure)
print(result)













data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]




#Все числа (не важно, являются они ключами или значениям или ещё чем-то).
#Все строки (не важно, являются они ключами или значениям или ещё чем-то)