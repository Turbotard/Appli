def vente_marche_noir():
    age = int(input("quel age ? "))
    nombre = int(input("combien d'enfants voulez vous ? "))
    assert age < 90, "Trop vieux"
    assert nombre < 10, "Trop nombreux"
    if age < 18:
        return f"Cela vous fera donc {nombre*50*1.2}€"
    else:
        return f"Cela vous fera donc {nombre*75*1.2}€"
print(vente_marche_noir())