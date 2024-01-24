import speech_recognition as sr
import os
import webbrowser
import platform
import subprocess
import random

from openai import OpenAI
from config import apikey
client = OpenAI(api_key=apikey)


# def ai(prompt):
#     text = f"Openai response for prompt: {prompt}\n ******* \n\n"
#
#     response = client.completions.create(
#         model="gpt-3.5-turbo-instruct",
#         prompt=prompt,
#         temperature=1,
#         max_tokens=256,
#         top_p=1,
#         frequency_penalty=0,
#         presence_penalty=0
#     )
#
#     text += response["choices"][0]["text"]
#
#     if not os.path.exists("Openai"):
#         os.mkdir("Openai")
#
#
#     with open(f"Openai/prompt- {random.randint(1,23256327635)}", "w") as f:
#         f.write(text)

def ai(prompt):
    text = f"Openai response for prompt: {prompt}\n ******* \n\n"

    response = client.completions.create(
        model="gpt-3.5-turbo-instruct",
        prompt=prompt,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    # the response from the open ai is a object not a dictionary
    text += response.choices[0].text

    if not os.path.exists("Openai"):
        os.mkdir("Openai")

    with open(f"Openai/prompt- {random.randint(1, 23256327635)}", "w") as f:
        f.write(text)




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


    if "using artificial intelligence".lower() in query.lower():
        ai(prompt=query)

# start from 45 minutes again
    # say(query)