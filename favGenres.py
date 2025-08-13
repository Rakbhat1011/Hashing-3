"""
Build a song -> genre lookup for O(1) genre access
For each user, tally genres of their songs using the lookup
Pick all genres tied for the user’s max count
"""
"""
Time Complexity:  O(U·S + G·T)
U·S to iterate each user’s songs, G·T to build the song->genre map (G genres, total T songs listed)
Space Complexity: O(T) for the song_to_genre map (plus small per-user counters)
"""


from collections import defaultdict
from typing import Dict, List

def favorite_genre(user_songs: Dict[str, List[str]],
                   song_genres: Dict[str, List[str]]) -> Dict[str, List[str]]:

    song_to_genre = {}
    for genre, songs in song_genres.items():
        for song in songs:
            song_to_genre[song] = genre


    result: Dict[str, List[str]] = {}
    for user, songs in user_songs.items():
        counts = defaultdict(int)
        for song in songs:
            if song in song_to_genre:            
                counts[song_to_genre[song]] += 1

        if not counts:
            result[user] = []    
            continue

        max_count = max(counts.values())
        result[user] = [g for g, c in counts.items() if c == max_count]

    return result


if __name__ == "__main__":
    userSongs = {
        "David": ["song1", "song2", "song3", "song4", "song8"],
        "Emma":  ["song5", "song6", "song7"]
    }

    songGenres = {
        "Rock":   ["song1", "song3"],
        "Dubstep":["song7"],
        "Techno": ["song2", "song4"],
        "Pop":    ["song5", "song6"],
        "Jazz":   ["song8", "song9"]
    }

    print(favorite_genre(userSongs, songGenres))
    # Expected:
    # {'David': ['Rock', 'Techno'], 'Emma': ['Pop']}

    # Extra edge cases
    print(favorite_genre({"A": ["x","y"]}, {}))                   # {'A': []}
    print(favorite_genre({"A": ["x","y"]}, {"G": ["x"]}))         # {'A': ['G']}
    print(favorite_genre({"A": []}, {"G": ["x"]}))                # {'A': []}
