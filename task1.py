import random
start=str(input("(っ◔◡◔)っ Хотите сыграть в игру? y/n "))
if start == 'y':
    class Character:
        def __init__(self):
            self.__power = 25
            print("Герой создан")
    
        def buff(self,buff):
            self.__power += buff
    
        def power(self):
            return self.__power
    

    class Monster:
        def __init__(self):
            self.__monster=random.randint(5,100)
            print("Монстры созданы ;3")
        def pm(self):
            return self.__monster
    
    class Artifacts:
        def __init__(self):
            self.__artifacts=random.randint(10,80)
            print("Артефакты созданы ;3")       

    

    chr = Character()
    mnst = Monster()
    artf = Artifacts()
    levels = [random.randint(0,1) for i in range(10)]
    doors = []
    while True:
        a = int(input("И в какую же дверь вы хотите зайти (от 0 до 9): "))
        doors.append(random.randint(0,10))
        
        if levels[a] == 0:
            b = random.randint(10,80)
            chr.buff(b)
            print("Герой получил бафф в размере " + str(b) + " очков")
        else:
            c = random.randint(5,100)
            print("Ты встретил монстра с силой равной " + str(c) + " очкам ;3")
            if chr.power() >= c:
                print("Ну молодец, ты победил монстра (っ◔◡◔)っ")
            else:
                print("Ты проиграл в неравном бою! (´｡• - •｡)")
                exit()
        if len(doors) >= 10:
            print("Ты победил!!!!! (っ◔◡◔)っ❤")
            print("Твоя сила составляет ", chr.power() , " очков ;3")
            break
   
else:
    print("Ну и ладно (´｡• ^ •｡)")
    exit()
    


# Герой компьютерной игры, обладающий силой в 25 баллов, находится в круглом зале, из которого ведут 10 закрытых дверей.
# За каждой дверью героя ждет либо магический артефакт, дарующий силу от 10 до 80 баллов, либо монстр,
#  имеющий силу от 5 до 100 баллов, с которым герою нужно сразиться. Битву выигрывает персонаж, обладающий наибольшей силой;
#  если силы равны, побеждает герой.
# Информация о том, что находится за дверями выбирается используя генератор случайных чисел.
# Вывести эту самую информацию на экран в понятном табличном виде. Хотя бы подобие таблички