from keyboard import *
from random import *

def start():
    """
    Teeme valik kellega mängime 
    Tagastame m muutuja int formaadis

    :rtype: int
    """
    print("Kivi, Käärid, Paber")
    m=3
    while m not in [1,2]:
        try:
            m=int(input("Kellega mängime?\n1-Botid \n2-Robotiga"))

        except:
            ValueError
    return m

def botvsbot(v1:list,v2:list):
    """Robootite mäng
    Näitame ekraanile võitja nime
    Tagastame m muutuja int formaadis
    :param list v1: järjend esimese roboti jaoks
    :param list v2: järjend teise roboti jaoks
    """
    while True:
        print("Kas mängime? ESC + Välja, Enter - mängime")
        if read_key()=="esc":
            break
        elif read_key()=="enter":
            p1= choice(v1)
            print("Esimene bot:",p1)
            p2= choice(v2)
            print("Teine bot:",p2)
            if p1==p2:
                print("Viik")
            elif p1==v1[0] and p2==v2[1] or p1==v1[2] and p2==v2[0] or p1==v1[1] and p2==v2[2]:
                print("Võitis 1")
            else:
                print("Võitis 2")

def robotvs():
    a=0
    while a!="x" not in [1,2,3]:
            try:
                player = int(input("1 - Камень, 2 - Ножницы, 3 - Бумага"))
                if (player==1 or player==2 or player==3):
                    a=1
                if player==1:
                    print("Вы выбрали камень.")
                elif player==2:
                    print("Вы выбрали ножницы.")
                elif player==3:
                    print("Вы выбрали бумагу.")
                bot=randint(1,3)
                if bot==1:
                    print("Компьютер выбрали камень.")
                elif bot==2:
                    print("Компьютер ножницы.")
                elif bot==3:
                    print("Компьютер бумагу.")
                if player==1 and bot==2 or player==2 and bot==3 or player==3 and bot==1:
                    win=1
                if player==1 and bot==3 or player==2 and bot==1 or player==3 and bot==2:
                    win=2
                if player==3 and bot==3 or player==2 and bot==2 or player==1 and bot==1:
                    win=0
                if win==0:
                    print("Ничья.")
                elif win==1:
                    print("Вы победили!")
                elif win==2:
                    print("Победил компьютер.")
            except:
                ValueError