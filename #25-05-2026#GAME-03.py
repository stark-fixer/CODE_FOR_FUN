import math

# Start the infinite game loop
while True:
    x = '🛰️  DEEP-SPACE 1: ORBITAL FLUX SURVIVAL'
    print(x.center(50))  # printing the first heading
    print()  # one line gap
    print("📡 SCANNER: Cosmic Storm Detected!")
    print()

    print("-> Electric Field Intensity (E) = 500 N/C [⚠️ HIGH DENSITY]")  # fixed electric field intensity
    E = 500  # defining E
    print("🚨 CRITICAL CAPACITOR LIMIT (after this, the metal will be defected) = 3000 Units")
    print()
    y = "🛠️ DEPLOY CONFIGURATION HYPER-DRIVE:"
    print(y.center(50))
    print()

    # user inputs
    print("Select Deflection Panel Surface Area (A): ")
    print()
    print("[1] Titanium Shield Core  [Area = 2 m²]")
    print()
    print("[2] Graphene Energy Grid  [Area = 10 m²]")
    print()
    user_Input1 = int(input('👉 Choose Panel Size (1/2): '))

    print('Adjust Hull Alignment Angle (θ to Vector Normal)')
    print("[A] 0°   [PERPENDICULAR FACE - Direct Vector Intercept]")
    print("[B] 90°  [PARALLEL BYPASS - Sliding Flow Deflection]")
    print("[C] 180° [INVERTED ALIGNMENT - Reverse Vector Flow]")
    print()
    user_input2 = input("👉 Choose Angular Alignment (A/B/C): ")
    A1 = 2
    A2 = 10
    #THE FULL IF-ELSE(THE MAIN SYSTEM OF THE GAME):
    if user_Input1 == 1:
        print("[SYSTEM]: Surface Area locked at A = 2.0 m²")
        print()
        if user_input2.lower() == 'a':
            thetha = 0
            thetha_radians = math.radians(thetha)
            result = math.cos(thetha_radians)
            print("⚙️ PROCESSING GEOMETRIC FLUX SOLVER...")
            print("[THEORY]: Area vector is parallel to the Electric Field Lines.")
            print()
            
            result_2 = E * A1 * result  # Fixed: removed set braces
            print(f"Vector Equation : Φ = {result_2}")
            print()
            print("📊 COCKPIT TELEMETRY REPORT:")
            print()
            print(f"NET GAUSSIAN FLUX (Φ) : {result_2} [ZERO FLUX INTEGRAL] ")
            print()
            print("▪️ SYSTEM HULL INTEGRITY  : 100% [STABLE]")        
            print()

            print("🏆 MISSION EVALUATION: ABSOLUTE SUCCESS")
            print()
            print("The deadly solar storm lines slid parallel past the panel surface. ")
            print("Clean orbital maneuver, Captain! Deep-Space 1 is completely safe.")
        elif user_input2.lower() == 'b':
            thetha = 90
            thetha_radians = math.radians(thetha)  # Fixed typo: radinas -> radians
            result = math.cos(thetha_radians)
            print("⚙️ PROCESSING GEOMETRIC FLUX SOLVER...")
            print()
            print("[THEORY] : Area vector is perpendicular to the Electric field lines.")
            print()
            
            result_2 = E * A1 * result  # Fixed: removed set braces
            print(f"Vector Equation : Φ = {result_2} ")
            print("📊 COCKPIT TELEMETRY REPORT:")
            print(f"NET GAUSSIAN FLUX (Φ) : {result_2} ")
            print()
            print("▪️ SYSTEM HULL INTEGRITY  : 90% [STABLE]")        
            print()
            print()
            print("🏆 MISSION EVALUATION:  SUCCESS")
            print()
            print("The deadly solar story came, but your slid were powerful enough to come in front of the storm, and save your life")
        else:
            thetha = 180
            thetha_radians = math.radians(thetha)
            result = math.cos(thetha_radians)
            print("⚙️ PROCESSING GEOMETRIC FLUX SOLVER...")
            print()
            print("[THEORY]: Area vector is anti-parallel to the Electric Field Lines. ")
            
            result_2 = E * A1 * result  # Fixed: removed set braces
            print(f"Vector Equation : Φ = {result_2} ")
            print("📊 COCKPIT TELEMETRY REPORT:")
            print(f"NET GAUSSIAN FLUX (Φ) : {result_2} ")
            print()
            print("▪️ SYSTEM HULL INTEGRITY  : 9% [STABLE]")        
            print()
            print()
            print("❌ MISSION ABORTED: FAILURE")
            print()
            print("You just forced your panels to go antiparallel, which gained a lot amount of friction, and destroyed your crew, better you had learned physics..... ")
    else:
        print("[SYSTEM]: Surface Area locked at A = 10.0 m²")  # Fixed string to say 10.0 m²
        print()
        if user_input2.lower() == 'a':
            thetha = 0
            thetha_radians = math.radians(thetha)
            result = math.cos(thetha_radians)
            print("⚙️ PROCESSING GEOMETRIC FLUX SOLVER...")
            print("[THEORY]: Area vector is parallel to the Electric Field Lines.")
            print()
            
            result_2 = E * A2 * result  # Fixed math: Changed A1 to A2
            print(f"Vector Equation : Φ = {result_2}")
            print()
            print("📊 COCKPIT TELEMETRY REPORT:")
            print()
            print(f"NET GAUSSIAN FLUX (Φ) : {result_2} [ZERO FLUX INTEGRAL] ")
            print()
            print("▪️ SYSTEM HULL INTEGRITY  : 100% [STABLE]")        
            print()

            print("🏆 MISSION EVALUATION: ABSOLUTE SUCCESS")
            print()
            print("The deadly solar storm lines slid parallel past the panel surface. ")
            print("Clean orbital maneuver, Captain! Deep-Space 1 is completely safe.")
        elif user_input2.lower() == 'b':
            thetha = 90
            thetha_radians = math.radians(thetha)
            result = math.cos(thetha_radians)
            print("⚙️ PROCESSING GEOMETRIC FLUX SOLVER...")
            print()
            print("[THEORY] : Area vector is perpendicular to the Electric field lines.")
            print()
            
            result_2 = E * A2 * result  # Fixed: removed set braces
            print(f"Vector Equation : Φ = {result_2} ")
            print("📊 COCKPIT TELEMETRY REPORT:")
            print(f"NET GAUSSIAN FLUX (Φ) : {result_2} ")
            print()
            print("▪️ SYSTEM HULL INTEGRITY  : 0% [STABLE]")        
            print()
            print()
            print("❌ MISSION ABORTED: FAILURE")
            print()
            print("Your Slid's capacity was only 3000, and the flux was of 5000, which just systematically destroyed your space shuttle")
        else:  
            thetha = 180
            thetha_radians = math.radians(thetha)  # Fixed typo: radinas -> radians
            result = math.cos(thetha_radians)
            print("⚙️ PROCESSING GEOMETRIC FLUX SOLVER...")
            print()
            print("[THEORY]: Area vector is anti-parallel to the Electric Field Lines. ")
            
            result_2 = E * A2 * result  # Fixed: removed set braces
            print(f"Vector Equation : Φ = {result_2} ")
            print("📊 COCKPIT TELEMETRY REPORT:")
            print(f"NET GAUSSIAN FLUX (Φ) : {result_2} ")
            print()
            print("▪️ SYSTEM HULL INTEGRITY  : .9% [STABLE]")        
            print()
            print()
            print("❌ MISSION ABORTED: FAILURE")
            print()
            print("You just forced your panels to go antiparallel, which gained a lot amount of friction, and destroyed your crew, better you had learned physics..... ")

    # Ask user if they want to play again
    play_again = input("🔄 Play another round, Captain? (y/n): ").strip().lower()
    
    # Break out of the loop if they want to stop
    if play_again not in ['y', 'yes']:
        print("🚀 Hyper-drive shut down. Safe travels through the cosmos!")
        break
#YEAH! CODE IS COMPLETE!!
#HAVE FUN.
