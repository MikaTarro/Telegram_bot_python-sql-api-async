def list_gamer(persons):
    gamers = []
    if (persons):
        for person in persons:
            persons = person[4]
            gamers.append(persons)
        gamers = '\n'.join(gamers)
    else:
        gamers = 'На это событие нет записей'
    return gamers
