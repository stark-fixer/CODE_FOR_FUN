tom='⚡ 𝑾𝑬𝑳𝑪𝑶𝑴𝑬 𝑻𝑶 𝑻𝑯𝑬 𝟏-𝑴𝑬𝑻𝑬𝑹 𝑷𝑹𝑶𝑩𝑬 𝑮𝑨𝑴𝑬 🔮'
print(tom.center(50)) #this is gonna print our desired heading
#IMPORTING MODULE
import random #importing the random module so that that the computer can choose its own number
Q=random.randint(-7,7) #now it will choose a random integer b/w -7 and 7, and will display on the output screen(terminal)
if Q==0:
    q=5 #since we know, that source charge or any charge can never be zero, so if the computer accendiently chose the no. 0, then it will have to consider it 5(you can take any other integer here)

#PRINTING THE INITIAL THINGS:
print(f"[SYSTEM]: Source charge given = {Q}") #this will print the things along with the random value of source charge
print(f"[SYSTEM]: Fixed distance b/w the test charge and Q (r) is 1m")#I have taken a fixed distance 'r' for eaiser calculations, and for better understanding
r = 1 #for calculation purpose later

#TAKIN INPUTS:
user_input = float(input('Input The Value of Your Test charge \'q in coulombs: '))#taking the value of test charge
q = user_input #storing the user's value for furthur calculation

#THE BACKEND COADING:
if Q*q > 0: #I have chosen this way to compare the charges (to be honest, I asked from gemini, how to compare +ve and -ve)
    Electric_Field = 'OUTWARDS (Away from the source charge)'
    s = 'REPULSIVE Force felt by your charge'
else:
    Electric_Field = 'INWARDS (Towards the source charge)' 
    s = 'ATTRACTIVE Force felt by your charge'

#Calculation:
#1
K = 9 * 10^9
Field_intensity =  (K*Q)/(r**2) #choosing the variable as 'Field_intensity' to make the programmer understand
E = Field_intensity #storing the value of field_intensity in E to make the code easy later

#2
Coulombian_Force = (K * Q * q)/(r**2)
F = abs(Coulombian_Force) #since I have considered the direction before(throught negative and positive sign), so I will use here the abs()function, which acts like maths modulus

#PRINT AFTER CALCULATIONS:
print()
z = "📊 CONCEPT ANALYSIS (THEORY)"
print(z.center(50)) #this the the heading in centre
print()
print()
print(f"1. Electric Field: {Electric_Field}")
print()
print(f"2.Field Intensity: {E}N/C (Force potential at 1m)")
print()
print(f"3.Coulombian Force: {F} {s}")
print()

#INTERESTED PART:
u = "🎯 THE REALITY GUESS"
print(u.center(50))

user_input1 = input("🧠 Quick Question: Will a real-world lab experiment give you exactly -72.0 N of force? (Yes/No): ")

if user_input1.lower() == 'yes':
    print("\n❌ WRONG GUESS! You trapped into theoretical physics!")
    print("Here is the Reality Check:")
else:
    print("\n🎉 CORRECT GUESS! You catch the matrix! +10 Points!")
    print("Here is why you are 100 percent right:")

print("\n1. Theory vs Reality (The Medium): In a real lab, air particles and moisture polarize, making the real force LOWER.")
print("2. The Field Lines Myth: Teacher drew arrows on the board, but space is empty. Field lines are completely IMAGINARY!")
print("3. Intensity vs Force: Intensity was already present in empty space, but Force only came when YOU entered 'q'.")        

#YEAH! CODE IS COMPLETE......
