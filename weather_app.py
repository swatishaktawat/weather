
from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
from tkinter import ttk, messagebox
from datetime import datetime
import requests
import pytz

root = Tk()
root.title('Weather App')
root.geometry("900x500+300+200")
root.resizable(False,False)

def getWeather():
    try:
        city = textfield.get()

        geolocator = Nominatim(user_agent='geopiExercises')
        location = geolocator.geocode(city)
        obj = TimezoneFinder()
        result = obj.timezone_at(lng=location.longitude,lat=location.latitude)

        home = pytz.timezone(result)
        local_time = datetime.now(home)
        current_time = local_time.strftime("%H:%M %p")
        clock.config(text=current_time)
        name.config(text="CURRENT WEATHER")

        #weather
        key = '58edf27349b40d08fa547425f478b568'
        url = 'https://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=' + key

        jdata = requests.get(url).json()

        condition = jdata['weather'][0]['main']
        description = jdata['weather'][0]['description']
        temp = int(jdata['main']['temp'] - 273.15)
        feels_like = int(jdata['main']['feels_like'] - 273.15)
        pressure = jdata['main']['pressure']
        humidity = jdata['main']['humidity']
        wind_speed = jdata['wind']['speed']

        degree_sign = u'\N{DEGREE SIGN}'

        t.config(text=(temp,degree_sign))
        c.config(text=(condition,"|","FEELS","LIKE",feels_like,degree_sign))
        w.config(text=(wind_speed,'m/s'))
        h.config(text=(humidity,"%"))
        p.config(text=(pressure,'hPa'))
        d.config(text=description)

    except Exception as e:
        messagebox.showerror("Weather App","Invalid Entry")

search_image = PhotoImage(file="search.png")
myimage = Label(image=search_image)
myimage.place(x=20, y=20)

textfield = tk.Entry(root,justify='center',width=17,font=('poppins',25,'bold'),bg='#404040',border=0,fg='white')
textfield.place(x=50,y=40)
textfield.focus()

search_icon = PhotoImage(file='search_icon.png')
myimage_icon = Button(image=search_icon,borderwidth=0, cursor="hand2",bg='#404040',command=getWeather)
myimage_icon.place(x=400,y=34)

#logo
logo_image = PhotoImage(file='logo.png')
logo = Label(image=logo_image)
logo.place(x=150,y=100)

#bottom box
frame_image = PhotoImage(file='box.png')
frame = Label(image=frame_image)
frame.pack(padx=5,pady=5,side=BOTTOM)

#time
name = Label(root,font=('arial',15,'bold'))
name.place(x=30,y=100)
clock = Label(root,font=('Helvetica',20))
clock.place(x=30,y=130)

#label
label1 = Label(root,text="WIND",font=('Helvetica',15,'bold'),fg='white',bg='#1ab5ef')
label1.place(x=120,y=400)

label2 = Label(root,text="HUMIDITY",font=('Helvetica',15,'bold'),fg='white',bg='#1ab5ef')
label2.place(x=250,y=400)

label3 = Label(root,text="DESCRIPTION",font=('Helvetica',15,'bold'),fg='white',bg='#1ab5ef')
label3.place(x=430,y=400)

label4 = Label(root,text="PRESSURE",font=('Helvetica',15,'bold'),fg='white',bg='#1ab5ef')
label4.place(x=650,y=400)

t = Label(font=('arial',70,'bold'),fg='#ee666d')
t.place(x=400,y=150)
c = Label(font=('arial',15,'bold'))
c.place(x=400,y=250)

w = Label(text=' ...',font=('arial',20,'bold'),bg='#1ab5ef')
w.place(x=110,y=430)
h = Label(text='...',font=('arial',20,'bold'),bg='#1ab5ef')
h.place(x=280,y=430)
d = Label(text='      ...',font=('arial',20,'bold'),bg='#1ab5ef')
d.place(x=430,y=430)
p = Label(text='  ...',font=('arial',20,'bold'),bg='#1ab5ef')
p.place(x=650,y=430)

root.mainloop()
