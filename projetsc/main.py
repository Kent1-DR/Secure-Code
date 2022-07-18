from rdflib import Graph

if __name__ == '__main__':
    txt = open("Projet.owl")
    g = Graph().parse(txt, format="xml")

condition = input('Si vous voulez une tranche de prix et un degré d alcool, veuillez renseigner un champ sinon laissez vide')
choix = input('SVP selectionner un ingredient')
if condition:
    degre = input('Choisissez votre teneur en alcool entre 1=0-20 2=20-40 3=40-60')
    if degre == "1":
        degre = "0_20"
        print("Liste d'alcool en teneur de 0 à 20 degré")
    elif degre == "2":
        degre = "21_40"
        print("Liste d'alcool en teneur de 20 à 40 degré")
    elif degre == "3":
        degre = "41_60"
        print("Liste d'alcool en teneur de 41 à 60 degré")
    else:
        print("Erreur")

    prix = input('Choisissez la tranche de prix entre 0_20 21_40 ou 41_60')
    if prix == "1":
        prix = "0_20"
        print("Liste d'alcool en teneur de 0 à 20 degré")
    elif prix == "2":
        prix = "21_40"
        print("Liste d'alcool en teneur de 21 à 40 degré")
    elif prix == "3":
        prix = "41_60"
        print("Liste d'alcool en teneur de 41 à 60 degré")
    else:
        print("Erreur")

    q = """
            PREFIX onto: <http://www.semanticweb.org/king1/ontologies/2022/4/Projet#>
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
            SELECT *
                WHERE
                {
                   ?a onto:estFort onto:DEGRE. ?a onto:composeDe onto:INGREDIENT. ?a onto:coute onto:PRIX
                }
        """
    q = q.replace('INGREDIENT', choix)
    q = q.replace('DEGRE', degre)
    q = q.replace('PRIX', prix)

else:
    print("pas de condition")
    q = """
                PREFIX onto: <http://www.semanticweb.org/king1/ontologies/2022/4/Projet#>
                PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
                SELECT *
                    WHERE
                    {
                       ?a onto:composeDe onto:INGREDIENT
                    }
            """
    q = q.replace('INGREDIENT', choix)
for r in g.query(q):
    print(r)


    # Apply the query to the graph and iterate through results
    #print("genre available: ")
    #menu = ['Cocktail alcoolisé', 'Cocktail Non Alcoolisé', 'Boisson sans bulle', 'Boisson avec bulle', 'Alcool faible', 'Alcool Fort']
    #for i in menu:
        #print('-' + i)