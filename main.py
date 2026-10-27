"""
CS 1430 Assignment 2: The Cost of College

All of your Python for this assignment goes in this file.
The student guide explains what to build. Run check.py to test your work.
"""

# ---- CONSTANTS: do not change ----
SEMESTERS_PER_YEAR = 2
MONTHS_PER_YEAR = 9
CLASS_DAYS_PER_SEMESTER = 75
CS1430_CREDITS = 3
CS1430_MEETINGS_PER_SEMESTER = 45


# ---- FUNCTIONS: replace each return 0 ----

def cost_per_semester(annual_cost):
    """Give back what one semester costs."""
    return annual_cost / SEMESTERS_PER_YEAR


def cost_per_month(annual_cost):
    """Give back what one month of the academic year costs."""
    return annual_cost / MONTHS_PER_YEAR


def cost_per_day(annual_cost):
    """Give back what one( class day costs."""
    return annual_cost / (CLASS_DAYS_PER_SEMESTER * 2)


def cost_per_credit(annual_cost, credits):
    """Give back what one credit costs. credits is the number taken this semester."""
    return annual_cost / (credits * 2)


def cost_per_class(annual_cost, credits):
    """Give back what one 50-minute CS 1430 class meeting costs."""
    return annual_cost / (CS1430_MEETINGS_PER_SEMESTER * 2 * (credits / CS1430_CREDITS))

def how_many_games(annual_cost, cost_per_game):
    """Give back how many games you could have bought instead of going to college this year."""
    return annual_cost / cost_per_game
# ---- PROGRAM ----

def main():
    # Ask for the total cost for one year here.
    college_cost = float(input("What is the total cost of college for one year? "))
    # Then ask for the credits this semester.
    credits_this_semester = int(input("How many credits are you taking this semester? "))
    while True:
        # Show your menu here.
        print("Options:")
        print(" 1. Cost per semester")
        print(" 2. Cost per month")
        print(" 3. Cost per day")
        print(" 4. Cost per credit")
        print(" 5. Cost per class")
        print(" 6. How many games?")
        print(" Q. Quit")
        choice = input("Choose an option: ")

        if choice == "Q":
            print("Goodbye!")
            break

        # Add a branch for each menu option here.
        if choice == "1":
            print(f"Cost per semester: ${cost_per_semester(college_cost):,.2f}")

        elif choice == "2":
            print(f"Cost per month: ${cost_per_month(college_cost):,.2f}")

        elif choice == "3":
            print(f"Cost per day: ${cost_per_day(college_cost):,.2f}")

        elif choice == "4":
            print(f"Cost per credit: ${cost_per_credit(college_cost, credits_this_semester):,.2f}")
            
        elif choice == "5":
            print(f"Cost per class: ${cost_per_class(college_cost, credits_this_semester):,.2f}")

        elif choice == "6":
            cost_per_game = float(input("How much does the next videogame you want to buy cost? "))
            print(f"You could have bought {how_many_games(college_cost, cost_per_game):,.0f} copies of the game instead of going to college this year!")

        else:
            print("You did not choose a valid option. Please try again.")

# ---- LAUNCH: do not change ----
if __name__ == "__main__":
    main()
