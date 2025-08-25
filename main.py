import random

deux = ['R', 'L', 'R|', 'L|', 'U', 'U|', 'D', 'D|', 'B', 'B|', 'F', 'F|', 'R2', 'L2', 'U2', 'D2', 'B2']
trois = ['R', 'L', 'R|', 'L|', 'U', 'U|', 'D', 'D|', 'B', 'B|', 'F', 'F|', 'M', 'M|', 'L2', 'U2', 'D2', 'B2', 'F2', 'M2']
quatre = ['R', 'L', 'U', 'D', 'F', 'B', 'R|', 'L|', 'U|', 'D|', 'F|', 'B|', 'r', 'l', 'u', 'd', 'f', 'b', 'r|', 'l|', 'u|', 'd|', 'f|', 'b|']
cinq = ['R', 'L', 'U', 'D', 'F', 'B', 'R|', 'L|', 'U|', 'D|', 'F|', 'B|', 'r', 'l', 'u', 'd', 'f', 'b', 'r|', 'l|', 'u|', 'd|', 'f|', 'b|', '3r', '3l', '3u', '3d', '3f', '3b', '3r|', '3l|', '3u|', '3d|', '3f|', '3b|']
six = ['R', 'L', 'U', 'D', 'F', 'B', 'R|', 'L|', 'U|', 'D|', 'F|', 'B|', 'r', 'l', 'u', 'd', 'f', 'b', 'r|', 'l|', 'u|', 'd|', 'f|', 'b|', '3r', '3l', '3u', '3d', '3f', '3b', '3r|', '3l|', '3u|', '3d|', '3f|', '3b|']
sept = ['R', 'L', 'U', 'D', 'F', 'B', 'R|', 'L|', 'U|', 'D|', 'F|', 'B|', 'r', 'l', 'u', 'd', 'f', 'b', 'r|', 'l|', 'u|', 'd|', 'f|', 'b|', '3r', '3l', '3u', '3d', '3f', '3b', '3r|', '3l|', '3u|', '3d|', '3f|', '3b|', '4r', '4l', '4u', '4d', '4f', '4b', '4r|', '4l|', '4u|', '4d|', '4f|', '4b|']
pyraminx = ['R', 'L', 'U', 'B', 'R|', 'L|', 'U|', 'B|']
skewb = ['R', 'L', 'U', 'B', 'R|', 'L|', 'U|', 'B|']

def generer_melange(liste_cube, taille_melange, nom_cube):
    melange = random.sample(liste_cube, min(taille_melange, len(liste_cube)))
    print(f"\nVoici ton mélange pour {nom_cube} :\n{melange}\n")

print("""Salut !
Je voudrais te donner quelques informations avant de commencer:
1) Les | que tu verras signifient 'prime', c'est-à-dire: le même mouvement mais à l'envers.
(ex: R est une rotation vers le haut, et bien R| est une rotation vers le bas).
Voilà !""")

continuer = True
while continuer:
    choix_rubik = 0
    while choix_rubik not in range(1, 9):
        try:
            choix_rubik = int(input("Pour avoir un mélange, tape 1 pour le 2x2, 2 pour le 3x3, 3 pour le 4x4, 4 pour le 5x5, 5 pour le 6x6, 6 pour le 7x7, 7 pour le pyraminx et 8 pour le skewb: "))
            if choix_rubik not in range(1, 9):
                print("Veuillez entrer un chiffre correct.")
        except ValueError:
            print("Veuillez entrer un chiffre correct.")

    if choix_rubik == 1:
        generer_melange(deux, 10, "2x2")
    elif choix_rubik == 2:
        generer_melange(trois, 25, "3x3")
    elif choix_rubik == 3:
        generer_melange(quatre, 25, "4x4")
    elif choix_rubik == 4:
        generer_melange(cinq, 25, "5x5")
    elif choix_rubik == 5:
        generer_melange(six, 25, "6x6")
    elif choix_rubik == 6:
        generer_melange(sept, 25, "7x7")
    elif choix_rubik == 7:
        generer_melange(pyraminx, 10, "Pyraminx")
    elif choix_rubik == 8:
        generer_melange(skewb, 10, "Skewb")

    choix = 0
    while choix not in [1, 2]:
        try:
            choix = int(input("Tape 1 pour choisir un autre cube, tape 2 pour arrêter: "))
        except ValueError:
            print("Veuillez entrer un chiffre correct.")
    if choix == 2:
        continuer = False
