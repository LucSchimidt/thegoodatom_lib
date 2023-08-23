import thegoodatom as tga

def main():

    meu_habito = tga.Habit('beber água','Vou beber água na cozinha toda vez que eu for pegar um café.','','','','night')
    meu_habito2 = tga.Habit('treinar', 'Irei treinar na academia todos os dias as 15h.','','','','night')
    lista_habitos = tga.HabitList()



    lista_habitos.addHabit(meu_habito)
    lista_habitos.addHabit(meu_habito2)

    print(meu_habito)


    print(lista_habitos)
    print(lista_habitos.habits['night_habits']['beber água'].period)

    lista_habitos.deleteHabit(meu_habito)

    print(lista_habitos)


if __name__ == "__main__":
    main()