import tkinter as tk
import requests
import json

def get_weather(city):
    api_key = "YOUR_API_KEY"  # Replace with your actual API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url)
    weather_info = response.json()
    return weather_info

def show_weather():
    city_name = city_value.get()
    weather_info = get_weather(city_name)
    if weather_info['cod'] == 200:
        tfield.delete("1.0", "end")
        tfield.insert("end", f"Weather in {city_name}: {weather_info['weather'][0]['description']}\n")
        tfield.insert("end", f"Temperature: {weather_info['main']['temp']} K\n")
        tfield.insert("end", f"Humidity: {weather_info['main']['humidity']} %\n")
        tfield.insert("end", f"Wind Speed: {weather_info['wind']['speed']} m/s\n")
    else:
        tfield.delete("1.0", "end")
        tfield.insert("end", "City not found")

root = tk.Tk()
root.title("Weather App")
root.geometry("400x400")

city_value = tk.StringVar()
city_entry = tk.Entry(root, textvariable=city_value)
city_entry.pack()

search_button = tk.Button(root, text="Search Weather", command=show_weather)
search_button.pack()

tfield = tk.Text(root, height=10, width=40)
tfield.pack()

root.mainloop()
