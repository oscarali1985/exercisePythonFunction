# Your code goes here:
def render_person(name,date,color,age,sex):
    param = name +" is a "+ str(age) +" years old "+sex+" born in "+date+" with "+color+" eyes"
    return param

2
# Do not edit below this line
print(render_person('Bob', '05/22/1983', 'green', 23, 'male'))