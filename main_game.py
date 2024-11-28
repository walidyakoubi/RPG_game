import csv


class Arme :
    def __init__(self, name, dammage, use):
        self.Nom = name
        self.DegA = dammage
        self.NU = use
    def set_name(self, name):
        self.Nom = name
    def set_DegA(self, dammage):
        self.DegA = dammage
    def set_NU(self, use):
        self.NU = use
    def get_name(self):
        return self.Nom
    def get_DegA(self):
        return self.DegA
    def get_NU(self):
        return self.NU
    
class Sort :
    def __init__(self,name,dammage,cs):
        self.Nom = name
        self.DegMag = dammage
        self.cons_mana = cs
    def set_Nom(self,name):
        self.Nom = name
    def set_DegMag(self,dammage):
        self.DegMag = dammage
    def get_DegMag(self):
        return self.DegMag
    def set_cons_mana(self,cs):
        self.cons_mana = cs
    def get_cons_mana(self):
        return self.cons_mana
    def get_Nom(self):
        return self.Nom

class Armure:
    def __init__(self, name, phydef, magdef):
        self.Nom = name
        self.DefPhys = phydef
        self.DefMag = magdef
    def set_Nom(self, name):
        self.Nom = name
    def set_DefPhys(self, phydef):
        self.DefPhys = phydef
    def get_DefPhys(self):
        return self.DefPhys
    def set_DefMag(self, magdef):
        self.DefMag = magdef
    def get_DefMag(self):
        return self.DefMag
    def get_Nom(self):
        return self.Nom
    
class personnage :
    pv = 200
    mana = 200
    arme = Arme("",0,0)
    armure = Armure("",0,0)
    sort = Sort("",0,0)
    def __init__(self, name, intel, force):
        self.Nom = name
        self.Intel = intel
        self.Force = force
    def set_Arme(self, name, dmg, usee):
        self.arme = Arme(name, dmg, usee)
        # Réduire les PV et le mana en fonction de l'arme
        self.pv -= dmg  # Réduction des PV pour l'achat de l'arme

    def set_Armure(self, name, defP, defM):
        self.armure = Armure(name, defP, defM)
        # Réduction des PV et du mana en fonction de l'armure
        self.pv -= defP  # Réduction des PV selon la défense physique
        self.mana -= defM  # Réduction du mana selon la défense magique

    def set_Sort(self, name, dmg, cm):
        self.sort = Sort(name, dmg, cm)
        # Réduction du mana pour l'achat du sort
        self.mana -= cm

    def Affiche(self):
        print(f"Je suis {self.Nom}, force: {self.Force}, intelligence: {self.Intel}")
        print(f"PV: {self.pv}, Mana: {self.mana}")

    def Affiche_Arme(self):
        print(f"Arme: {self.arme.get_name()}, Dégâts: {self.arme.get_DegA()}, Utilisations: {self.arme.get_NU()}")

    def Affiche_Sort(self):
        print(f"Sort: {self.sort.get_Nom()}, Dégâts magiques: {self.sort.get_DegMag()}, Mana requis: {self.sort.get_cons_mana()}")

    def Affiche_Armure(self):
        print(f"Armure: {self.armure.get_Nom()}, Défense physique: {self.armure.get_DefPhys()}, Défense magique: {self.armure.get_DefMag()}")

    # Méthode pour l'attaque physique
    def Attaque_Phys(self, ennemi):
        degats = self.arme.get_DegA() * self.Force * 0.1 - ennemi.armure.get_DefPhys()
        degats = max(degats, 0)  # Les dégâts ne peuvent pas être négatifs
        ennemi.pv -= degats
        print(f"{self.Nom} inflige {degats} points de dégâts physiques à {ennemi.Nom}.")

    # Méthode pour l'attaque magique
    def Attaque_Mag(self, ennemi):
        if self.mana >= self.sort.get_cons_mana():
            degats = self.sort.get_DegMag() * self.Intel * 0.1 - ennemi.armure.get_DefMag()
            degats = max(degats, 0)  # Les dégâts ne peuvent pas être négatifs
            ennemi.pv -= degats
            self.mana -= self.sort.get_cons_mana()  # Réduction du mana
            print(f"{self.Nom} inflige {degats} points de dégâts magiques à {ennemi.Nom}.")
        else:
            print(f"{self.Nom} n'a pas assez de mana pour attaquer.")

    # Accesseurs pour les points de vie et de mana
    def get_pv(self):
        return self.pv

    def get_mana(self):
        return self.mana



liste_Perso = []
liste_Arme = []
liste_Sort = []
liste_Armure = []

# Chargement des personnages
with open("New_data\Personnage.csv", encoding='utf-8-sig') as f:
    contenu = csv.DictReader(f, delimiter=",")
    for elem in contenu:
        liste_Perso.append(elem)

# Chargement des armes
with open("New_data\Arme.csv", encoding='utf-8-sig') as f:
    contenu = csv.DictReader(f, delimiter=",")
    for elem in contenu:
        liste_Arme.append(elem)

# Chargement des sorts
with open("New_data\Sort.csv" , encoding='utf-8-sig') as f:
    contenu = csv.DictReader(f, delimiter=",")
    for elem in contenu:
        liste_Sort.append(elem)

# Chargement des armures
with open("New_data\Armure.csv" , encoding='utf-8-sig') as f:
    contenu = csv.DictReader(f, delimiter=",")
    for elem in contenu:
        liste_Armure.append(elem)

#CHOIX DE PERSONNAGE ----------------------------------------------
print("Joueur 1, choisissez votre personnage :")
for elem in liste_Perso:
    print(elem["Nom"])
Nom_p = input("Nom : ")
for elem in liste_Perso:
    if elem["Nom"] == Nom_p:
        joueur1 = personnage(elem["Nom"], int(elem["Intel"]), int(elem["Force"]))
        break     

print("Joueur 2, choisissez votre personnage :")
for elem in liste_Perso:
    print(elem["Nom"])
Nom_p = input("Nom : ")
for elem in liste_Perso:
    if elem["Nom"] == Nom_p:
        joueur2 = personnage(elem["Nom"], int(elem["Intel"]), int(elem["Force"]))
        break

#CHOIX D'ARME ----------------------------------------------
print("Joueur 1, choisissez votre arme :")
for elem in liste_Arme:
    print(elem["Nom"])
arme_p = input("Choisi une arme : ")
for elem in liste_Arme:
    if elem["Nom"] == arme_p:
        joueur1.set_Arme(elem["Nom"], int(elem["DegA"]), int(elem["NU"]))
        break

print("Joueur 2, choisissez votre arme :")
for elem in liste_Arme:
    print(elem["Nom"])
arme_p = input("Choisi une arme : ")
for elem in liste_Arme:
    if elem["Nom"] == arme_p:
        joueur2.set_Arme(elem["Nom"], int(elem["DegA"]), int(elem["NU"]))
        break

#CHOIX D'ARMURE ----------------------------------------------
print("Joueur 1, choisissez votre Armure :")
for elem in liste_Armure:
    print(elem["Nom"])
armure_p = input("Choisi une Armure : ")
for elem in liste_Armure:
    if elem["Nom"] == armure_p:
        joueur1.set_Armure(elem["Nom"], int(elem["DefPhys"]), int(elem["DefMag"]))
        break

print("Joueur 2, choisissez votre Armure :")
for elem in liste_Armure:
    print(elem["Nom"])
armure_p = input("Choisi une Armure : ")
for elem in liste_Armure:
    if elem["Nom"] == armure_p:
        joueur2.set_Armure(elem["Nom"], int(elem["DefPhys"]), int(elem["DefMag"]))
        break

#CHOIX DE SORT ----------------------------------------------
print("Joueur 1, choisissez votre Sort :")
for elem in liste_Sort:
    print(elem["Nom"])
sort_p = input("Choisi une Sort : ")
for elem in liste_Sort:
    if elem["Nom"] == sort_p:
        joueur1.set_Sort(elem["Nom"], int(elem["DegMag"]), int(elem["ConsMana"]))
        break

print("Joueur 2, choisissez votre Sort :")
for elem in liste_Sort:
    print(elem["Nom"])
sort_p = input("Choisi une Sort : ")
for elem in liste_Sort:
    if elem["Nom"] == sort_p:
        joueur2.set_Sort(elem["Nom"], int(elem["DegMag"]), int(elem["ConsMana"]))
        break




# Affichage des infos initiales des joueurs
joueur1.Affiche()
joueur2.Affiche()

while joueur1.get_pv() > 0 and joueur2.get_pv() > 0:
    # Tour du joueur 1
    print("Joueur 1, choisissez une action : 1. Attaque Physique, 2. Attaque Magique")
    choix = int(input("Votre choix : "))
    
    if choix == 1:
        joueur1.Attaque_Phys(joueur2)
    elif choix == 2:
        joueur1.Attaque_Mag(joueur2)
    
    joueur1.Affiche()  # Affiche les infos après l'attaque du joueur 1
    joueur2.Affiche()  # Affiche les infos après l'attaque du joueur 1

    # Si joueur 2 est encore en vie, il joue
    if joueur2.get_pv() > 0:
        print("Joueur 2, choisissez une action : 1. Attaque Physique, 2. Attaque Magique")
        choix = int(input("Votre choix : "))
        
        if choix == 1:
            joueur2.Attaque_Phys(joueur1)
        elif choix == 2:
            joueur2.Attaque_Mag(joueur1)
        
        joueur1.Affiche()  # Affiche les infos après l'attaque du joueur 2
        joueur2.Affiche()  # Affiche les infos après l'attaque du joueur 2
    else:
        break  # Fin de la boucle si joueur 2 n'a plus de PV

# Affichage du gagnant
if joueur1.get_pv() > 0:
    print(f"{joueur1.get_Nom()} a gagné !")
else:
    print(f"{joueur2.get_Nom()} a gagné !")