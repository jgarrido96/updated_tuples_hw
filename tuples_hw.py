
# 1. Tuple Mastery in Python

# Task 1: Formatting Flight Itineraries

new_itinerary = ()
itineraries = ()
def format_itinerary(index, routes):
    itinerary = f"Itinerary {str(index + 1)}: {routes[0]} - From {routes[1]} to {routes[2]}."
    return itinerary

def flight_itinerary():    
    itinerary_count = 1
    while True:
        traveler_name = input("Please enter the name of the person flying today: or type 'quit' ")
        if traveler_name == 'quit':
            break
        origin = input("Where are you coming from? ")
        destination = input("Where would you like to go? ")
        if itinerary_count == 1:
            itineraries = (traveler_name, origin, destination)
        else:
            new_itinerary = (traveler_name, origin, destination)
            itineraries = ((itineraries,) + (new_itinerary,))
            print(itineraries)
        itinerary_count += 1
    for index in range(len(itineraries)):
        formatted_itinerary = format_itinerary(index, itineraries[index])
        print(formatted_itinerary)

# flight_itinerary()

print('\n')

# 2. Python Data Structure Challenges in Real-World Scenarios

# Task 1: Library System Enhancement

library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]
def library_times():
    while True:
        user_input = input("Welcome to the library! What would you like to do? (add, view, leave) ")
        try:
            if user_input == "leave":
                break
            elif user_input == "add":
                title_input = input("What book would you like to add? ")
                author_input = input("Who is the author of this book? ")
                if (title_input, author_input) not in library:
                    library.append((title_input, author_input))
                    print(f"{title_input} by {author_input} was added to the library!")
                else:
                    print("This title is already here!")
            elif user_input == "view":
                for item in library:
                    print(item)
        except:
            pass

# library_times()

# 3. Python Loops and Tuples in Analytical Applications

# Task 1: Stock Market Data Analysis
        
# Create a function to calculate the average closing price of a specific stock symbol over all dates.
# Ensure your solution handles cases where the stock symbol does not exist in the data.

stock_data = [
    ("AAPL", "2024-01-01", 130.0),
    ("AAPL", "2024-02-01", 132.0),
    ("AAPL", "2024-03-01", 136.0),
    ("MSFT", "2024-01-01", 220.0),
    ("MSFT", "2024-02-01", 225.0),
    ("MSFT", "2024-03-01", 221.0),
    ("NVDA", "2024-01-01", 894.52),
    ("NVDA", "2024-02-01", 893.33),
    ("NVDA", "2024-03-01", 896.77),
    ("AMZN", "2024-01-01", 180.69),
    ("AMZN", "2024-02-01", 185.88),
    ("AMZN", "2024-03-01", 187.99),
    ]


def company_list():
    stock_list = []
    for stock in range(len(stock_data)):
        stock_list.append(stock_data[stock][0])
    companies = tuple(set(stock_list))
    return companies

def stock_analysis():
    avg = 0
    avg_counter = 0
    try:
        while True:
            companies = company_list()
            print(f"\nCompanies:\n{companies}")
            stock_input = input("\nWhich stock symbol would you like to calculate the average of? Type 'quit' to quit. ")
            if stock_input == "quit":
                break
            elif stock_input not in companies:
                print("\nPlease select a stock symbol from the list")
            elif stock_input in companies:
                for stock in stock_data:
                    if stock[0] == stock_input:
                        avg = avg + stock[2]
                        avg_counter += 1
                avg = avg / avg_counter
                print(f"\nThe average closing price for {stock_input} was {str(avg)} for the last quarter in record.")
    except Exception as e:
        print(f"An error occured: {e}")

stock_analysis()