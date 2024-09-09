def cash():
    try:
        while True:
            amount = input("Input youer wage: ")
            ouput = float(amount) * 40 * 52
            print(f"Your yearly amout of pay is ${ouput:,.2f}")
            
    except KeyboardInterrupt:
        print("\nKeyboardInterrupt")
cash()