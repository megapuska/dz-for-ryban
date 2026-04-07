rost = 145000
for year in range(1, 6):
    rost += rost * 0.03
    print(f"Год {year}: {rost} руб.")