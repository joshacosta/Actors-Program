import csv

def main(reader): #call for main function
    movieList=set()

    for row in reader:  #creates 2D list for spreadsheet
        x=1
        for movie in row:
            if x==1:
                x+=1
                continue
            if movie!="":
                movieList.add(movie)

    methods(movieList,reader) #calls on part one of program involving set methods
    actors(movieList,reader) #calls on part two of program for actors

def methods(movieList,reader):
    for movie in movieList: #prints out movies for user to choose to analyze
        print(movie)
    print("\nWhich two movies would you like to compare?\n***Enter EXACTLY as presented above.***\n")
    choiceOne=input("Choice one: ")
    choiceTwo=input("Choice two: ")
    
    one=set()
    two=set()
    for row in reader: #if movies found, add those actors 
        if choiceOne in row:
            for x in row:
                one.add(row[0])
        if choiceTwo in row:
            for x in row:
                two.add(row[0])
    
    #union
    
    print("\nThese are the actors in the two movies.")
    print(one.union(two))

    #intersection

    print("\nThese are the actors that play in both movies.")
    if one.intersection(two)== None:
        print("\nThere are no common actors between the two movies.")
    else:
        print(one.intersection(two))

    #difference

    print("\nThese are the different actors between the two movies.")
    print(one.symmetric_difference(two))

def actors(movieList, reader):

    for row in reader: #print actors for user to choose
          print(row[0])
    print("\nWhich actor would you like to analyze? ")
    actor=input("Enter as ***EXACTLY*** as presented above: ")

    actorList=set()
    coActors=set()

    for row in reader: #create list of movies that actor has acted in
        if actor in row:
            for x in row:
                actorList.add(x)

    for row in reader: #take movies, and add all those actors in those movies into a list
        for movie in actorList:
            if movie in row:
                coActors.add(row[0])
    coActors.remove(actor) #remove original actor from list
                    
    print("\nThese are all the actors that ", actor," has ever worked with:\n")
    for actor in coActors:
        print(actor)
    
with open("imdb_update.csv") as csvfile: #open file, automatically closes when finished
    readCSV= csv.reader(csvfile,delimiter=",") 
    reader=[] 

    for row in readCSV: #converts spreadsheet into 2D list
        if row[0]!="":
            reader.append(row)
        
    main(reader) #call for main function
