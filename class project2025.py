
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
transactions = []  # Initialize transactions as an empty list
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



