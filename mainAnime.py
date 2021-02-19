from Organize import moveAnimes
from alphabetiz import write
from alphabetiz import listOfAnime

option = input("Would you like to move an Anime? ")
option = option.lower()
if option == "yes" or option == "y":
    initialPos = int(input("From what list? "))
    finalPos = int(input("To what list? "))

    moved = moveAnimes(initialPos, finalPos)

    animeList1 = moved[0]
    animeList2 = moved[1]
    animeList3 = moved[2]

    write(animeList1, animeList2, animeList3)

elif option == "no" or option == "n":
    write(listOfAnime(1), listOfAnime(2), listOfAnime(3))

anime1 = open("/Users/marcobarreirinhas/Programs/Python/AnimeList.txt", "w")
anime2 = open("/Users/marcobarreirinhas/Programs/Python/AnimeList2.txt", "r")

for lines in anime2:
    anime1.write(lines)
