import serial
import pyttsx3
import time

# --- SERIAL SETUP ---
ser = serial.Serial('/dev/cu.usbserial-1140', 9600)

# --- PYTTSX3 SETUP ---
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[5].id)  # Aman voice
engine.setProperty('rate', 165)            # Speed of speech
engine.setProperty('volume', 1.0)          # Max volume

# --- SPEAK FUNCTION ---
def speak(message):
    print("Speaking:", message)
    engine.say(message)
    engine.runAndWait()

# --- MAIN LOOP ---
while True:
    if ser.in_waiting > 0:
        data = ser.readline().decode().strip()

        if data == "MEDICINE":
            speak("I need medicine, please help me.")
        elif data == "DOCTOR":
            speak("Please call the doctor immediately.")
        elif data == "PAIN":
            speak("I am in pain, please help me.")
        elif data == "FAMILY":
            speak("Please call my family.")
        
        time.sleep(0.5)