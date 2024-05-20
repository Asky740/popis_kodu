for i in range(5): #cyklus
    print("Opakování číslo:", i) #kod se opakuje 5krat a cislo se po kazde o 1 zvetsi

#cyklus s podmínkou
j = 0
while j < 5:
    print("Podmíněné opakování číslo:", j) #cyklus se opakuje dokud je j vetsi nez 5
    j += 1

#funkce s parametrem
def pozdrav(jmeno): #"jmeno" je parametr
    print("cau", jmeno)

pozdrav("mami") #po pouziti funkce "pozdrav" se mi spusti dany kod

#pole
my_list = [1, 2, 3]
my_list.append(4)  #pridani cisla 4 do pole
print("pole po pridani:", my_list) #vypsani pole

my_list.remove(2)  #odebrani cisla 2 z pole ()
print("pole po odebrani:", my_list) #vypsani pole

#datové typy
my_int = 69
my_str = "chleba chleba chleba chleba chleba chleba chleba chleba chleba chleba chleba chleba chleba chleba chleba chleba"
my_float = 0.420
my_bool = True

#vstup a vystup s pretypovanim
user_input = input("zadej cislo: ") #zadam cislo do inputu jako string
user_input = int(user_input) #pretypovani na integer

#podminky a log funkce
if user_input > 0 and user_input < 10: #jestli je input v rozmezi 0-10, tak se napise to prvni idk
    print("je v 0-10")
else:
    print("neni v 0-10")