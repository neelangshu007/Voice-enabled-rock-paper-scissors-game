import pyttsx3  # windows API text to speak module(sapi5 API) it uses the voices that are present inside the windows
from gtts import gTTS  # Google Text To Speech, for converting the given text to speech
import os  # to save/open files
import playsound  # to play saved mp3 file
import speech_recognition as sr  # for recognizing the voice command and converting to text
import random  # to get random element from list using random.choice()

# num = 1

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
# print(voices[0].id)
engine.setProperty("voice", voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


# def speak(audio):
#     global num
#     num += 1
#     engine = gTTS(text=audio, lang="en", slow=False)
#     file = str(num)+".mp3"
#     engine.save(file)
#     playsound.playsound(file, True)
#     os.remove(file)


def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening........")
        r.pause_threshold = 1
        r.energy_threshold = 6500
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        print("Recognizing.......")
        command = r.recognize_google(audio, language='en-in')
        #         print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Could not understand your audio, lets try again !")
        speak("Could not understand your audio, lets try again !")
        return "None"
    return command


if __name__ == '__main__':

    speak("Welcome to the Game of Rock Paper Scissor!")
    print("Welcome to the Game of Rock Paper Scissor!")
    choice_list = ["rock", "paper", "scissor"]
    computer_score = 0
    player_score = 0
    count_down = 0

    while True:

        print("Rock Paper Scissor Shoot! \n")
        speak("Rock Paper Scissor Shoot!")
        computer_move = random.choice(choice_list)
        player_move = take_command().lower()

        if player_move == 'rock' and computer_move == 'scissor':
            speak(computer_move)
            print(f"Player Move:{player_move}\nComputer Move:{computer_move}\n")
            player_score += 1
            count_down += 1
            print(f"Player Score:{player_score}\nComputer Score:{computer_score}\n")

        elif player_move == 'rock' and computer_move == 'paper':
            speak(computer_move)
            print(f"Player Move:{player_move}\nComputer Move:{computer_move}\n")
            computer_score += 1
            count_down += 1
            print(f"Player Score:{player_score}\nComputer Score:{computer_score}\n")

        elif player_move == 'rock' and computer_move == 'rock':
            speak(computer_move)
            print(f"Player Move:{player_move}\nComputer Move:{computer_move}\n")
            count_down += 1
            print(f"Player Score:{player_score}\nComputer Score:{computer_score}\n")

        elif player_move == 'paper' and computer_move == 'rock':
            speak(computer_move)
            print(f"Player Move:{player_move}\nComputer Move:{computer_move}\n")
            player_score += 1
            count_down += 1
            print(f"Player Score:{player_score}\nComputer Score:{computer_score}\n")

        elif player_move == 'paper' and computer_move == 'paper':
            speak(computer_move)
            print(f"Player Move:{player_move}\nComputer Move:{computer_move}\n")
            count_down += 1
            print(f"Player Score:{player_score}\nComputer Score:{computer_score}\n")

        elif player_move == 'paper' and computer_move == 'scissor':
            speak(computer_move)
            print(f"Player Move:{player_move}\nComputer Move:{computer_move}\n")
            computer_score += 1
            count_down += 1
            print(f"Player Score:{player_score}\nComputer Score:{computer_score}\n")

        elif player_move == 'scissor' and computer_move == 'rock':
            speak(computer_move)
            print(f"Player Move:{player_move}\nComputer Move:{computer_move}\n")
            computer_score += 1
            count_down += 1
            print(f"Player Score:{player_score}\nComputer Score:{computer_score}\n")

        elif player_move == 'scissor' and computer_move == 'paper':
            speak(computer_move)
            print(f"Player Move:{player_move}\nComputer Move:{computer_move}\n")
            player_score += 1
            count_down += 1
            print(f"Player Score:{player_score}\nComputer Score:{computer_score}\n")

        elif player_move == 'scissor' and computer_move == 'scissors':
            speak(computer_move)
            print(f"Player Move:{player_move}\nComputer Move:{computer_move}\n")
            count_down += 1
            print(f"Player Score:{player_score}\nComputer Score:{computer_score}\n")

        else:
            print(player_move)
            if player_move != "none":
                speak("Could not understand your audio lets try again!")
                print("Could not understand your audio lets try again!")


        if count_down == 3:
            print(f"Count:{count_down}")
            if computer_score > player_score:
                print("Computer wins!")
                speak("Computer wins!")
                print(f"Computer score:{computer_score}\nPlayer score:{player_score}\n")
                break
            elif player_score > computer_score:
                print("Player wins!")
                speak("Player wins!")
                print(f"Player score:{player_score}\nComputer score:{computer_score}\n")
                break
            elif player_score == computer_score:
                print("Match Draw!")
                speak("Match Draw!")
                print(f"Player score:{player_score}\nComputer score:{computer_score}\n")
                break






