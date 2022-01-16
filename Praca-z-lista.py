# Praca z listą
autorzy=["Mickiewicz","Norwid","Rilke","Lem"]
imiona=["Adam", "Cyprian", "Rainer"]
imiona.append("Stanislaw")
autorzy.insert(2, "Tolstoy")
autorzy.extend(imiona)
autorzy.remove("Norwid")
autorzy.pop(5)
autorzy.sort(reverse=0)
print(autorzy[0:])
print(autorzy.index("Tolstoy"))