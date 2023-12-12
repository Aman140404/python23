import tkinter as tk
import datetime
import time

# Create the main window.
root = tk.Tk()
root.title("Alarm Clock")

# Create the labels and entry widgets.
hour_label = tk.Label(root, text="Hour:")
hour_entry = tk.Entry(root)

minute_label = tk.Label(root, text="Minute:")
minute_entry = tk.Entry(root)

# Create the set alarm button.
set_alarm_button = tk.Button(root, text="Set Alarm", command=lambda: set_alarm(
    hour_entry.get(), minute_entry.get()))

# Pack the widgets.
hour_label.pack(side=tk.TOP, anchor="w")
hour_entry.pack(side=tk.TOP, anchor="e")

minute_label.pack(side=tk.TOP, anchor="w")
minute_entry.pack(side=tk.TOP, anchor="e")

set_alarm_button.pack(side=tk.BOTTOM)

# Start the main loop.
root.mainloop()

# Define the set_alarm function.


def set_alarm(hour, minute):
    # Get the current time.
    current_time = datetime.datetime.now()

    # Calculate the time until the alarm goes off.
    alarm_time = datetime.datetime(
        current_time.year, current_time.month, current_time.day, int(hour), int(minute))

    # Create a while loop to wait for the alarm time to arrive.
    while True:
        # Get the current time.
        current_time = datetime.datetime.now()

        # If the current time is equal to the alarm time, play a sound and break out of the loop.
        if current_time == alarm_time:
            winsound.PlaySound("dingdong.wav", winsound.SND_ASYNC)
            break

        # Sleep for 1 second.
        time.sleep(1)
