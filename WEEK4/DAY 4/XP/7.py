import random

def get_random_temperature(season):
    season_temperatures = {
        "winter": (0, 16),
        "fall": (16, 23),
        "spring": (24, 32),
        "summer": (32, 40)
    }
    temperature_range = season_temperatures.get(season, (-10, 0))
    return random.randint(*temperature_range)

def main():
    user_season = input("Please enter the current season: ")
    if user_season:
        random_temperature = get_random_temperature(user_season)
        print(f"The current temperature is {random_temperature} degrees Celsius and it's {user_season}.")
        if random_temperature < 0:
            print("Brrr, it's freezing! Wear extra layers today.")
        elif 0 <= random_temperature < 16:
            print("Quite cold! Don't forget your coat.")
        elif 16 <= random_temperature <= 23:
            print("A bit cool even if the weather is nice.")
        elif 24 <= random_temperature < 32:
            print("Very good weather.")
        elif 32 <= random_temperature < 40:
            print("It's hot.")
        else:
            print("Bad weather too hot.")
    else:
        print("No season entered.")
        
main()
