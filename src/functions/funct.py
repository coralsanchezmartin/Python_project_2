import csv


def represents_int(s):  # Method that checks if a string is an integer
    try:
        int(s)
        return True
    except ValueError:
        return False


def represents_float(s):  # Method that checks if a string is a float
    try:
        float(s)
        return True
    except ValueError:
        return False


def positives(list_post, upper_post):
    list_post_complete = []
    for linea_i in list_post:
        # if linea_i[0] == "Sebastian Graham":
        # print(linea_i[1])
        if represents_int(linea_i[1]) or represents_float(linea_i[1]):  # call the method to check whether the value in
            # the second column (linea_i[1]) is a float or an integer
            # if linea_i[0] == "Sebastian Graham":
            # print("inside")
            if 0 < float(linea_i[1]) < upper_post:
                list_post_complete.append(linea_i)

    return list_post_complete  # return the list


def negatives(list_post, lower_post):
    list_neg_complete = []
    for linea_i in list_post:
        if represents_int(linea_i[1]) or represents_float(linea_i[1]):
            if 0 > float(linea_i[1]) > lower_post:
                list_neg_complete.append(linea_i)

    return list_neg_complete


def null(list_null, equal_null):
    list_null_complete = []
    for linea_i in list_null:
        if linea_i[1] == equal_null:
            list_null_complete.append(linea_i)

    return list_null_complete


def open_csv(new_file):
    with open(new_file) as data:
        entry = csv.reader(data, delimiter=';')
        list_i = list(entry)
    return list_i


def create_csv(create_new_csv, csvlist1):
    output_f = open(create_new_csv, "w+")
    csv_str = ""

    for linea_i in csvlist1:
        csv_str += str(linea_i[0]) + ',' + str(
            linea_i[1]) + '\n'

    output_f.write(csv_str)
    output_f.close()
