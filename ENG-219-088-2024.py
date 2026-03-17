# Code converting temparature from degree fahrenheit to degree celcius
T_f = 46
T_c = (5/9) * (T_f - 32)

print(f"{T_f} degrees Fahrenheit is {T_c:.2f} in degrees Celsius.")

# Program that computes the monthly interest payable
principal = 172000
boe_rate = 2.25
margin_rate = 1.49
total_annual_rate_pct = boe_rate + margin_rate
total_annual_rate_decimal = total_annual_rate_pct / 100
annual_interest = principal * total_annual_rate_decimal
interest = annual_interest / 12

print(f"Total Annual Rate: {total_annual_rate_pct}%")
print(f"Monthly Interest Payable: £{interest:.2f}")