import tkinter as tk
import time
import math


class AnalogClock(tk.Canvas):
    def __init__(self, master=None):
        tk.Canvas.__init__(self, master)
        self.master = master
        self.pack(fill=tk.BOTH, expand=1)
        self.center_x = 200
        self.center_y = 200
        self.clock_radius = 190
        self.create_oval(
            self.center_x - self.clock_radius,
            self.center_y - self.clock_radius,
            self.center_x + self.clock_radius,
            self.center_y + self.clock_radius,
            outline="black",
            width=4,
        )
        self.draw_clock_face()
        self.update_clock()

    def draw_clock_face(self):
        for i in range(60):
            angle = math.pi / 2 - (2 * math.pi * i / 60)
            x_inner = self.center_x + (self.clock_radius - 10) * math.cos(angle)
            y_inner = self.center_y - (self.clock_radius - 10) * math.sin(angle)
            if i % 5 == 0:
                x_outer = self.center_x + self.clock_radius * math.cos(angle)
                y_outer = self.center_y - self.clock_radius * math.sin(angle)
                self.create_line(
                    x_inner, y_inner, x_outer, y_outer, fill="black", width=3
                )
                # Numeracja godzinowa
                hour = i // 5 if i // 5 != 0 else 12
                x_text = self.center_x + (self.clock_radius - 30) * math.cos(angle)
                y_text = self.center_y - (self.clock_radius - 30) * math.sin(angle)
                self.create_text(
                    x_text, y_text, text=str(hour), font=("Arial", 14, "bold")
                )
            else:
                x_outer = self.center_x + (self.clock_radius - 5) * math.cos(angle)
                y_outer = self.center_y - (self.clock_radius - 5) * math.sin(angle)
                self.create_line(
                    x_inner, y_inner, x_outer, y_outer, fill="black", width=1
                )

    def update_clock(self):
        self.delete("hands")

        # Get current time
        current_time = time.localtime()
        hours = current_time.tm_hour % 12
        minutes = current_time.tm_min
        seconds = current_time.tm_sec

        # Draw the hour hand
        hour_angle = math.pi / 2 - (
            2 * math.pi * hours / 12 + 2 * math.pi * minutes / (12 * 60)
        )
        hour_hand_length = self.clock_radius * 0.5
        hour_x = self.center_x + hour_hand_length * math.cos(hour_angle)
        hour_y = self.center_y - hour_hand_length * math.sin(hour_angle)
        self.create_line(
            self.center_x,
            self.center_y,
            hour_x,
            hour_y,
            fill="black",
            width=6,
            tags="hands",
        )

        # Draw the minute hand
        minute_angle = math.pi / 2 - (2 * math.pi * minutes / 60)
        minute_hand_length = self.clock_radius * 0.75
        minute_x = self.center_x + minute_hand_length * math.cos(minute_angle)
        minute_y = self.center_y - minute_hand_length * math.sin(minute_angle)
        self.create_line(
            self.center_x,
            self.center_y,
            minute_x,
            minute_y,
            fill="blue",
            width=4,
            tags="hands",
        )

        # Draw the second hand
        second_angle = math.pi / 2 - (2 * math.pi * seconds / 60)
        second_hand_length = self.clock_radius * 0.9
        second_x = self.center_x + second_hand_length * math.cos(second_angle)
        second_y = self.center_y - second_hand_length * math.sin(second_angle)
        self.create_line(
            self.center_x,
            self.center_y,
            second_x,
            second_y,
            fill="red",
            width=2,
            tags="hands",
        )

        # Redraw every 1000 ms (1 second)
        self.after(1000, self.update_clock)


def main():
    root = tk.Tk()
    root.title("Analog Clock")
    root.geometry("400x400")
    clock = AnalogClock(master=root)
    root.mainloop()


if __name__ == "__main__":
    main()
