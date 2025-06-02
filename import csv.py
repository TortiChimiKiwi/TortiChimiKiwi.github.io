{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "76ac4e66",
   "metadata": {},
   "source": [
    "# Smart Personal Finance Analyzer\n",
    "\n",
    "starting file: financial_transactions.csv\n",
    "\n",
    "location: [https://github.com/RamaKattunga/Code-Notes/blob/main/financial_transactions.csv](https://github.com/RamaKattunga/Code-Notes/blob/main/financial_transactions.csv)\n",
    "\n",
    "This will say you cannot view the file, you will need to download the raw data."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "6a6fe97f",
   "metadata": {},
   "source": [
    "## Step 1:\n",
    "\n",
    "\n",
    "### Import csv:\n",
    "Remember: CSVs are read line-by-line\n",
    "We need to read that line in a specific way\n",
    "Typically do this by opening the file, read each line, then close the file\n",
    "\n",
    "DictReader: Turns each row into a dictionary with the column names as the key and the values of each row will act as the values for each key.\n",
    "\n",
    "Examples:\n",
    "\n",
    "Typical dictionaries\n",
    "{'transaction_id':'1', 'date':'2020-10-26', 'customer_id':'926', 'amount':'6478.39', 'type':'credit', 'description':'Expect series shake art again our.'}\n",
    "\n",
    "[dictionaryLine1, dictionaryLine2, ...., dictionaryLineLast]\n",
    "\n",
    "Read in with the DictReader, reiterate over result to print out each line\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "245ab0c2",
   "metadata": {},
   "source": [
    "### Change Data Types\n",
    "\n",
    "DictReader automatically makes everything a string, so we need to fix that.\n",
    "\n",
    "We need to access list elements and modify the dictionaries.\n",
    "\n",
    "List access: list_name[index]\n",
    "\n",
    "Access Dictionary: [Example](https://courses.cs.washington.edu/courses/cse140/13wi/csv-parsing.html)\n",
    "\n",
    "Expected dtypes:\n",
    "    transaction_id: integer\n",
    "    date: datetime\n",
    "    customer_id: integer\n",
    "    amount: float\n",
    "    type: string\n",
    "    description: string\n",
    "\n",
    "We need to change from a string to the correct data type for each row, then reassign it back to the original\n",
    "\n",
    "```python\n",
    "#ex: \n",
    "x = 5\n",
    "\n",
    "print(x + 1) #6\n",
    "\n",
    "print(x) #5\n",
    "\n",
    "x = x + 1\n",
    "\n",
    "print(x) #6\n",
    "```\n",
    "\n",
    "Using dictionary access example above:\n",
    "\n",
    "```python\n",
    "#Example:\n",
    "age = int(row[\"age\"])\n",
    "\n",
    "#We are assigning the value to a new variable\n",
    "#We want to reassign back to itself\n",
    "row[\"age\"] = int(row[\"age\"])\n",
    "```\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "666153b4",
   "metadata": {},
   "source": [
    "### Additional Tasks for Loading\n",
    "\n",
    "1. Parse the date with datetime.strptime\n",
    "2. Make all transactions with a type of 'debit' have a negative amount\n",
    "3. Add to transactions\n",
    "\n",
    "#### Date Parsing\n",
    "\n",
    "Specifies:\n",
    "```python\n",
    "from datetime import datetime\n",
    "```\n",
    "\n",
    "We want to use datetime.strptime function and reassign it back to the column, as shown above.\n",
    "\n",
    "[Official Documentation including format options](https://docs.python.org/3/library/datetime.html)\n",
    "[GeeksForGeeks Article](https://www.geeksforgeeks.org/python-datetime-strptime-function/)\n",
    "\n",
    "#### Making debit transactions negative\n",
    "\n",
    "We want to make sure the transaction is a debit >> check the type and make sure it's 'debit'\n",
    "\n",
    "```python\n",
    "#Check the transaction type:\n",
    "row[\"type\"].lower() #check if it is 'debit' \n",
    "```\n",
    "If this is debit, then we need to make it negative:\n",
    "```\n",
    "-x = x * -1\n",
    "```\n",
    "\n",
    "#### Add to transactions\n",
    "\n",
    "Starter code has us initializing an empty list called transactions\n",
    "\n",
    "```python\n",
    "transactions = []\n",
    "```\n",
    "\n",
    "We want to add to the list. [Python Lists](https://www.w3schools.com/python/python_lists.asp)\n",
    "\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "dd703167",
   "metadata": {},
   "source": [
    "## Putting Step 1 Together\n",
    "\n",
    "Work on each of the above one by one.\n",
    "Test each step before you move on.\n",
    "Put them together.\n",
    "\n",
    "```python\n",
    "import csv\n",
    "from datetime import datetime\n",
    "\n",
    "def load_transactions(filename='financial_transactions.csv'):\n",
    "    \"\"\"Load transactions from a CSV file into a list of dictionaries.\"\"\"\n",
    "    transactions = []\n",
    "    # Open file with 'with' statement\n",
    "    # Use csv.DictReader\n",
    "    # For each row:\n",
    "    #   Parse date with datetime.strptime\n",
    "    #   Make amount negative for 'debit'\n",
    "    #   Create dictionary with all fields\n",
    "    #   Add to transactions\n",
    "    # Catch FileNotFoundError, ValueError\n",
    "    return transactions\n",
    "```"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "01264f4c",
   "metadata": {},
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "name": "python",
   "version": "3.12.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

import csv
from datetime import datetime

def load_transactions(filename='financial_transactions.csv'):
    """Load transactions from a CSV file into a list of dictionaries."""
    transactions = []
    # Open file with 'with' statement
    # Use csv.DictReader
    # For each row:
    #   Parse date with datetime.strptime
    #   Make amount negative for 'debit'
    #   Create dictionary with all fields
    #   Add to transactions
    # Catch FileNotFoundError, ValueError
    return transactions
import datetime

def add_transaction(transactions):
    """Add a new transaction from user input."""
    
    # Step 1: Prompt for user input
    date_str = input("Enter transaction date (YYYY-MM-DD): ")
    customer_id = input("Enter customer ID: ")
    amount_str = input("Enter transaction amount: ")
    trans_type = input("Enter transaction type (e.g., purchase, refund): ")
    description = input("Enter description: ")

    # Step 2: Validate input values
    try:
        date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        return
    
    try:
        amount = float(amount_str)
        if amount <= 0:
            raise ValueError
    except ValueError:
        print("Invalid amount. Please enter a positive number.")
        return

    valid_types = ["purchase", "refund", "withdrawal", "deposit"]
    if trans_type.lower() not in valid_types:
        print(f"Invalid transaction type. Choose from: {valid_types}")
        return
    
    # Step 3: Generate unique transaction ID
    transaction_id = len(transactions) + 1

    # Step 4: Create and append transaction dictionary
    transaction = {
        "transaction_id": transaction_id,
        "date": date,
        "customer_id": customer_id,
        "amount": amount,
        "type": trans_type.lower(),
        "description": description
    }
    
    transactions.append(transaction)
    print(f"Transaction {transaction_id} successfully added!")
    return transaction
def save_transactions(transactions, filename='financial_transactions.csv'):
    """Save transactions to a CSV file."""
    # Open file with 'with' statement
    # Use csv.DictWriter
    # Write header and rows
    # Catch IOError
    pass  # Placeholder for implementation
def display_transactions(transactions):
    """Display all transactions in a readable format."""
    view_transactions(transactions)

def view_transactions(transactions):
    """Display transactions in a table format."""
    
    if not transactions:
        print("No transactions to display.")
    else:
        print("Displaying transactions...")
    
    # Step 1: Print header
    header = f"{'ID':<5}{'Date':<12}{'Customer ID':<12}{'Amount':<10}{'Type':<15}{'Description':<20}"
    print(header)
    print("-" * len(header))
    
    # Step 2: Loop through transactions
    for transaction in transactions:
        trans_id = transaction["transaction_id"]
        date = transaction["date"]
        customer_id = transaction["customer_id"]
        amount = f"${transaction['amount']:,.2f}"
        trans_type = transaction["type"]
        description = transaction["description"]
        
        # Step 3: Format each row
        row = f"{trans_id:<5}{str(date):<12}{customer_id:<12}{amount:<10}{trans_type:<15}{description:<20}"
        print(row)

# Example usage:
transactions_list = [
    {"transaction_id": 1, "date": "2025-05-10", "customer_id": "C123", "amount": 45.99, "type": "purchase", "description": "Book"},
    {"transaction_id": 2, "date": "2025-05-12", "customer_id": "C456", "amount": 120.50, "type": "refund", "description": "Headphones"},
    {"transaction_id": 3, "date": "2025-05-15", "customer_id": "C789", "amount": 75.00, "type": "withdrawal", "description": "Cash withdrawal"},
    {"transaction_id": 4, "date": "2025-05-20", "customer_id": "C123", "amount": 200.00, "type": "deposit", "description": "Salary"},
    {"transaction_id": 5, "date": "2025-05-22", "customer_id": "C456", "amount": 30.00, "type": "purchase", "description": "Coffee"},
    {"transaction_id": 6, "date": "2025-05-25", "customer_id": "C789", "amount": 15.00, "type": "refund", "description": "Book return"},
    {"transaction_id": 7, "date": "2025-05-28", "customer_id": "C123", "amount": 60.00, "type": "withdrawal", "description": "ATM withdrawal"},
    {"transaction_id": 8, "date": "2025-05-30", "customer_id": "C456", "amount": 150.00, "type": "deposit", "description": "Paycheck"}, 
    {"transaction_id": 9, "date": "2025-06-01", "customer_id": "C789", "amount": 90.00, "type": "purchase", "description": "Groceries"},
    {"transaction_id": 10, "date": "2025-06-03", "customer_id": "C123", "amount": 25.00, "type": "refund", "description": "Coffee return"},
    {"transaction_id": 11, "date": "2025-06-05", "customer_id": "C456", "amount": 300.00, "type": "withdrawal", "description": "Cash withdrawal"},
    {"transaction_id": 12, "date": "2025-06-07", "customer_id": "C789", "amount": 200.00, "type": "deposit", "description": "Investment return"},
    {"transaction_id": 13, "date": "2025-06-10", "customer_id": "C123", "amount": 80.00, "type": "purchase", "description": "Clothes"},
    {"transaction_id": 14, "date": "2025-06-12", "customer_id": "C456", "amount": 45.00, "type": "refund", "description": "Shoes return"},
    {"transaction_id": 15, "date": "2025-06-15", "customer_id": "C789", "amount": 120.00, "type": "withdrawal", "description": "ATM withdrawal"},
    {"transaction_id": 16, "date": "2025-06-18", "customer_id": "C123", "amount": 500.00, "type": "deposit", "description": "Bonus"},
    {"transaction_id": 17, "date": "2025-06-20", "customer_id": "C456", "amount": 60.00, "type": "purchase", "description": "Lunch"},
    {"transaction_id": 18, "date": "2025-06-22", "customer_id": "C789", "amount": 30.00, "type": "refund", "description": "Book return"},
    {"transaction_id": 19, "date": "2025-06-25", "customer_id": "C123", "amount": 100.00, "type": "withdrawal", "description": "Cash withdrawal"},
    {"transaction_id": 20, "date": "2025-06-28", "customer_id": "C456", "amount": 200.00, "type": "deposit", "description": "Paycheck"}
]

# Display the transactions
view_transactions(transactions_list)




# Function to save transactions to CSV
def save_to_csv(filename, transactions):
    """Save transaction data to a CSV file."""
    with open(filename, "w", newline="", encoding="utf-8") as file:
        fieldnames = ["transaction_id", "date", "customer_id", "amount", "type", "description"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        
        writer.writeheader()  # Write column headers
        writer.writerows(transactions)  # Write data rows
        
    print(f"Transactions saved to {filename}")

# Save data to CSV
# Ensure transactions are defined before saving
transactions = load_transactions("financial_transactions.csv")
save_to_csv("financial_transactions.csv", transactions)

def add_transaction(transactions):
    """Add a new transaction."""
    date = input("Enter transaction date (YYYY-MM-DD): ")
    customer_id = input("Enter customer ID: ")
    amount = float(input("Enter amount: "))
    trans_type = input("Enter type (credit/debit/transfer): ").strip().lower()
    description = input("Enter description: ")

    transaction_id = max(int(t["transaction_id"]) for t in transactions) + 1 if transactions else 1

    transactions.append({
        "transaction_id": str(transaction_id),
        "date": date,
        "customer_id": customer_id,
        "amount": amount,
        "type": trans_type,
        "description": description
    })

    print(f"Transaction {transaction_id} added successfully!")
def view_transactions(transactions, filter_type=None):
    """Display transactions (optionally filter by type)."""
    print(f"{'ID':<5}{'Date':<12}{'Customer ID':<12}{'Amount':<10}{'Type':<12}{'Description':<20}")
    print("-" * 70)

    for transaction in transactions:
        if filter_type and transaction["type"] != filter_type:
            continue  # Skip transactions that don’t match the filter
        
        print(f"{transaction['transaction_id']:<5}{transaction['date']:<12}{transaction['customer_id']:<12}{'$' + str(transaction['amount']):<10}{transaction['type']:<12}{transaction['description']:<20}")

view_transactions(transactions, filter_type="credit")  # Example: Viewing credits only

def update_transaction(transactions):
    """Update an existing transaction."""
    trans_id = input("Enter transaction ID to update: ")
    
    transaction = next((t for t in transactions if t["transaction_id"] == trans_id), None)
    if not transaction:
        print("Transaction not found.")
        return

    field_to_update = input("Enter field to update (date, customer_id, amount, type, description): ").strip().lower()
    if field_to_update not in transaction:
        print("Invalid field.")
        return

    new_value = input(f"Enter new value for {field_to_update}: ")
    transaction[field_to_update] = new_value
    print(f"Transaction {trans_id} updated successfully!")

def delete_transaction(transactions):
    """Delete a transaction."""
    trans_id = input("Enter transaction ID to delete: ")
    
    transactions[:] = [t for t in transactions if t["transaction_id"] != trans_id]
    print(f"Transaction {trans_id} deleted successfully!")

import csv

def load_transactions(filename):
    """Load transactions from CSV."""
    transactions = []
    try:
        with open(filename, newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                row["amount"] = float(row["amount"])  # Convert amount to float
                transactions.append(row)
    except FileNotFoundError:
        print("File not found. Starting fresh.")
    
    return transactions

# Test loading
transactions = load_transactions("financial_transactions.csv")
print(transactions[:5])  # Print first 5 transactions

transactions = []
add_transaction(transactions)
print(transactions)  # Verify transaction was added


update_transaction(transactions)
print(transactions)  # Check if changes applied


delete_transaction(transactions)
print(transactions)  # Ensure transaction is removed

import csv
import datetime

def load_transactions(filename):
    """Load transactions from CSV file and validate data."""
    transactions = []
    
    try:
        with open(filename, newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                # Validate date format
                try:
                    row["date"] = datetime.datetime.strptime(row["date"], "%Y-%m-%d").strftime("%b %d, %Y")  # Convert to "Oct 26, 2020"
                except ValueError:
                    print(f"Skipping invalid date format: {row['date']}")
                    continue
                
                # Convert amount to float and validate
                try:
                    row["amount"] = float(row["amount"])
                    if row["amount"] <= 0:
                        print(f"Skipping invalid amount: {row['amount']}")
                        continue
                except ValueError:
                    print(f"Skipping non-numeric amount: {row['amount']}")
                    continue
                
                transactions.append(row)

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    
    return transactions

transactions = load_transactions("financial_transactions.csv")
print(transactions[:5])  # View first 5 transactions

import csv
import datetime

def load_transactions(filename, error_log="errors.txt"):
    """Load transactions from CSV file, validate data, and log errors."""
    transactions = []
    errors = []

    try:
        with open(filename, newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Validate date format
                try:
                    try:
                        row["date"] = datetime.datetime.strptime(row["date"], "%Y-%m-%d").strftime("%b %d, %Y")
                    except ValueError:
                        print(f"Skipping invalid date: {row['date']}")
                        continue
                except ValueError:
                    warning = f"Skipping row due to invalid date format: {row['date']}"
                    print(warning)
                    errors.append(warning)
                    continue

                # Validate amount
                try:
                    row["amount"] = float(row["amount"])
                    if row["amount"] <= 0:
                        warning = f"Skipping row due to invalid amount: {row['amount']}"
                        print(warning)
                        errors.append(warning)
                        continue
                except ValueError:
                    warning = f"Skipping row due to non-numeric amount: {row['amount']}"
                    print(warning)
                    errors.append(warning)
                    continue
                
                transactions.append(row)

        # Print the number of successfully loaded transactions
        print(f"Total transactions loaded: {len(transactions)}")

        # Log errors to errors.txt
        if errors:
            with open(error_log, "w", encoding="utf-8") as error_file:
                for error in errors:
                    error_file.write(error + "\n")

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    
    return transactions

transactions = load_transactions("financial_transactions.csv")

import csv
import datetime

# Load transactions from CSV file
def load_transactions(filename):
    transactions = []
    try:
        with open(filename, newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                row["amount"] = float(row["amount"])
                transactions.append(row)
    except FileNotFoundError:
        print("No existing transactions found. Starting fresh.")
    return transactions

# Save transactions to CSV file
def save_transactions(filename, transactions):
    with open(filename, "w", newline="", encoding="utf-8") as file:
        fieldnames = ["transaction_id", "date", "customer_id", "amount", "type", "description"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(transactions)

# Function to add a transaction
def add_transaction(transactions):
    """Add a new transaction with user input and validation."""
    date_str = input("Enter transaction date (YYYY-MM-DD): ")
    customer_id = input("Enter customer ID: ")
    amount_str = input("Enter transaction amount: ")
    trans_type = input("Enter transaction type (credit/debit/transfer): ").strip().lower()
    description = input("Enter description: ")

    # Validate inputs
    try:
        date = datetime.datetime.strptime(date_str, "%Y-%m-%d").strftime("%b %d, %Y")  # Format date as "Oct 26, 2020"
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        return

    try:
        amount = float(amount_str)
        if amount <= 0:
            raise ValueError
    except ValueError:
        print("Invalid amount. Please enter a positive number.")
        return

    if trans_type not in {"credit", "debit", "transfer"}:
        print("Invalid transaction type. Choose from credit, debit, transfer.")
        return

    transaction_id = max(int(t["transaction_id"]) for t in transactions) + 1 if transactions else 1

    transaction = {
        "transaction_id": str(transaction_id),
        "date": date,
        "customer_id": customer_id,
        "amount": amount,
        "type": trans_type,
        "description": description
    }

    transactions.append(transaction)
    print(f"Transaction {transaction_id} successfully added!")

# Function to view transactions with optional filtering
def view_transactions(transactions, filter_type=None):
    """Display transactions with an optional filter by type."""
    if not transactions:
        print("No transactions to display.")
        return

    print(f"{'ID':<5}{'Date':<15}{'Customer ID':<12}{'Amount':<10}{'Type':<10}{'Description':<20}")
    print("-" * 70)

    for transaction in transactions:
        if filter_type and transaction["type"] != filter_type:
            continue  # Skip transactions that don’t match the filter
        
        print(f"{transaction['transaction_id']:<5}{transaction['date']:<15}{transaction['customer_id']:<12}{'$' + str(transaction['amount']):<10}{transaction['type']:<10}{transaction['description']:<20}")

# Function to update transactions
def update_transaction(transactions):
    """Allow user to modify an existing transaction."""
    view_transactions(transactions)  # Display current transactions
    try:
        trans_id = input("Enter transaction ID to update: ").strip()
        transaction = next(t for t in transactions if t["transaction_id"] == trans_id)
    except StopIteration:
        print("Invalid transaction ID.")
        return

    fields = ["date", "customer_id", "amount", "type", "description"]
    print(f"Fields available for update: {fields}")
    field_to_update = input("Enter the field name to update: ").strip().lower()

    if field_to_update not in fields:
        print("Invalid field selection.")
        return

    new_value = input(f"Enter new value for {field_to_update}: ")
    transaction[field_to_update] = new_value
    print(f"Transaction {trans_id} updated successfully!")

# Function to delete transactions
def delete_transaction(transactions):
    """Delete a transaction from the list."""
    view_transactions(transactions)
    try:
        trans_id = input("Enter transaction ID to delete: ").strip()
        transactions[:] = [t for t in transactions if t["transaction_id"] != trans_id]
        print(f"Transaction {trans_id} deleted successfully!")
    except ValueError:
        print("Invalid transaction ID.")

# Function to generate reports
def generate_report(transactions, filename="report.txt"):
    """Generate a summary report of transactions."""
    credits = sum(t["amount"] for t in transactions if t["type"] == "credit")
    debits = sum(t["amount"] for t in transactions if t["type"] == "debit")
    transfers = sum(t["amount"] for t in transactions if t["type"] == "transfer")

    with open(filename, "w", encoding="utf-8") as file:
        file.write(f"Transaction Report\n")
        file.write("=" * 30 + "\n")
        file.write(f"Total Credits: ${credits:,.2f}\n")
        file.write(f"Total Debits: ${debits:,.2f}\n")
        file.write(f"Total Transfers: ${transfers:,.2f}\n")

    print("Report generated successfully!")
# Step 1: Import necessary libraries
# Step 2: Create the main script (`transactions.py`)
### **Step 4: Create the README (`README.md`)**
# The README should include:
# - How to run the script
# - Usage examples
# - Explanation of files
# - Future improvements
# - **How to run the script** (install Python, install dependencies, run `transactions.py`).
# - **Usage examples** (adding/viewing/updating/deleting transactions).
# - **Explanation of files** (`financial_transactions.csv`, `report.txt`).
# Future improvements (e.g., database integration, web interface).
### **Step 5: Test Everything!**
# Run the Python script and ensure transactions are correctly added, viewed, updated, and deleted.
# Verify that the CSV file persists changes correctly.
# - Check if 'report.txt' accurately summarizes transaction data.
# - Ensure all functions work as expected.
# - Test with various inputs to ensure robustness.

