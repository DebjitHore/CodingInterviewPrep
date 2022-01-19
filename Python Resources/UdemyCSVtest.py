import csv
with open("deb.csv", "w") as f:
	r= csv.writer(f, delimiter= ",")
	r.writerow(["one", "two", "three"])
	r.writerow(["four", "five", "six"])
