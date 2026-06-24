import random
import datetime
import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init()
engine.setProperty("rate", 170)   
engine.setProperty("volume", 1.0)  


def speak(text):
    """Convert text to audible speech and print it for reference."""
    print(f"Assistant: {text}")
    engine.say(text)
    engine.runAndWait()


recognizer = sr.Recognizer()


def listen():
    """Capture audio from the microphone and convert it to text."""
    with sr.Microphone() as source:
        print("\nListening... (speak now)")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=6)
        except sr.WaitTimeoutError:
            return ""

    try:
        text = recognizer.recognize_google(audio)
        print(f"You said: {text}")
        return text.lower()
    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that. Could you repeat?")
        return ""
    except sr.RequestError:
        speak("Speech recognition service is unavailable right now.")
        return ""



def tell_time():
    now = datetime.datetime.now().strftime("%I:%M %p")
    speak(f"The current time is {now}")


def tell_date():
    today = datetime.datetime.now().strftime("%B %d, %Y")
    speak(f"Today's date is {today}")


def tell_joke():
    jokes = [
        "Why do programmers prefer dark mode? Because light attracts bugs.",
        "Why did the computer go to therapy? It had too many unresolved issues.",
        "I told my computer I needed a break, and it said no problem, it'll go to sleep.",
    ]
    speak(random.choice(jokes))


def greet():
    speak("Hello! I'm your voice assistant. How can I help you today?")


def say_goodbye():
    speak("Goodbye! Have a great day.")



COMMANDS = {
    "what time is it": tell_time,
    "tell me the time": tell_time,
    "what's the date": tell_date,
    "what is the date": tell_date,
    "tell me a joke": tell_joke,
    "joke": tell_joke,
    "hello": greet,
    "hi": greet,
    "bye": say_goodbye,
    "goodbye": say_goodbye,
    "exit": say_goodbye,
}


def handle_command(text):
    """Match recognized text against known commands."""
    if not text:
        return True  

    for phrase, action in COMMANDS.items():
        if phrase in text:
            action()
            if action == say_goodbye:
                return False  
            return True

    speak("I don't recognize that command yet. Try asking the time or for a joke.")
    return True


def main():
    speak("Voice assistant is starting. Say 'hello' to begin, or 'exit' to quit.")
    running = True
    while running:
        text = listen()
        running = handle_command(text)


if __name__ == "__main__":
    main()