def get_stats(class_list):
    new_stats = []
    for element in class_list:
        new_stats.append([element[0], element[1], average(element[1])])
    return new_stats

def average(grades):
    try: 
        return sum(grades)/len(grades)
    except ZeroDivisionError:
        print("no grades data")
        return 0.0 # return a value 

my_list = [
    ["bob",[50,50,50]],
    ["john",[50,50,50]],
    ["charlie",[]]
]

print(get_stats(my_list))