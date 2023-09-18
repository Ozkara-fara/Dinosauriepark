#skapa en tom dictionary att representera dinosaurieparken
dinosaur_park = {}

# Function för att addera nya dinosaurier till parken
def add_dinosaur():
    #samla information från användaren att addera dinosaurier till parken i the dictionary
    name = input("Enter the name of the dinosaur: ")
    if not name:
        print("Name cannot be empty. Please enter a valid name.")
        return #denna gör så att proecessen går tillbaka om det inte finns ett giltigt namn
    
    species = input("Enter the species of the dinosaur: ")
    if not species:
        print("Species cannot be empty. Please enter a valid species.")
        return #return early if empty blabla

    #level är en integer och måste besvaras med en siffra
    while True:
        try:
            level = int (input("Enter the level of the dinosaur: "))
            break #denna avbryter loopen om svaret inte är valid
        except ValueError:
            print("invalid input. Please enter a valid number for the level.")
    
    food = input("Enter what food the dinosaur prefers: ")
    if not food:
        print("Food cannot be empty. Please enter a valid food.")
        return #denna gör så att proecessen går tillbaka om det inte finns ett giltigt namn

    dinosaur = {
        "Name": name,
        "Species": species,
        "Level": level,
        "Food": food,
}

    #kolla om species redan finns i parken
    if species not in dinosaur_park:
        dinosaur_park[species] = [] #detta ger en tom lista för den nya rasen (species)
    dinosaur_park[species].append(dinosaur)
    print(f"{name} has been added to the dinosaur park.")   

#Function för att lista alla dinosaurier i parken
def list_dinosaurs():
    #här ska jag lista alla dinosaurier och deras information
    species_count = {} #det här är en ny dictionary som håller räkningen på alla species

    if not dinosaur_park:
       print("There are no Dinosaurs in the park")
    else:
        print("list of Dinosaurs by Species:")
    for species, dinosaurs in dinosaur_park.items():
        species_count[species] = len(dinosaurs) #counts the number of dinosaurs
    
    for species, count in species_count.items():
        print(f"Species: {species}")
        print(f"Number of {species}: {count}")

        for dinosaur in dinosaur_park[species]:
            if dinosaur['Species'] == species:
                print(f"Name: {dinosaur['Name']}")
                print(f"Level: {dinosaur['Level']}")
                print(f"Food: {dinosaur['Food']}")

#Function för att söka efter dinosaurier via namn
def search_dinosaur(name_or_species):
    #sök på dinosaurien med hjälp av namn eller ras och visa information om den
    found_dinosaurs = []
    for species, dinosaurs in dinosaur_park.items():
        for dinosaur in dinosaurs:
            if name_or_species.lower() in dinosaur['Name'].lower() or name_or_species.lower() in dinosaur['Species'].lower():
                found_dinosaurs.append(dinosaur)

    if found_dinosaurs:
        print(f"Dinosaurs Found - Details:")
        for dinosaur in found_dinosaurs:
            print(f"Name: {dinosaur['Name']}")
            print(f"Species: {dinosaur['Species']}")
            print(f"Level: {dinosaur['Level']}")
            print(f"Food: {dinosaur['Food']}")
    else:
        print(f"Dinosaurs with the name or species '{name_or_species}' not found in park")        

#function för att ta bort en dinosaurie från parken med hjälp av dess namn
def remove_dinosaur(name):#ta bort dinosaurien från dictionary
    #Börja med att kolla om det finns dinosaurier i parken
    removed = False #flag to track if dinosaur was removed
    #iterate  through all the species in the park
    for species, dinosaurs in dinosaur_park.items():
        #iterate through the dinosaurs in the current species
        for dinosaur in dinosaurs:
            if dinosaur['Name'].lower() == name.lower():
                dinosaurs.remove(dinosaur) #remove the dinosaur
                removed = True #set the flag to true
                print(f"{name} have been removed from your park")
                break #exit the inner loop
        if removed:
            break #exit the outer loop if a dinosaur was removed
    if not removed:
        print(f"Dinosaur with the name '{name}' not found in park")

#huvudmeny
while True:
    print("\nDinosaur Park Menu: ")
    print("1. Add a Dinosaur")
    print("2. List Dinosaurs")
    print("3. Search for a Dinosaur")
    print("4. Remove a Dinosaur")
    print("5. quit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        add_dinosaur()
    elif choice == "2":
        list_dinosaurs()
    elif choice == "3":
        name = input("Enter the name or species of the dinosaur to search for: ")
        search_dinosaur(name)
    elif choice == "4":
        name = input("enter the name of the dinosaur to remove: ")
        remove_dinosaur(name)
    elif choice == "5":
        break
    else:
        print("Invalid choice. Please select a valid option.")