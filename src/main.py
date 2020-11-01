import random

from src.metier.LinkedList import LinkedList

if __name__ == '__main__':
    # Vos tests ici
    lk = LinkedList()
    # Ajouter des nombres aléatoires dans la liste
    for i in range(0, 10):
        lk.add(random.randint(0, 1000000))
    # Afficher la liste
    print(lk)
