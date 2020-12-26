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
    csvlist = open_csv(csv_file)

    list_positives = positives(csvlist, upper)
    list_negatives = negatives(csvlist, lower)
    null_val = null(csvlist, null_values)
    list_replace = replace(csvlist)

    create_csv(csv_file2, null_val)
    create_csv(csv_file3, list_positives)
    create_csv(csv_file4, list_negatives)
    create_csv(csv_file5, list_replace)


main()
