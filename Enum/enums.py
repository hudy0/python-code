from enum import Enum

class Day(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7

# Example usage
def is_weekend(day):
    if day in (Day.SATURDAY, Day.SUNDAY):
        return True
    return False

# Test the function
today = Day.SATURDAY
print(f"Is {today.name} a weekend? {'Yes' if is_weekend(today) else 'No'}")
