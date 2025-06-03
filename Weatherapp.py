import requests
import tkinter as tk
from tkinter import messagebox

# Replace with your actual OpenWeatherMap API key
API_KEY = "253100e2d00f918285428bc0091a95f8"

def get_weather():
    city = city_entry.get()
    if not city:
        messagebox.showwarning("Input Error", "Please enter a city name.")
        return

    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'imperial'
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()

        # Extract and display weather data
        city_name = data['name']
        country = data['sys']['country']
        temp = data['main']['temp']
        humidity = data['main']['humidity']
        description = data['weather'][0]['description'].capitalize()

        result = (
            f" Location: {city_name}, {country}\n"
            f"️ Temperature: {temp} °F\n"
            f" Humidity: {humidity}%\n"
            f" Description: {description}"
        )
        result_label.config(text=result)

    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", "Failed to retrieve data.")
    except KeyError:
        messagebox.showerror("Error", "City not found. Try again.")

# ---- Tkinter UI ----
root = tk.Tk()
root.title("Weather Checker")
root.geometry("350x300")

# Input Label + Entry
tk.Label(root, text="Enter City Name:", font=("Arial", 12)).pack(pady=10)
city_entry = tk.Entry(root, width=30, font=("Arial", 12))
city_entry.pack()

# Get Weather Button
tk.Button(root, text="Get Weather", command=get_weather, font=("Arial", 12)).pack(pady=10)

# Results Display
result_label = tk.Label(root, text="", font=("Arial", 11), justify="left")
result_label.pack(pady=20)

root.mainloop()
