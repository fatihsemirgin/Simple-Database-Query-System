from blist import sorteddict
import csv
import json

sorted_dict = sorteddict()
temp_start = []
file = open('students.csv')
csvreader = csv.reader(file)
counter = 0
value2 = " "
key2 = 0

for rows in csvreader:  # Reading .csv file
    temp_start = (rows[0].split(';'))
    if counter != 0:
        key2 = temp_start[0]
        value2 = ""
        for x in range(1, 5):
            if x < 4:
                value2 += temp_start[x] + ","
            elif x == 4:
                value2 += temp_start[x]
    if counter != 0:
        sorted_dict[key2] = str(value2)
    counter = 1

characters = ("!", "<", ">", "=")  # Condition operator


def condition(*cond):  # Since the cond part comes together, it splits it and sends it.
    temp, temp_str, temp_str2 = [], "", ""
    c = cond[0]
    char = ""
    for i in characters:
        if c.__contains__(i):
            temp.append(c.index(i))
            char += i
    if len(temp) > 1:
        temp_str = c[:temp[0]]
        temp_str2 = c[temp[1] + 1:]
    else:
        temp_str = c[:temp[0]]
        temp_str2 = c[temp[0] + 1:]
    temp_str2 = clean_string(temp_str2)
    return temp_str, temp_str2, char


def value(temp, values, keyy):  # For the desired part after Select (name,grade,id or ALL)
    temp_value = ""
    if len(temp) == 0 or temp[0] == "ALL":
        temp_value = "Name: " + values[0] + ", lastname: " + values[1] + ", email: " + values[2] + ", grade: " + values[
            3]
    else:
        for m in temp:
            if m == "name" or m =="NAME":
                temp_value += "Name: " + values[0]
            elif m == "lastname" or m == "LASTNAME":
                temp_value += ", lastname: " + values[1]
            elif m == "email" or m == "EMAIL":
                temp_value += ", email: " + values[2]
            elif m == "grade" or m=="GRADE":
                temp_value += ", grade: " + values[3]
            elif m == "id" or m== "ID":
                temp_value += ", id: " + keyy
    return temp_value


def clean_string(str):  # If name comes with a punctuation mark, it clears it.
    if str[:1] == "‘" or str[:1] == "'":
        str = str[1:]
    if str[len(str) - 1] == "’" or str[len(str) - 1] == "'":
        str = str[:len(str) - 1]
    return str


def subvalue(values, id):  # To get all values.
    return values[0] + "," + values[1] + "," + values[2] + "," + values[3]


def value_cond(m, values, id):  # It pulls the element required for the condition for each item in the data.
    temp_value = ""
    if m == "id" or m== "ID":
        temp_value = id
    elif m == "name" or m == "NAME":
        temp_value = values[0]
    elif m == "lastname"or m == "LASTNAME":
        temp_value = values[1]
    elif m == "email" or m == "EMAIL":
        temp_value = values[2]
    elif m == "grade" or m == "GRADE":
        temp_value = values[3]
    return temp_value


sub_dict = sorteddict()  # To keep the dataset up to date.
temp_sorted = sorteddict()  # To keep the dataset with the desired properties.


def print_without_select(order):  # To pull the dataset with all its properties if no select has been made.
    tempor = []
    print_sorted = sorteddict()
    for id, data in order.items():
        dotum = str(data).split(",")
        print_sorted[int(id)] = value(tempor, dotum, id)
    return print_sorted


def column(condit, temp, temp2, column_value, key, condit2, column_value2, bool,
           cond_name, delete_flag):
    flag = False  # It assigns the items to a new dict in accordance with the conditions.
    flag2 = False  # Additionally, considering the requirements for deletion and it returns the delete confirmation.
    column_result = False
    chosen_op = False
    if cond_name == "AND":  # Determine and,or.
        chosen_op = True

    if condit[0] == "id" or condit[0] == "grade" or condit[0] == "id":
        column_value = int(column_value)
        condit[1] = int(condit[1])
    # CONDITIONS
    if condit[2] == "=":
        if column_value == condit[1]:
            flag = True
    elif condit[2] == "!=":
        if column_value != condit[1]:
            flag = True
    elif condit[2] == "<":
        if column_value < condit[1]:
            flag = True
    elif condit[2] == ">":
        if column_value > condit[1]:
            flag = True
    elif condit[2] == "!>":
        if not (column_value > condit[1]):
            flag = True
    elif condit[2] == "!<":
        if not (column_value < condit[1]):
            flag = True
    elif condit[2] == "<=":
        if column_value <= condit[1]:
            flag = True
    elif condit[2] == ">=":
        if column_value == condit[1]:
            flag = True

    if flag and not bool:
        if delete_flag:
            column_result = True
        else:
            temp_sorted[int(key)] = value(temp, temp2, key)
            temp = []
            sub_dict[int(key)] = subvalue(temp2, key)

    #### FOR AND and OR
    if bool:
        if condit2[0] == "id" or condit2[0] == "grade":
            column_value2 = int(column_value2)
            condit2[1] = int(condit2[1])
        # CONDITIONS
        if condit2[2] == "=":
            if column_value2 == condit2[1]:
                flag2 = True  ## tekrar bak
        elif condit2[2] == "!=":
            if column_value2 != condit2[1]:
                flag2 = True
        elif condit2[2] == "<":
            if column_value2 < condit2[1]:
                flag2 = True
        elif condit2[2] == ">":
            if column_value2 > condit2[1]:
                flag2 = True
        elif condit2[2] == "!>":
            if not (column_value2 > condit2[1]):
                flag2 = True
        elif condit2[2] == "!<":
            if not (column_value2 < condit2[1]):
                flag2 = True
        elif condit2[2] == "<=":
            if column_value2 <= condit2[1]:
                flag2 = True
        elif condit2[2] == ">=":
            if column_value2 >= condit2[1]:
                flag2 = True
        if chosen_op:
            if flag and flag2:  # FOR AND
                if delete_flag:
                    column_result = True
                else:
                    temp_sorted[int(key)] = value(temp, temp2, key)
                    temp = []
                    sub_dict[int(key)] = subvalue(temp2, key)
        else:
            if flag or flag2:  # FOR ELSE
                if delete_flag:
                    column_result = True
                else:
                    temp_sorted[int(key)] = value(temp, temp2, key)
                    temp = []
                    sub_dict[int(key)] = subvalue(temp2, key)

    return column_result


def fragmentation(data):  # For insertion. It shreds the data in the command and returns it.
    temp_value2 = ""
    data = data[7:len(data) - 1]
    arr = data.split(",")
    for x in range(1, 5):
        if x < 4:
            temp_value2 += arr[x] + ","
        elif x == 4:
            temp_value2 += arr[x]
    return arr[0], temp_value2


temp = []
select_flag = False
sub_temp = []
temp_order = ""
try:
    print("******* Simple Database Query System *******")
    print("Please for conditions write the terms adjacent. For example; grade<20 ")
    while True:  # System loop
        flag = False
        command = input("Enter a command:")
        command_detail = command.split(" ")
        if command_detail[0] == "SELECT":
            temp = command_detail[1].split(",")  # For desired fields after select.
        if not select_flag and not command_detail[0] == "SELECT":
            sub_dict = sorted_dict
            temp_sorted = sorted_dict
        if command_detail[0] == "SELECT" or command_detail[0] == "DELETE":  # For both DELETE and INSERT
            if command_detail[0] == "SELECT":
                select_flag = True
                condit = condition(command_detail[5])  # First condition for insertion.
            if command_detail[0] == "DELETE":  # First condition for delete
                deleted_items = []
                condit = condition(command_detail[4])
            condit = list(condit)  # If there is only one condition
            condit_other = []
            if command_detail[len(command_detail) - 1] == "DSC" or command_detail[len(command_detail) - 1] == "ASC":
                temp_order = command_detail[len(command_detail) - 1]
            if command_detail[0] == "SELECT" and (command_detail[6] == "AND" or command_detail[6] == "OR"):
                condit_other = condition(command_detail[7])  # If more than one condition , it is for second cond.
                condit_other = list(condit_other)
                flag = True
            elif len(command_detail) > 5 and command_detail[0] == "DELETE" and (
                    command_detail[5] == "AND" or command_detail[5] == "OR"):
                condit_other = condition(command_detail[6])  # If more than one condition , it is for second cond.
                condit_other = list(condit_other)  # Delete part
                flag = True
            else:
                condit_other.append(-1)

            if command_detail[0] == "SELECT":  # Sub-arrays are opened again before each selection.
                temp_sorted = sorteddict()
                sub_dict = sorteddict()
                print("The select operation has been performed.")
            for key in sorted_dict.keys():  # This dict is update always
                values = str(sorted_dict.get(key))
                temp2 = values.split(',')
                if command_detail[0] == "SELECT":
                    column(condit, temp, temp2, value_cond(condit[0], temp2, key), key, condit_other,
                           value_cond(condit_other[0], temp2, key), flag, command_detail[6], False)
                else:  # This part for delete.
                    if not flag:
                        result = column(condit, temp, temp2, value_cond(condit[0], temp2, key), key, condit_other,
                                        value_cond(condit_other[0], temp2, key), flag, sub_temp, True)
                    else:
                        result = column(condit, temp, temp2, value_cond(condit[0], temp2, key), key, condit_other,
                                        value_cond(condit_other[0], temp2, key), flag, command_detail[5], True)
                    if result:  # Indicates that the item is available for deletion.
                        if select_flag:
                            deleted_items.append(key)
                        else:
                            deleted_items.append(key)
            if command_detail[0] == "DELETE":  # For delete process.
                flag_print=False
                for x in deleted_items:
                    del_key = x
                    if sorted_dict.keys().__contains__(x):
                        flag_print = True
                        sorted_dict.__delitem__(del_key)
                        temp_sorted.__delitem__(del_key)
                    else:
                        print("No record with such an id could be found in the current dictionary. Deletion failed.")
                if flag_print:
                    print("Item(s) is deleted")
        if command_detail[0] == "INSERT":  # For insertion process.
            temp_data = fragmentation(command_detail[3])
            splited_temp_data = temp_data[1].split(",")
            valid_flag = True
            if select_flag:
                if sorted_dict.keys().__contains__(int(temp_data[0])):
                    valid_flag = False
                if not valid_flag:
                    print("The data is included same id.That's why it is not adding!")
                else:
                    temp_sorted[int(temp_data[0])] = value(temp, splited_temp_data, temp_data[0])
                    sub_dict[int(temp_data[0])] = subvalue(splited_temp_data, temp_data[0])
                    print("Data insertion successful.")
            else:
                if not sorted_dict.keys().__contains__(temp_data[0]):
                    temp_sorted[temp_data[0]] = value(sub_temp, splited_temp_data, temp_data[0])
                    sub_dict[temp_data[0]] = subvalue(splited_temp_data, temp_data[0])
                    print("Data insertion successful.")
                else:
                    print("The data is included same id.That's why it is not adding!")
        if select_flag:
            sorted_dict = sub_dict
        if command_detail[0] == "exit" or command_detail[0] == "EXIT":  # Exit and write to json file.
            if not select_flag:
                temp_sorted = print_without_select(temp_sorted)
            my_dict = []
            temp2 = {}
            for key, value in temp_sorted.items():
                temp2 = {int(key): value}
                my_dict.append(temp2)
            if temp_order == "DSC":
                my_dict.reverse()
            dict_jsn = {"STUDENTS": [my_dict]}  # Write last data set to json
            with open("students.json", "w") as f:
                json.dump(dict_jsn, f, indent=5)
            print("The system is closed and resulting data set stored in json file.")
            break
        if not (command_detail[0] == "SELECT" or command_detail[0] == "DELETE" or command_detail[0] == "INSERT"):
            print("Please enter valid command.")
except Exception as err:
    print(err+"! Invalid input. Please enter valid input !")
