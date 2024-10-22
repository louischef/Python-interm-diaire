from geometrie.triangle import *
from ticket_price import *
from geometrie.triangle import *
from geometrie.circle import *


def main():
    weeks = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    ages = [1,5,12,13,15,30,59,60,61]
    for day in weeks:
        for age in ages:
            
            price = calculate_movie_ticket_price(age, day)
            print(f"The price for the age {age} and for the movie ticket is ${round(price,2)} on a {day}.")
    
    
    result = determine_triangle_type(3,14,3)
    print(result)
    circle_diameter = 10
    print(f"Perimetre {calculate_circle_perimeter(circle_diameter)}")
    print(f"Aire {calculate_circle_area(circle_diameter)}")
    print("------------------------------------------------------------")
    rectangle_l = 20
    rectangle_h = 5
    print(f"Perimetre {calculate_rectangle_perimeter(circle_diameter)}")
    print(f"Aire {calculate_circle_area(circle_diameter)}")
    print("------------------------------------------------------------")
    triangle_s1 = 3
    triangle_s2 = 3
    triangle_s3 = 3
    
    calcul = input("quel est votre calcul à résoudre ?")

    
if __name__ == "__main__":
    main()