# CPP102 Week 17: Integrative Programming Project

## Device Temperature Monitoring System

**Student Name:** Xander Jann M. De Los Santos  
**Student Number:** 2601306  
**Section:** 1CpE-A  
**Course:** CPP102 – Programming Logic and Design

## 1. Project Description

The Device Temperature Monitoring System is a Python program that monitors temperature readings. It allows users to view existing readings, add new readings, classify temperatures, and generate a summary report.

The program uses lists, variables, loops, conditional statements, functions, and input validation. It helps users understand how basic programming concepts can be applied to a simple temperature-monitoring task.

## 2. Project Objectives

The objectives of this project are to:

- Apply Python programming concepts in a working program.
- Store and manage temperature readings using a list.
- Classify readings based on the required temperature ranges.
- Calculate the total, average, minimum, and maximum readings.
- Validate user input and reject invalid temperature values.
- Practice writing functions and testing program behavior.

## 3. Features

The program provides the following features:

1. **View Readings** – Displays all recorded temperature readings.
2. **Add Reading** – Accepts a new valid whole-number temperature.
3. **Classify Readings** – Identifies each reading as NORMAL, WARNING, or CRITICAL.
4. **Generate Summary** – Displays the number of readings, total, average, minimum, maximum, category counts, category percentages, and overall status.
5. **Exit** – Ends the program.

## 4. Program Requirements

The program requires:

- Python 3
- A code editor, such as Visual Studio Code
- A terminal or command prompt

No external Python packages are required.

## 5. How to Run the Program

1. Open Visual Studio Code.
2. Open the folder containing `device_monitor.py`.
3. Open the terminal by selecting **Terminal → New Terminal**.
4. Make sure the terminal is in the folder where `device_monitor.py` is located.
5. Run the following command:

   ```bash
   python3 device_monitor.py
   ```

6. Select a menu option by entering its corresponding number.
7. Follow the instructions displayed by the program.

If `python3` does not work on your computer, check your Python installation and use the appropriate Python command for your system.

## 6. Temperature Classification Rules

Each temperature reading is classified according to the following rules:

- **NORMAL:** Below 30 °C
- **WARNING:** From 30 °C through 35 °C, inclusive
- **CRITICAL:** Above 35 °C

Examples:

- 28 °C is NORMAL.
- 30 °C is WARNING.
- 35 °C is WARNING.
- 36 °C is CRITICAL.

The program accepts only whole-number readings from 0 °C to 100 °C, inclusive. Blank inputs, non-numeric inputs, decimal values, and values outside the permitted range are rejected.

## 7. Overall Status Rules

The program determines the overall status using the following rules:

- **ATTENTION REQUIRED:** At least one reading is classified as CRITICAL.
- **MONITOR:** No CRITICAL readings exist, but at least one reading is classified as WARNING.
- **NORMAL:** All readings are classified as NORMAL.

If a CRITICAL reading exists, the overall status is ATTENTION REQUIRED even if other readings are NORMAL or WARNING.

## 8. How the Program Works

The program starts with these initial temperature readings:

`[28, 31, 35, 37, 29]`

A menu allows the user to choose an operation. The program uses a loop to keep displaying the menu until the user selects Exit.

Functions perform specific tasks, such as displaying readings, validating new inputs, classifying temperatures, calculating numerical results, and generating the summary report.

The summary calculations use loops to calculate the total, minimum, and maximum values. The average is calculated by dividing the total by the number of readings. Category percentages are calculated by dividing the number of readings in each category by the total number of readings and multiplying the result by 100.

## 9. Sample Output

The following is the expected summary when the program starts with the five initial readings and no additional readings have been added:

```text
Number of readings: 5
Total: 160
Average: 32.00 °C
Minimum: 28 °C
Maximum: 37 °C

NORMAL: 2 (40.00%)
WARNING: 2 (40.00%)
CRITICAL: 1 (20.00%)

Overall Status: ATTENTION REQUIRED
```

The output above represents the expected initial summary. The actual menu and other messages may vary depending on the user's selections.

## 10. Test Cases

The program must be tested using valid and invalid inputs to verify that its functions work correctly.

The test cases are documented in `test_cases.md`. They cover viewing readings, adding a valid reading, rejecting invalid inputs, checking the classification boundaries, generating the summary, handling invalid menu choices, and exiting the program.

The test results must be based on actual program execution. Each test should be marked PASS or FAIL only after checking the actual output.

## 11. Known Limitations

- The program stores readings only while it is running.
- Readings are not saved permanently after the program closes.
- Only whole-number temperature readings are accepted.
- The program uses a fixed classification system with the specified temperature ranges.
- The program is a basic educational project and is not intended to replace professional temperature-monitoring equipment.

## 12. Reflection

Through this project, I learned how to organize a Python program using functions, lists, loops, and conditional statements. I also learned the importance of input validation and checking boundary values to make sure temperature readings are classified correctly. Testing different inputs helps me verify the calculations and identify possible errors. This project improved my understanding of how basic programming concepts can be used to solve a simple real-world problem.

## 13. GitHub Submission

The project must be saved in a folder named `Week17` inside the CPP102 GitHub repository.

The folder must contain these three files:

- `device_monitor.py` – The Python source code.
- `README.md` – The project description, instructions, rules, sample output, and reflection.
- `test_cases.md` – The test cases and their actual results.

Commit and push the project files to GitHub. Make sure the repository contains at least four meaningful commits, as required by the project instructions.

Before submitting, verify that all three files are present, the program runs correctly, and the test results match the actual program output. Be prepared to demonstrate the program and explain how it works.