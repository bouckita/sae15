fic=open("C:/Users/Alain/Documents/Recherches 1ère année/Semestre 1/SAE/SAE1.05 Traitement de données/ADESAE15.ics")
res=fic.read() #lire le fichier ligne par ligne
resultat=res.split('\n')
print(type(resultat))
fic.close()
#print(res)
for event in resultat: 
    if event.startswith('UID'):
        cours=event.split(':')
        UID=cours[1]
        print(UID)
    if event.startswith('DTSTART'):
        cours=event.split(':')
        annee=cours[1][0:4]
        mois=cours[1][4:6]
        jour=cours[1][6:8]
        temp=event.split('T')
        heure=cours[1][9:11]
        minutes=cours[1][11:13]
    if event.startswith('SUMMARY'):
        cours=event.split(':')
        type=cours[1][8:10]
        ressource=cours[1][0:7]
    if event.startswith('LOCATION'):
        cours=event.split(':')
        salle=cours[1][0:5]
    if event.startswith('DESCRIPTION'):
        cours=event.split(':')
        Prof=cours[1][15:28]
        gp=cours[1][11:13]

texte=UID+';'+jour+'-'+mois+'-'+annee+';'+heure+':'+minutes+';'+type+';'+ressource+';'+salle+';'+Prof+';'+gp
print(texte)
        

        




