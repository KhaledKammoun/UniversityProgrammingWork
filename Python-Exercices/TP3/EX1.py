import datetime
L=[('nom','Duprès'),('prenom','Jaques'),('poste','ingénieur'),('date',datetime.date(2014, 10, 9))]
#question_1
dic={}
for c in L :
    dic[c[0]]=c[1]
print(dic)
#question_2
print(dic.keys()) # dict_keys(['nom', 'prenom', 'poste', 'date'])
print(dic.values()) # dict_values(['Duprès', 'Jaques', 'ingénieur', datetime.date(2014, 10, 9)])
print(dic.items()) # dict_items([('nom', 'Duprès'), ('prenom', 'Jaques'), ('poste', 'ingénieur'), ('date', datetime.date(2014, 10, 9))])
print(dict(dic.items())) # {'nom': 'Duprès', 'prenom': 'Jaques', 'poste': 'ingénieur', 'date': datetime.date(2014, 10, 9)}
print({k:dic[k] for k in dic.keys()}) # {'nom': 'Duprès', 'prenom': 'Jaques', 'poste': 'ingénieur', 'date': datetime.date(2014, 10, 9)}
print({k:v for k,v in dic.items()}) # {'nom': 'Duprès', 'prenom': 'Jaques', 'poste': 'ingénieur', 'date': datetime.date(2014, 10, 9)}
#question_3
print(dic['prenom'],dic['nom'],'était un',dic['poste'],'en',dic['date'])
#question_4
dic1=dic.copy()
dic1['poste']='chef de projet'
dic1['date']=datetime.date(2016,10,9)
#question_5
dic['age']=30
#qustion_6
dic1['age']=dic['age'] + dic1['date'].year - dic['date'].year