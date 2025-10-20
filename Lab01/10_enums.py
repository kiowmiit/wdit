from enum import Enum

# class syntax
class DayOfWeek(Enum):
    MONDAY = 0
    TUESDAY = 513
    WEDNESDAY = 199
    THURSDAY = 4
    FRIDAY = 8
    SATURDAY = 3
    SUNDAY = 1

day_of_week = DayOfWeek.TUESDAY
print(f"day_of_week : {day_of_week}")
print(f"day_of_week.name: {day_of_week.name}")
print(f"day_of_week.value : {day_of_week.value}\n")

for i in DayOfWeek:
    print(i)

# functional syntax
Color = Enum('Color', [('RED', 1), ('GREEN', 2), ('BLUE', 3)])

color = Color.BLUE

print(f"\ncolor: {color}")
print(f"color.name: {color.name}")
print(f"color.value: {color.value}")

# przykład użycia z konstrukcją if
if color == Color.BLUE:
    print("color is blue")
elif color == Color.GREEN:
    print("color is green")
else:
    print("color is neither blue nor green")

