class RecommendationSystem:
    def __init__(self, items):
        self.items = items

    def getRecommendations(self, category, priceRange):
        recommendedItems = []

        for item in self.items:
            if item['category'] == category and priceRange[0] <= item['price'] <= priceRange[1]:
                recommendedItems.append(item['name'])

        return recommendedItems

bookItems = [
    {'name': 'Thus Spoke Zarathustra', 'category': 'philosophy', 'price': 28},
    {'name': 'Critique of Pure Reason', 'category': 'philosophy', 'price': 24},
    {'name': 'The Stranger', 'category': 'philosophy', 'price': 19},
    {'name': '1984', 'category': 'science fiction', 'price': 26},
    {'name': 'Brave New World', 'category': 'science fiction', 'price': 27},
    {'name': 'Neuromancer', 'category': 'science fiction', 'price': 21},
    {'name': 'Dracula', 'category': 'horror', 'price': 16},
    {'name': 'Frankenstein', 'category': 'horror', 'price': 20},
    {'name': 'Pet Sematary', 'category': 'horror', 'price': 17},
    {'name': 'The Hobbit', 'category': 'fantasy', 'price': 23},
    {'name': 'A Game of Thrones', 'category': 'fantasy', 'price': 25},
    {'name': 'The Lord of the Rings', 'category': 'fantasy', 'price': 29},
    {'name': 'Sapiens: A Brief History of Humankind', 'category': 'history', 'price': 18},
    {'name': 'Guns, Germs, and Steel', 'category': 'history', 'price': 22},
    {'name': 'The Rise and Fall of the Third Reich', 'category': 'history', 'price': 30},
    {'name': 'To Kill a Mockingbird', 'category': 'fiction', 'price': 20},
    {'name': 'The Great Gatsby', 'category': 'fiction', 'price': 24},
    {'name': 'Pride and Prejudice', 'category': 'fiction', 'price': 26},
    {'name': 'The Catcher in the Rye', 'category': 'fiction', 'price': 23},
    {'name': "Harry Potter and the Sorcerer's Stone", 'category': 'fiction', 'price': 28},
    {'name': 'Crime and Punishment', 'category': 'fiction', 'price': 27},
    {'name': 'The Art of War', 'category': 'philosophy', 'price': 29},
    {'name': 'Meditations', 'category': 'philosophy', 'price': 25},
    {'name': 'The Communist Manifesto', 'category': 'philosophy', 'price': 21},
    {'name': "The Hitchhiker's Guide to the Galaxy", 'category': 'science fiction', 'price': 20},
    {'name': 'The Martian Chronicles', 'category': 'science fiction', 'price': 18},
    {'name': 'Snow Crash', 'category': 'science fiction', 'price': 16},
    {'name': 'The Stand', 'category': 'horror', 'price': 19},
    {'name': 'IT', 'category': 'horror', 'price': 30},
    {'name': 'The Haunting of Hill House', 'category': 'horror', 'price': 17},
    {'name': 'The Odyssey', 'category': 'classics', 'price': 22},
    {'name': 'The Iliad', 'category': 'classics', 'price': 26},
    {'name': 'Don Quixote', 'category': 'classics', 'price': 23},
    {'name': 'Les Misérables', 'category': 'classics', 'price': 29},
    {'name': 'The Picture of Dorian Gray', 'category': 'classics', 'price': 28},
    {'name': 'The Divine Comedy', 'category': 'classics', 'price': 24},
    {'name': 'Fahrenheit 451', 'category': 'science fiction', 'price': 20},
    {'name': 'I, Robot', 'category': 'science fiction', 'price': 18},
    {'name': 'The Time Machine', 'category': 'science fiction', 'price': 16},
    {'name': 'The War of the Worlds', 'category': 'science fiction', 'price': 19},
    {'name': 'The Invisible Man', 'category': 'science fiction', 'price': 17},
    {'name': 'Jurassic Park', 'category': 'science fiction', 'price': 21},
    {'name': 'American Gods', 'category': 'fantasy', 'price': 22},
    {'name': 'The Name of the Wind', 'category': 'fantasy', 'price': 26},
    {'name': 'The Wheel of Time', 'category': 'fantasy', 'price': 24},
    {'name': 'The Dark Tower', 'category': 'fantasy', 'price': 27},
    {'name': 'A Song of Ice and Fire', 'category': 'fantasy', 'price': 30},
    {'name': 'The Color Purple', 'category': 'fiction', 'price': 20},
    {'name': "The Handmaid's Tale", 'category': 'fiction', 'price': 24},
    {'name': 'The Road', 'category': 'fiction', 'price': 28},
    {'name': 'The Book Thief', 'category': 'fiction', 'price': 23},
    {'name': 'Life of Pi', 'category': 'fiction', 'price': 25},
    {'name': 'One Hundred Years of Solitude', 'category': 'fiction', 'price': 29},
    {'name': 'The Count of Monte Cristo', 'category': 'classics', 'price': 21},
    {'name': 'Moby-Dick', 'category': 'classics', 'price': 20},
    {'name': 'War and Peace', 'category': 'classics', 'price': 22},
    {'name': 'Anna Karenina', 'category': 'classics', 'price': 23},
    {'name': 'Madame Bovary', 'category': 'classics', 'price': 24},
    {'name': 'Wuthering Heights', 'category': 'classics', 'price': 25},
    {'name': 'The Brothers Karamazov', 'category': 'fiction', 'price': 26},
    {'name': 'Catch-22', 'category': 'fiction', 'price': 27},
    {'name': 'A Clockwork Orange', 'category': 'fiction', 'price': 28},
    {'name': 'Gone with the Wind', 'category': 'fiction', 'price': 29},
    {'name': 'Catch-22', 'category': 'fiction', 'price': 27},
    {'name': 'A Clockwork Orange', 'category': 'fiction', 'price': 28},
    {'name': 'Gone with the Wind', 'category': 'fiction', 'price': 29},
    {'name': 'The Sun Also Rises', 'category': 'classics', 'price': 30},
    {'name': 'The Grapes of Wrath', 'category': 'classics', 'price': 30}
]

movieItems = [
    {'name': 'The Shawshank Redemption', 'category': 'drama', 'price': 22},
    {'name': 'Forrest Gump', 'category': 'drama', 'price': 19},
    {'name': 'Fight Club', 'category': 'drama', 'price': 21},
    {'name': 'Schindler\'s List', 'category': 'drama', 'price': 23},
    {'name': 'The Lion King', 'category': 'animation', 'price': 18},
    {'name': 'Toy Story', 'category': 'animation', 'price': 16},
    {'name': 'Finding Nemo', 'category': 'animation', 'price': 20},
    {'name': 'The Avengers', 'category': 'action', 'price': 24},
    {'name': 'The Dark Knight', 'category': 'action', 'price': 25},
    {'name': 'Avatar', 'category': 'action', 'price': 28},
    {'name': 'Jurassic Park', 'category': 'action', 'price': 26},
    {'name': 'The Social Network', 'category': 'drama', 'price': 22},
    {'name': 'The Departed', 'category': 'crime', 'price': 20},
    {'name': 'Goodfellas', 'category': 'crime', 'price': 21},
    {'name': 'Seven', 'category': 'crime', 'price': 19},
    {'name': 'The Sixth Sense', 'category': 'thriller', 'price': 18},
    {'name': 'Se7en', 'category': 'thriller', 'price': 19},
    {'name': 'Gone Girl', 'category': 'thriller', 'price': 21},
    {'name': 'The Usual Suspects', 'category': 'thriller', 'price': 20},
    {'name': 'The Conjuring', 'category': 'horror', 'price': 17},
    {'name': 'A Nightmare on Elm Street', 'category': 'horror', 'price': 16},
    {'name': 'Saw', 'category': 'horror', 'price': 18},
    {'name': 'Halloween', 'category': 'horror', 'price': 15},
    {'name': 'The Exorcism of Emily Rose', 'category': 'horror', 'price': 17},
    {'name': 'The Exorcist', 'category': 'horror', 'price': 18},
    {'name': 'Paranormal Activity', 'category': 'horror', 'price': 16},
    {'name': 'The Blair Witch Project', 'category': 'horror', 'price': 15},
    {'name': 'Psycho', 'category': 'horror', 'price': 19},
    {'name': 'Insidious', 'category': 'horror', 'price': 17},
    {'name': 'Annabelle', 'category': 'horror', 'price': 16},
    {'name': 'The Babadook', 'category': 'horror', 'price': 18},
    {'name': 'The Grudge', 'category': 'horror', 'price': 15},
    {'name': 'The Ring', 'category': 'horror', 'price': 16},
    {'name': 'Silent Hill', 'category': 'horror', 'price': 17},
    {'name': 'The Others', 'category': 'horror', 'price': 18},
    {'name': 'The Sixth Sense', 'category': 'horror', 'price': 19},
    {'name': 'The Texas Chain Saw Massacre', 'category': 'horror', 'price': 20},
    {'name': 'Night of the Living Dead', 'category': 'horror', 'price': 21},
    {'name': 'Evil Dead', 'category': 'horror', 'price': 22},
    {'name': 'The Hills Have Eyes', 'category': 'horror', 'price': 23},
    {'name': 'The Descent', 'category': 'horror', 'price': 24},
    {'name': 'The Cabin in the Woods', 'category': 'horror', 'price': 25},
    {'name': 'Hereditary', 'category': 'horror', 'price': 26},
    {'name': 'Get Out', 'category': 'horror', 'price': 27},
    {'name': 'A Quiet Place', 'category': 'horror', 'price': 28},
    {'name': 'Us', 'category': 'horror', 'price': 29},
    {'name': 'The Conjuring 2', 'category': 'horror', 'price': 30}
]

productItems = [
    {'name': 'Sony PlayStation 5', 'category': 'electronics', 'price': 500},
    {'name': 'Microsoft Xbox Series X', 'category': 'electronics', 'price': 500},
    {'name': 'Dell XPS 15 Laptop', 'category': 'electronics', 'price': 1500},
    {'name': 'Apple Watch Series 6', 'category': 'electronics', 'price': 400},
    {'name': 'Bose QuietComfort 35 II Headphones', 'category': 'electronics', 'price': 300},
    {'name': 'Canon EOS R5 Camera', 'category': 'electronics', 'price': 3500},
    {'name': 'GoPro Hero 9', 'category': 'electronics', 'price': 450},
    {'name': 'Amazon Echo Dot', 'category': 'electronics', 'price': 50},
    {'name': 'Samsung Galaxy Tab S7', 'category': 'electronics', 'price': 650},
    {'name': 'LG OLED CX Series TV', 'category': 'electronics', 'price': 2000},
    {'name': 'Google Pixel 5', 'category': 'electronics', 'price': 700},
    {'name': 'iPad Air', 'category': 'electronics', 'price': 600},
    {'name': 'Sony WH-1000XM4 Headphones', 'category': 'electronics', 'price': 350},
    {'name': 'Dyson V11 Cordless Vacuum Cleaner', 'category': 'home appliances', 'price': 600},
    {'name': 'iRobot Roomba 960', 'category': 'home appliances', 'price': 500},
    {'name': 'Phillips Hue Starter Kit', 'category': 'home appliances', 'price': 200},
    {'name': 'Samsung Family Hub Refrigerator', 'category': 'home appliances', 'price': 3000},
    {'name': 'LG Front Load Washing Machine', 'category': 'home appliances', 'price': 1000},
    {'name': 'Nest Learning Thermostat', 'category': 'home appliances', 'price': 250},
    {'name': 'Weber Genesis II Gas Grill', 'category': 'home appliances', 'price': 1000},
    {'name': 'Cuisinart 14-Cup Food Processor', 'category': 'kitchen appliances', 'price': 200},
    {'name': 'Vitamix 5200 Blender', 'category': 'kitchen appliances', 'price': 400},
    {'name': 'Keurig K-Elite Coffee Maker', 'category': 'kitchen appliances', 'price': 150},
    {'name': 'Breville Smart Oven Air Fryer', 'category': 'kitchen appliances', 'price': 300},
    {'name': 'KitchenAid Classic Stand Mixer', 'category': 'kitchen appliances', 'price': 250},
    {'name': 'Instant Pot Duo Nova Pressure Cooker', 'category': 'kitchen appliances', 'price': 120},
    {'name': 'NutriBullet Blender', 'category': 'kitchen appliances', 'price': 80},
    {'name': 'Samsung Galaxy S20', 'category': 'electronics', 'price': 800},
    {'name': 'Apple MacBook Air', 'category': 'electronics', 'price': 1000},
    {'name': 'Sony 65" 4K OLED TV', 'category': 'electronics', 'price': 2500},
    {'name': 'Nintendo Switch', 'category': 'electronics', 'price': 300},
    {'name': 'Fitbit Versa 3', 'category': 'electronics', 'price': 200},
    {'name': 'Garmin Forerunner 945', 'category': 'electronics', 'price': 600},
    {'name': 'Ring Video Doorbell Pro', 'category': 'electronics', 'price': 250},
    {'name': 'Apple AirPods Pro', 'category': 'electronics', 'price': 250},
    {'name': 'Sony A7 III Camera', 'category': 'electronics', 'price': 2000},
    {'name': 'Logitech MX Master 3 Mouse', 'category': 'electronics', 'price': 100},
    {'name': 'Apple iPad Pro', 'category': 'electronics', 'price': 800},
    {'name': 'Microsoft Surface Laptop 3', 'category': 'electronics', 'price': 1200},
    {'name': 'Bose SoundLink Revolve Speaker', 'category': 'electronics', 'price': 200},
    {'name': 'Roku Ultra 2020', 'category': 'electronics', 'price': 100},
    {'name': 'Google Nest Hub Max', 'category': 'electronics', 'price': 230},
    {'name': 'Sonos One Smart Speaker', 'category': 'electronics', 'price': 200},
    {'name': 'DJI Mavic Air 2 Drone', 'category': 'electronics', 'price': 800},
    {'name': 'NVIDIA GeForce RTX 3080', 'category': 'electronics', 'price': 700},
    {'name': 'Corsair K95 RGB Platinum Mechanical Keyboard', 'category': 'electronics', 'price': 200},
    {'name': 'Samsung Galaxy Watch 3', 'category': 'electronics', 'price': 400},
    {'name': 'Amazon Kindle Paperwhite', 'category': 'electronics', 'price': 130}
]



class RecommendationSystem:
    def __init__(self, items):
        self.items = items

    def getRecommendations(self, category, priceRange):
        recommendations = [item['name'] for item in self.items if
                           item['category'] == category and priceRange[0] <= item['price'] <= priceRange[1]]
        return recommendations


def getUserInput():
    print("Welcome to the Recommendation System!")
    print("What would you like to be recommended?")
    print("1. Books")
    print("2. Movies")
    print("3. Products")
    print("Enter 'exit' to quit.")

    choice = input("Enter your choice (1/2/3): ")
    return choice


def main():
    while True:
        choice = getUserInput()

        if choice == 'exit':
            print("Exiting the program.")
            break

        choice = int(choice)

        if choice == 1:
            category = input(
                "What genre of book are you interested in (e.g., philosophy, horror, science fiction)? ").lower()
            minPrice = float(input("Enter minimum price you are willing to pay: "))
            maxPrice = float(input("Enter maximum price you are willing to pay: "))
            priceRange = (minPrice, maxPrice)
            rs = RecommendationSystem(bookItems)
            recommendations = rs.getRecommendations(category, priceRange)

        elif choice == 2:
            category = input("What genre of movie are you interested in (e.g., science fiction, horror, crime)? ").lower()
            minPrice = float(input("Enter minimum price you are willing to pay: "))
            maxPrice = float(input("Enter maximum price you are willing to pay: "))
            priceRange = (minPrice, maxPrice)
            rs = RecommendationSystem(movieItems)
            recommendations = rs.getRecommendations(category, priceRange)

        elif choice == 3:
            category = input("What category of product are you interested in (e.g., electronics, kitchen appliances)? ").lower()
            minPrice = float(input("Enter minimum price you are willing to pay: "))
            maxPrice = float(input("Enter maximum price you are willing to pay: "))
            priceRange = (minPrice, maxPrice)
            rs = RecommendationSystem(productItems)
            recommendations = rs.getRecommendations(category, priceRange)

        else:
            print("Invalid choice!")
            continue

        if recommendations:
            print("\nHere are some recommendations for you:")
            for i, item in enumerate(recommendations, 1):
                print(f"{i}. {item}")
        else:
            print("\nSorry, no items match your preferences.")


if __name__ == "__main__":
    main()
