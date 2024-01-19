from time import sleep
import random

def procedural(string, speed):
    i = string
    o = "1234567890!@#$%^&*()_+abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ "
    a = ""
    b = ""

    for x in i:
        for y in o:
            b = a + y
            # alternative way to print
            print(b, end="\r", flush=True)
            # print(b, end="\r")
            # print(b, end="")
            # print(b)
            sleep(speed)
            if y == x:
                a = a + x

    return

def letter_cycle(string, speed):
    finalWord = string
    allChars = "1234567890!@#$%^&*()_+abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ "
    currentWord = "".join(random.choice(allChars) for _ in range(len(finalWord)))

    while currentWord != finalWord:
        for i in range(len(currentWord)):
            if currentWord[i] != finalWord[i]:
                if allChars.index(currentWord[i]) == len(allChars) - 1:
                    currentWord = currentWord[:i] + allChars[0] + currentWord[i+1:]
                else:
                    currentWord = currentWord[:i] + allChars[allChars.index(currentWord[i]) + 1] + currentWord[i+1:]
                print(currentWord, end="\r", flush=True)
                #alternative way to print
                # print(currentWord, end="\r")
                # print(currentWord, end="")
                # print(currentWord)
                sleep(speed)
            else:
                continue
    
    print(currentWord)
    return

def letter_sort(string, speed):
    finalWord = string
    scrambled = "".join(random.sample(finalWord, len(finalWord)))
    for i in range(len(finalWord)):
        while finalWord[i] != scrambled[i]:
            scrambled = scrambled[:i] + scrambled[i+1:] + scrambled[i]
            print(scrambled, end="\r", flush=True)
            sleep(speed)
    print(scrambled)
    return

        

if __name__ == "__main__":
    input_string = input("Enter a string: ")
    speed = float(input("Enter a speed: "))
    choice = int(input("Which print animation would you like to see? (procedural, letter_cycle, letter_sort)(1/2/3): "))
    if choice == 1:
        procedural(input_string, speed)
    elif choice == 2:
        letter_cycle(input_string, speed)
    elif choice == 3:
        letter_sort(input_string, speed)
    else:
        print("Invalid choice")
        exit(1)

