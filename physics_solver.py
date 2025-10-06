# Physics Cheatsheet and Solver for NumWorks
# By Jules

def display_menu():
    print("--------------------")
    print("  PHYSICS HELPER  ")
    print("--------------------")
    print("1. Equation Solvers")
    print("2. Multi-Step Motion")
    print("3. V-T Graph Area Calc")
    print("4. Graphing Concepts")
    print("5. Key Definitions")
    print("6. Exit")
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
    print("\n--- Position vs. Time (x-t) Graphs ---")
    print("The slope of the line is the velocity.")
    print("  - Positive slope: moving in + direction.")
    print("  - Negative slope: moving in - direction.")
    print("  - Zero slope (horizontal line): at rest.")
    print("  - Steeper slope: faster speed.")
    print("  - Curved line: acceleration.")
    print("  - Change in slope sign: change in direction.")
    print("\n--- Velocity vs. Time (v-t) Graphs ---")
    print("The area under the graph is displacement.")
    print("  - Area above x-axis: positive displacement.")
    print("  - Area below x-axis: negative displacement.")
    print("The value of the line is the velocity.")
    print("  - Line above x-axis: positive velocity.")
    print("  - Line on x-axis: at rest.")
    print("  - Line below x-axis: negative velocity.")
    print("  - Crossing the x-axis: change in direction.")
    input("\nPress Enter to return.")

def display_definitions():
    print("\n--- Key Definitions (Expanded) ---")
    print("Position (x): An object's location relative")
    print("  to a reference point (origin).")
    print("\nDisplacement (dx): The 'as the crow flies'")
    print("  change in position. Formula: x_final - x_initial.")
    print("  It is a vector, so it can be negative.")
    print("\nDistance (d): The total path an object")
    print("  travels. It is always positive.")
    print("\n--- Key Distinction ---")
    print("Avg. Velocity = Displacement / Time")
    print("  (can be negative, depends on direction)")
    print("\nAvg. Speed = Distance / Time")
    print("  (always positive)")
    print("\nExample: You run 2m East, then 1m West.")
    print("  Distance = 2 + 1 = 3m")
    print("  Displacement = 2 + (-1) = 1m East")
    input("\nPress Enter to return.")

def multi_step_motion_calculator():
    print("\n--- Multi-Step Motion Calculator ---")
    segments = []
    while True:
        print(f"\n--- Segment {len(segments) + 1} ---")
        try:
            v = get_float_input("Enter velocity (m/s): ")
            t = get_float_input("Enter time (s): ")
            if t < 0:
                print("Time cannot be negative. Please try again.")
                continue

            segments.append({'v': v, 't': t})

            another = input("Add another segment? (y/n): ").lower()
            if another != 'y':
                break
        except Exception as e:
            print(f"An error occurred: {e}. Please try again.")

    if not segments:
        print("\nNo segments entered.")
        input("Press Enter to return.")
        return

    total_dist = 0
    total_disp = 0
    total_time = 0

    for seg in segments:
        disp = seg['v'] * seg['t']
        total_disp += disp
        total_dist += abs(disp)
        total_time += seg['t']

    print("\n--- Results ---")
    print(f"Total Distance: {total_dist} m")
    print(f"Final Displacement: {total_disp} m")
    print(f"Total Time: {total_time} s")

    if total_time > 0:
        avg_speed = total_dist / total_time
        avg_velo = total_disp / total_time
        print(f"Average Speed: {avg_speed:.2f} m/s")
        print(f"Average Velocity: {avg_velo:.2f} m/s")
    else:
        print("Cannot calculate averages with zero total time.")

    input("\nPress Enter to return.")

def vt_graph_area_calculator():
    print("\n--- V-T Graph Area Calculator ---")
    total_displacement = 0
    while True:
        print("\nCalculate area of which shape?")
        print("1. Rectangle (constant velocity)")
        print("2. Triangle (constant acceleration)")
        print("3. Finish and get total displacement")

        choice = input("Select an option (1-3): ")

        if choice == '1':
            print("\n-- Rectangle Area --")
            v = get_float_input("Enter velocity (height): ")
            t = get_float_input("Enter time (width): ")
            area = v * t
            print(f"Area (Displacement) = {area}")
            total_displacement += area
        elif choice == '2':
            print("\n-- Triangle Area --")
            v_change = get_float_input("Enter change in velocity (height): ")
            t = get_float_input("Enter time (base): ")
            area = 0.5 * v_change * t
            print(f"Area (Displacement) = {area}")
            total_displacement += area
        elif choice == '3':
            break
        else:
            print("\nInvalid selection.")

    print(f"\n--- Total Displacement: {total_displacement} ---")
    input("\nPress Enter to return.")

def main():
    while True:
        display_menu()
        try:
            choice = input("Select an option (1-6): ")
            if choice == '1':
                solvers_menu()
            elif choice == '2':
                multi_step_motion_calculator()
            elif choice == '3':
                vt_graph_area_calculator()
            elif choice == '4':
                display_graphing_concepts()
            elif choice == '5':
                display_definitions()
            elif choice == '6':
                print("Exiting. Good luck on your test!")
                break
            else:
                print("\nInvalid choice. Please enter a number from 1 to 6.\n")
        except (Exception) as e:
            print(f"\nAn error occurred: {e}. Please try again.\n")

# This is the standard entry point for NumWorks scripts
if __name__ == "__main__":
    main()