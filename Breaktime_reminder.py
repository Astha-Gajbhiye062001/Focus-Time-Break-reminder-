import time, random, ctypes

quotes = [
    "Take a deep breath and stretch",
    "Sometimes the most productive thing you can do is take a break",
    "You deserve a break today",
    "Move around a little"
]

def remind():
    message = random.choice(quotes)
    ctypes.windll.user32.MessageBoxW(0, message, "FocusTime Reminder", 1)

print("FocusTime running... (Press CTRL+C to stop)")
try:
    while True:
        time.sleep(10)  # remind  me every 10 sec
        remind()
except KeyboardInterrupt:
    print("\nFocusTime stopped.")
