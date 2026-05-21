# 1. Dictionary storing Standard Electrode Potential (E°) values for different metals
elect_potential={"Sodium" : -2.71, "Zinc" : -0.76, "Hydrogen" : 0.00, "Copper" : +0.34, "Silver" : +0.80}#storing all the values(these are only a few)

# 2. Display the dictionary to let the user see available metal choices
print(elect_potential)

# 3. Take input from the user for two different metals
MetalA=input('enter the first metal from the following dictionary: ')
MetalB=input("enter the second metal from the following dictionary: ")

# 4. If MetalA has a higher potential, it becomes the Cathode (Acceptor) and MetalB becomes the Anode (Donor)
if elect_potential[MetalA] > elect_potential[MetalB]:
    print("Electrons will flow from",MetalB, "to", MetalA) # Electrons always flow from Anode (lower potential) to Cathode (higher potential)
    Cathode=MetalA
    Anode=MetalB

# 5. If both metals are the same, there is no potential difference and no electron movement
elif elect_potential[MetalA] == elect_potential[MetalB]:
    print('Dono barabar hai, electron will not move, Electrode potential=0')
    Cathode=MetalA # Assigning variables to prevent the final print line from crashing
    Anode=MetalB

# 6. If MetalB has a higher potential, it becomes the Cathode and MetalA becomes the Anode
else:
    print("Electron will flow from", MetalA, "to", MetalB)
    Cathode=MetalB
    Anode=MetalA    

# 7. Calculate and print the final cell voltage using the formula: E°cell = E°Cathode - E°Anode
print("Final voltage is ",elect_potential[Cathode]-elect_potential[Anode])
