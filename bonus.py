weather_data = {}


city = input("Enter city name: ")
date = input("Enter date: ")
temperature = input("Enter temperature: ")
humidity = input("Enter humidity: ")
condition = input("Enter condition: ")

weather_data[city] = {
    date: {
        "temperature": temperature,
        "humidity": humidity,
        "condition": condition
    }
}


search_city = input("Enter city to search: ")

if search_city in weather_data:
    print(weather_data[search_city])
else:
    print("City not found")