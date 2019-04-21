#Task 6
x=input("Enter a string to speak or press x to exit=")
i=0
while(i!=1):
    import pyttsx3
    engine=pyttsx3.init()
    engine.say(x)
    engine.runAndWait()
    x=input("Enter a string to speak or press x to exit=")
    if x=="x":
        break
    