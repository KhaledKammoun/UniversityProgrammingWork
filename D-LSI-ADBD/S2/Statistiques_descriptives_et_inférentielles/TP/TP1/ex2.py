import matplotlib.pyplot as plt 
age = [43, 64,45,55,43,38,64,55,47,64,29,46,29,64,43,39,19,55,29,19]
age_unique = sorted(list(set(age)))
age_unique_eff = [age.count(c) for c in age_unique]

age_unique_freq = [round(c / len(age),2) for c in age_unique_eff]
print(age_unique)
print(age_unique_eff)
print(age_unique_freq)


age_unique_freq_cum = [0]*len(age_unique_eff)
age_unique_freq_cum[0] = age_unique_freq[0]
for i in range (1, len(age_unique_freq)) :
    age_unique_freq_cum[i] = round(age_unique_freq[i] + age_unique_freq_cum[i-1], 2)
    
print(age_unique_freq_cum)
plt.bar(age_unique, age_unique_freq_cum, width=0.5)
plt.xlabel("Age")
plt.ylabel("Age effectifs cum")
plt.title("Representation diagramme en batons")
plt.show()
# plt.pie(age_unique_eff, labels=age_unique, autopct='%1.1f%%')
# plt.show()
# plt.bar(age_unique, age_unique_eff, width=0.5)
# plt.xlabel("age")
# plt.ylabel("age effectifs")
# plt.title("Representation diagramme en batons")
# plt.show()
# plt.bar(age_unique, age_unique_freq, width=0.5)
# plt.show()