def identify_variable_type(filepath):
    keywords = {"val", "var"}
    types = {
        "Int": "Int", "Double": "Double", "Float": "Float", "Long": "Long",
        "Short": "Short", "Byte": "Byte", "Char": "Char", "Boolean": "Boolean",
        "IntArray": "IntArray", "Array<String>": "Array<String>"
    }
    var_count = 0
    type_count = {}
    array_count = 0
    init_count = 0
    const_count = 0
    var_set = set()
    type_dict = {}

    with open(filepath, "r") as file:
        for line in file:
            words = line.strip().split()
            if len(words) >= 2 and words[0] in keywords:
                var_name = words[1]
                if var_name not in var_set:
                    var_set.add(var_name)
                    var_count += 1
                    if words[0] == "val":
                        init_count += 1
                        const_count += 1
                    if len(words) >= 3 and words[2] in types:
                        var_type = types[words[2]]
                        type_count[var_type] = type_count.get(var_type, 0) + 1
                        if var_type.endswith("Array"):
                            array_count += 1
                        if var_type in type_dict:
                            type_dict[var_type].append(var_name)
                        else:
                            type_dict[var_type] = [var_name]
                    else:
                        print(f"No se puede determinar {var_name}.")

    print(f"Total de variables declaradas: {var_count}")
    print(f"Total de tipo de variables : {len(type_count)}")
    for var_type, count in type_count.items():
        print(f"Número de {var_type} variables: {count}")
    print(f"Total de variables tipo ARRAY: {array_count}")
    print(f"Total de variables INICIALIZADAS: {init_count}")
    print(f"Total de variables CONSTANTES: {const_count}")

    print("\nClasificación por tipo de variable:")
    for var_type, var_list in type_dict.items():
        print(f"\n{var_type} variables:")
        for var_name in var_list:
            print(f"\t{var_name}")



if __name__ == "__main__":
    identify_variable_type("prueba.kt")

