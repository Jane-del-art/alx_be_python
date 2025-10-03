from datetime import datetime, timedelta

def display_current_datetime():
    # Save current date and time in variable
    current_date = datetime.now()
    # Format as "YYYY-MM-DD HH:MM:SS"
    print("Current date and time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))
    return current_date

def calculate_future_date(current_date):
    try:
        days = int(input("Enter the number of days to add to the current date: "))
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return
    # Calculate future date
    future_date = current_date + timedelta(days=days)
    print("Future date:", future_date.strftime("%Y-%m-%d"))
    return future_date

if __name__ == "__main__":
    current_date = display_current_datetime()
    calculate_future_date(current_date)
