import random as rdm  
from time import sleep
from os import system

# ASCII animācija, kas parādīsies, kad spēle sākas
animation_start = '''
*******************************
***   Laipni lūdzam spēlē!  ***
*******************************
'''

# ASCII animācija, kas parādīsies, kad spēle ir uzvarēta
animation_win = '''
*******************************
***   Apsveicu, tu uzvarēji! ***
*******************************
'''

#Šeit lietotājam tiek uzprasīts vārds spēles sākumam
vārds1 = input("Kā tevi sauc?:")  

print(animation_start)
print("Veiksmi", vārds1)  
   
 # Vārdi masīva ko izmantos uzminēt vārdu  
vardi1 = ['dzīvnieks', 'latvija', 'javascript', 'programma',
'python', 'valoda', 'futbols', 'hokejs',
'basketbols', 'csharp', 'github', 'matemātika', 'astronomija',
'ķīmija', 'bioloģija', 'vēsture', 'ekonomika', 'filozofija', 'socioloģija', 'politika', 'kompilators', 'kods', 'dati', 'tīmeklis', 'serveris', 'sistēma'] 
   
#rdm.choice() funkcija izvēlēsies vienu nejauši vārdu no vārdi1 masīva
vards2 = rdm.choice(vardi1)  
   
   
print ("Uzmini burtus: ")  
   
meginajumi1 = ''  
   
# Var izvēlēties jebkādu ciparu meģinājumu skaitam
gajieni1 = 10  
   
   
while gajieni1 > 0:  
       
    # skaita cik reizes lietotājs ir neuzminējis pareizo burtu
    zaudejis1 = 0  
       
    # katrs ierakstītais burts tiks lietots viens reize
    for burts in vards2:  
           
           
        if burts in meginajumi1:  
            print(burts)  
               
        else:  
            print("_")  
               
            # Par katru neatminētu burtu lietotājam noņemsies meģinājumu skaits
            zaudejis1 += 1  
               
   
    if zaudejis1 == 0:  
        # Lietotājs uzvarēs spēli ja zudejuma numurs ir 0
        print(animation_win)  


        # Šis izprintēs pareizo vārdu
        print("Pareizais vārds ir: ", vards2)  
        break  
        
    # Ja lietotājs ievadīs nepareizo burtu, tas liks burtu ievadīt velreiz
    minejums1 = input("Mini burtu velreiz:")  
       
        
    meginajumi1 += minejums1  
       

    # Šeit pārbauda ievadīto burtu ar pareizo vārdu
    if minejums1 not in vards2:  
           
        gajieni1 -= 1  
           
        # Ja ievadītais burts nebūs pareizs, izvadīsies "Nepareizs minējums"
        print("Nepareizs minējums")  
           
        # Šis parādīs cik gājieni vēl ir palikuši lietotājam
        print("Tev ir", + gajieni1, 'gājieni ')  
           
           
        if gajieni1 == 0: 

            print("""
*************************
***   Tu zaudēji! ***
*************************
""")

            print("Pareizais vārds bija:", vards2)

