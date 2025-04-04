import math

def calculate_area():
    print("==================")
    print("Area Calculator 📐")
    print("==================")

    while True:
        print("\n1) Triangle")
        print("2) Rectangle")
        print("3) Square")
        print("4) Circle")
        print("5) Quit")

        shape_choice = input("Which shape: ")

        if shape_choice == '1':  # Triangle
            base = float(input("Base: "))
            height = float(input("Height: "))
            area = (base * height) / 2
            print(f"The area is {area}")

        elif shape_choice == '2':  # Rectangle
            length = float(input("Length: "))
            width = float(input("Width: "))
            area = length * width
            print(f"The area is {area}")

        elif shape_choice == '3':  # Square
            side = float(input("Side: "))
            area = side ** 2
            print(f"The area is {area}")

        elif shape_choice == '4':  # Circle
            radius = float(input("Radius: "))
            area = math.pi * radius ** 2
            print(f"The area is {area}")

        elif shape_choice == '5':  # Quit
            print("Exiting program...")
            break

        else:
            print("Invalid choice, please select a valid option.")

if __name__ == "__main__":
    calculate_area()
