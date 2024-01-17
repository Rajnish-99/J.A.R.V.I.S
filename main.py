import speech_recognition as sr
import os
import webbrowser


def say(text):
    os.system(f"say {text}")

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # r.pause_threshold = 1
        audio = r.listen(source)
        try:
            print("Recognizing")
            query = r.recognize_google(audio, language = "en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "Some Error Occured . Sorry from Jarvis"



say("Hello i am jarvis")
while True:
    print("Listening")
    query = take_command()
    sites = [["youtube", "https://www.youtube.com"], ["wikipedia", "https://www.wikipedia.com"],["google", "https://www.google.com"]]
    for site in sites:

        if f"open {site[0]}".lower() in query.lower():
            say(f"Opening {site[0]} Sir..")
            webbrowser.open(site[1])

    import platform
    import subprocess

    system_platform = platform.system()

    if "open music" in query:
        music_path = "/Users/rajnishranjan/Downloads/better-day-186374.mp3"

        if system_platform == "Windows":
            os.startfile(music_path)
        elif system_platform == "Darwin":  # macOS
            subprocess.call(["open", music_path])
        elif system_platform == "Linux":
            subprocess.call(["xdg-open", music_path])

    if "open facetime".lower() in query.lower():
        face_path = "/System/Applications/FaceTime.app"
        if system_platform == "Darwin":
            subprocess.call(["open", face_path])

# start from 45 minutes again
    # say(query)