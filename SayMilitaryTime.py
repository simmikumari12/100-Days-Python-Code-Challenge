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

    print(time(hours, minutes))

def convert_minutes(minutes):
    min_dict = {
        1: "ONE",
        2: "TWO",
        3: "THREE",
        4: "FOUR",
        5: "FIVE",
        6: "SIX",
        7: "SEVEN",
        8: "EIGHT",
        9: "NINE",
        10: "TEN",
        11: "ELEVEN",
        12: "TWELVE",
        13: "THIRTEEN",
        14: "FORTEEN",
        15: "FIFTEEN",
        16: "SIXTEEN",
        17: "SEVENTEEN",
        18: "EIGHTEEN",
        19: "NINETEEN",
        20: "TWENTY",
        21: "TWENTY ONE",
        22: "TWENTY TWO",
        23: "TWENTY THREE",
        24: "TWENTY FOUR",
        25: "TWENTY FIVE",
        26: "TWENTY SIX",
        27: "TWENTY SEVEN",
        28: "TWENTY EIGHT",
        29: "TWENTY NINE",
        30: "THIRTY",
        31: "THIRTY ONE",
        32: "THIRTY TWO",
        33: "THIRTY THREE",
        34: "THIRTY FOUR",
        35: "THIRTY FIVE",
        36: "THIRTY SIX",
        37: "THIRTY SEVEN",
        38: "THIRTY EIGHT",
        39: "THIRTY NINE",
        40: "FORTY",
        41: "FORTY ONE",
        42: "FORTY TWO",
        43: "FORTY THREE",
        44: "FORTY FOUR",
        45: "FORTY FIVE",
        46: "FORTY SIX",
        47: "FORTY SEVEN",
        48: "FORTY EIGHT",
        49: "FORTY NINE",
        50: "FIFTY",
        51: "FIFTY ONE",
        52: "FIFTY TWO",
        53: "FIFTY THREE",
        54: "FIFTY FOUR",
        55: "FIFTY FIVE",
        56: "FIFTY SIX",
        57: "FIFTY SEVEN",
        58: "FIFTY EIGHT",
        59: "FIFTY NINE",
        60: "SIXTY"
    }
    return min_dict[minutes]

def convert_hours(hours):
    hour_dict = {
        1: "ONE",
        2: "TWO",
        3: "THREE",
        4: "FOUR",
        5: "FIVE",
        6: "SIX",
        7: "SEVEN",
        8: "EIGHT",
        9: "NINE",
        10: "TEN",
        11: "ELEVEN",
        12: "TWELVE",
        13: "THIRTEEN",
        14: "FORTEEN",
        15: "FIFTEEN",
        16: "SIXTEEN",
        17: "SEVENTEEN",
        18: "EIGHTEEN",
        19: "NINETEEN",
        20: "TWENTY",
        21: "TWENTY ONE",
        22: "TWENTY TWO",
        23: "TWENTY THREE",
        24: "TWENTY FOUR"
    }
    return hour_dict[hours]

def time(h, t):
    if h < 10:
        return f"ZERO {convert_hours(h)} {convert_minutes(t)}"
    else:
        return f"{convert_hours(h)} HUNDRED {convert_minutes(t)} HOURS"

if __name__ == "__main__":
    main()
	