import random

wordlist = []
guesses = ""
turns = 5

for i in range(1):
    words = input("PLEASE INPUT RANDOM WORDS")
    wordlist.append(words)
    if len(wordlist) >= 5:
        print("RANDOM WORDS LIST")
        print("________________________________")
        print(*wordlist, sep="\n")
        break

yn = input("lets play the game yes or no")
if yn == "yes" or yn == "y" or yn == 'Y':

    player2 = input("whats your name???")
    print("Good luck !!", player2)
    word = random.choice(wordlist)

    while turns > 0:
        failed = 0

        for character in word:
            if character in guesses:
                print(character, end=" ")
            else:
                print("_", end=" ")
                failed = failed + 1
        if failed == 0:
            print("      ")
            print("YOU WON")
            print("THE WORD IS", word)
            break
        print("                         ")
        guess = input("guess the character...")
        guesses = guesses + guess
        if guess not in word:
            turns = turns - 1
            print("Wrong")
            if turns == 0:
                print("    -----                        ||")
                print("   | 0 0 |                       ||")
                print("   |  *  |                       ||")
                print("  ( ------ )---------------------||")
                print("      |                          ||")
                print("<-----|----->                    ||")
                print("      |                          ||")
                print("   ___|___                       ||")
                print("   |      |                      ||")
                print("   |      |                      ||")
                print("   ()     ()                     ||")

            elif turns == 1:
                print("    -----                        ||")
                print("   | 0 0 |                       ||")
                print("   |  *  |                       ||")
                print("  ( ------ )---------------------||")
                print("      |                          ||")
                print("<-----|----->                    ||")
                print("      |                          ||")
                print("   ___|___                       ||")
            elif turns == 2:
                print("    -----                        ||")
                print("   | 0 0 |                       ||")
                print("   |  *  |                       ||")
                print("  ( ------ )---------------------||")
                print("      |                          ||")
                print("<-----|----->                    ||")
            elif turns == 3:
                print("    -----                        ||")
                print("   | 0 0 |                       ||")
                print("   |  *  |                       ||")
                print("  ( ------ )---------------------||")
                print("      |                          ||")
            elif turns == 4:
                print("    -----                        ||")
                print("   | 0 0 |                       ||")
                print("   |  *  |                       ||")
                print("  ( ------ )---------------------||")
            elif turns == 5:
                print("    -----                        ||")
                print("   | 0 0 |                       ||")
                print("   |  *  |                       ||")
            print("You have", turns, 'more guesses')
            if turns == 0:
                print("You Loose")

