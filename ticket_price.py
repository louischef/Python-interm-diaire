    # TODO: Implement a program that determines the price of a movie ticket
    # based on age (child, adult, senior) and day of the week
    # Age categories:
        # Child: 12 years old or younger
        # Adult: Between 13 and 59 years old (inclusive)
        # Senior: 60 years old or older
        
    # Pricing rules:
        # Base ticket price: $12
        # Children and seniors receive a 20% discount
        # On Tuesdays, all tickets are $8 (regardless of age)
        # On weekends (Saturday and Sunday), all tickets have a $2 surcharge
def calculate_movie_ticket_price(age: int, day: str) -> float:
    day = day.lower()
    if day == "tuesday":
        return 8
    price = 12
    if day == "saturday" or day == "sunday":
        price += 2
    if age <= 12 or age >= 60:
        price *= 0.8
    return price
    pass