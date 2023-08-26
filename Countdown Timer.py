import time

def countdown_timer(seconds):
    while seconds > 0:
        print(f"Time remaining: {seconds} seconds")
        time.sleep(1)
        seconds -= 1
    print("Time's up!")

countdown = int(input("Enter countdown duration (seconds): "))
countdown_timer(countdown)
