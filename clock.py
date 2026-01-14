import tkinter as tk
from time import strftime
import requests

# Global variables
USE_24_HOUR = True
CURRENT_THEME = "Matrix"
ALWAYS_ON_TOP = True

THEMES = {
    "Matrix": {"bg": "black", "fg": "#00ff00"},
    "Neon Purple": {"bg": "#0d001a", "fg": "#d000ff"},
    "Ocean": {"bg": "#001a33", "fg": "#00ccff"},
    "Light": {"bg": "#f0f0f0", "fg": "#000000"}
}

# Window setup
root = tk.Tk()
root.title("Advanced Digital Clock by Sayur")
root.configure(bg=THEMES[CURRENT_THEME]["bg"])
root.geometry("800x500")
root.resizable(False, False)
root.attributes("-topmost", ALWAYS_ON_TOP)

# Time display
time_label = tk.Label(root, font=('Helvetica', 80, 'bold'),
                      bg=THEMES[CURRENT_THEME]["bg"],
                      fg=THEMES[CURRENT_THEME]["fg"])
time_label.pack(anchor='center', pady=40)

# Date display
date_label = tk.Label(root, font=('Helvetica', 28),
                      bg=THEMES[CURRENT_THEME]["bg"],
                      fg=THEMES[CURRENT_THEME]["fg"])
date_label.pack(anchor='center')

# Weather display
weather_label = tk.Label(root, font=('Helvetica', 24),
                         bg=THEMES[CURRENT_THEME]["bg"],
                         fg=THEMES[CURRENT_THEME]["fg"])
weather_label.pack(pady=20)

# Control buttons frame
controls = tk.Frame(root, bg=THEMES[CURRENT_THEME]["bg"])
controls.pack(pady=30)

# 24/12 hour toggle
format_btn = tk.Button(controls, text="24h", width=10, font=('Helvetica', 12),
                       bg="#444444", fg="white",
                       command=lambda: [globals().__setitem__('USE_24_HOUR', not USE_24_HOUR),
                                        format_btn.config(text="24h" if USE_24_HOUR else "12h")])
format_btn.pack(side="left", padx=10)

# Always on top toggle
ontop_btn = tk.Button(controls, text="On Top: ON", width=12, font=('Helvetica', 12),
                      bg="#444444", fg="white",
                      command=lambda: [globals().__setitem__('ALWAYS_ON_TOP', not ALWAYS_ON_TOP),
                                       root.attributes("-topmost", ALWAYS_ON_TOP),
                                       ontop_btn.config(text="On Top: ON" if ALWAYS_ON_TOP else "On Top: OFF")])
ontop_btn.pack(side="left", padx=10)

# Theme buttons
for theme_name in THEMES:
    tk.Button(controls, text=theme_name, width=12, font=('Helvetica', 12),
              bg="#444444", fg="white",
              command=lambda t=theme_name: change_theme(t)).pack(side="left", padx=5)

# ────────────────────────────── FUNCTIONS ──────────────────────────────

def change_theme(theme):
    global CURRENT_THEME
    CURRENT_THEME = theme
    bg = THEMES[theme]["bg"]
    fg = THEMES[theme]["fg"]
    root.configure(bg=bg)
    time_label.config(bg=bg, fg=fg)
    date_label.config(bg=bg, fg=fg)
    weather_label.config(bg=bg, fg=fg)
    controls.config(bg=bg)

def update_time():
    time_str = strftime('%H:%M:%S') if USE_24_HOUR else strftime('%I:%M:%S %p')
    date_str = strftime('%A, %d %B %Y')
    time_label.config(text=time_str)
    date_label.config(text=date_str)
    root.after(1000, update_time)

def update_weather():
    try:
        url = "https://api.open-meteo.com/v1/forecast?latitude=21.15&longitude=79.09&current_weather=true"
        r = requests.get(url, timeout=5)
        temp = r.json()['current_weather']['temperature']
        weather_label.config(text=f"Nagpur: {temp}°C")
    except:
        weather_label.config(text="Weather unavailable")
    root.after(600000, update_weather)  # 10 min

# Start everything
update_time()
update_weather()

root.mainloop()
