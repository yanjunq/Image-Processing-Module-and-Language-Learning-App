# Image-Processing-Module-and-Language-Learning-App

#Image Processing Module
Implement the following 5 functions and place them into a custom module called draw.py.  

1. recolorImage(img, color) - Changes all non-white pixels of the image referred to by the parameter img to the specified color, and returns a new image with the changes. img is a  2D array of RGB pixels as seen in class to represent images. color is a list containing 3 integers, each from 0 to 255, representing RGB values. To create a new image use the cmpt120image.getBlackImage() function which returns a new canvas to draw on.

2. minify(img) - Shrinks the image img by half in both height and width and returns the result. For this function, you can assume the width and height of images are even. Use the cmpt120image.getBlackImage() function which returns a new canvas to draw on. Hint: The average of each 2x2 block of pixels from the original image becomes one pixel in the result image. As an example, the R/G/B values of the pixel at result[0][0] with have the average-R/average-G/average-B values of the pixels at original[0][0], original[0][1], original[1][0], and original[1][1].

3. mirror(img) - Flips the image img left-to-right, and returns a new image with the result. Use the cmpt120image.getBlackImage() function which returns a new canvas to draw on. 

4. drawItem(canvas, item, row, col) - Modify canvas by drawing the non-white pixels of the item (intended to be the image of a word) onto canvas. Row and col represent the top left pixel of canvas where the item (the item's top left 0,0 pixel) should be placed. Canvas and item are 2D images of RGB pixels. This function should assume that the canvas image is large enough to contain the item img in the row col indicated; row and col do NOT need to be validated. 

5. distributeItems(canvas, item, n) - Draws the item onto the Canvas n times in random locations. Overlapping item images  is OK.

#Language Learning App

The app will first show a menu to the user to choose if they want to Learn, Play, or change Settings.

menu_descrip.JPG
 

The items (words) that the app will teach the user in this game are listed in a provided blackfoot.csv file, included in the the Starter Kit below. Some examples: apples, bread, burger, child, coffee, tipi, etc. Your application must first read this .csv file containing all possible items/words. Separate files for each item corresponding to their image (.png) and sound (.wav) are also provided. The names of these files are the same as each word, with the corresponding extension. Note: When marking, slightly different files may be used, but will have the same characteristics. Hence, you should not hardcode any of the words nor file names, but rather use the items names in the .csv file.

The app should use this list of words and the provided image and sound files to implement the following parts of the application.

1. Learn. Displays each item image to be learned randomly on the canvas, and plays the sound of the corresponding word. The user presses enter to continue to the next item to be learned. When the program first starts, only the first 3 items in the .csv file are taught to the user (and their corresponding image and sound are shown and played respectively). The user can change this number in the Settings menu, up to the number of items in the .csv  and at least 3.

2. Play. This is a seek-and-count game, where the user has to listen to a word, and count how many of that item are in the image.

First, the user can specify how many rounds they’d like to play. Then, for each round, the program must:

Create a challenge list of 3 words from the list of items (the list of items being only the words currently being learned, i.e. either 3 or what the user indicated in settings). You must ensure that the same word is not repeated in this list of 3 randomly chosen words. You can explore the random.shuffle() function.

For each item in the challenge list, choose a random number n between 1 and 4, and display n of that item to the canvas. 
Your program should first recolor the image, then randomly decide to minify (or not), and mirror the item (or not) before drawing it to the screen.  All images for the item will have the same property. For example, if a randomly chosen item is orange and the number randomly chosen is 3, and it is randomly decided to minify, all 3 of the oranges should be half sized on the canvas. One specific item (e.g. oranges) may have more than one image processing applied before placing all copies in the canvas; i.e. if oranges are minimized, they may also be mirrored, although all n copies would have the same processing.

Ask the user how many of the items they found. If they enter the number correctly, then a message confirming that it is correct should be printed to the user, otherwise inform that it is incorrect. 

To play audio, call the function provided playSound(soundfile,env) (The function is included in the Started Kit code, in the main file). Depending on your coding environment, the implementation of this function will differ and it will depend on the ENV variable. 

3. Settings. By default, the player learns 3 words. They can change the number of words to learn and or to play using the Settings option  in this menu. The application should NOT allow the user to change the number of words to less than 3 or more than the number of words in the blackfoot.csv file.
4. 



