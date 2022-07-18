def invest(principal, rate, years):
    for year in range(1, years+1):
        principal = principal * (rate + 1)
        print(f"year {year}: ${principal:,.2f}")


print(invest(200, 0.5, 5));

