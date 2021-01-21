# IFT 2125  Devoir 4 question_2
# Yifu Zhou 20092235
# Tester si deux graphes sont isomorphismes ( représentée par la matrice adjacence)

#Test1 same graph
A = [[0, 1, 1, 0, 0],
      [1, 0, 0, 1, 1],
      [1, 0, 0, 1, 0],
      [0, 1, 1, 0, 1],
      [0, 1, 0, 1, 0]]

B = [[0, 1, 1, 0, 0],
      [1, 0, 1, 0, 1],
      [1, 1, 0, 1, 0],
      [0, 0, 1, 0, 1],
      [0, 1, 0, 1, 0]]

#Test2 different graph
A2 = [[0, 1, 1, 0, 0],
     [1, 0, 0, 1, 1],
     [1, 0, 0, 1, 1],
     [0, 1, 1, 0, 1],
     [0, 1, 1, 1, 0]]

B2 = [[0, 1, 1, 0, 0],
     [1, 0, 1, 0, 1],
     [1, 1, 0, 1, 0],
     [0, 0, 1, 0, 1],
     [0, 1, 0, 1, 0]]

#Test5 same graph
A5 = [[0, 1, 1, 0, 1, 0],
     [1, 0, 1, 1, 0, 0],
     [1, 1, 0, 0, 1, 1],
     [0, 1, 0, 0, 0, 1],
     [1, 0, 1, 0, 0, 1],
     [0, 0, 1, 1, 1, 0]]

B5 = [[0, 1, 0, 1, 1, 0],
     [1, 0, 1, 0, 1, 1],
     [0, 1, 0, 1, 0, 1],
     [1, 0, 1, 0, 0, 0],
     [1, 1, 0, 0, 0, 1],
     [0, 1, 1, 0, 1, 0]]

# fonction qui reçois deux matrice d'adjacences de même taille
# et teste si m2 est un isomorphisme de m1
def testerIso(m1, m2):
    visited = []
    temp = []
    res = []
    #remettre le stopSearching à False pour un nouveau teste
    global stopSearching
    stopSearching = False

    length = len(m1)
    #créer une liste des Noeuds
    listNoeud1 = list(range(0, length))
    print(backtrack(m1, m2, listNoeud1,visited, temp, res))

# variable globale qui aide à quitter la récursion quand la bonne permutation est trouvée
stopSearching = False

# Construire une permutation candidate et la tester
def backtrack(m1, m2, listNoeud, visited, temp, res):

    global stopSearching
    if stopSearching == True:
        return True
    # Une fois qu'on a une permutation candidate, on le tester
    # Si c'est pas une bonne reponse, on cherche sur la branche suivante
    # avec la recherche en profondeur

    # pour faciliter la notation, une permutation s'écrit ici comme [2,3,0,1] est
    # équivalente à une permutation de m1 à m2 (0->2, 1->3, 2->0, 3->1)


    if len(temp) == len(listNoeud) and (temp not in visited):
        if verifierPermutation(m1, m2, temp) == True:
            visited.append(temp)
            print("On a trouvé une bonne permutation : ", temp)
            stopSearching = True  # on va arreter la recherche et retourne stopSearching = True
            return stopSearching

    else:
        for y in listNoeud:
            if y in temp:
                continue

            temp.append(y)
            backtrack(m1,m2,listNoeud,visited, temp, res)
            temp.pop()
    return stopSearching

# Verifier si une permutation envoie une matrice à une autre (isomorphisme)
def verifierPermutation(m1, m2, p):

    for i in range (0, len(p)):

        for j in range (0, len(p)):
            a=m1[i]
            b=m2[p[i]]
            if m1[i][j] != m2[p[i]][p[j]]:
                return False

    return True
#
# testerIso(A5,B5)  # oui
# testerIso(A,B)    # oui
# testerIso(A2,B2)  # pas isomorphisme

