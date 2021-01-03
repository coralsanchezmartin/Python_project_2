import csv
import os


def current_directory():
    """
    Gets the directory you are currently working at.
    :return: the current working directory
    """
    return os.getcwd()


def remove_ext(path, ext):
    """
    Removes all files in a directory with the extension given.
    :param path: the path of the directory from where you want to remove all the files with the given extension.
    :param ext: the extension of the file you want to remove.
    :return: Nothing
    """
    for f in os.listdir(path):  # Go through all files in the directory. (f is a string of the name od the file)
        split_f = f.split(".")  # Splits the string f where there is a "." and it saves it in a list

        if split_f[-1] == ext:  # Compares the last item of the list with the parameter ext.
            os.remove(os.path.join(path, f))  # os.path.join, joins the path with the file name (this way we dont have
            # to create an intermediate variable), os.remove, removes it.


def list_of_colons(list_post, column):
    """
    Takes the values that contain colons
    :param list_post: list from where you want to extract the values
    :param column: specific column of the list
    :return: list_colons, a list of the values containing colons and count, the total number of values from the list.
    """
    list_colons = []  # creating a list
    count = 0  # The count starts at 0
    for linea_i in list_post:  # runs every element of the list.
        if linea_i[column].__contains__(","):  # see if an specific column contains the element ","
            list_colons.append(linea_i)  # if this is fulfilled then add the line containing this value to the list.
            count += 1  # every time you add a value count +1

    return list_colons, count


def represents_int(s):
    """
    Checks if a string is an integer
    :param s: the string that it checks to see if is an integer.
    :return: True, if the string is an integer and False if not.
    """
    try:
        int(s)
        return True
    except ValueError:
        return False


def represents_float(s):
    """
    Checks if a string is a float
    :param s: the string that it checks to see if is a float.
    :return: True, if the string is an float and False if not.
    """
    try:
        float(s)
        return True
    except ValueError:
        return False


def positives(list_post, upper_post, column):
    """
    Takes the positive values from a list generating a new list with only the values meeting the requirements.
    :param list_post: is from where you want to extract the values.
    :param upper_post: upper constant.
    :param column: the specific column where the number that we are looking for is at.
    :return: the new list generated by adding the values that meet the if requirements and the count.
    """
    list_post_complete = []  # creating a new list
    count = 0  # The list starts at 0
    for linea_i in list_post:  # runs every element of the list
        # calls the methods to check whether the value in the specific column (linea_i[column]) is a float or an integer
        if represents_int(linea_i[column]) or represents_float(linea_i[column]):
            # checks if the value is contained between 0 and the upper_post constant.
            if 0 <= float(linea_i[column]) < upper_post:
                list_post_complete.append(linea_i)  # add the line containing this value to the list.
                count += 1  # It adds 1 with each new element added to the list.

    return list_post_complete, count


def negatives(list_post, lower_post, column):
    """
    Takes the negative values from a list generating a new list with only the values meeting the requirements.
    :param list_post: the list from where we extract the values.
    :param lower_post: lower constant.
    :param column: the specific column where the number that we are looking for is at.
    :return: the new list generated by adding the values that meet the if requirements
             and the count of this new list.
    """
    list_neg_complete = []  # creating a new list.
    count = 0  # count starts at 0
    for linea_i in list_post:  # runs every element of the list
        # checks check whether the value in the specific column (linea_i[column]) is a float or an integer
        if represents_int(linea_i[column]) or represents_float(linea_i[column]):
            # checks if the value is between 0 and the lower constant.
            if 0 > float(linea_i[column]) > lower_post:
                list_neg_complete.append(linea_i)  # add the line containing this value to the new list.
                count += 1  # It adds 1 with each new element added to the list.

    return list_neg_complete, count


def outliers(list_post, upper_post, lower_post, column, bol_positives, bol_negatives):
    """
    Takes the outlier values from a list generating a new list with only the values meeting the requirements.
    :param list_post: the list from where we extract the values.
    :param upper_post: upper constant
    :param lower_post: lower constant
    :param column: specific column where the value we want is at
    :param bol_positives: boolean to indicate if we take into consideration the positive values
    :param bol_negatives: boolean to indicate if we take into consideration the negative values
    :return: the new list generated by adding the values that meet the if requirements
             and the count of this new list.
    """
    list_outliers_complete = []  # creating a new list
    count = 0   # counts starts at 0.
    for linea_i in list_post:  # runs every item of the list.
        # checks if the value is an integer or a float.
        if represents_int(linea_i[column]) or represents_float(linea_i[column]):

            # check the booleans to see if it need to run the positives if.
            if bol_positives is True and bol_negatives is False:
                if float(linea_i[column]) > upper_post:  # checks if the value is over the upper constant.
                    list_outliers_complete.append(linea_i)  # adds this line containing the value to the new list
                    count += 1  # It adds 1 with each new element added to the list.

            # check the booleans to see if it need to run the negatives if.
            if bol_negatives is True and bol_positives is False:
                if float(linea_i[column]) < lower_post:  # checks if the value is under the lower constant.
                    list_outliers_complete.append(linea_i) # adds this line containing the value to the new list
                    count += 1  # It adds 1 with each new element added to the list.

    return list_outliers_complete, count


def null(list_null, equal_null, column):
    """
    Takes the null values from a list generating a new list with only the values meeting the requirements.
    :param list_null: the list from where we extract the values
    :param equal_null: the string that the requirements need to match
    :param column: the specific column where the value that we are looking for is at.
    :return: it returns the new list generated by adding the values that meet the if requirements
    and the count of the new list.
    """
    list_null_complete = []  # creating a new list
    count = 0  # count starts at 0
    for linea_i in list_null:  # runs every element in the list
        if linea_i[column] == equal_null:  # checks if the value in the specific column matches the string constant
            list_null_complete.append(linea_i)  # if so it adds it to the new list
            count += 1  # It adds 1 with each new element added to the list.

    return list_null_complete, count


def empty(list_post, column):
    """
    Takes the empty values from a list generating a new list with only the values meeting the requirements.
    :param list_post: the list from where we extract the values.
    :param column: the specific column where the values we want are at.
    :return: it returns the new list generated by adding the values that meet the if requirements
    and the count of the new list.
    """
    list_empty = []  # creating a new list
    count = 0  # count starts at 0
    for linea_i in list_post:  # runs every element in the list
        if len(linea_i[column]) == 0:  # checks if the length of the value on the specific column is 0
            list_empty.append(linea_i)  # if so it adds it to the new list
            count += 1  # It adds 1 with each new element added to the list.

    return list_empty, count


def replace(list_replace, column, search_v, replace_v):
    """
    Changes commas for dots.
    :param list_replace: the list from where we extract the values.
    :param column: the specific column where the number that we are looking for is at.
    :param search_v: the parameter we are searching for in the list.
    :param replace_v: the parameter we use to replace the search_v.
    :return: the new list generated by adding the values once the colons are replace with dots
    and the count of this new list.
    """
    list_replace_complete = []  # creating a new list
    count = 0  # count starts at 0
    for linea_i in list_replace:  # runs every element in the list
        # goes through every value in the specific column searching for the search_v and replacing it with the replace_v
        place = linea_i[column].replace(search_v, replace_v)
        linea_i[column] = place
        list_replace_complete.append(linea_i)  # once th replacing is done, it adds the values to the new list.
        count += 1  # It adds 1 with each new element added to the list.

    return list_replace_complete, count


def counts(lists, count):
    """

    :param lists: the list we want to work with
    :param count: the count we are using to compare the count to
    :return: True, if the length of the list matches the count and False if not.
    """
    if len(lists) == count:
        return True
    else:
        return False


def open_csv(new_file, delimiter_param):
    """
    Opens a file
    :param new_file: the file we want to open
    :param delimiter_param: the delimiter used in this file
    :return: the list of values in this file
    """
    with open(new_file) as data:  # open this file as data
        entry = csv.reader(data, delimiter=delimiter_param)  # reading the file as data and using the delimiter given
        list_i = list(entry)  # reading the file as a list
    return list_i


def create_csv(create_new_csv, csvlist, delimiter_param, column_lists):
    """
    Creates a new csv
    :param create_new_csv: the csv we are creating
    :param csvlist: the list we are putting into the csv
    :param delimiter_param: the delimiter we are using in our csv
    :param column_lists: the list of columns we are using in our csv
    :return: Nothing
    """
    output_f = open(create_new_csv, "w+")  # opens the new csv and writes on it
    csv_str = ""  # the text in our new csv

    for linea_i in csvlist:  # runs every element in the list for each line
        for column_i in column_lists:  # runs every element in the list for each column
            # add the text in each line and column using the delimiter given at the end of each element
            csv_str += str(linea_i[column_i]) + delimiter_param
        csv_str = csv_str[:-1] + '\n'  # add an enter at the end of each line

    output_f.write(csv_str)
    output_f.close()
