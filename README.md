# QAP-4-Files-JW
Graph.py README:

How to Use

1.Clone or download this repository to your local machine.
2.Ensure you have Python 3.x and Matplotlib installed (see Requirements section).
3.Open a terminal or command prompt and navigate to the directory where the Python script sales_graph.py is located.
4.Run the Python script by typing the following command: python sales_graph.py

The program will prompt you to enter the total sales for each month from January to December.
For each month, enter a numeric value representing the total sales. If you enter an invalid input (non-numeric value), the program will ask you to re-enter the value.
After entering all the sales values, the program will create a graph using Matplotlib and display it in a new window.
The graph will show the total sales against the months, with the x-axis representing the months of the year and the y-axis representing the total sales in dollars.



One Stop Insurance company
README:

Features

1.Read Default Values: The program starts by reading default values from the "OSICDef.dat" data file. These default values include the next policy number, basic premium, discount for additional cars, costs for extra liability coverage, glass coverage, loaner car coverage, HST rate, and processing fee for monthly payments.

2.User Input: The application prompts the insurance agent to input customer details such as first and last name, address, city, province (with validation), postal code, phone number, number of cars being insured, and options for extra liability coverage, glass coverage, and loaner car coverage.

3.Policy Calculation: The program calculates the total insurance premium, including any applicable discounts and additional costs based on the user's selections.

4.HST Calculation: The program calculates the Harmonized Sales Tax (HST) amount on the total insurance premium.

5.Total Cost: The total cost of the insurance policy, which includes the insurance premium and the HST amount, is computed.

6.Payment Options: Customers can choose to pay the insurance in full or opt for monthly payments. If they choose the monthly payment option, the program calculates the monthly payment amount, considering a processing fee.

7.Receipt Generation: A well-designed receipt is displayed on the screen, showing all the input values, calculated costs, and payment details.

8.Policy Storage: The program saves the policy number, customer details, selected options, total insurance premium, and payment method in the "Policies.dat" file for future reference. Each policy's entry is appended to the file.

9.Policy Number Increment: After processing each policy, the program automatically increments the next policy number to maintain uniqueness for each new policy.

10.Flexibility: The program allows the insurance agent to enter multiple policies in succession. It repeats the process until the agent chooses to stop entering policies.


Usage

1.Run the program: Execute the Python script to start the Insurance Policy Processing Program.

2.Input Customer Details: The program will prompt you to enter customer details and policy options for each policy.

3.Receipt Display: After entering the necessary information, the program will display a well-formatted receipt on the screen.

4.Policy Storage: The policy information, along with the total insurance premium, will be saved in the "Policies.dat" file for future reference.

5.Continue or Exit: You have the option to enter additional policies or exit the program.

