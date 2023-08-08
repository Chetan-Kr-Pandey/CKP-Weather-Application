from tkinter import *
import tkinter as tk
import ttkbootstrap as tb
from ttkbootstrap.constants import *
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import *
import requests
import pytz
import time
from PIL import ImageTk, Image

def currentlocation():
    try:
        city = "Ranchi"
        geolocator = Nominatim(user_agent="geoapiExerxises")
        location =geolocator.geocode(city)
        obj = TimezoneFinder()
        result = obj.timezone_at(lng=location.longitude,lat=location.latitude)
        home=pytz.timezone(result)
        local_time=datetime.now(home)
        current_time=local_time.strftime("%I:%M:%p")
        api = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&exclude={exclude}&appid=06c921750b9a82d8f5d1294e1586276f"
        api1 = "https://api.openweathermap.org/data/2.5/onecall?lat="+str(location.latitude)+"&lon="+str(location.longitude)+"&units=metric&exclude=hourly&appid=06c921750b9a82d8f5d1294e1586276f"
        json_data = requests.get(api).json()
        data = requests.get(api1).json()
        condition = json_data['weather'][0]['main']
        temp = int(json_data['main']['temp'] - 273.15)
        min_temp = int(json_data['main']['temp_min'] - 273.15)
        max_temp = int(json_data['main']['temp_max'] - 273.15)
        pressure = json_data['main']['pressure']
        humidity = json_data['main']['humidity']
        wind = json_data['wind']['speed']
        sunrise = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunrise'] - 21600))
        sunset = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunset'] - 21600))
        description = json_data['weather'][0]['main']
        
        final_info = condition + "\n" + str(temp) + "°C"

        location= "Ranchi"
        rc.config(text=location)
        mint.config(text=min_temp)
        maxt.config(text=max_temp)
        p.config(text=pressure)
        h.config(text=humidity)
        w.config(text=wind)
        sr.config(text=sunrise)
        ss.config(text=sunset)
        tc.config(text=final_info)
        tt.config(text=current_time)

        #days
        #1st cell
        firstdayimage = json_data['weather'][0]['icon']
        photo1 = ImageTk.PhotoImage(file=f"icon/{firstdayimage}@2x.png")
        firstimage.config(image=photo1)
        firstimage.image=photo1

        first =datetime.now()
        day1.config(text=first.strftime("%A"))

        #2nd cell
        second= first+timedelta(days=1)
        day2.config(text=second.strftime("%A"))

        db = data['daily'][1]['weather'][0]['main']
        temp2 = data['daily'][1]['temp']['day']
        d2.config( text=db )
        t2.config( text=temp2)

        #3rd cell
        third= second+timedelta(days=1)
        day3.config(text=third.strftime("%A"))

        db = data['daily'][2]['weather'][0]['main']
        temp3 = data['daily'][2]['temp']['day']
        d3.config( text=db)
        t3.config( text=temp3)

        #4th cell
        fourth= third+timedelta(days=1)
        day4.config(text=fourth.strftime("%A"))

        dc = data['daily'][3]['weather'][0]['main']
        temp4 = data['daily'][3]['temp']['day']
        d4.config( text=dc)
        t4.config( text=temp4)

        #5th cell
        fifth= fourth+timedelta(days=1)
        day5.config(text=fifth.strftime("%A"))

        dd = data['daily'][4]['weather'][0]['main']
        temp5 = data['daily'][4]['temp']['day']
        d5.config( text=dd)
        t5.config( text=temp5)

        #6th cell
        sixth= fifth+timedelta(days=1)
        day6.config(text=sixth.strftime("%A"))

        de = data['daily'][5]['weather'][0]['main']
        temp6 = data['daily'][5]['temp']['day']
        d6.config( text=de)
        t6.config( text=temp6)

        #7th cell
        seventh= sixth+timedelta(days=1)
        day7.config(text=seventh.strftime("%A"))

        df = data['daily'][6]['weather'][0]['main']
        temp7 = data['daily'][6]['temp']['day']
        d7.config( text=df)
        t7.config( text=temp7)

    except Exception as e:
        messagebox.showerror("Weather app" , "Invalid Entry!!")

def getWeather():
    try:
        city = textField.get()
        geolocator = Nominatim(user_agent="geoapiExerxises")
        location =geolocator.geocode(city)
        obj = TimezoneFinder()
        result = obj.timezone_at(lng=location.longitude,lat=location.latitude)
        home=pytz.timezone(result)
        local_time=datetime.now(home)
        current_time=local_time.strftime("%I:%M:%p")
        api = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&exclude={exclude}&appid=06c921750b9a82d8f5d1294e1586276f"
        api1 = "https://api.openweathermap.org/data/2.5/onecall?lat="+str(location.latitude)+"&lon="+str(location.longitude)+"&units=metric&exclude=hourly&appid=06c921750b9a82d8f5d1294e1586276f"
        json_data = requests.get(api).json()
        data = requests.get(api1).json()
        condition = json_data['weather'][0]['main']
        temp = int(json_data['main']['temp'] - 273.15)
        min_temp = int(json_data['main']['temp_min'] - 273.15)
        max_temp = int(json_data['main']['temp_max'] - 273.15)
        pressure = json_data['main']['pressure']
        humidity = json_data['main']['humidity']
        wind = json_data['wind']['speed']
        sunrise = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunrise'] - 21600))
        sunset = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunset'] - 21600))
        description = json_data['weather'][0]['main']
        
        final_info = condition + "\n" + str(temp) + "°C"
        
        mint.config(text=min_temp)
        maxt.config(text=max_temp)
        p.config(text=pressure)
        h.config(text=humidity)
        w.config(text=wind)
        sr.config(text=sunrise)
        ss.config(text=sunset)
        tc.config(text=final_info)
        tt.config(text=current_time)

        #days
        #1st cell
        firstdayimage = json_data['weather'][0]['icon']
        photo1 = ImageTk.PhotoImage(file=f"icon/{firstdayimage}@2x.png")
        firstimage.config(image=photo1)
        firstimage.image=photo1

        first =datetime.now()
        day1.config(text=first.strftime("%A"))

        #2nd cell
        second= first+timedelta(days=1)
        day2.config(text=second.strftime("%A"))

        db = data['daily'][1]['weather'][0]['main']
        temp2 = data['daily'][1]['temp']['day']
        d2.config( text=db )
        t2.config( text=temp2)

        #3rd cell
        third= second+timedelta(days=1)
        day3.config(text=third.strftime("%A"))

        db = data['daily'][2]['weather'][0]['main']
        temp3 = data['daily'][2]['temp']['day']
        d3.config( text=db)
        t3.config( text=temp3)

        #4th cell
        fourth= third+timedelta(days=1)
        day4.config(text=fourth.strftime("%A"))

        dc = data['daily'][3]['weather'][0]['main']
        temp4 = data['daily'][3]['temp']['day']
        d4.config( text=dc)
        t4.config( text=temp4)

        #5th cell
        fifth= fourth+timedelta(days=1)
        day5.config(text=fifth.strftime("%A"))

        dd = data['daily'][4]['weather'][0]['main']
        temp5 = data['daily'][4]['temp']['day']
        d5.config( text=dd)
        t5.config( text=temp5)

        #6th cell
        sixth= fifth+timedelta(days=1)
        day6.config(text=sixth.strftime("%A"))

        de = data['daily'][5]['weather'][0]['main']
        temp6 = data['daily'][5]['temp']['day']
        d6.config( text=de)
        t6.config( text=temp6)

        #7th cell
        seventh= sixth+timedelta(days=1)
        day7.config(text=seventh.strftime("%A"))

        df = data['daily'][6]['weather'][0]['main']
        temp7 = data['daily'][6]['temp']['day']
        d7.config( text=df)
        t7.config( text=temp7)

    except Exception as e:
        messagebox.showerror("Weather app" , "Invalid Entry!!")

def close():
    canvas.destroy()


#app
canvas = tk.Tk()
canvas.geometry("900x700")
canvas.title("CKP Weather")
f = ("poppins", 15, "bold")
t = ("poppins", 35, "bold")
image = Image.open(r"logos\wallpaperflare.png")  # Replace "path_to_image.jpg" with the actual path to your image

background_image = ImageTk.PhotoImage(image)
background_label = tk.Label(canvas, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
canvas.resizable(False,False)

#search box

#textField = tb.Entry(canvas, justify='center', width = 20 , font = t,bootstyle="info")
#textField.pack(pady = 50)
#textField.focus()
textField = tb.Combobox(canvas, justify='center', width = 20 , font = t,bootstyle="info", height= 8)
textField.pack(pady = 50)
locations = [
    ]

textField['value'] = ("Afghanistan", "Albania", "Algeria", "Andorra", "Angola", "Antigua and Barbuda",
    "Argentina", "Armenia", "Australia", "Austria", "Azerbaijan", "Bahamas", "Bahrain",
    "Bangladesh", "Barbados", "Belarus", "Belgium", "Belize", "Benin", "Bhutan",
    "Bolivia", "Bosnia and Herzegovina", "Botswana", "Brazil", "Brunei", "Bulgaria",
    "Burkina Faso", "Burundi", "Cabo Verde", "Cambodia", "Cameroon", "Canada",
    "Central African Republic", "Chad", "Chile", "China", "Colombia", "Comoros",
    "Congo (Congo-Brazzaville)", "Costa Rica", "Croatia", "Cuba", "Cyprus", "Czechia",
    "Democratic Republic of the Congo", "Denmark", "Djibouti", "Dominica",
    "Dominican Republic", "Ecuador", "Egypt", "El Salvador", "Equatorial Guinea",
    "Eritrea", "Estonia", "Eswatini", "Ethiopia", "Fiji", "Finland", "France", "Gabon",
    "Gambia", "Georgia", "Germany", "Ghana", "Greece", "Grenada", "Guatemala",
    "Guinea", "Guinea-Bissau", "Guyana", "Haiti", "Holy See", "Honduras", "Hungary",
    "Iceland", "India", "Indonesia", "Iran", "Iraq", "Ireland", "Israel", "Italy",
    "Jamaica", "Japan", "Jordan", "Kazakhstan", "Kenya", "Kiribati", "Kuwait",
    "Kyrgyzstan", "Laos", "Latvia", "Lebanon", "Lesotho", "Liberia", "Libya",
    "Liechtenstein", "Lithuania", "Luxembourg", "Madagascar", "Malawi", "Malaysia",
    "Maldives", "Mali", "Malta", "Marshall Islands", "Mauritania", "Mauritius",
    "Mexico", "Micronesia", "Moldova", "Monaco", "Mongolia", "Montenegro", "Morocco",
    "Mozambique", "Myanmar (formerly Burma)", "Namibia", "Nauru", "Nepal",
    "Netherlands", "New Zealand", "Nicaragua", "Niger", "Nigeria", "North Korea",
    "North Macedonia (formerly Macedonia)", "Norway", "Oman", "Pakistan", "Palau",
    "Palestine State", "Panama", "Papua New Guinea", "Paraguay", "Peru", "Philippines",
    "Poland", "Portugal", "Qatar", "Romania", "Russia", "Rwanda", "Saint Kitts")
textField.focus()

#textField.bind('<Return>', getWeather)

#button
style = tb.Style()
style.configure("TButton", font=("Arial", 16))

button = tb.Button(canvas, text="SEARCH" ,command=getWeather , width=10 , style="success.TButton" )
button.pack(side="right", padx=10, pady=10)
button.place(x=380,y=120)

button = tb.Button(canvas, text="YL" ,command=currentlocation , width=2 , style="primary.TButton" )
button.pack(side="right", padx=10, pady=10)
button.place(x=5,y=5)

button = tb.Button(canvas, text="X" ,command=close , width=1 , style="danger.TButton" )
button.pack(side="right", padx=10, pady=10)
button.place(x=860,y=5)

#label
label3 = tb.Label(canvas, text="Pressure :",font=("Arial", 20),bootstyle="inverse-danger")
label3.place(x=20,y=400)


label4 = tb.Label(canvas, text="Humidity :",font=("Arial", 20),bootstyle="inverse-danger")
label4.place(x=20,y=450)


label5 = tb.Label(canvas, text="Wind :",font=("Arial", 20),bootstyle="inverse-danger")
label5.place(x=20,y=350)


label6 = tb.Label(canvas, text="Sunrise :",font=("Arial", 20),bootstyle="inverse-danger")
label6.place(x=620,y=400)


label7 = tb.Label(canvas, text="Sunset :",font=("Arial", 20),bootstyle="inverse-danger")
label7.place(x=620,y=450)

label8 = tb.Label(canvas, text="Time :",font=("Arial", 20),bootstyle="inverse-danger")
label8.place(x=620,y=350)

#main box

tc= tb.Label(canvas,font=t,bootstyle="inverse-info")
tc.place(x=380,y=200)

rc=tb.Label(canvas,font=("Arial", 20),bootstyle="inverse-info")
rc.place(x=60,y=5)
#main box end

p=tb.Label(text="",font=("arial",20),bootstyle="inverse-primary")
p.place(x=200,y=400)

h=tb.Label(text='',font=("arial",20),bootstyle="inverse-primary")
h.place(x=200,y=450)

w=tb.Label(text="",font=("arial",20),bootstyle="inverse-primary")
w.place(x=200,y=350)

sr=tb.Label(text="",font=("arial",20),bootstyle="inverse-primary")
sr.place(x=750,y=400)

ss=tb.Label(text="",font=("arial",20),bootstyle="inverse-primary")
ss.place(x=750,y=450)

tt=tb.Label(text="",font=("arial",20),bootstyle="inverse-primary")
tt.place(x=750,y=350)

#bottom boxes

firstbox=PhotoImage(file="logos/Rectangle.png")
secondbox=PhotoImage(file="logos/Rectangle2.png")

Label(canvas,image=firstbox,bg="black").place(x=20,y=550)
Label(canvas,image=secondbox,bg="black").place(x=300,y=560)
Label(canvas,image=secondbox,bg="black").place(x=400,y=560)
Label(canvas,image=secondbox,bg="black").place(x=500,y=560)
Label(canvas,image=secondbox,bg="black").place(x=600,y=560)
Label(canvas,image=secondbox,bg="black").place(x=700,y=560)
Label(canvas,image=secondbox,bg="black").place(x=800,y=560)

#1st cell
firstframe = tb.Frame(canvas,width=230,height=132,bootstyle="info")
firstframe.place(x=25,y=555)

day1=tb.Label(firstframe, font="Arial 20",bootstyle="inverse-info")
day1.place(x=100,y=5)

firstimage=Label(firstframe,bg="Red")
firstimage.place(x=2,y=15,width=95, height=100)

label1 = tb.Label(firstframe, text="Min. Temp. :" ,font=("Arial", 10,"bold"),bootstyle="inverse-info")
label1.place(x=100,y=75)


label2 = tb.Label(firstframe, text="Max. Temp. :",font=("Arial", 10,"bold"),bootstyle="inverse-info")
label2.place(x=100,y=45)

mint=tb.Label(firstframe,text="...",font=("arial",10,"bold"),bootstyle="inverse-info")
mint.place(x=200,y=75)

maxt=tb.Label(firstframe,text="...",font=("arial",10,"bold"),bootstyle="inverse-info")
maxt.place(x=200,y=45)

#2nd cell
secondframe = tb.Frame(canvas,width=70,height=115,bootstyle="danger")
secondframe.place(x=305,y=565)

day2=tb.Label(secondframe, font=("Arial",10,"bold"),bootstyle="inverse-danger")
day2.place(x=7,y=5)

d2=tb.Label(secondframe,text="...",font=("arial",10,"bold"),bootstyle="inverse-danger")
d2.place(x=18,y=35)

t2=tb.Label(secondframe,text="...",font=("arial",10,"bold"),bootstyle="inverse-danger")
t2.place(x=20,y=65)

#3rd cell
thirdframe = tb.Frame(canvas,width=70,height=115,bootstyle="success")
thirdframe.place(x=405,y=565)

day3=tb.Label(thirdframe, font=("Arial",10,"bold"), bootstyle="inverse-success")
day3.place(x=7,y=5)

d3=tb.Label(thirdframe,text="...",font=("arial",10,"bold"),bootstyle="inverse-success")
d3.place(x=18,y=35)

t3=tb.Label(thirdframe,text="...",font=("arial",10,"bold"),bootstyle="inverse-success")
t3.place(x=20,y=65)

#4th cell
fourthframe = tb.Frame(canvas,width=70,height=115,bootstyle="warning")
fourthframe.place(x=505,y=565)

day4=tb.Label(fourthframe, font=("Arial",10,"bold"), bootstyle="inverse-warning")
day4.place(x=7,y=5)

d4=tb.Label(fourthframe,text="...",font=("arial",10,"bold"),bootstyle="inverse-warning")
d4.place(x=18,y=35)

t4=tb.Label(fourthframe,text="...",font=("arial",10,"bold"),bootstyle="inverse-warning")
t4.place(x=20,y=65)


#5th cell
fifthframe = tb.Frame(canvas,width=70,height=115,bootstyle="primary")
fifthframe.place(x=605,y=565)

day5=tb.Label(fifthframe, font=("Arial",10,"bold"), bootstyle="inverse-primary")
day5.place(x=7,y=5)

d5=tb.Label(fifthframe,text="...",font=("arial",10,"bold"),bootstyle="inverse-primary")
d5.place(x=18,y=35)

t5=tb.Label(fifthframe,text="...",font=("arial",10,"bold"),bootstyle="inverse-primary")
t5.place(x=20,y=65)

#6th cell
sixthframe = tb.Frame(canvas,width=70,height=115,bootstyle="secondary")
sixthframe.place(x=705,y=565)

day6=tb.Label(sixthframe, font=("Arial",10,"bold"),bootstyle="inverse-secondary")
day6.place(x=7,y=5)

d6=tb.Label(sixthframe,text="...",font=("arial",10,"bold"),bootstyle="inverse-secondary")
d6.place(x=18,y=35)

t6=tb.Label(sixthframe,text="...",font=("arial",10,"bold"),bootstyle="inverse-secondary")
t6.place(x=20,y=65)

#7th cell
seventhframe = tb.Frame(canvas,width=70,height=115,bootstyle="dark")
seventhframe.place(x=805,y=565)

day7=tb.Label(seventhframe, font=("Arial",10,"bold"), bootstyle="inverse-dark")
day7.place(x=7,y=5)

d7=tb.Label(seventhframe,text="...",font=("arial",10,"bold"),bootstyle="inverse-dark")
d7.place(x=18,y=35)

t7=tb.Label(seventhframe,text="...",font=("arial",10,"bold"),bootstyle="inverse-dark")
t7.place(x=20,y=65)


canvas.mainloop()



