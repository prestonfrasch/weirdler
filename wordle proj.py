import random

# ------------------------------------------------------------
# Store themes and word lists in a dictionary.
# ------------------------------------------------------------

themes = {
    "Animals": [

        # Mammals
            # (Domistic)
        "Hamster", "Sheep", "Cow", "Pig", "Hedgehog", "Ferret", "Rabbit",
        "Guinea Pig", "Chinchilla", "Sugar Glider", "Dog", "Cat", "Horse",
        "Goat",  
            # (Arfican)
        "Giraffe", "Capybara", "Zebra", "Antelope", "Cheetah", "Jaguar", "Lion",
        "Elephant", "Buffalo", "Hyena", "Badger", "Meerkat", "Armadillo", "Rhino", 
        "Tapir",
            # (North American)
        "Porcupine",  "Wolf", "Brown Bear", "Deer", "Raccoon",  "Opossum", "Skunk", "Coyote",
        "Otter", "Bison", "Moose", "Rat", "Mouse", "Squirrel", "Beaver", "Weasel", "Mole", "Fox",
            # (Australian)
        "Sloth", "Kangaroo", "Koala", "Wombat", "Wallaby", "Platypus", "Echidna",
            # (Monkeys)
        "Chimpanzee", "Gorilla", "Baboon", "Lemur", 
            # (Other)
        "Bat", "Polar Bear", 
        # Reptiles
        "Iguana", "Python", "Anaconda", "Chameleon", "Gecko", "Rattlesnake",
        # Fish
        "Koi", "Goldfish", "Shark", "Dolphin", "Octopus", "Eel", "whale", "Narwhal", "Seahorse",
        "Clownfish", "Tuna", "Salmon", "Trout", "Carp", "Catfish", "Barracuda", "Swordfish",
        "Manta Ray", "Stingray", "Pufferfish", "Angelfish", "Bluga", "Orca", 
        # Birds
        "Owl", "Eagle", "Pigeon", "Parrot", "Penguin", "Flamingo", "Hawk", "Woodpecker", 
        "Chicken", "Duck", "Goose", "Swan", "Turkey", "Vulture", "Seagull", "Pelican", "Crane",
        "Toucan", "Macaw", "Canary", "Finch", 
        # Mythical Animals
        "Phoenix", "Unicorn", "Dragon", "Qilin", "Griffin", "Hippogriff", "Basilisk"
    ],

    "Dog Breeds": [
        "Labrador", "Poodle", "Bulldog", "Beagle", "Chihuahua", "Dachshund",
        "Boxer", "Rottweiler", "German Shepherd", "Golden Retriever", "Siberian Husky",
        "Great Dane", "Doberman", "Corgi", "Shih Tzu", "Mastiff", "Saint Bernard",
        "Border Collie", "Australian Shepherd", "Basset Hound", "Plot Hound", "Bull Terrier"
    ],

    "Cat Breeds": [
        "Siamese", "Persian", "Maine Coon", "Ragdoll", "Bengal", "Sphynx",
        "British Shorthair", "Abyssinian", "Scottish Fold", "Birman",
        "Oriental Shorthair", "Devon Rex", "Norwegian Forest", "Russian Blue",
        "Turkish Angora", "Egyptian Mau", "Tonkinese", "Himalayan", "Savannah"
    ],

    "Home Furniture/Appliances": [
        "Couch", "Chair", "Table", "Fridge", "Television", "Bed", "Coffee Table",
        "Rug", "Sofa", "Stove", "Toaster", "Blender", "Microwave", "Washer",
        "Dryer", "Dishwasher", "Dresser", "Air Conditioner", "Oven", "Air Fryer"
    ],

    "Christmas": [
        "Tree", "Star", "Angel", "Baby", "Snow", "Sled", "Manger", "Carols",
        "Holly", "Ornament", "Mistletoe", "Gifts", "Stocking", "Candy Cane",
        "Bells", "Candles", "Santa", "Wreath", "Gingerbread", "Advent",
        "Reindeer", "Elf", "Nutcracker", "Presents", "Snowman", "Sleigh"
    ],

    "Vehicles": [
        "Car", "Plane", "Train", "Subway", "Truck", "Jet", "Bus", "Boat",
        "Helicopter", "Yacht", "Bullet Train", "Double Decker Bus", "Tram",
        "Motorcycle", "Bicycle", "Ambulance", "Fire Truck", "Police Car",
        "Skateboard", "Scooter", "Spaceship"
    ],

    "Landmarks": [
        "Mount Rushmore", "Washington Monument", "Niagara Falls",
        "Grand Canyon", "Yellowstone", "Old Faithful", "Badlands",
        "Eiffel Tower", "Statue of Liberty", "Golden Gate Bridge",
        "Leaning Tower of Pisa", "Pyramids of Giza", "Taj Mahal",
        "Easter Island", "Stonehenge", "Colosseum", "Big Ben",
        "Spinx", "Christ the Redeemer", "Sydney Opera House"
    ], 

    "Instruments": [
        "Guitar", "Piano", "Violin", "Drums", "Flute", "Saxophone",
        "Trumpet", "Cello", "Harp", "Trombone", "Clarinet", "Oboe",
        "Bassoon", "Accordion", "Banjo", "Mandolin", "Ukulele",
        "Xylophone", "Marimba", "Conga", "Bongo"
    ],
    
    "Human Anatomy": [
        "Femur", "Tibia", "Fibula", "Humerus", "Radius", "Ulna",
        "Scapula", "Clavicle", "Sternum", "Patella", "Cranium",
        "Mandible", "Pelvis", "Vertebrae", "Carpals", "Tarsals",
        "Phalanges", "Ribs", "Skull",  "Heart", "Lungs", "Liver",
        "Kidneys", "Brain", "Stomach", "Intestines"
    ],

    "Food": [
        "Pizza", "Burger", "Pasta", "Sushi", "Taco", "Salad", "Steak",
        "Soup", "Sandwich", "Fries", "Curry", "Dumplings", "Paella",
        "Quiche", "Risotto", "Gnocchi", "Falafel", "Kebab", "Ramen",
        "Burrito", "Waffles", "Pancakes", "Omelette", "Casserole",
        "Lasagna", "Chili"
    ],

    "Resturants": [
        "McDonalds", "Burger King", "Wendys", "Taco Bell", "KFC",
        "Subway", "Pizza Hut", "Dominos", "Chipotle", "Olive Garden",
        "Red Lobster", "Chilis", "Applebees", "Paneras", "Dunkin",
        "Starbucks", "Popeyes", "Five Guys", "In n Out", "Shake Shack"
    ],

    "World Countries": [
        "Afghanistan", "Albania", "Algeria", "Andorra", "Angola", "Antigua and Barbuda", "Argentina",
        "Armenia", "Australia", "Austria", "Azerbaijan", "Bahamas", "Bahrain", "Bangladesh",
        "Barbados", "Belarus", "Belgium", "Belize", "Benin", "Bhutan", "Bolivia", "Bosnia and Herzegovina",
        "Botswana", "Brazil", "Brunei", "Bulgaria", "Burkina Faso", "Burundi", "Cape Verde", "Cambodia",
        "Cameroon", "Canada", "Central African Republic", "Chad", "Chile", "China", "Colombia", "Comoros",
        "Congo", "Costa Rica", "Cote d'Ivoire", "Croatia", "Cuba", "Cyprus", "Czechia", "Denmark",
        "Djibouti", "Dominica", "Dominican Republic", "Ecuador", "Egypt", "El Salvador", "Equatorial Guinea",
        "Eritrea", "Estonia", "Eswatini", "Ethiopia", "Fiji", "Finland", "France", "Gabon", "Gambia", "Georgia",
        "Germany", "Ghana", "Greece", "Grenada", "Guatemala", "Guinea", "Guinea-Bissau", "Guyana", "Haiti",
        "Honduras", "Hungary", "Iceland", "India", "Indonesia", "Iran", "Iraq", "Ireland", "Israel", "Italy",
        "Jamaica", "Japan", "Jordan", "Kazakhstan", "Kenya", "Kiribati", "Kuwait", "Kyrgyzstan", "Laos",
        "Latvia", "Lebanon", "Lesotho", "Liberia", "Libya", "Liechtenstein", "Lithuania", "Luxembourg",
        "Madagascar", "Malawi", "Malaysia", "Maldives", "Mali", "Malta", "Marshall Islands", "Mauritania",
        "Mauritius", "Mexico", "Micronesia", "Moldova", "Monaco", "Mongolia", "Montenegro", "Morocco",
        "Mozambique", "Myanmar", "Namibia", "Nauru", "Nepal", "Netherlands", "New Zealand", "Nicaragua",
        "Niger", "Nigeria", "North Korea", "North Macedonia", "Norway", "Oman", "Pakistan", "Palau",
        "Panama", "Papua New Guinea", "Paraguay", "Peru", "Philippines", "Poland", "Portugal", "Qatar",
        "Romania", "Russia", "Rwanda", "Saint Kitts and Nevis", "Saint Lucia", "Samoa", "San Marino", 
        "Saudi Arabia", "Senegal", "Serbia", "Seychelles", "Sierra Leone", "Singapore", "Slovakia",
        "Slovenia", "Solomon Islands", "Somalia", "South Africa", "South Korea", "South Sudan", "Spain",
        "Sri Lanka", "Sudan", "Suriname", "Sweden", "Switzerland", "Syria", "Taiwan", "Tajikistan", "Tanzania",
        "Thailand", "Timor-Leste", "Togo", "Tonga", "Trinidad and Tobago", "Tunisia", "Turkey", "Turkmenistan",
        "Tuvalu", "Uganda", "Ukraine", "United Arab Emirates", "United Kingdom", "United States", "Uruguay",
        "Uzbekistan", "Vanuatu", "Vatican City", "Venezuela", "Vietnam", "Yemen", "Zambia", "Zimbabwe", "Palestine"
    ],

    "U.S. States": [
        "Ohio", "California", "Texas", "Florida", "New York", "Pennsylvania",
        "Illinois", "Michigan", "Georgia", "North Carolina", "New Jersey",
        "Virginia", "Washington", "Arizona", "Massachusetts", "Tennessee",
        "Indiana", "Missouri", "Maryland", "Wisconsin", "Colorado", "Minnesota",
        "South Carolina", "Alabama", "Louisiana", "Kentucky", "Oregon", "Oklahoma",
        "Connecticut", "Iowa", "Utah", "Nevada", "Arkansas", "Mississippi", "Kansas",
        "New Mexico", "Nebraska", "West Virginia", "Idaho", "Hawaii", "Maine",
        "New Hampshire", "Montana", "Rhode Island", "Delaware", "South Dakota", "North Dakota",
        "Alaska", "Vermont", "Wyoming"
    ]

}

# ------------------------------------------------------------
# Allow the user to pick a theme (or pick one at random)
# ------------------------------------------------------------
def choose_theme_interactive():
    keys = list(themes.keys())
    print("Available themes:")
    for i, k in enumerate(keys, start=1):
        print(f"  {i}. {k}")
    choice = input("Choose a theme by number or name (press Enter for random): ").strip()
    if not choice:
        return random.choice(keys)
    # try number
    if choice.isdigit():
        idx = int(choice) - 1
        if 0 <= idx < len(keys):
            return keys[idx]
        else:
            print("Number out of range, picking randomly.")
            return random.choice(keys)
    # try name (case-insensitive)
    for k in keys:
        if k.lower() == choice.lower():
            return k
    # fallback: try partial match
    matches = [k for k in keys if choice.lower() in k.lower()]
    if len(matches) == 1:
        return matches[0]
    if matches:
        print("Multiple themes match, choosing the first:", matches[0])
        return matches[0]
    print("No matching theme found, picking randomly.")
    return random.choice(keys)


chosen_theme = choose_theme_interactive()
chosen_word = random.choice(themes[chosen_theme])

print(f"Random Theme: {chosen_theme}")
print(f"Random Word: {chosen_word}")
