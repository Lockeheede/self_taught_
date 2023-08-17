import csv

movies = [["Top Gun", "Risky Business", "Minority Report"],["Titanic", "The Revenant", "Inception"], ["Training Day", "Man on Fire", "Flight"]]

with open("movies.csv", "w", newline='') as f:
          w = csv.writer(f, delimiter=",")
          w.writerow([movies[0][0], movies[0][1], movies[0][2]])
          w.writerow([movies[1][0], movies[1][1], movies[1][2]])
          w.writerow([movies[2][0], movies[2][1], movies[2][2]])




