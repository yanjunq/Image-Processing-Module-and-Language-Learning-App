#should rename the draw module to draw_mu.py
#draw_program
#Author1: Yanjun Qian
#Section1 : OL01
#Author2: Tianyu Cai
#Section2 :D300
#Group: FinalProject - 180
#Date : Nov 19 / 22


import cmpt120image
import random
import draw_mu


###############################################################
# Keep this block at the beginning of your code. Do not modify.
def initEnv():
    print("\nWelcome! Before we start...")
    env = input("Are you using mu w/pygame0 (m), replit (r) or idle (i)? ").lower()
    while env not in "mri":
        print("Environment not recognized, type again.")
        env = input("Are you using mu w/pygame0 (m), replit (r) or idle (i)? ").lower()
    print("Great! Have fun!\n")
    return env

# Use the playSound() function below to play sounds.
# soundfilename does not include the .wav extension,
# e.g. playSound(apples,ENV) plays apples.wav
def playSound(soundfilename,env):
    if env == "m":
        exec("sounds." + soundfilename + ".play()")
    elif env == "r":
        from replit import audio
        audio.play_file("sounds/"+soundfilename+".wav")
    elif env == "i":
        pygame.mixer.init()
        pygame.mixer.music.load("sounds/"+soundfilename+".wav")
        pygame.mixer.music.play()

ENV = initEnv()
###############################################################


#get the object name and put all into a list
def getobjectlist(filename):
    file = open(filename)
    objectlist = []
    for line in file:
        linelist = line.strip()
        objectlist += [linelist]

    return objectlist

#print the menu
def printmenu():
    print()
    for i in menulist:
        print(i)

#print the instruction in play section
def playinstruction():
    print()
    print("PLAY")
    print()
    print("This is a seek and find game. You will hear a word.")
    print("Count how many of that you find!")

# put the learnlist into this function for the playing
#get the first three of item for the image paly on canva in PLAY section
def challengelist(alist):
    random.shuffle(alist)
    challengL = alist[0:3]
    return challengL

# used to recolour the item in the PLAY section
def randomcolor():
    colorlist = ["red","green","blue"]
    random.shuffle(colorlist)
    #in order to prevent the color become white or some color that are too slight to see
    colorlist[0] = random.randint(0,180)
    colorlist[1] = random.randint(0,255)
    colorlist[2] = random.randint(0,255)
    randcolour = (colorlist[0],colorlist[1], colorlist[2])
    return randcolour

#use to get the num if single item show in canva in the PLAY section
def countOfShowlist(alist):
    countlist = []
    for i in range(len(alist)):
        num = random.randint(1,4)
        countlist += [num]

    return countlist

#get the random num of 0 or 2 for the actualdraw(img) fundtion
def randomdraw():
    num = random.randint(0, 2)
    if num == 0:
        result = True
    else:
        result = False
    return result

#random modify the img (minify and mirror)
#get used in the PLAY section
def actualdraw(img):

    res1 = randomdraw()
    res2 = randomdraw()

    runlist = [res1, res2]
    #minify or not
    if runlist[0] == True:
        modifityImg1 = draw_mu.minify(img)
    else:
        modifityImg1 = img
    # mirror or not
    if runlist[1] == True:
        modifityImg2 = draw_mu.mirror(modifityImg1)
    else:
        modifityImg2 = modifityImg1

    return modifityImg2

#section 1:learn
def image_show(lst, n):

    for i in range(n):
        canva = cmpt120image.getWhiteImage(400,300)
        img = cmpt120image.getImage("images/"+lst[i]+".png")
        #random the position of img show in canva by call out the function from draw_mu
        img3 = draw_mu.distributeItems(canva,img, 1)
        cmpt120image.showImage(canva)
        playSound(lst[i],ENV)
        input("{}. Press enter to continue...".format(i+1))

#section 2:Play
def play(showL, countL, testnum):

    for i in range(len(showL)):
        img = cmpt120image.getImage("images/" + showL[i] + ".png")
        color = randomcolor()
        #recolor
        img2 = draw_mu.recolorImage(img,color)
        #random modify the img (minify and mirror)
        img3 = actualdraw(img2)
        countnum = countL[i]
        draw_mu.distributeItems(canva, img3, countnum)

    cmpt120image.showImage(canva)
    playSound(showL[len(showL)-1],ENV)
    num = input("Listen to the word. How many of them can you find?")
    #add a while loop to check valid input

    while not num.isdigit():
            num = input("Listen to the word. How many of them can you find?").strip(" .,/?!")

    num = int(num)

    if num == testnum:
        input("Right! Press enter to continue.")
        print()
    else:
        input("Sorry, there were {}. Press enter to continue.".format(testnum))
        print()




menulist = ["MAIN MENU","1. Learn - Word Flashcards", "2. Play - Seek and Find Game",\
"3. Settings - Change Difficulty","4. Exit"]

drawlist = ["mirror", "minify"]


#get the object from a file
objectlist = getobjectlist("blackfoot.csv")
learnlist = objectlist[:3]
learnnum = 3
count = 0
ongoing = True
##In order to check the correct input and to exit
while ongoing:
    printmenu()
    print()
    option = input("Choose an option:")

    if option == "1":

        image_show(learnlist, len(learnlist))


    elif option == "2":
        playinstruction()
        print()
        rounds = input("How many rounds would you like to play?").strip(" .,/?!")

        #add a while loop to check valid input
        while not rounds.isdigit():
            rounds = input("How many rounds would you like to play?").strip(" .,/?!")

        rounds = int(rounds)


        for i in range(rounds):
            #get the random list by using shuffle
            showItermList = challengelist(learnlist)
            #and then get the last one on the list for the guess for player
            countlist = countOfShowlist(showItermList)
            testcount = countlist[len(countlist)-1]

            canva = cmpt120image.getWhiteImage(400, 300)

            play(showItermList,countlist,testcount)



    elif option == "3":

        print()
        print("You are currently learning {} words.".format(learnnum))

        #reset the learnobject
        learnnum = (input("How many would you like to learn(3-"+ str(len(objectlist))+")?").strip(" .,/?!"))
        if learnnum.isdigit():
            learnnum = int(learnnum)
            if int(learnnum) > 3 and int(learnnum) <= len(objectlist):
                learnnum = int(learnnum)
                learnlist = objectlist[:learnnum]

            else:
                 print("Sorry, that is not a valid number. Resetting to 3 words.")
                 learnnum = 3
                 learnlist = objectlist[:learnnum]

        else:
            print("Sorry, that is not a valid number. Resetting to 3 words.")
            learnnum = 3
            learnlist = objectlist[:learnnum]

    elif option == "4":
        ongoing = False
        print("Goodbye!")

    else:
        print("Invalid number.")
