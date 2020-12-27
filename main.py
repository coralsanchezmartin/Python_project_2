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

    remove_csv(OUTPUT_PATH)

    list_colons = list_of_colons(csvlist)
    list_replace = replace(csvlist)
    create_csv(CSV_FILE_REPLACE, list_replace, DELIMITER_COLON)

    csv_new_list = open_csv(CSV_FILE_REPLACE, DELIMITER_COLON)
    list_positives = positives(csv_new_list, UPPER)
    list_negatives = negatives(csv_new_list, LOWER)
    null_val = null(csvlist, NULL_VALUES)

    create_csv(CSV_FILE_COLONS, list_colons, DELIMITER_COLON)
    create_csv(CSV_FILE_NULL, null_val, DELIMITER_COLON)
    create_csv(CSV_FILE_POSITIVES, list_positives, DELIMITER_COLON)
    create_csv(CSV_FILE_NEGATIVES, list_negatives, DELIMITER_COLON)


main()
