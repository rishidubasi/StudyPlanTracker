import matplotlib.pyplot as plt

total_days = 7
total_study_hours = 36
daily_study_hours = []

# update the remaining study hours and calculate the new daily goal
def update_study_plan(daily_hours, total_study_hours, days_left):
    total_study_hours -= sum(daily_hours)
    days_left -= len(daily_hours)
    if days_left > 0:
        new_daily_goal = total_study_hours / days_left
    else:
        new_daily_goal = 0
    return total_study_hours, new_daily_goal

#plot the study progress
def plot_study_progress(daily_hours, new_daily_goal, days_left):
    plt.figure(figsize=(10, 5))
    plt.plot(range(1, len(daily_hours) + 1), daily_hours, label='Actual Study Hours', marker='o')
    plt.axhline(y=new_daily_goal, color='y', linestyle='--', label=f'Required Daily Hours: {new_daily_goal:.2f}')
    plt.xlabel('Days')
    plt.ylabel('Hours')
    plt.title('Study Plan Progress')
    plt.legend()
    plt.grid(True)
    plt.show()

# collect daily study hours input and update the study plan
remaining_study_hours = total_study_hours
remaining_days = total_days

while remaining_days > 0:
    try:
        today_hours = float(input("Enter study hours for today: "))
        if today_hours < 0 or today_hours > 24:
            print("Please enter a valid number of hours (0-24).")
            continue
        daily_study_hours.append(today_hours)
        remaining_study_hours, new_daily_goal = update_study_plan(daily_study_hours, total_study_hours, total_days)
        remaining_days -= 1
        plot_study_progress(daily_study_hours, new_daily_goal, remaining_days)

        print(f"Remaining Study Hours: {remaining_study_hours:.2f}")
        print(f"Remaining Days: {remaining_days}")
        print(f"New Daily Study Goal: {new_daily_goal:.2f} hours/day")

        if remaining_days == 0 or remaining_study_hours <= 0:
            break
    except ValueError:
        print("Please enter a valid number of hours.")

print("Study plan completed or total required hours achieved!")
