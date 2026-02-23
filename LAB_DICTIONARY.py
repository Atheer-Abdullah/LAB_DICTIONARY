phone_book = {
    "0568323222": "Amal",
    "0522222232": "Mohammed",
    "0532335983": "Khadijah",
    "0545341144": "Abdullah",
    "0545534556": "Rawan",
    "0560664566": "Faisal",
    "0567917077": "Layla"
}

owner_number = input("Enter owner number: ")


if not owner_number.isdigit() or len(owner_number) != 10:
    print("This is invalid number")

elif owner_number in phone_book:
    print("Owner:", phone_book[owner_number])

else:
    print("Sorry, the number is not found")