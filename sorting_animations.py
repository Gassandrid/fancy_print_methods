from time import sleep
import random

def shuffle_sort_anim(string, speed):
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
    shuffle_sort_anim(input_string, speed)