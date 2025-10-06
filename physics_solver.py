# Physics Cheatsheet and Solver for NumWorks
# By Jules

def display_menu():
    print("--------------------")
    print("  PHYSICS HELPER  ")
    print("--------------------")
    print("1. Equation Solvers")
    print("2. Graphing Concepts")
    print("3. Key Definitions")
    print("4. Exit")
    print("--------------------")

def get_float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")

def solve_v_avg_dx_dt():
    print("\n--- Solver: v_avg = dx / dt ---")
    print("What do you want to solve for?")
    print("1. Average velocity (v_avg)")
    print("2. Displacement (dx)")
    print("3. Time interval (dt)")

    choice = input("Select an option (1-3): ")

    if choice == '1':
        dx = get_float_input("Enter displacement (dx): ")
        dt = get_float_input("Enter time interval (dt): ")
        if dt == 0:
            print("\nError: Time interval (dt) cannot be zero.")
        else:
            v_avg = dx / dt
            print(f"\nResult: Average velocity (v_avg) = {v_avg}")
    elif choice == '2':
        v_avg = get_float_input("Enter average velocity (v_avg): ")
        dt = get_float_input("Enter time interval (dt): ")
        dx = v_avg * dt
        print(f"\nResult: Displacement (dx) = {dx}")
    elif choice == '3':
        dx = get_float_input("Enter displacement (dx): ")
        v_avg = get_float_input("Enter average velocity (v_avg): ")
        if v_avg == 0:
            print("\nError: Average velocity (v_avg) cannot be zero for this calculation.")
        else:
            dt = dx / v_avg
            print(f"\nResult: Time interval (dt) = {dt}")
    else:
        print("\nInvalid selection.")
    input("\nPress Enter to return.")

def solve_v_avg_v0_vf():
    print("\n--- Solver: v_avg = 0.5 * (v0 + vf) ---")
    print("What do you want to solve for?")
    print("1. Average velocity (v_avg)")
    print("2. Initial velocity (v0)")
    print("3. Final velocity (vf)")

    choice = input("Select an option (1-3): ")

    if choice == '1':
        v0 = get_float_input("Enter initial velocity (v0): ")
        vf = get_float_input("Enter final velocity (vf): ")
        v_avg = 0.5 * (v0 + vf)
        print(f"\nResult: Average velocity (v_avg) = {v_avg}")
    elif choice == '2':
        v_avg = get_float_input("Enter average velocity (v_avg): ")
        vf = get_float_input("Enter final velocity (vf): ")
        v0 = (2 * v_avg) - vf
        print(f"\nResult: Initial velocity (v0) = {v0}")
    elif choice == '3':
        v_avg = get_float_input("Enter average velocity (v_avg): ")
        v0 = get_float_input("Enter initial velocity (v0): ")
        vf = (2 * v_avg) - v0
        print(f"\nResult: Final velocity (vf) = {vf}")
    else:
        print("\nInvalid selection.")
    input("\nPress Enter to return.")

def solvers_menu():
    while True:
        print("\n--- Equation Solvers ---")
        print("1. v_avg = dx / dt")
        print("2. v_avg = 0.5 * (v0 + vf)")
        print("3. Back to main menu")
        print("--------------------")
        try:
            choice = input("Select a solver (1-3): ")
            if choice == '1':
                solve_v_avg_dx_dt()
            elif choice == '2':
                solve_v_avg_v0_vf()
            elif choice == '3':
                break
            else:
                print("\nInvalid choice. Please enter a number from 1 to 3.\n")
        except Exception as e:
            print(f"\nAn error occurred: {e}. Please try again.\n")

def display_graphing_concepts():
    print("\n--- Position vs. Time Graphs ---")
    print("* Slope = velocity (dx/dt)")
    print("* Horizontal line = at rest")
    print("* Steeper slope = faster motion")
    print("* Positive slope = positive direction")
    print("* Negative slope = negative direction")
    print("\n--- Velocity vs. Time Graphs ---")
    print("* Area under curve = displacement")
    print("* Horizontal line = constant velocity")
    print("* Above x-axis = positive velocity")
    print("* Below x-axis = negative velocity")
    input("\nPress Enter to return to the menu.")

def display_definitions():
    print("\n--- Key Definitions ---")
    print("* Position (x): Location vs. reference point.")
    print("* Displacement (dx): Change in position (x - x0).")
    print("* Distance (d): Total path traveled (always +).")
    print("* Velocity (v): Rate of change of position.")
    print("* Avg. Velocity: Displacement / time.")
    print("* Avg. Speed: Distance / time.")
    input("\nPress Enter to return to the menu.")

def main():
    while True:
        display_menu()
        try:
            choice = input("Select an option (1-4): ")
            if choice == '1':
                solvers_menu()
            elif choice == '2':
                display_graphing_concepts()
            elif choice == '3':
                display_definitions()
            elif choice == '4':
                print("Exiting. Good luck on your test!")
                break
            else:
                print("\nInvalid choice. Please enter a number from 1 to 4.\n")
        except (Exception) as e:
            print(f"\nAn error occurred: {e}. Please try again.\n")

# This is the standard entry point for NumWorks scripts
if __name__ == "__main__":
    main()