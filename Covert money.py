def convert_usd_to_gbp(usd_amount, exchange_rate=0.74):
    gbp_amount = usd_amount * exchange_rate
    return gbp_amount

# Example usage
usd_amount = float(input("Enter the amount in US dollars: "))
gbp_amount = convert_usd_to_gbp(usd_amount)

print(f"{usd_amount} US dollars is equal to {gbp_amount:,.2f} UK pounds.")

