SLABS = [
    (50, 3.20),
    (200, 3.95),
    (float('inf'), 5.00)
]

FIXED_RATE = 20
ELECTRICITY_DUTY = 0.06
METER_RENT = 10

def energy_charge(units):
    charge = 0
    previous = 0

    for limit, rate in SLABS:
        if units <= 0:
            break

        slab = min(units, limit - previous)
        charge += slab * rate
        units -= slab
        previous = limit

    return charge

def calculate_bill(units, load):
    energy = energy_charge(units)
    fixed = load * FIXED_RATE
    duty = units * ELECTRICITY_DUTY
    total = energy + fixed + duty + METER_RENT

    print("Units Consumed     :", units)
    print("Load (kW)          :", load)
    print("----------------------------------------")
    print("Energy Charge      : ₹", round(energy, 2))
    print("Fixed Charge       : ₹", round(fixed, 2))
    print("Electricity Duty   : ₹", round(duty, 2))
    print("Meter Rent         : ₹", METER_RENT)
    print("----------------------------------------")
    print("Total Bill         : ₹", round(total, 2))

print("TORRENT POWER BILL CALCULATOR")

while True:

    units = int(input("\nEnter Units Consumed : "))
    load = float(input("Enter Load (kW)      : "))

    calculate_bill(units, load)

    choice = input("\nCalculate Again? (y/n): ").lower()

    if choice != "y":
        print("\nThank You!")
        break
