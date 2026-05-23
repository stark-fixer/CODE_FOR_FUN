# Electrochemical Series in Ascending Order (Lowest to Highest SRP); creating a choise for the user
electro_series = {
    "Lithium (Li)": -3.04,
    "Potassium (K)": -2.93,
    "Barium (Ba)": -2.90,
    "Calcium (Ca)": -2.87,
    "Sodium (Na)": -2.71,
    "Magnesium (Mg)": -2.37,
    "Aluminium (Al)": -1.66,
    "Manganese (Mn)": -1.18,
    "Zinc (Zn)": -0.76,
    "Chromium (Cr)": -0.74,
    "Iron (Fe)": -0.44,
    "Cadmium (Cd)": -0.40,
    "Cobalt (Co)": -0.28,
    "Nickel (Ni)": -0.25,
    "Tin (Sn)": -0.14,
    "Lead (Pb)": -0.13,
    "Hydrogen (H2)": 0.00,  # Reference Electrode (SHE)
    "Copper (Cu)": 0.34,
    "Iodine (I2)": 0.54,
    "Silver (Ag)": 0.80,
    "Mercury (Hg)": 0.85,
    "Bromine (Br2)": 1.06,
    "Platinum (Pt)": 1.20,
    "Chlorine (Cl2)": 1.36,
    "Gold (Au)": 1.50,
    "Fluorine (F2)": 2.87
}
print()
print('MAKE SURE TO WRITE THE NAME WITH THEIR SYMBOLS AS IT IS(YOU CAN ALSO COPY AND PASTE FROM THE ABOVE SERIES(#ONLY NAMES))')
print("YOUR VISUAL ELECTORCHEMICAL SERIES IS:-")
#looping every element and will give each value in a new line:
for element,values in electro_series.items(): # the for loop, in which two variable will go through each key-value pair in the dictionary(electro_series)
    print(f"{element} : {values}")  #using fstring to make code eaiser
print()
print('MAKE SURE TO WRITE THE NAME WITH THEIR SYMBOLS AS IT IS(YOU CAN ALSO COPY AND PASTE FROM THE ABOVE SERIES(#ONLY NAMES))')
print()
#Taking inputs:
user_input = input('Enter the first element of your own choise:')
user_input1 = input('Enter the second element from the above values of your own choise:')

print()

#FIRST PRINT:
print('WELCOME TO THE CHEMISTRY ARENA!!')
title="🥊 --- ELECTRO-CHEMICAL BATTLE --- 🥊"
print(title.center(50))#printing the desired output in the centre
consecutive_centre=f"[{user_input}]  V/S  [{user_input1}]"
print(consecutive_centre.center(50))

#backend coding:
if user_input > user_input1:
    cathode=user_input1
    anode=user_input
elif user_input < user_input1:
    cathode=user_input
    anode=user_input1
else:
    print('Its a tie!')

#THE OUTPUTS:
print(f"⚡ THE FIGHT: {anode} looses electrons faster!")
print(f"🏆 WINNER (Cathode): {cathode} (Gets Reduced)")
print(f"💀 LOSER  (Anode): {anode} (Gets oxidised)")
print()#for an empty line
print()#for another empty line

#CALCULATING THE E(NOT) VALUE
E_cathode=electro_series[cathode]
E_anode=electro_series[anode]
E_not=E_cathode - E_anode

print("📊 MATCH STATS:")
print(f"HIT POWER(E0 cell):{E_not}");print()
print(f"Best Sheild(oxidiser): {cathode}");print()
print(f"Best Sword(Reducer): {anode}");print();print()

#FINAL OUTPUT:
print(f"🔥 KNOCKOUT: {anode} pushes {cathode} out of its solution")


