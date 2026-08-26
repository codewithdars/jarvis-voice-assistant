import speech_recognition as sr
import webbrowser
import pyttsx3
import time
import musicLibrary


# ------- SPEAK 

def speak(text):
    print("jarvis:", text)

    engine = pyttsx3.init()
    engine.setProperty("rate", 165)
    engine.setProperty("volume", 1.0)

    engine.say(text)
    engine.runAndWait()
    engine.stop()


# ---- COMMANDS 

def process_command(command):

    command = command.lower()

    if "open google" in command:
        speak("Opening Google")
        webbrowser.open("https://google.com")

    elif "open youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://youtube.com")

    elif "open instagram" in command:
        speak("Opening Instagram")
        webbrowser.open("https://instagram.com")

    elif "open facebook" in command:
        speak("Opening Facebook")
        webbrowser.open("https://facebook.com")

    elif "open linkedin" in command:
        speak("Opening LinkedIn")
        webbrowser.open("https://linkedin.com")

    elif "exit" in command or "quit" in command:
        speak("Goodbye sir")

    elif"cricbuzz" in command:
        speak("Opening cricbuzz")
        webbrowser.open("https://www.cricbuzz.com/")

    # elif c.lower().startswith("play"):
    #     song = c.lower().split[1]
    #     link = musicLibrary.music[song]
    #     webbrowser.open(link)
    elif command.lower().startswith("play"):

        song = command.lower().split(" ", 1)[1]

        if song in musicLibrary.music:
            speak(f"Playing {song}")
            link = musicLibrary.music[song]
            webbrowser.open(link)

        else:
            speak("Sorry, this song is not in my library.")
            return False

    else:
        speak("I don't understand that command")

    return True


# ----- MAIN 

if __name__ == "__main__":

    speak("Initializing jarvis")

    recognizer = sr.Recognizer()

    running = True

    while running:

        try:

            # === LISTEN FOR JARVIS

            with sr.Microphone() as source:

                print("\nListening for jarvis...")

                audio = recognizer.listen(
                    source,
                    timeout=5,
                    phrase_time_limit=3
                )

            word = recognizer.recognize_google(audio)

            print("You said:", word)

            # == WAKE WORD

            if "jarvis" in word.lower():

                speak("Yeah, how can I help you?")

                # IMPORTANT
                time.sleep(1)

                # === LISTEN FOR COMMAND 

                with sr.Microphone() as source:

                    print("Listening for command...")

                    audio = recognizer.listen(
                        source,
                        timeout=5,
                        phrase_time_limit=5
                    )

                command = recognizer.recognize_google(audio)

                print("Command:", command)

                running = process_command(command)


        except sr.WaitTimeoutError:

            print("No speech detected.")

        except sr.UnknownValueError:

            print("Could not understand.")

        except sr.RequestError:

            print("Google speech service unavailable.")

        except KeyboardInterrupt:

            speak("Goodbye.")
            break