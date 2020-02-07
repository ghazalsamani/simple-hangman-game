from random_word import RandomWords
r= RandomWords()
chosenword=r.get_random_word(hasDictionaryDef = True)
letterslist = list(chosenword)
if "-" in letterslist:
    letterslist.remove("-")  
if " " in letterslist:
    letterslist.remove(" ")
words_length= len(chosenword)
underlines = ["___"] * words_length
print(" welcome to my world of words!The word that I have in my mind has " + str(words_length)+" letters")
print(" ".join(underlines))
chance = 0
wrongs = []
while chance <= words_length:
    print("Guess a letter please")
    guess= input()
    if guess in letterslist:
        print("that was correct")
        correct = letterslist.index(guess)
        underlines[correct] = guess
        letterslist[correct] = "&"
        print(" ".join(underlines))
    if guess not in  letterslist :
        if guess in wrongs and guess not in underlines:
            print("you had said that before")
            print(" ,".join(wrongs))
        if guess  in underlines:
            print("there is no more of this letter in your word")
        if guess not in wrongs  and  guess not in underlines:
                chance +=1
                wrongs.append(guess)
                print("you lost a chance !list of the words you have guessed wrong till now")
                print(" ,".join(wrongs))
if "___" in underlines:
    print("looser!it was " + chosenword)
else:
    print("we have a winner")
    
    

