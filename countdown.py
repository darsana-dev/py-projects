import time

def countdown(minutes):
    seconds = minutes * 60
    while seconds:
        mins, secs = divmod(seconds, 60)
        print(f"{mins:02}:{secs:02}", end='\r')
        time.sleep(1)
        seconds -= 1
    print(" Time's up!")

countdown(1)  # 1-minute timer