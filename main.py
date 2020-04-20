import win32com.client as wc
speak = wc.Dispatch("Sapi.SpVoice")

say = speak.speak

def testing():
    say("testing...")
    say("so far so good!")

def start():
    say("Welcome... Choose a door to begin! (1, 2 or 3)")
    door = input("door: ")

    if door == "1":
        say("Great, door 1 it is!")
        say("In this door, there is a lion that is so hungry. he hasent eaten in 1000 years. would you like to turn back or keep going?")
        dire = input("b\\f")

        if dire == ("b"):
            say("ok, choose a door! 2 or 3.")


start()