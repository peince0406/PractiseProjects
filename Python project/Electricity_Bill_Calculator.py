SLABS = [
    (50,  3.20),   
    (200, 3.95),  
    (999, 5.00),  
]
FIXED_RATE     = 20   
ELECTRICITY_DUTY = 0.06  
METER_RENT     = 10   

def energy_charge(units):
    charge = 0
    prev   = 0
    for limit, rate in SLABS:
        if units <= 0:
            break
        slab_units = min(units, limit - prev)
        charge    += slab_units * rate
        units     -= slab_units
        prev       = limit
    return charge

def calculate_bill(units, load_kw):

    e_charge  = energy_charge(units)
    f_charge  = load_kw * FIXED_RATE
    e_duty    = units * ELECTRICITY_DUTY
    total     = e_charge + f_charge + e_duty + METER_RENT

    print("\n" + "="*42)
    print("   TORRENT POWER - ELECTRICITY BILL")
    print("="*42)
    print(f"  Units Consumed  : {units} units")
    print(f"  Sanctioned Load : {load_kw} kW")
    print("-"*42)
    print(f"  Energy Charges  : ₹{e_charge:.2f}")
    print(f"  Fixed Charges   : ₹{f_charge:.2f}")
    print(f"  Electricity Duty: ₹{e_duty:.2f}")
    print(f"  Meter Rent      : ₹{METER_RENT:.2f}")
    print("="*42)
    print(f"  TOTAL BILL      : ₹{total:.2f}")
    print("="*42)

    return total

def get_input(prompt, min_val=0):
    while True:
        try:
            val = float(input(prompt))
            if val < min_val:
                print(f"  ❌ Value must be >= {min_val}. Try again.")
            else:
                return val
        except ValueError:
            print("  ❌ Invalid input! Enter a number.")

print("\n  TORRENT POWER Bill Calculator")
print("  RGP Category - Ahmedabad")

while True:
    print("\n" + "-"*42)
    units  = int(get_input("  Enter units consumed : ", 0))
    load   = get_input("  Enter load in kW     : ", 0.5)

    calculate_bill(units, load)

    again = input("\n  Calculate again? (y/n): ").strip().lower()
    if again != 'y':
        print("\n  Thank You! 💡")
        break
