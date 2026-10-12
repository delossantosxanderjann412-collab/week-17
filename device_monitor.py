"""
Simulated Device Monitoring and Alert System
CPP102 - Programming Logic and Design, Week 17
"""

def get_initial_readings():
    """Return the starting list of simulated temperature readings."""
    return [28, 31, 35, 37, 29]


def display_menu():
    """Display the main menu."""
    print("\n===== DEVICE MONITORING MENU =====")
    print("[1] View Readings")
    print("[2] Add Reading")
    print("[3] Classify Readings")
    print("[4] Generate Summary")
    print("[5] Exit")


def display_readings(readings):
    """Display each reading with its position."""
    print("\n===== STORED READINGS =====")
    for index in range(len(readings)):
        print("Reading", index + 1, ":", readings[index], "°C")


def read_whole_number(prompt):
    """Return a whole number, or None when the input is invalid."""
    text = input(prompt).strip()

    if text == "":
        return None

    digits = text
    if text[0] == "-":
        digits = text[1:]

    if digits == "" or not digits.isdigit():
        return None

    return int(text)


def add_reading(readings, lowest, highest):
    """Add a reading only if it is a whole number in the allowed range."""
    new_reading = read_whole_number("Enter a temperature reading (0-100): ")

    if new_reading is None:
        print("Invalid input. Enter a whole number only.")
    elif new_reading < lowest or new_reading > highest:
        print("Invalid reading. The value must be from", lowest, "to", highest, ".")
    else:
        readings.append(new_reading)
        print("Reading added successfully.")


def classify_reading(reading, warning_limit, critical_limit):
    """Return NORMAL, WARNING, or CRITICAL for one reading."""
    if reading < warning_limit:
        return "NORMAL"
    elif reading <= critical_limit:
        return "WARNING"
    else:
        return "CRITICAL"


def display_classifications(readings, warning_limit, critical_limit):
    """Display the classification of each reading."""
    print("\n===== READING CLASSIFICATIONS =====")
    for index in range(len(readings)):
        category = classify_reading(
            readings[index], warning_limit, critical_limit
        )
        print(readings[index], "°C ->", category)


def compute_total(readings):
    """Calculate the total using a loop."""
    total = 0
    for reading in readings:
        total = total + reading
    return total


def compute_average(readings):
    """Calculate the average of the readings."""
    if len(readings) == 0:
        return 0
    return compute_total(readings) / len(readings)


def find_minimum(readings):
    """Find the smallest reading using a loop."""
    smallest = readings[0]
    for reading in readings:
        if reading < smallest:
            smallest = reading
    return smallest


def find_maximum(readings):
    """Find the largest reading using a loop."""
    largest = readings[0]
    for reading in readings:
        if reading > largest:
            largest = reading
    return largest


def count_category(readings, warning_limit, critical_limit, category_to_count):
    """Count readings that match a category."""
    count = 0
    for reading in readings:
        category = classify_reading(reading, warning_limit, critical_limit)
        if category == category_to_count:
            count = count + 1
    return count


def determine_overall_status(warning_count, critical_count):
    """Return the overall status, prioritizing CRITICAL readings."""
    if critical_count >= 1:
        return "ATTENTION REQUIRED"
    elif warning_count >= 1:
        return "MONITOR"
    else:
        return "NORMAL"


def display_summary(readings, warning_limit, critical_limit):
    """Display totals, averages, category counts, and overall status."""
    print("\n===== NUMERICAL SUMMARY =====")

    number_of_readings = len(readings)
    total = compute_total(readings)
    average = compute_average(readings)
    smallest = find_minimum(readings)
    largest = find_maximum(readings)

    normal_count = count_category(
        readings, warning_limit, critical_limit, "NORMAL"
    )
    warning_count = count_category(
        readings, warning_limit, critical_limit, "WARNING"
    )
    critical_count = count_category(
        readings, warning_limit, critical_limit, "CRITICAL"
    )

    print("Number of readings:", number_of_readings)
    print("Total:", total)
    print("Average: {:.2f} °C".format(average))
    print("Minimum:", smallest, "°C")
    print("Maximum:", largest, "°C")

    print("\nCategory Counts and Percentages:")
    print("NORMAL:", normal_count, "({:.2f}%)".format(
        normal_count / number_of_readings * 100))
    print("WARNING:", warning_count, "({:.2f}%)".format(
        warning_count / number_of_readings * 100))
    print("CRITICAL:", critical_count, "({:.2f}%)".format(
        critical_count / number_of_readings * 100))

    status = determine_overall_status(warning_count, critical_count)
    print("\nOverall Status:", status)


def main():
    """Run the menu until the user chooses Exit."""
    readings = get_initial_readings()
    lowest = 0
    highest = 100
    warning_limit = 30
    critical_limit = 35

    while True:
        display_menu()
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            display_readings(readings)
        elif choice == "2":
            add_reading(readings, lowest, highest)
        elif choice == "3":
            display_classifications(readings, warning_limit, critical_limit)
        elif choice == "4":
            display_summary(readings, warning_limit, critical_limit)
        elif choice == "5":
            print("Thank you for using the Device Monitoring System.")
            break
        else:
            print("Invalid menu choice. Please choose a number from 1 to 5.")


if __name__ == "__main__":
    main()
