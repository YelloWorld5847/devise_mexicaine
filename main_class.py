class DecompositionMonnaie:
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

    def __init__(self, nombre):
        self.nombre = nombre
        #self.frequence = {v: 0 for v in self.DEVISE_MEXICAINE.values()}

    def decomposer(self):
        self.reponse = ""
        for key, value in self.DEVISE_MEXICAINE.items():
            coef = int(self.nombre // key)
            self.nombre = round(self.nombre - key * coef, 1)
            if coef:
                self.reponse += f"{value}: {coef}\n"
        return self.reponse


nombre_str = input("Entrer un chiffre à décomposer : ")

try:
    nombre = float(nombre_str)
    arrondi = round(nombre, 1)

    if nombre != arrondi:
        print("La valeur de départ à été arrondi au dixième")

    decomposeur = DecompositionMonnaie(arrondi)
    print(decomposeur.decomposer())

except ValueError:
    print("Veuillez entrer un nombre valide.")
