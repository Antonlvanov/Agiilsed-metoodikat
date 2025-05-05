import random
from datetime import datetime, timedelta

NEWS_TEMPLATES = {
    "Tehnoloogia": [
        "{} avalikustas uue AI-toega seadme, mis muudab {} tööstust",
        "{} investeeris {} miljonit eurot {} startupi",
        "Tehnoloogiahiid {} lansseeris {} põhineva platvormi",
        "Uus tarkvaravärskendus {} parandab jõudlust {} seadmetel"
    ],
    "Sport": [
        "{} võitis {} turniiri, alistades {} punktiga",
        "Atleet {} püstitas uue rekordi {} võistlusel {} linnas",
        "{} meeskond sõlmis lepingu {} mängijaga",
        "Spordikeskus {} avati {} piirkonnas"
    ],
    "Majandus": [
        "{} aktsiad tõusid {}% pärast {} teadet",
        "Rahvusvaheline ettevõte {} omandas {} miljardi eest",
        "{} prognoosib majanduskasvu {}% järgmisel aastal",
        "Keskpank {} muutis intressimäärasid {} baaspunkti võrra"
    ]
}

NAMES = ["TechCorp", "InnovateX", "GlobalSys", "StarPlayer", "EconoBank", "MarketPro"]
LOCATIONS = ["Tallinn", "Tartu", "Helsingi", "Stockholm", "London", "New York"]
TECH_TERMS = ["pilvepõhine", "autonoomne", "krüptograafiline", "virtuaalne"]
SPORT_EVENTS = ["maraton", "meistrivõistlused", "olümpia", "karikavõistlus"]
ECONOMIC_TERMS = ["turg", "investeering", "kvartaliaruanne", "rahaühik"]

def generate_random_date():
    """Generate a random date within the last 7 days."""
    today = datetime.now()
    days_ago = random.randint(0, 7)
    random_date = today - timedelta(days=days_ago)
    return random_date.strftime("%Y-%m-%d")

def generate_news(category):
    """Generate a single news item for the given category."""
    template = random.choice(NEWS_TEMPLATES.get(category, ["Uudiseid pole"]))
    placeholders = {
        0: random.choice(NAMES),
        1: random.choice([random.randint(1, 100), random.choice(LOCATIONS), random.choice(TECH_TERMS + SPORT_EVENTS + ECONOMIC_TERMS)]),
        2: random.choice([random.choice(NAMES), random.choice(LOCATIONS), random.choice(TECH_TERMS + SPORT_EVENTS + ECONOMIC_TERMS)])
    }
    date = generate_random_date()
    return f"{date}: {template.format(placeholders[0], placeholders[1], placeholders[2])}"

def display_menu():
    """Display the category selection menu."""
    print("\nVali uudiste kategooria:")
    print("1. Tehnoloogia")
    print("2. Sport")
    print("3. Majandus")
    print("4. Välju")

def main():
    news_list = []
    
    while True:
        display_menu()
        choice = input("Sisesta oma valik (1-4): ")
        
        categories = {"1": "Tehnoloogia", "2": "Sport", "3": "Majandus"}
        if choice == "4":
            print("Programmist väljumine.")
            break
        
        if choice not in categories:
            print("Vigane valik. Proovi uuesti.")
            continue
        
        category = categories[choice]
        
        try:
            num_news = int(input("Mitu uudist genereerida? (1-10): "))
            if not 1 <= num_news <= 10:
                print("Palun sisesta number vahemikus 1 kuni 10.")
                continue
        except ValueError:
            print("Palun sisesta kehtiv number.")
            continue
        
        news_list = [generate_news(category) for _ in range(num_news)]
        print(f"\nGenereeritud uudised ({len(news_list)}):")
        for news in news_list:
            print(news)
        
        while True:
            print(f"\nPraegu on nimekirjas {len(news_list)} uudist.")
            action = input("Mida soovid teha? (lisa/taasgenereeri/välju): ").lower()
            
            if action == "lisa":
                custom_news = input("Sisesta uudise sisu: ")
                date = generate_random_date()
                news_list.append(f"{date}: {custom_news}")
                print(f"\nUuendatud uudiste nimekiri ({len(news_list)}):")
                for news in news_list:
                    print(news)
            
            elif action == "taasgenereeri":
                try:
                    num_news = int(input("Mitu uudist uuesti genereerida? (1-10): "))
                    if not 1 <= num_news <= 10:
                        print("Palun sisesta number vahemikus 1 kuni 10.")
                        continue
                except ValueError:
                    print("Palun sisesta kehtiv number.")
                    continue
                news_list = [generate_news(category) for _ in range(num_news)]
                print(f"\nTaasgenereeritud uudised ({len(news_list)}):")
                for news in news_list:
                    print(news)
            
            elif action == "välju":
                break
            
            else:
                print("Vigane tegevus. Vali 'lisa', 'taasgenereeri' või 'välju'.")

if __name__ == "__main__":
    main()