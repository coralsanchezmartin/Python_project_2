# Hacer un csv identificando los valores errores y arreglandolos (coma por punto),
# hay valores null que hay que quitar, hay nombres sin valor que hay que quitar.
# Leer el csv con ;
# Count que cada grupo de valores, y crear un csv con la cuenta.  (valores positivos normales, negativos normales,
# positivos upper bound, negativos lower bound)
# positivos decimal incorrecto, negativos decimal incorrecto, null, vacios.
# Con llamadas a metodos
# Pasar el uno, ; como argumento
# Definir , y ; como constantes


from src.functions.funct import *
from src.constants.const import *


def main():
    columns = [COLUMN_NUMBER1, COLUMN_NUMBER2]
    currently_working = current_directory()

    csvlist = open_csv(CSV_FILE, DELIMITER_SEMICOLON)

    remove_csv(currently_working + OUTPUT_PATH, EXTENSION)

    list_colons, count_colons = list_of_colons(csvlist, COLUMN_NUMBER)
    print('Count in colons csv : ', count_colons)
    list_replace, count_replace = replace(csvlist, COLUMN_NUMBER, SEARCH_VALUE, REPLACE_VALUE)
    print('Count in replace csv : ', count_replace)

    create_csv(CSV_FILE_REPLACE, list_replace, DELIMITER_COLON, columns)

    csv_new_list = open_csv(CSV_FILE_REPLACE, DELIMITER_COLON)
    list_positives, count_positive = positives(csv_new_list, UPPER, COLUMN_NUMBER)
    print('Count in positives csv : ', count_positive)
    list_negatives, count_negative = negatives(csv_new_list, LOWER, COLUMN_NUMBER)
    print('Count in negatives csv : ', count_negative)
    list_out_positives, count_out_positive = outliers(csv_new_list, UPPER, LOWER, COLUMN_NUMBER,
                                                      bol_positives=True, bol_negatives=False)
    print('Count in outlier positives csv : ', count_out_positive)
    list_out_negatives, count_out_negative = outliers(csv_new_list, UPPER, LOWER, COLUMN_NUMBER,
                                                      bol_positives=False, bol_negatives=True)
    print('Count in outlier negatives csv : ', count_out_negative)
    list_empty_values, count_empty_values = empty(csvlist, COLUMN_NUMBER)
    print('Count in empty values csv : ', count_empty_values)

    null_val, count_null = null(csvlist, NULL_VALUES, COLUMN_NUMBER)
    print('Count in null values csv : ', count_null)

    create_csv(CSV_FILE_COLONS, list_colons, DELIMITER_COLON, columns)
    create_csv(CSV_FILE_NULL, null_val, DELIMITER_COLON, columns)
    create_csv(CSV_FILE_POSITIVES, list_positives, DELIMITER_COLON, columns)
    create_csv(CSV_FILE_NEGATIVES, list_negatives, DELIMITER_COLON, columns)
    create_csv(CSV_FILE_POSITIVES_OUTLIERS, list_out_positives, DELIMITER_COLON, columns)
    create_csv(CSV_FILE_NEGATIVES_OUTLIERS, list_out_negatives, DELIMITER_COLON, columns)
    create_csv(CSV_FILE_EMPTY_VALUES, list_empty_values, DELIMITER_COLON, [COLUMN_NUMBER1])


main()
