from datetime import datetime, time

def main():
    time_format = "%H:%M"

    full_current_time = datetime.now()
    current_time = full_current_time.strftime(time_format)
    print(current_time)

if __name__ == "__main__":
    main()

