song_titles = ['Янанебiбув', 'Той день', 'Мало менi', 'Сосни', 'Кавачай', 'Вiдпусти', 'Африка', 'Поясни', 'Фiалки', 'Коли тебе нема', 'Етюд']
length_songs = ['3.19', '3.58', '5.06', '4.31', '4.39', '3.52', '4.24', '3.39', '3.43', '3.17', '2.21']
def song_length(x):
    return x[-1]

def title_length(x):
    return len(x[0])
    
def last_word(x):
    splited_title = x[0].split()
    word = splited_title[-1]
    return word[0]

def sort_songs(song_titles, length_songs, key):
    if len(song_titles) != len(length_songs):
        return None
    else: 
        tracks = zip(song_titles, length_songs)
        if key == song_length:
            return sorted(tracks, key = song_length)
        elif key == title_length:
            return sorted(tracks, key = title_length)
        elif key == last_word:
            return sorted(tracks, key = last_word)

print(sort_songs(song_titles, length_songs, key = last_word))
