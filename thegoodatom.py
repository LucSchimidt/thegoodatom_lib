#Classe para definição dos objetos hábitos:
class Habit(object):

    def __init__(self, name:str, intention:str, group:str, origin:str, status:str, period:str):
        self.name = name
        self.intention  = intention
        self.group = group
        self.origin = origin
        self.status = status
        self.period = period


    def __str__(self) -> str:
        info = [self.name, self.intention, self.group, self.origin, self.status, self.period]
        return f'Habit Info: {str(info)}'


class HabitList(object):

    #Class variables:
    habits = {
        'morn_habits': {
            '':'',
        },
        'noon_habits': {
            '':'',
        },
        'night_habits': {
            '':'',
        }
    }
    
    def __init__(self) -> None:
        pass

    
    #Método que adiciona novos hábitos para a lista:
    def addHabit(self, habit) -> None:

        new_habit = habit

        #Adicionando o habito novo para o dicionário de habitos:
        try:
            if (str(type(new_habit)) == "<class 'thegoodatom.Habit'>"): #Se o objeto que for passado para o método addHabit for do tipo habito, aí ele é adicionado ao dicionário.

                try:

                    if (new_habit.period == 'morn'):
                        self.habits['morn_habits'].update({new_habit.name: new_habit})

                    elif (new_habit.period == 'noon'):
                        self.habits['noon_habits'].update({new_habit.name: new_habit})

                    elif (new_habit.period == 'night'):
                        self.habits['night_habits'].update({new_habit.name: new_habit})
                        
                
                except Exception as ex:
                    print(ex)
                    print(type(str(ex)))

            else:
                print("Your object isn't a habit.")

        except Exception as ex:
            print(ex)
            print(type(str(ex)))


    #Método que deleta um hábito específico da lista de hábitos:
    def deleteHabit(self, habit) -> None:

        deleted_habit = habit

        #Adicionando o habito novo para o dicionário de habitos:
        try:
            if (str(type(deleted_habit)) == "<class 'thegoodatom.Habit'>"): #Se o objeto que for passado para o método deleteHabit for do tipo habito, aí ele é deletado do dicionário.

                try:
                    
                    if (deleted_habit.period == 'morn'):
                        habits = self.habits['morn_habits']
                        habits.pop(str(deleted_habit.name))
                        print('Hábito deletado')

                    elif (deleted_habit.period == 'noon'):
                        habits = self.habits['noon_habits']
                        habits.pop(str(deleted_habit.name))
                        print('Hábito deletado')

                    elif (deleted_habit.period == 'night'):
                        habits = self.habits['night_habits']
                        habits.pop(str(deleted_habit.name))
                        print('Hábito deletado')
                
                except Exception as ex:
                    print(ex)
                    print(type(str(ex)))

            else:
                print("Your object isn't a habit.")

        except Exception as ex:
            print(ex)
            print(type(str(ex)))


    def __str__(self) -> str:
        return f'{self.habits}'