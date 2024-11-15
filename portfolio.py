import datetime

# Initialize a portfolio dictionary to hold stock positions and cash balance
portfolio = {
    "cash_balance": 0.0,
    "stocks": {},
    "transactions": []
}

def deposit_money():
    """Add money to the cash balance."""
    amount = input("Enter amount to deposit (or 'q' to quit): ")
    if amount.lower() == 'q':  # User wants to quit
        return
    try:
        amount = float(amount)
        if amount > 0:  # Check if the deposit amount is positive
            portfolio["cash_balance"] += amount
            timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # Get the current time
            portfolio["transactions"].append(("Deposited", amount, timestamp))  # Store the description, amount, and timestamp
            print(f"\n${amount:.2f} deposited.")
        else:
            print("\nDeposit amount must be positive.")  # Invalid deposit amount
    except ValueError:
        print("\nInvalid amount. Please enter a numerical value.")  # Invalid input format

def withdraw_money():
    """Withdraw money from the cash balance."""
    amount = input("Enter amount to withdraw (or 'q' to quit): ")
    if amount.lower() == 'q':  # User wants to quit
        return
    try:
        amount = float(amount)
        if amount > 0 and amount <= portfolio["cash_balance"]:  # Check if withdrawal is positive and within balance
            portfolio["cash_balance"] -= amount
            timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # Get the current time
            portfolio["transactions"].append(("Withdrew", amount, timestamp))  # Store the description, amount, and timestamp
            print(f"\n${amount:.2f} withdrawn.")
        elif amount <= 0:  # Withdrawal amount must be positive
            print("\nWithdrawal amount must be positive.")
        else:  # Insufficient funds
            print("\nInsufficient funds.")
    except ValueError:
        print("\nInvalid amount. Please enter a numerical value.")  # Invalid input format

def buy_stock():
    """Buy stock and add it to the portfolio."""
    symbol = input("Enter stock abbreviation (or 'q' to quit): ")
    if symbol.lower() == 'q':  # User wants to quit
        return
    price = input("Enter stock price: ")
    if price.lower() == 'q':  # User wants to quit
        return
    quantity = input("Enter quantity: ")
    if quantity.lower() == 'q':  # User wants to quit
        return
    try:
        price = float(price)
        quantity = int(quantity)
        if price <= 0 or quantity <= 0:  # Check if price and quantity are positive
            print("\nPrice and quantity must be positive.")
            return
        
        cost = price * quantity
        if cost <= portfolio["cash_balance"]:  # Check if there are enough funds to buy the stock
            portfolio["cash_balance"] -= cost
            if symbol in portfolio["stocks"]:  # Stock already exists in portfolio
                total_quantity = portfolio["stocks"][symbol]["quantity"] + quantity
                portfolio["stocks"][symbol]["average_price"] = (
                    (portfolio["stocks"][symbol]["average_price"] * portfolio["stocks"][symbol]["quantity"] + cost) / total_quantity
                )
                portfolio["stocks"][symbol]["quantity"] = total_quantity
            else:  # First time buying this stock
                portfolio["stocks"][symbol] = {"quantity": quantity, "average_price": price}
            timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # Get the current time
            portfolio["transactions"].append(("Bought", cost, timestamp))  # Store the description, amount, and timestamp
            print(f"\nBought {quantity} shares of {symbol}.")
        else:
            print("\nInsufficient funds to buy stock.")  # Insufficient funds to purchase stock
    except ValueError:
        print("\nInvalid input. Please enter a valid symbol, price, and quantity.")  # Invalid input format

def sell_stock():
    """Sell stock from the portfolio."""
    symbol = input("Enter stock abbreviation to sell (or 'q' to quit): ")
    if symbol.lower() == 'q':  # User wants to quit
        return
    price = input("Enter stock price: ")
    if price.lower() == 'q':  # User wants to quit
        return
    quantity = input("Enter quantity to sell: ")
    if quantity.lower() == 'q':  # User wants to quit
        return
    try:
        price = float(price)
        quantity = int(quantity)
        if symbol not in portfolio["stocks"]:  # Check if stock exists in the portfolio
            print(f"\nYou do not own any shares of {symbol}.")
            return
        if quantity <= 0:  # Quantity must be positive
            print("\nQuantity must be positive.")
            return

        if portfolio["stocks"][symbol]["quantity"] >= quantity:  # Check if there are enough shares to sell
            proceeds = price * quantity
            portfolio["cash_balance"] += proceeds
            portfolio["stocks"][symbol]["quantity"] -= quantity
            timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # Get the current time
            portfolio["transactions"].append(("Sold", proceeds, timestamp))  # Store the description, amount, and timestamp
            print(f"\nSold {quantity} shares of {symbol}.")
            if portfolio["stocks"][symbol]["quantity"] == 0:  # Remove stock if quantity is zero
                del portfolio["stocks"][symbol]
        else:
            print("\nInsufficient quantity of shares to sell.")  # Not enough shares to sell
    except ValueError:
        print("\nInvalid input. Please enter a valid symbol, price, and quantity.")  # Invalid input format

def display_portfolio():
    """Display the current stocks and cash balance in the portfolio, even when empty."""
    print("\nPortfolio Summary:")

    # Display cash balance at the top of the table
    print(f"\n{'Cash Balance':<20} {'${:.2f}'.format(portfolio['cash_balance']):<15}")
    
    # Print a table header for stocks section
    print(f"\n{'Stock':<10} {'Quantity':<10} {'Avg Price':<15}")
    
    # Check if there are any stocks in the portfolio
    if portfolio["stocks"]:
        for symbol, data in portfolio["stocks"].items():
            # Display stock details
            print(f"{symbol:<10} {data['quantity']:<10} ${data['average_price']:<15.2f}")
    else:
        # Print an empty row when no stocks are present
        print(f"{'':<10} {'':<10} {'':<15}")
    
    print("\n")  # Add a newline for clean formatting

def display_transaction_history():
    """Display the history of all transactions made (deposit, withdrawal, buy, sell), even when empty."""
    print("\nTransaction History:")

    # Table header for transactions
    print(f"\n{'Transaction':<20} {'Amount':<15} {'Date/Time'}")

    # Check if there are any transactions
    if portfolio["transactions"]:
        for transaction in portfolio["transactions"]:
            # Each transaction in the portfolio is expected to be a tuple (description, amount, timestamp)
            description, amount, timestamp = transaction

            # Format the output with proper alignment
            print(f"{description:<20} ${amount:<14.2f} {timestamp:<20}")
    else:
        # Print an empty row when no transactions have been made
        print(f"{'No transactions yet':<20} {'':<15} {'':<20}")

    print("\n")  # Add a newline for clean formatting
