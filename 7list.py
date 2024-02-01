countries = ["Kenya", "Uganda","Zambia"]
countries.append("Ghana")
#print(countries)

colByFrench=("Mali", "Burkina")
countries.extend(colByFrench)
#print(countries)

countries.remove("Uganda")
print (countries)

countries.pop(1)
#print(countries)

countries.clear()
print(countries)