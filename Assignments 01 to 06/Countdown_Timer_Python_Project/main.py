import time

def start_timer(duration):
    while duration > 0:
        minutes, seconds = divmod(duration, 60) 
        timer_display = f'{minutes:02}:{seconds:02}' 
        print(timer_display, end='\r') 
        time.sleep(1) 
        duration -= 1  

    print("Time's up! 🕒")

def prompt_for_time():
    while True:
        try:
            total_seconds = int(input("Please enter the time in seconds: "))
            if total_seconds <= 0:
                print("Time must be a positive integer! Try again.")
            else:
                return total_seconds
        except ValueError:
            print("Invalid input! Please provide a valid number.")
time_input = prompt_for_time()
start_timer(time_input)
