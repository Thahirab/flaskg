import speedtest
from keyboard import write
import pyjokes
from pywikihow import search_wikihow
from bs4 import BeautifulSoup
import requests
import pywhatkit
from time import sleep
import webbrowser as web
import os
from geopy.distance import great_circle
from geopy.geocoders import Nominatim
import geocoder
from notifypy import Notify
from keyboard import press_and_release
from keyboard import press
from pytube import YouTube
from pyautogui import click
from pyautogui import hotkey
import pyperclip
import googletrans
from PIL import Image
from speak import talk
from listen import listen
import datetime
def news():
    main_url = "https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=bbe33ed5281f4e74bddcccf1d36d1446"
    main_page = requests.get(main_url).json()
    articles = main_page["articles"]
    head = []
    day = ["first", "second", "third"]
    for ar in articles:
        head.append(ar["title"])
    for i in range(len(day)):
        talk(f"today's {day[i]} new is : {head[i]}")
Api_Key = "KrsOGOZLgYGcxYVBLZld2U65PevfTyOfbdqy7ggK"
def NasaNews():
    talk("Extracting Data From Nasa . ")
    Url = "https://api.nasa.gov/planetary/apod?api_key=" + str(Api_Key)
    Date = datetime.date.today()
    r = requests.get(Url)
    Data = r.json()
    Info = Data["explanation"]
    Title = Data['title']
    Image_Url = Data['url']
    Image_r = requests.get(Image_Url)
    FileName = str(Date) + '.jpg'
    with open(FileName, 'wb') as f:
        f.write(Image_r.content)
    img = Image.open(FileName)

    img.show()
    talk(f"Title : {Title}")
    talk(f"Details : {Info}")
def sb(body):
    url = "https://api.le-systeme-solaire.net/rest/bodies/" + body
    r = requests.get(url)
    data = r.json()
    talk(data)
def Time():
    time = datetime.datetime.now().strftime("%H:%M")
    talk(time)
def Date():
    date = datetime.date.today()
    talk(date)
def Day():
    day = datetime.datetime.now().strftime("%A")
    talk(day)
def NonInputExecution(query):
    if "time" in query:
        Time()
    elif "date" in query:
        Date()
    elif "day" in query:
        Day()
def InputExecution(tag, query):
    if "wikipedia" in tag:
        name = str(query).replace("who is", "").replace("about", "").replace("what is", "").replace("wikipedia", "")
        import wikipedia
        try:
            result = wikipedia.summary(name, sentences=2)
            talk(result)
        except:
            talk("No Speakable Data Available!")
    elif "google" in tag:
        query = str(query).replace("google", "").replace("search", "").replace("google search", "")
        pywhatkit.search(query)

    elif 'play' in tag:
        song = query.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)

    elif "temperature" in tag:
        search = query.replace("what is the", "")
        url = f"https://www.google.com/search?q={search}"
        s = requests.get(url)
        data = BeautifulSoup(s.text, "html.parser")
        temp = data.find("div", class_="BNeawe").text
        talk(f"current {search} is {temp}")

    elif "how to" in tag:
        rs = 1
        ht = search_wikihow(query, rs)
        assert len(ht) == 1
        talk(ht[0].summary)

    elif "news" in tag:
        talk("fetching news please wait sir ... ")
        news()

    elif "where am i" in tag:
        try:
            ipadd = requests.get('https://api.ipify.org').text
            url = "https://get.geojs.io/v1/ip/geo/" + ipadd + ".json"
            geo_requests = requests.get(url)
            geo_data = geo_requests.json()
            city = geo_data["city"]
            country = geo_data["country"]
            talk(f"sir i am not sure,but i think we are in {city} city of {country}")
        except Exception as y:
            print(y)
            talk("sorry")

    elif "ip address" in tag:
        ip = requests.get('https://api.ipify.org').text
        talk(f"your ip address is {ip}")

    elif 'joke' in tag:
        talk(pyjokes.get_joke())

    elif 'planet' in tag:
        messi = query.replace('tell me about planet', '').replace('tell me planet', "").replace('planet', '').replace(
            'provide me some information about planet', '')
        sb(messi)

    elif 'remember' in tag:
        remeberMsg = query.replace("remember that", "")
        remeberMsg = remeberMsg.replace("genie", "")
        talk("You Tell Me To remember That :" + remeberMsg)
        remebr = open('data.txt', 'a')
        remebr.write(remeberMsg)
        remebr.close()

    elif 'rememebered data' in tag:
        remebe = open('data.txt', 'r')
        talk("You Tell Me That" + remebe.read())

    elif 'youtube search' in tag:
        query = query.replace("youtube search", "")
        result = "https://www.youtube.com/results?search_query=" + query
        web.open(result)
        talk("This Is What I Found For Your Search .")
        pywhatkit.playonyt(query)
        talk("This May Also Help You Sir .")

    elif 'download' in tag:
        sleep(2)
        click(x=942, y=59)
        hotkey('ctrl', 'c')
        value = pyperclip.paste()
        Link = str(value)  # Important

        def Download(link):
            url = YouTube(link)
            video = url.streams.first()
            video.download('DataBase\\YouTube\\')

        Download(Link)
        talk("Done Sir , I Have Downloaded The Video .")
        talk("You Can Go And Check It Out.")
        os.startfile('DataBase\\YouTube\\')

    elif 'speedtest' in tag:
        speed = speedtest.Speedtest()
        upload = speed.upload()
        correct_Up = int(int(upload) / 800000)
        download = speed.download()
        correct_down = int(int(download) / 800000)
        talk(f"Downloading Speed Is {correct_down} M B Per Second .")
        talk(f"Uploading Speed Is {correct_Up} M B Per Second .")

    elif 'where-is' in tag:
        Place = query.replace("where is ", "")
        try:
            Url_Place = "https://www.google.com/maps/place/" + str(Place)
            geolocator = Nominatim(user_agent="a")
            location = geolocator.geocode(Place, addressdetails=True)
            target_latlon = location.latitude, location.longitude
            web.open(url=Url_Place)
            location = location.raw['address']
            target = {'city': location.get('city', ''),
                      'state': location.get('state', ''),
                      'country': location.get('country', '')}
            current_loca = geocoder.ip('me')
            current_latlon = current_loca.latlng
            distance = str(great_circle(current_latlon, target_latlon))
            distance = str(distance.split(' ', 1)[0])
            distance = round(float(distance), 2)
            talk(target)
            talk(f"Sir , {Place} iS {distance} Kilometre Away From Your Location . ")
        except Exception as e:
            print(e)
    elif 'table' in tag:
        talk("Checking....")
        from DataBase.timetable.t import Time
        value = Time()
        Noti = Notify()
        Noti.title = "TimeTable"
        Noti.message = str(value)
        Noti.send()

    elif "chrome" in tag:
        if 'new tab' in query:
            press_and_release('ctrl + t')
        elif 'closed tab' in query:
            press_and_release('ctrl + w')
        elif 'new window' in query:
            press_and_release('ctrl + n')
        elif 'history' in query:
            press_and_release('ctrl + h')
        elif 'bookmark' in query:
            press_and_release('ctrl + d')
            press('enter')
        elif 'incognito' in query:
            press_and_release('Ctrl + Shift + n')
        elif 'switch tab' in query:
            tab = query.replace("switch tab ", "")
            Tab = tab.replace("to", "")
            num = Tab
            bb = f'ctrl + {num}'
            press_and_release(bb)

    elif 'YouTubeAuto' in tag:
        if 'pause' or 'pass' in query:
            press('space bar')
        elif 'resume' in query:
            press('space bar')
        elif 'full screen' in query:
            press('f')
        elif 'film screen' in query:
            press('t')
        elif 'skip' in query:
            press('l')
        elif 'back' in query:
            press('j')
        elif 'increase' in query:
            press_and_release('SHIFT + .')
        elif 'decrease' in query:
            press_and_release('SHIFT + ,')
        elif 'previous' in query:
            press_and_release('SHIFT + p')
        elif 'next' in query:
            press_and_release('SHIFT + n')
        elif 'mute' in query:
            press('m')
        elif 'unmute' in query:
            press('m')
        else:
            talk("No Command Found!")

    elif 'WindowsAuto' in tag:
        if 'home screen' in query:
            press_and_release('windows + m')
        elif 'minimize' in query:
            press_and_release('windows + down')
        elif 'show start' in query:
            press_and_release('windows')
        elif 'open setting' in query:
            press_and_release('windows + i')
        elif 'open search' in query:
            press_and_release('windows + s')
        elif 'screen shot' in query:
            press_and_release('windows + SHIFT + s')
        elif 'restore windows' in query:
            press_and_release('Windows + Shift + M')
        elif 'maximize' in query:
            press_and_release('Windows + up')
        else:
            talk("Sorry , No Command Found!")

    elif 'open' in tag:
        talk("Ok Sir, Wait a second!")
        name = query.replace("open", "").strip().lower()
        press_and_release('windows + s')
        sleep(5)
        write(name)
        sleep(0.5)
        press_and_release('enter')
        talk("Your Command Has Been Completed Sir!")

    elif 'website' in tag:
        talk("Ok Sir, Wait a second!")
        name = query.replace("open", "").strip().lower()
        if name == 'youtube':
            web.open("https://www.youtube.com/")
        elif name == 'instagram':
            web.open("https://www.instagram.com/")
        else:
            website_url = f"https://www.{name}.com"
            web.open(website_url)
        talk("Your Command Has Been Completed Sir!")

    elif 'close' in tag:
        press_and_release("alt + f4")

    elif 'WhatsappMsg' in tag:
        name = query.replace("whatsapp message", "")
        name = name.replace("send ", "")
        name = name.replace("to ", "")
        Name = str(name)
        talk(f"Whats The Message For {Name}")
        message = listen()
        press_and_release('windows + s')
        sleep(5)
        write("whatsapp")
        sleep(0.5)
        press_and_release('enter')
        sleep(25)
        click(x=195, y=115)
        sleep(1)
        write(Name)
        sleep(0.5)
        click(x=188, y=200)
        sleep(3)
        write(message)
        press_and_release('enter')


    elif "call" in tag:
        name = query.replace("call ", "")
        press_and_release('windows + s')
        sleep(5)
        write("whatsapp")
        sleep(0.5)
        press_and_release('enter')
        sleep(25)
        click(x=195, y=115)
        sleep(1)
        write(name)
        sleep(1)
        click(x=188, y=200)
        sleep(1)
        click(x=1198, y=63)
        sleep(1)
        click(x=1580, y=450)

    elif "showchat" in tag:
        talk("whose numer")
        name = listen()
        press_and_release('windows + s')
        sleep(5)
        write("whatsapp")
        sleep(0.5)
        press_and_release('enter')
        sleep(25)
        click(x=195, y=115)
        sleep(1)
        write(name)
        sleep(1)
        click(x=188, y=200)
        sleep(1)
        click(x=571, y=690)
        sleep(1)

    elif "translate" in tag:
        s = query.replace("translate", "")
        talk("say the language to translate")
        adxg = listen()
        tans = googletrans.Translator()
        t = tans.translate(s, dest=adxg)
        talk(t.text)

    elif "nasa" in tag:
        NasaNews()

    else:
        pass
