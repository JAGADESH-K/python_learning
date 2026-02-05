import winsound
import time

def countdown_timer(seconds):
    for sec in range(seconds, 0, -1):
        mins, secs = divmod(sec, 60)
        time_format = f"{mins:02} :{secs:02}"
        print(f"Time remaining {time_format}", end='\r')
        time.sleep(1)
    winsound.Beep(1000,1000)
    
    return "\nTime is up!!"

while True:
    try:
        seconds = int(input("Enter the time in seconds: "))
        if seconds < 1:
            print("Value must be grater then 1 ")
            continue
        else: break
    except ValueError:
        print("Enter a valid seconds in number. ")

timer = countdown_timer(seconds)

print(timer)

