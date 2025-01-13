import sys
from gtts import gTTS
from preferredsoundplayer import soundplay

def main():
    
    if len(sys.argv) > 3:
        print("Too many arguments!")
        print("Usage: python3 SayMilitaryTime.py 1859 USA")
        sys.exit()
    if len(sys.argv) < 3:
        print("Too few arguments!")
        print("Usage: python3 SayMilitaryTime.py 1859 USA")
        sys.exit()
    try:    
        military_time = int(sys.argv[1])
    except ValueError:
        print("Invalid 1st command line argument. Should contain only digits.")
        sys.exit()
    accent = sys.argv[2]

    valid_accent = ["AUS", "IND", "USA"]
    if accent not in valid_accent:
        print("Invalid 2nd argument. Must be one of IND, AUS, USA")
        sys.exit()
    hours = military_time//100
    minutes = military_time % 100

    if minutes > 59:
        print("Invalid 1st command line argument. Minutes cannot be more than 59")
        sys.exit()
    if hours > 23:
        print("Invalid 1st command line argument. Hours cannot be more than 23.")
        sys.exit()

    print(convert_minutes(minutes))

def convert_minutes(minutes):
    pass
	