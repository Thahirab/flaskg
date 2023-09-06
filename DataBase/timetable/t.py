from speak import talk as Speak
import datetime

FiveTo6 = '''
In This Time , 
You Have To Get Up & Listen Somethintg Positive .
5:00 Am To 6:00 Am 
Thanks.
'''

SixTo8 = '''
In This Time , 
You Have to bath,eat your breakfast and get ready for school.
6:00 Am To 8:00 Am .
Thanks .
'''

EightTo15 = '''
In This Time ,
You Have to study in school.
8:00 Am To 3:00 Pm .
Thanks .
'''

FifteenTo17 = '''
In This Time ,
You Have To Code .
3:00 Pm To 5:00 Pm .
Thanks .
'''

seventeenTo18 = '''
In This Time ,
You Have To study in tution .
5:00 Pm To 6:00 Pm .
Thanks .
'''
eightteenTo19 = '''
In This Time ,
You Have To study in madarsa .
6:00 Pm To 7:00 Pm .
Thanks .
'''
nineteenTo20 = '''
In This Time ,
You Have To Play .
7:00 Pm To 8:00 Pm .
Thanks .
'''
TwentyTo22 = '''
In This Time ,
You Have To eat and watch tv or mobile to relax.
8:00 Pm To 10:00 Pm .
Thanks .
'''

def Time():

    hour = int(datetime.datetime.now().strftime("%H"))

    if hour>=5 and hour<6:
        Speak(FiveTo6)
        return FiveTo6
        
    elif hour>=6 and hour<8:
        Speak(SixTo8)
        return SixTo8

    elif hour>=8 and hour<15:
        Speak(EightTo15)
        return EightTo15

    elif hour>=15 and hour<17:
        Speak(FifteenTo17)
        return FifteenTo17

    elif hour>=17 and hour<18:
        Speak(seventeenTo18)
        return seventeenTo18

    elif hour>=18 and hour<19:
        Speak(eightteenTo19)
        return eightteenTo19
    
    elif hour>=19 and hour<20:
        Speak(nineteenTo20)
        return nineteenTo20
    
    elif hour>=20 and hour<22:
        Speak(TwentyTo22)
        return TwentyTo22
    
        
    else:
        Speak("In This Time , You Have To Sleep ")

        return '''In This Time , You Have To Sleep .'''