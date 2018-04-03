#EXERCISE NO. 5 - DICTIONARIES
#Alinea Grace M. Del Mundo
#This program displays the basic infos [age, birthday,and movies/tv shows] 


print ("\nCAST OF DESCENDANTS OF THE SUN 2016\n\t\tBASIC INFORMATION ABOUT: \n\n 1. Song Joong-ki \t\t 7. Song Hye-kyo\n 2. Kim Ji-won \t\t 8. Jin Goo\n 3. Onew\t 9. Kim Min-seok\n 4. David Lee Mclnnis \t 10. Kang Shin-il\n 5. Lee Yi-kyung \t 11. Lee Seung-Jun\n 6. Hyun Jyu-in \t 12. Jeon Soo-jin\n" )
def qt():

     
    alea = {"1":"Name: Song Joong-ki\nAge: 32 years old\nBirthday: September 19, 1985\nMovies and Tv Shows: The Battleship Island, A werewolf Boy, Penny Pinchers, A Frozen Flower, Five Senses of Eros, Descendants of the Sun, Running Man, The Innocent Man, Sungkyunkwan Scandal, Deep Rooted Tree, My Fair Lady, Music Bank, The Sound of Your Heart, Tripe","2":"Name: Kim Ji-won\nAge: 25 years old\nBirthday: October 19,1992\nMovies and Tv Shows: Horror Stories, Romantic Heaven, Horror Stories 2, Alive, Descendants of the Sun, Fight for my Way, The Heirs, To the Beautiful You, One Sunny Day, Waiting For Love","3":"Name: Onew\nAge: 28 years old\nBirthday: December 14, 1989\nTV Shows: Descendants of the Sun, Shinee's Yunhanam","4":"Name: David Lee Mclnnis\nAge: 44 years old\nBirthday: December 12 1973\nMovies and Tv Shows: Never Forever, The Cut Runs Deep, A Moment to Remember, Iris, Typhoon, Descendants of the Sun, Into the Fire","5":"Name: Lee Yi-kyung\nAge: 29 years old\nBirthday: January 8, 1989\nMovies and Tv Shows: White Night, Descendants of the Sun, Welcome to Waikiki, The Pirates, One on One, Ruby Ruby Love","6":"Name: Hyun Jyu-in\nAge: 32 years old\nBirthday: August 1, 1985\nMovies/Tv Shows: Sky and Sea, Descendants of the Sun, Perfect Game, I am Legend","7":"Name: Song Hye-kyo\nAge: 36 years old\nBirthday: November 22, 1981\nMovies/Tv Shows: The Grandmaster, The Queens, Love and let Love, My Brilliant Life, My Girl and I, A reason to Live, Full House, Autumn in My Hesrt, Worlds Within","8":"Name: Jin Goo\nAge: 37 years old\nBirthday: July 20, 1980\nMovies and Tv Shows: Descendants of the Sun, Night Light, One-line, Beating Again, Swallow the Sun, A Dirty Carnival, Love Me Not, Sensitive Couple, Ice Bar, Romantic Assassin, Always","9":"Name: Kim Min-seok\nAge: 28 years old\nBirthday: January 24, 1990\nMovies and Tv Shows: The Beast, Descendants of the Sun, Imaginary Cat, Flower Crew, Aftermath","10":"Name: Kang Shin-il\nAge: 57 years old\nBirthday: November 26, 1960\nMovies and Tv Shows: Descendants of the Sun, Pandora, When a Man Falls in Love, Kimchi Family, Always, Personal Taste, Black House, My Girlfriend Is an Agent, Glove","11":"Name: Lee Seung-Jun\nAge: 45 years old\nBirthday: February 11, 1973\nMovies and Tv Shows: Descendants of the Sun, War of the Arrows, Doomsday Book, Obsessed, Whistle Blower, Handphone","12":"Name: Jeon Soo-jin\nAge: 29 years old\nBirthday: November 9, 1988\nMovies and Tv Shows: Hot Young Bloods, Descendants of the Sun, The Heirs",}
    
    rey = input("\n NO.  ")
    if rey == 1:
        print alea["1"]
    elif rey == 2:
        print alea["2"]
    elif rey == 3:
        print alea["3"]
    elif rey == 4:
        print alea["4"]
    elif rey == 5:
        print alea["5"]
    elif rey == 6:
        print alea["6"]
    elif rey == 7:
        print alea["7"]
    elif rey == 8:
        print alea["8"]
    elif rey == 9:
        print alea["9"]
    elif rey == 10:
        print alea["10"]
    elif rey == 11:
        print alea["11"]
    elif rey == 12:
        print alea["12"]
    else:
        print ("No name matched with the no. you've entered!!!")
        return qt()
    return qt()

    
qt()




