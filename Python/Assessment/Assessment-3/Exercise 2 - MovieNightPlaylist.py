'''
    Movie Night Playlist
    Scenario: You are organizing a movie marathon. You start with a playlist: ["Inception", "The Matrix", "Interstellar"]. 
    Prompt the user to enter the name of a movie they want to add.
    If the movie is already in the list, print "Already added!" and do not insert it.
    If it is not in the list, append it to the end of the list. Finally, sort the movie list alphabetically and print the 
    updated playlist.
    Sample Input: "Interstellar"
    Sample Output:
    Already added!
    Alphabetical Playlist: ['Inception', 'Interstellar', 'The Matrix']
    Sample Input: "Avatar"
    Sample Output:
    Added Avatar!
    Alphabetical Playlist: ['Avatar', 'Inception', 'Interstellar', 'The Matrix']
'''
import os
def is_movie_already_exist(current_playlist, new_movie):
    return new_movie.lower() in [movie.lower() for movie in current_playlist]
def movie_night_playlist(current_playlist, new_movie):
    if is_movie_already_exist(current_playlist, new_movie):
        print("Already added!")
    else:
        current_playlist.append(new_movie)
        print(f"Added {new_movie}!")
    current_playlist.sort()
    return current_playlist
def main():
    append_movie = input("Enter the movie name to add: ").strip()
    current_movie_playlist = ["Inception", "The Matrix", "Interstellar"]    
    updated_playlist = movie_night_playlist(current_movie_playlist, append_movie)
    print(f"Alphabetical Playlist: {updated_playlist}")
if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    print("*" * 80)
    print(f"{' Movie Night Playlist ':^80}")
    print("-" * 80)
    main()