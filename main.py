from wordleUI  import Wordle

w = Wordle()

while True:
    w.play()
    
    print(f"\nWins: {w.wins}, Losses: {w.losses}\nCurrent streak: {w.streak}\nCurrent score: {w.score}\n")
    play_again = input("Press any key to play again or (q)uit: ")
    if play_again.lower() == "q": break
