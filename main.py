import portfolio  # Import the portfolio module

def display_menu():
    """Displays the main menu with options."""
    print("\nStock Portfolio Management\n")
    print("1. Deposit Money")
    print("2. Withdraw Money")
    print("3. Buy Stock")
    print("4. Sell Stock")
    print("5. Display Portfolio")
    print("6. Display Transaction History")
    print("Press q to exit the program.\n")

def main():
    """Main program loop for user interaction."""
    while True:
        display_menu()
        choice = input("Select an option (1-6 or Q to quit): ").strip().upper()  # Accept Q or q
        
        if choice == "1":
            portfolio.deposit_money()  # No need to pass arguments here
        elif choice == "2":
            portfolio.withdraw_money()  # No need to pass arguments here
        elif choice == "3":
            portfolio.buy_stock()  # No need to pass arguments here
        elif choice == "4":
            portfolio.sell_stock()  # No need to pass arguments here
        elif choice == "5":
            portfolio.display_portfolio()
        elif choice == "6":
            portfolio.display_transaction_history()
        elif choice == "Q":  # Check for 'Q' or 'q' to quit
            print("Exiting the program.")
            break  # Exit the loop and terminate the program
        else:
            print("\nInvalid choice. Please select an option between 1 and 6, or q to quit.")

if __name__ == "__main__":
    main()