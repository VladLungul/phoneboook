import json
import csv
import configparser

class JSON:
    def load(self):
        try:
            with open("Pb.json", "rt") as f:
                return json.load(f)
        except FileNotFoundError as e:
            return None


    def save(self, obj):
        with open ("Pb.json", "wt") as f:
            json.dump(obj,f)

class CSV:
    def load(self):
        with open ("Pb.csv","rt") as f:
            r = csv.reader(f)
            pb1 = {name:phone for name, phone in r}


    def save(self, obj):
        with open ("Pb.csv", 'wt') as f:
            w = csv.writter(f)
            for row in Pb.items():
                w.writerow(row)


config = configparser.ConfigParser()
config.read("123.ini")

if config['Serializer']['format'] == 'JSON':
    j = JSON()
elif config['Serializer']['format'] == 'CSV':
    j = CSV()
    
def verify (n):
    if n in Pb:
        return True
    else:
        return False

def delete (n):
    if n in Pb:
        del Pb[n]

def Inp():
  return input("Name ")


Pb = {}  
while True:
    Pb = j.load()
    a = input("Create/Find/Delete/Update/Exit c/f/d/u/e? ").lower()
    if a == "c":   
        n = Inp()
        if verify(n) == False:
            num = input ("number")
            Pb[n] = num
            j.save(Pb)
        else:
            print ("You have this contact"+Pb[n])
            
    if a == "f":
        n = Inp()
        if verify (n) == True:
            print(Pb[n])
        else:
            print ("You dont have this contact")
            
    if a == "d":
        n = Inp()
        if verify(n) == True:
            delete(n)
            j.save(Pb)
        else:
            print ("You dont have this contact")
            
    if a == "u":
        n = Inp()
        if verify(n) == True:
            num = input ("number")
            Pb[n] = num
            j.save(Pb)
        else:
            print ("You dont have this contact")

    if a == "e":
        pass
    
    
            
    
    
    
    
