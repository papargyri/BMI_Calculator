height=float(input("Please enter your height in centimeters: "))

weight=float(input("Please enter your Weight in Kg: "))

height = height/100

BMI=weight/(height*height)

print("Your Body Mass Index (BMI) is: ",round(BMI,2)) #Printing BMI with 2 decimal points

if(BMI>0):
    if(BMI<=16):
        print("According to the World Health Organization(WHO) you belong to the Severe Thinness category.")
    elif(BMI<=17):
        print("According to the World Health Organization(WHO) you belong to the Moderate Thinness category.")
    elif(BMI<=18.5):
        print("According to the World Health Organization(WHO) you belong to the Mild Thinness category.")
    elif(BMI<=25):
        print("According to the World Health Organization(WHO) you belong to the Normal category.")
    elif(BMI<=30):
        print("According to the World Health Organization(WHO) you belong to the Owergeight category.")
    elif(BMI<=35):
        print("According to the World Health Organization(WHO) you belong to the Obese Class I category.")
    elif(BMI<=40):
        print("According to the World Health Organization(WHO) you belong to the Obese Class II category.")
    else: 
        print("According to the World Health Organization(WHO) you belong to the Obese Class III category.")
        
else:("The details you have entered are not correct. Please try again")
