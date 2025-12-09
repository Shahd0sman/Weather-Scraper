import requests
import tkinter as tk

def get_weather():
    city = city_entry.get()
    url = f"https://wttr.in/{city}?format=%t"
    try:
        temp=requests.get(url).text
        result_label.config(text=f'Temperature in {city}:{temp}')
    except:
        result_label.config(text="Error fetching data.")
root=tk.Tk()
root.title('Weather Scraper')
root.geometry("300x150")

tk.Label(root,text="Enter City:").pack()
city_entry=tk.Entry(root)
city_entry.pack()
tk.Button(root,text='Get Weather',command=get_weather).pack()

result_label= tk.Label(root,text='',font=('Arial',12))
result_label.pack()
root.mainloop()