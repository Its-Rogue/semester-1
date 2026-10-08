# Week 1.2, Session 2: Task 6

import datetime

time = datetime.datetime.now()
filename = f"machine log {time}.txt"
file = open(filename, "a")
machine_temperature = input("Enter the machines temperature (Celcius): ")

try:
    machine_temperature = int(machine_temperature)
except:
    print("Invalid temperature input")
    exit()

machine_pressure = input("Enter the machine's pressure (PSI): ")

try:
    machine_pressure = int(machine_pressure)
except:
    print("Invalid pressure input")
    exit()

print("(1) Operating\n(2) Stopped")
machine_status = int(input("Enter the status of the machine: "))

if (not(machine_status == 1 or machine_status == 0)):
    print("Invalid status input")
    exit()

if (machine_status == 1):
    file.write("The machine is currently operating.\n\n")
    file.write(f"Machine temperature: {machine_temperature}\u00B0C\n")
    if (machine_temperature >= 80):
        print("The temperature is too high, shutting the machine down recommended.")
        file.write("The temperature is too high, shutting the machine down recommended.\n")
    elif (machine_temperature < 80 and machine_temperature >= 50):
        print("The temperature is within safe limits.")
        file.write("The temperature is within safe limits.\n")
    else:
        print("The temperature is too low, immediate action required.")
        file.write("The temperature is too low, immediate action required.\n")

    file.write(f"\nMachine pressure: {machine_pressure} PSI\n")
    if (machine_pressure >= 100):
        print("High pressure detected, maintainence recommended.")
        file.write("High pressure_detected, maintainence recommended.\n")
    elif (machine_pressure < 100 and machine_pressure >= 70):
        print("The pressure is stable.")
        file.write("The pressure is stable.\n")
    else:
        print("The pressure is low, the system is operating normally.")
        file.write("The pressure is low, the system is operating normally.\n")
else:
    file.write("The machine is not currently operating.")
    print("The machine is not currently operation, no immediate action required")
