from time import time
import random as ra
import re

def mistake(partest, usertest):
    errors = 0
    for i in range(len(partest)):
        try:
            if partest[i] != usertest[i]:
                errors += 1
        except:
            errors += 1
    return errors

def calculate_wpm(time_taken, userinput):
    words_typed = len(re.findall(r'\S+', userinput))
    wpm = (words_typed / time_taken) * 60
    return round(wpm)

if __name__ == '__main__':
    while True:
        ck = input("Ready to test: yes/no: ")
        if ck == "yes":
            test = [
                "The dog chased the cat across the street, its tail wagging furiously and its tongue lolling out of its mouth.",
                "The old man sat on the bench and watched the children play, a smile on his face as he remembered his own childhood.",
                "The woman in the red dress walked down the street, her high heels clicking on the pavement and her long hair flowing in the wind.",
                "The car drove past the house with the broken window, its tires squealing as it skidded to a stop.",
                "The bird flew into the tree and sang a beautiful song, its feathers glinting in the sunlight and its wings flapping gracefully.",
                "The fish swam in the clear water, its fins rippling and its tail wagging back and forth.",
                "The sun shone brightly in the sky, its rays warming the earth and its heat beating down on the ground.",
                "The clouds were white and fluffy, like cotton candy floating in the sky.",
                "The rain fell gently on the ground, its drops like tears falling from heaven.",
                "The wind blew through the trees, its branches swaying and its leaves rustling.",
                "The flowers bloomed in the garden, their petals like stars and their fragrance filling the air.",
                "The bees buzzed around the flowers, their wings a blur and their pollen-covered legs carrying the sweet nectar back to their hives.",
                "The children played in the park, their laughter ringing out and their joy contagious.",
                "The dog barked at the cat, its teeth bared and its hackles raised.",
                "The cat hissed at the dog, its fur bristling and its tail lashing back and forth.",
                "The man ate a sandwich, his mouth full and his eyes closed in satisfaction.",
                "The woman drank a glass of water, her throat parched and her lips dry.",
                "The child ate a cookie, its crumbs falling to the ground and its cheeks covered in chocolate.",
                "The baby cried, its wails piercing and its face red and blotchy.",
                "The teacher taught the students, her voice clear and concise and her enthusiasm infectious."
            ]

            test1 = ra.choice(test)
            print("***** Typing Speed Test *****")
            print(test1)
            print()

            time_start = time()
            test_input = input("Enter: ")
            time_end = time()

            time_taken = time_end - time_start
            wpm = calculate_wpm(time_taken, test_input)
            errors = mistake(test1, test_input)

            print('Speed:', wpm, 'WPM')
            print('Errors:', errors)
        elif ck == 'no':
            print("Thank you")
            break
        else:
            print("Wrong input")
