birthdays=["JAN 12 2022","MAR 2 2012","APR 20 2020","MAR 2 2012","MAR 2 2012","APR 20 2020"]
list_birth=[]
for c in birthdays :
    l = c.split()
    list_birth.append({"month" : l[0], "day" : l[1], "year" : l[2]})
print(sorted(list_birth,key=lambda x:x["year"]))
months = {'JAN': "01", 'FEB': "02", 'MAR': "03", 'APR': "04", 'MAY': "05", 'JUN': "06",
          'JUL': "07", 'AUG': "08", 'SEP': "09", 'OCT': "10", 'NOV': "11", 'DEC': "12"}
new_list_birth=[]
for c in list_birth :
    new_list_birth.append(str(c["day"]) + "/" + months[c["month"]] + "/" + c["year"])
list_birth=new_list_birth
print(list_birth)
occ_birth={}
for c in list_birth :
    occ_birth[c]=list_birth.count(c)
print(occ_birth)
min_count=int(input("donner le nombre minimal d'occurrence : "))
print([c for c in occ_birth if occ_birth[c]>=min_count])