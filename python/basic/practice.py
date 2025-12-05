#Ejercicio práctico

#Crea una función que tome una lista de números y devuelva la suma de todos los números en la lista.
#La función debe manejar posibles excepciones, como si la lista contiene elementos que no son números

num_list = [12, 45, 78, 5213, 36, 58, 98, 65, 59, "Hola"]


def sum_numbers(number_list):
    """Suma los valores numéricos en `number_list`.

    - Acepta `int`, `float` y cadenas que representen números (por ejemplo, "3.5").
    - Omite elementos no numéricos y los reporta en una advertencia.
    - Lanza `TypeError` si `number_list` no es iterable.

    Devuelve la suma (int si la suma es entera, float en otro caso).
    """

    total = 0.0
    non_numeric = []

    try:
        for item in number_list:
            if isinstance(item, (int, float)):
                total += item
            else:
                try:
                    # Intentar convertir cadenas numéricas a float
                    num = float(item)
                    total += num
                except (ValueError, TypeError):
                    non_numeric.append(item)
    except TypeError:
        raise TypeError("El argumento debe ser un iterable de elementos.")

    # Normalizar a int si no tiene parte decimal
    if float(total).is_integer():
        total = int(total)

    if non_numeric:
        print(f"Advertencia: se omitieron elementos no numéricos: {non_numeric}")

    return total


if __name__ == "__main__":
    result = sum_numbers(num_list)
    print(f"Suma resultante: {result}")










