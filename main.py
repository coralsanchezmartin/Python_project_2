# Hacer un csv identificando los valores errores y arreglandolos (coma por punto),
# hay valores null que hay que quitar, hay nombres sin valor que hay que quitar.
# Leer el csv con ;
# Count que cada grupo de valores, y crear un csv con la cuenta.  (valores positivos normales, negativos normales, positivos upper bound, negativos lower bound)
# positivos decimal incorrecto, negativos decimal incorrecto, null, vacios.
# Con llamadas a metodos

import csv


def positives(list_post, upper_post):
    list_post_complete = []  # Creating a list
    for linea_i in list_post:  # Iterates each line of the list (starting with the first one)
        if 0 < int(linea_i[1]) < upper_post:  # If the value 1 of the line is between 0 and 1000, go to the next line
            list_post_complete.append(linea_i)  # Add each value to the list above

    return list_post_complete  # return the list


def null(list_null, equal_null):
    list_null_complete = []
    for linea_i in list_null:
        if linea_i[1] == equal_null:
            list_null_complete.append(linea_i)


def open_csv(new_file):
    with open(new_file) as data:
        entry = csv.reader(data, delimiter=',')
        list_i = list(entry)
    return list_i


csv_file = 'C:/Users/coral/Documents/Python_Fran/data_last.csv'


def main():
    csvlist = open_csv(csv_file)
    list_positives = positives(csvlist, upper)
    null(csvlist, null_values)


main()

null_values = 'null'
upper = 1000
