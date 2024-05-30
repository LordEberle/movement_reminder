import time
import threading
from win10toast import ToastNotifier
import tkinter as tk

# Function to display the reminder messages
def remind_to_stand_up(toaster):
    toaster.show_toast("Reminder", "Time to stand up and stretch!", duration=5, threaded=True)

def remind_to_move(toaster):
    toaster.show_toast("Reminder", "Time for a movement break!", duration=5, threaded=True)

def remind_to_sit_down(toaster):
    toaster.show_toast("Reminder", "You can sit down now.", duration=5, threaded=True)

# Class to manage the reminder thread
class ReminderThread(threading.Thread):
    def __init__(self):
        super().__init__()
        self.running = threading.Event()
        self.running.set()
        self.toaster = ToastNotifier()
        self.daemon = True

    def run(self):
        while self.running.is_set():
            time.sleep(2400)  # 40 minutes
            if not self.running.is_set():
                break
            remind_to_stand_up(self.toaster)
            time.sleep(600)  # 10 minutes
            if not self.running.is_set():
                break
            remind_to_move(self.toaster)
            time.sleep(300)  # 5 minutes
            if not self.running.is_set():
                break
            remind_to_sit_down(self.toaster)

    def stop(self):
        self.running.clear()

# Main GUI application
class ReminderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Movement Reminder")

        # Get screen width and height
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Window size
        window_width = 300
        window_height = 150

        # Calculate x and y coordinates for the window
        x = screen_width - window_width
        y = 0

        # Set the geometry of the window
        self.root.geometry(f"{window_width}x{window_height}+{x}+{y}")

        self.label = tk.Label(root, text="Movement Reminder is running...", font=("Helvetica", 16))
        self.label.pack(pady=20)

        self.start_button = tk.Button(root, text="Start Reminders", command=self.start_reminder_thread)
        self.start_button.pack(pady=10)

        self.stop_button = tk.Button(root, text="Stop Reminders", command=self.stop_reminder_thread)
        self.stop_button.pack(pady=10)

        self.reminder_thread = None

    def start_reminder_thread(self):
        if self.reminder_thread is None or not self.reminder_thread.is_alive():
            self.reminder_thread = ReminderThread()
            self.reminder_thread.start()

    def stop_reminder_thread(self):
        if self.reminder_thread is not None:
            self.reminder_thread.stop()
            self.reminder_thread = None

if __name__ == "__main__":
    root = tk.Tk()
    app = ReminderApp(root)
    root.mainloop()
