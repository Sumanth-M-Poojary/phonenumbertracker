import phonenumbers
from phonenumbers import geocoder as pg, carrier
import folium
from opencage.geocoder import OpenCageGeocode
import tkinter as tk
from tkinter import messagebox
import webbrowser
import os

API_KEY = "1ec93b24ca5f4f299a02dde610c5a65f"

map_file = "Location.html"

def track_number():
    number = entry.get()

    try:
        phoneNumber = phonenumbers.parse(number)

        if not phonenumbers.is_valid_number(phoneNumber):
            messagebox.showerror("Error", "Invalid Phone Number")
            return

        location = pg.description_for_number(phoneNumber, "en")
        service = carrier.name_for_number(phoneNumber, "en")

        location_label.config(text=f"📍 Location: {location}")
        carrier_label.config(text=f"📡 Carrier: {service}")

        geocode = OpenCageGeocode(API_KEY)
        results = geocode.geocode(location)

        if results:
            lat = results[0]['geometry']['lat']
            lng = results[0]['geometry']['lng']

            coords_label.config(text=f"🌍 Lat: {lat}, Lng: {lng}")

            # Create map
            myMap = folium.Map(location=[lat, lng], zoom_start=9)
            folium.Marker([lat, lng], popup=location).add_to(myMap)
            myMap.save(map_file)

        else:
            messagebox.showerror("Error", "Location not found")

    except Exception as e:
        messagebox.showerror("Error", str(e))


def open_map():
    if os.path.exists(map_file):
        webbrowser.open('file://' + os.path.realpath(map_file))
    else:
        messagebox.showwarning("Warning", "Generate map first!")


# GUI
root = tk.Tk()
root.title("📱 Phone Tracker")

root.geometry("420x350")

tk.Label(root, text="Phone Number Tracker", font=("Arial", 16, "bold")).pack(pady=10)
tk.Label(root, text="Created by Sumanth Poojary", font=("Arial", 13, "bold")).pack(pady=10)
entry = tk.Entry(root, width=30, font=("Arial", 12))
entry.pack(pady=10)
entry.insert(0, "+91")

tk.Button(root, text="Track", command=track_number, bg="blue", fg="white").pack(pady=10)

location_label = tk.Label(root, text="📍 Location:", font=("Arial", 11))
location_label.pack()

carrier_label = tk.Label(root, text="📡 Carrier:", font=("Arial", 11))
carrier_label.pack()

coords_label = tk.Label(root, text="🌍 Coordinates:", font=("Arial", 11))
coords_label.pack()

# 🔥 Open Map Button
tk.Button(root, text="Open Map 🌍", command=open_map, bg="green", fg="white").pack(pady=15)

root.mainloop()