import copy
import random
passenger = {
    'name': "",
    'id': 0,
    'luggage_weight': 0.0
}
bus = {
    'id': 0,
    'spaces': 0,
    'passengers': [],
    'luggage_weight': 0,
    'spaces_left': 0
}
def uniqueid():
    seed = random.getrandbits(8)
    while True:
        yield seed
        seed += 1
starting_passenger_id = uniqueid()
def create_user(name, weight):
    created = copy.deepcopy(passenger)
    created['id'] = next(starting_passenger_id)
    created['name'] = name
    created['luggage_weight'] = weight
    return created
starting_bus_id = uniqueid()
buss = []
def create_bus():
    space = int(input("nombre de place:"))
    poid = float(input("poid maximum a contenir"))
    matricule = input("entrer le matricule")
    created = copy.deepcopy(bus)
    created['id']  = matricule
    created['space'] = space
    created['space_left'] = space
    created['luggage_weight'] = poid
    buss.append(created)
    return created
def add_user_bus(nom_client,weight):
    print(" Pour ajouter un ultilisateur a un bus")
    reponse=int(input("entrer 1 pour creer un bus ou 2 si le bus existe deja"))
    if reponse == 1:
        bus1=create_bus()
        user1 = create_user(nom_client, weight)
        bus1['passengers'].append(user1)
        print("le passager {} avec pour identifiant {} a ete ajouter au bus".format(user1['name'], user1['id'], bus1['id']))
        bus1['spaces_left'] = bus1['spaces_left'] - 1
        bus1['luggage_weight'] = bus1['luggage_weight'] - weight
    else:
        print("veuillez choisir parmi les bus suivant")
        for item in buss:
            print("BUS : {}".format(item['id']))
        choix = int(input("entrer votre choix"))
        for item1 in buss:
            if item1['id'] == choix:
                user = create_user(nom_client,weight)
                item1['passengers'].append(user)
                print("le passager {} avec pour identifiant {} a ete ajouter au bus".format(user['name'],user['id'],item1['id']))
                item1['spaces_left'] = item1['spaces_left'] - 1
                item1['luggage_weight'] = item1['luggage_weight'] - weight
            else:
                print("cette identifiant ne correspont a aucun bus veillez entrez un identifiand de bus valide")
add_user_bus("annie",23)
print(buss)


