# 📱 Phone Number Tracker (Tkinter GUI)

A Python-based desktop application that tracks the **region and carrier** of a phone number and visualizes its approximate location on a map.

> ⚠️ This project is for **educational purposes only**. It does NOT provide real-time or exact location tracking.

---

## 🚀 Features

- 📥 User-friendly GUI using Tkinter  
- 📍 Detects phone number location (country/region)  
- 📡 Displays telecom service provider  
- 🌍 Generates map with coordinates using Folium  
- 🔗 Opens map in browser  
- ⚠️ Error handling for invalid inputs  

---

## 🖼️ Output

- Shows:
  - Location (Region)
  - Carrier (Service Provider)
  - Latitude & Longitude
- Generates:
  - `Location.html` (interactive map)

---

## 🛠️ Technologies Used

- **Python 3**
- **Tkinter** – GUI
- **phonenumbers** – Phone number parsing
- **OpenCage API** – Geocoding (lat/lng)
- **Folium** – Map visualization

---

## 📦 Installation

Install required libraries:

```bash
pip install phonenumbers folium opencage

```
```bash
git clone https://github.com/Sumanth-M-Poojary/phonenumbertracker.git
cd phonenumbertracker
python track.py

