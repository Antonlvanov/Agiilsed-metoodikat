# Iteratiivne 

logs = []

def liitumine ():
    try: 
        a = float(input("sisesta 1 arv: "))
        b = float(input("sisesta 2 arv: "))
    except:
        print ("wrong input")
    sign = input("action: ")
    if sign == "+" :
        return a+b
        logs.append("liitumine "+ a + " ja " + b)
    if sign == "-" :
        return a-b
        logs.append("lahutamine "+ a + " ja " + b)
    if sign == "*" :
        return a*b
        logs.append("korrutamine "+ a + " ja " + b)
    if sign == "/" :
        try: 
            return a/b
            logs.append("jagamine "+ a + " ja " + b)
        except ZeroDivisionError:
            print ("cant devide by 0")
    else:
        return "wrong action"
    
def logs_out():
    jag=0
    korr=0
    liit=0
    lahut=0
    for elem in logs:
        if elem.__contains__("liitumine"):
            liit=+1
        if elem.__contains__("lahutamine"):
            lahut=+1
        if elem.__contains__("korrutamine"):
            korr=+1
        if elem.__contains__("jagamine"):
            jag=+1
    return [liit,lahut,korr,jag]

print (liitumine())


# Inkrementaalne lähenemine
# Tehtud 1-3 increment'id

class Patsient:
    def __init__(self, nimi, vanus):
        self.nimi = nimi
        self.vanus = vanus
        self.regAeg = None
        
class Arst:
    def __init__(self, nimi, eriala):
        self.nimi = nimi
        self.eriala = eriala
        self.kohtumised = [] 
        
    def lisa_kohtumine(self, kohtumine):
        self.kohtumised.append(kohtumine)
        
class Kohtumine:
    def __init__(self, aeg, arst, patsient):
        self.aeg = aeg
        self.arst = arst
        self.patsient = patsient
    
class Haigla:
    def __init__(self):
        self.patsiendid = [] 
        self.arstid = [] 

    def lisa_patsient(self, patsient):
        self.patsiendid.append(patsient)

    def lisa_arst(self, arst):
        self.arstid.append(arst)

    def patsiendite_kuvamine(self):
        for index, patsient in enumerate(self.patsiendid):
            print(f'id: {index}, Nimi: {patsient.nimi}, Vanus: {patsient.vanus}')

    def arstide_kuvamine(self):
        for index, arst in enumerate(self.arstid):
            print(f'id: {index}, Nimi: {arst.nimi}, Eriala: {arst.eriala}')

    def kohtumine_tegimine(self, patsient, arst, aeg):
        for kohtumine in arst.kohtumised:
            if kohtumine.aeg == aeg:
                print(f"Aja {aeg} võttis juba arst {arst.nimi}.")
                return
            
        kohtumine = Kohtumine(aeg, arst, patsient)
        arst.lisa_kohtumine(kohtumine)
        patsient.regAeg = aeg
        print(f"Patsiendi {patsient.nimi} kohtumine arstiga {arst.nimi} kuupäeval {aeg} oli edukalt planeeritud.")
                

patsient_1 = Patsient("Tomas", 66)
patsient_2 = Patsient("Karl", 55)

arst_1 = Arst("Tom", "perearst")
arst_2 = Arst("Bob", "meestearst")

haigla = Haigla()
haigla.lisa_patsient(patsient_1)
haigla.lisa_patsient(patsient_2)
haigla.lisa_arst(arst_1)
haigla.lisa_arst(arst_2)

haigla.patsiendite_kuvamine()
haigla.arstide_kuvamine()

haigla.kohtumine_tegimine(patsient_1, arst_1, "2025-04-07 10:00")
haigla.kohtumine_tegimine(patsient_2, arst_1, "2025-04-07 11:00")
haigla.kohtumine_tegimine(patsient_1, arst_1, "2025-04-07 10:00")

print("Patsient 1 ja 2 registreerimine aeg:")
print(patsient_1.regAeg)
print(patsient_2.regAeg)

print("Arst_1 esimene vastuvõtt on Patsient:", arst_1.kohtumised[0].patsient.nimi, "Aeg:", arst_1.kohtumised[0].aeg)
