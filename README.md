# Décomposeur de Monnaie - Devise Mexicaine

Ce programme décompose une somme d'argent en pesos mexicains en utilisant les plus grosses unités disponibles, incluant les billets et les pièces. Il est utile pour comprendre comment représenter une somme d'argent avec un nombre minimal d'unités.

---

## Fonctionnalités principales

1. **Décomposition d'un montant** :
   - Prend un montant en entrée (en pesos mexicains).
   - Décompose ce montant en utilisant les billets et les pièces disponibles :
     - **Billets** : 1000, 500, 200, 100, 50, 20 pesos.
     - **Pièces** : 10, 5, 2, 1 pesos ; 50, 20, et 10 centavos.
   - Produit une sortie indiquant le nombre d'unités pour chaque type de billet ou pièce.

2. **Gestion des arrondis** :
   - Arrondit automatiquement les montants au dixième le plus proche pour garantir la précision.

3. **Validation des entrées** :
   - Vérifie que l'entrée est un nombre valide.
   - Gère les cas d'erreur en demandant une nouvelle saisie.

