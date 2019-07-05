def music_playlist():    
    """
    playlist creation
    day = "Monday"....
    weather = "sunny", "cold", "hot"
    feeling = "happy", "sad", "angry", "surprised"
    """ 

    monday_songs = ['"Майже весна"', '"Без бою"','"Susy"', '"Airplane"', '"911"', '"Дзвони"']
    tuesday_songs = ['"Hello"', '"Padam"','"Papaoutai"', '"Molitva"', '"Funhose"', '"Waka-Waka"']
    wednesday_songs = ['"I will surely die "', '"Stay"','"Wild dances"', '"New York"', '"Money"', '"Twitter Song"']
    thursday_songs = ['"Rendez-Vous"', '"Wind of change"','"Heart On Fire"', '"Poison"', '"Bohemian rhapsody"', '"Feeling good"']
    friday_songs = ['"Hurt"', '"Forgiven "','"Let It Be"', '"I Will Survive"', '"Irish Folk"', '"He is a Pirate"']
    saturday_songs = ['"Skyscraper "', '"Lone wolf"','"Thunder"', '"Hero"', '"Superheroes"', '"Pretty woman"']
    sunday_songs = ['"Yesterday"', '"You Lost Me"','"She Said "', '"Its My Life"', '"Help!"', '"Holiday "']
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    feelings  = ['sad', 'angry', 'surprised', 'happy']
    weathers = ['hot', 'cold', 'warm']

    try:
        mood = int(feelings.index(input('Type one of these: sad, angry, surprised or happy.  ')))
        weath = int(weathers.index(input('Type one of these: hot, cold or warm.  ')))
        a = mood + weath
        day = int(days.index(input('Type the day of the week.  ')))
    
        if day == 0:
            print('play', monday_songs[a])
        elif day == 1:
            print('play', tuesday_songs[a])
        elif day == 2:
            print('play', wednesday_songs[a])
        elif day == 3:
            print('play', thursday_songs[a])
        elif day == 4:
            print('play', friday_songs[a])
        elif day == 5:
            print('play', saturday_songs[a])
        elif day == 6:
            print('play', sunday_songs[a])
    except ValueError:
        print('ValueError')
    except EOFError:
        print('EOFError')


music_playlist()