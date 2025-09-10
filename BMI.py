#  BMI Checker 

# BMI Constants 
UNDER = 18.5
NORMAL = 24.9
OVER = 29.9

# Pang we-welcome kay user
print (" Mabuhay!  eto ang BMI Checker ")

# Tagatanggap ng mga input mula sa user
name = input("Anong iyng pangalan: ")
weight = float(input("Ilagay anf iyong timbang kg: "))
height = float(input("Ilagay ang iyong taas sa metro: "))
height = height / 100  # Convert height from cm to m
 
# Pagkalkula ng BMI at kategorya

if (weight > 0 and height > 0):
    bmi = weight / (height ** 2)
    print(f"Ang iyong BMI ay: {bmi:.2f}")

    if bmi < UNDER:
        print(f"{name}, ikaw ay underweight.")
    elif UNDER <= bmi <= NORMAL:
        print(f"{name}, ikaw ay may normal na timbang.")
    elif NORMAL < bmi <= OVER:
        print(f"{name}, ikaw ay overweight.")
    else:
        print(f"{name}, ikaw ay obese.")