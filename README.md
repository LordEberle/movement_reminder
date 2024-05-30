# Movement Reminder Application

This is a simple movement reminder application that notifies you to stand up, move around, and sit down again at regular intervals. It uses the `tkinter` library for the GUI and the `win10toast` library for the notifications.

## Features

- **Start Reminders**: Begin receiving notifications to stand up, move, and sit down at specified intervals.
- **Stop Reminders**: Stop the notifications at any time.
- **Notifications**: Display notifications that automatically close after 5 seconds and do not produce any sound.

## Documentation
### Installation
pip install win10toast

Place the run_reminder.bat in the Autostart Folder C:\Users\ <Username>\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup if you want to autostart the app with windows

### Usage
Run the application:

python reminder.py
Graphical User Interface:

A window will appear with a "Start Reminders" button and a "Stop Reminders" button.
Click "Start Reminders" to begin receiving notifications.
Click "Stop Reminders" to stop receiving notifications.


### Code Description
reminder.py
The reminder.py script consists of the following main components:

Import Libraries:

tkinter for the GUI
win10toast for Windows toast notifications
time and threading for managing notification intervals
Notification Functions:

remind_to_stand_up(toaster): Displays a notification to stand up and stretch.
remind_to_move(toaster): Displays a notification to take a movement break.
remind_to_sit_down(toaster): Displays a notification to sit down.
ReminderThread Class:

Inherits from threading.Thread and manages the notification timings.
Contains methods to start and stop the reminder thread.
ReminderApp Class:

Manages the GUI using tkinter.
Contains methods to start and stop the reminder thread via GUI buttons.
Places the window in the upper right corner of the screen.
Main Execution:

Initializes and runs the tkinter main loop.


## Contributing
Contributions are welcome! Please feel free to submit a Pull Request or open an issue.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
