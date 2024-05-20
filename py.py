for i in range(5): #cyklus
    print("opakovane cislo:", i) #kod se opakuje 5krat a cislo se po kazde o 1 zvetsi

#cyklus s podmínkou
j = 0 # pismeno j se rovna 0
while j < 5: #cyklus se opakuje dokud je j vetsi nez 5
    print("opakovane cislo s podminkou:", j) #cyklus se opakuje dokud je j vetsi nez 5
    j += 1 #pricteni 1

#funkce s parametrem
def pozdrav(jmeno): #"jmeno" je parametr
    print("cau", jmeno) #napise se cau a za to ten parametr

pozdrav("mami") #po pouziti funkce "pozdrav" se mi spusti dany kod

my_list = [1, 2, 3] #pole
my_list.append(4)  #pridani cisla 4 do pole
print("pole po pridani:", my_list) #vypsani pole

my_list.remove(2)  #odebrani cisla 2 z pole ()
print("pole po odebrani:", my_list) #vypsani pole

#datové typy
my_int = 69 #integer
my_str = "chleba chleba chleba chleba chleba chleba chleba chleba chleba chleba chleba chleba chleba chleba chleba chleba" #string
my_float = 0.420 #float
my_bool = True #boolean

#vstup a vystup s pretypovanim
user_input = input("zadej cislo: ") #zadam cislo do inputu jako string
user_input = int(user_input) #pretypovani na integer

#podminky a log funkce
if user_input > 0 and user_input < 10: #jestli je input v rozmezi 0-10, tak se napise to prvni idk
    print("je v 0-10") #tohle se vypise kdyz je v rozmezi
else: #nebo
    print("neni v 0-10") #tohle se vypise kdyz neni v rozmezi