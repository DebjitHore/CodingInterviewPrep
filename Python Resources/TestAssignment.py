import csv
with open("deb.csv", "w") as f:
    r = csv.writer(f, delimiter=",")
    r.writerow(["Top Gun", "Risky Business", "Minority Report"])
    r.writerow(["Titanic", "The Revenant", "Inception"])
    r.writerow(["Training Day", "Man on Fire", "Flight"])

