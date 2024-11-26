
DEVISE_MEXICAINE = {
    1000: "billete 1000 pesos",
    500: "billete 500 pesos",
    200: "billete 200 pesos",
    100: "billete 100 pesos",
    50: "billete 50 pesos",
    20: "billete 20 pesos",
    10: "moneda 10 pesos",
    5: "moneda 5 pesos",
    2: "moneda 2 pesos",
    1: "moneda 1 peso",
    0.5: "moneda 50 centavos",
    0.2: "moneda 20 centavos",
    0.1: "moneda 10 centavos",
}

def decomposition_monnaie(nombre):
    frequence = {}

    for key, value in DEVISE_MEXICAINE.items():
        frequence[value] = 0

    while nombre != 0:
        for key, value in DEVISE_MEXICAINE.items():
            if key <= nombre:
                nombre -= key
                frequence[value] += 1
                break

    return frequence

dict_element = decomposition_monnaie(1541.5)

element_money = {}
for key, value in dict_element.items():
    if value != 0:
        element_money[key] = value


for key, value in element_money.items():
    print(f"{key} : {value}")