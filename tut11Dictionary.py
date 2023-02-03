# Dictionary is nothing just a key value pairs
d1={}
print(type(d1))
d2={"Moju":"Burger","NESU":"Biryani","Haider":"Piza","Waleed":{"BreakFast":"Maggi","Lunch":"Biryani","Dinner":"Pizza"}}
print(d2["Waleed"]["Lunch"])
d2["Ankit"]="Junk Food"
d2["Auranzaib"]="kebabs"
d2[420]="Fish"
del d2[420]
print(d2)
d3=d2.copy()
del d3["Waleed"]
print(d2)
print(d2.get("Waleed"))
d2.update({"Russian-Bitch":"Is Mine"})
print(d2)
print(d2.keys())#will print keys
print(d2.items())#Will print items