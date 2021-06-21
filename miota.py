import pyttsx3
def hola(nombre,te_amo):
    print(f"Hello {nombre} I love you so much")
    if te_amo == "a lot":
        print(f"I adore you {te_amo}")
        pyttsx3.speak("hello")
        pyttsx3.speak(nombre)
        pyttsx3.speak("I love you so much")
        pyttsx3.speak(te_amo)
hola("miota","a lot")
