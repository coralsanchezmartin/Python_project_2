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
    csvlist = open_csv(CSV_FILE, DELIMITER_SEMICOLON)

    remove_csv(OUTPUT_PATH, EXTENSION)

    list_colons = list_of_colons(csvlist, COLUMN_NUMBER)
    list_replace = replace(csvlist, COLUMN_NUMBER)
    create_csv(CSV_FILE_REPLACE, list_replace, DELIMITER_COLON)

    csv_new_list = open_csv(CSV_FILE_REPLACE, DELIMITER_COLON)
    list_positives = positives(csv_new_list, UPPER, COLUMN_NUMBER)
    list_negatives = negatives(csv_new_list, LOWER, COLUMN_NUMBER)
    list_out_positives = outliers_positives(csv_new_list, UPPER, COLUMN_NUMBER)
    list_out_negatives = outliers_negatives(csv_new_list, LOWER, COLUMN_NUMBER)
    list_empty_values = empty(csvlist, COLUMN_NUMBER)

    null_val = null(csvlist, NULL_VALUES, COLUMN_NUMBER)

    create_csv(CSV_FILE_COLONS, list_colons, DELIMITER_COLON)
    create_csv(CSV_FILE_NULL, null_val, DELIMITER_COLON)
    create_csv(CSV_FILE_POSITIVES, list_positives, DELIMITER_COLON)
    create_csv(CSV_FILE_NEGATIVES, list_negatives, DELIMITER_COLON)
    create_csv(CSV_FILE_POSITIVES_OUTLIERS, list_out_positives, DELIMITER_COLON)
    create_csv(CSV_FILE_NEGATIVES_OUTLIERS, list_out_negatives, DELIMITER_COLON)
    create_csv(CSV_FILE_EMPTY_VALUES, list_empty_values, DELIMITER_COLON)


main()
