# BAN701-Assignment8
Simple Number Calculator Python Project

## Project Description
A simple Python program that collects numbers from the user and calculates the total and average.

## Initial Version
- Collects numbers from the user.
- Stores numbers in a list.
- Calculates the total and average.
- Displays the results.

## AI Tool Used
ChatGPT.

## AI Assistance
ChatGPT helped add input validation to prevent the program from crashing when users enter invalid information.

## New or Modified Features
- Checks that the number of entries is greater than zero.
- Prevents letters from being entered instead of numbers.
- Asks users to try again when an invalid entry is provided.

## Evaluation of AI Output
I accepted the AI recommendations because they improved the program by handling invalid entries and making it easier to use.

## How to Run the Program
1. Open main.py in Visual Studio Code.
2. Click Run Python File.
3. Enter the requested numbers.
4. View the total and average.

## Feature Development Comparison

This assignment provided an opportunity to compare two approaches to developing Python features. The Enhanced Input Validation feature uses the math.isfinite() function to reject invalid numerical values, including NaN and infinity. The Additional Statistical Calculations feature used a more AI-primary approach. AI helped implement calculations for the minimum, maximum, and range of the numbers entered.

Both features were tested using multiple test cases. The manual validation feature was tested with invalid and valid inputs, while the statistical feature was tested with different number combinations, including identical values. Both features passed their tests and were successfully merged into the main branch through separate pull requests.

The AI-generated statistical code worked as expected on the first implementation. I reviewed the changes, examined the Git diff, and tested the results before committing. This process demonstrated the importance of reviewing AI-generated code rather than assuming it is correct. Overall, the assignment helped me understand Git branching, commits, pull requests, code reviews, testing, and how AI can assist with software development.