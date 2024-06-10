class NewMultipleFunctions():
    def subfields():
        subfieldsInAI =["Machine Learning","Neural Networks","Vision","Robotics","Speech Processing","Natural Language Processing"]
        print ("Sub-Fields in AI are : ")
        for fields in subfieldsInAI:
            print(fields)
            #fields = subfieldsInAI
        #return fields
        
    def oddEven():
                num = int(input("Enter The number : "))
                if(num%2==0):
                    print(num, "is Even number")
                    msg = num, "is Even number"
                else:
                    print(num, "is Odd number")
                    msg = num, "is Odd number"
                #return msg
        #oddEven()
        
    def eligible():
                    gender = input("Enter your gender : ")
                    age = int(input("Enter your age : "))
                    if (gender=="male" and age>20):
                        print("ELIGIBLE")
                    elif (gender=="female" and age>17):
                        print("ELIGIBLE")
                    else:
                        print("NOT ELIGIBLE")
        #eligible()
        
    def percentage():
            subject1 = int(input("Subject1 : "))
            subject2 = int(input("Subject2 : "))
            subject3 = int(input("Subject3 : "))
            subject4 = int(input("Subject4 : "))
            subject5 = int(input("Subject5 : "))
            Total = subject1 + subject2 + subject3 + subject4 + subject5
            print ("Total : ",Total)
            Percent = (Total/5)
            print("Percentage : ",Percent)
            if ((subject1 or subject2 or subject3 or subject4 or subject5)>=35):
                print ("Result : PASS")
            else:
                print ("Result : FAIL")
        #percentage()
        
    def areaTriangle():
            Height = int(input("Entre the Height of the Triangle : "))
            Breadth = int(input("Entre the Breadth of the Triangle : "))
            Area_Of_Triangle = (Height*Breadth)/2
            print ("Height :", Height )
            print ("Breadth :", Breadth)
            print ("Area of Triangle Formula : ", "(Height*Breadth)/2")
            print ("Area of Triangle :", Area_Of_Triangle)
            
    def perimeterTriangle():
            Height1 = int(input("Entre the Height1 of the Triangle : "))
            Height2 = int(input("Entre the Height2 of the Triangle : "))
            Breadth1 = int(input("Entre the Breadth of the Triangle : "))
            Perimeter_Of_Triangle = Height1 + Height2 + Breadth1
            print ("Height1 :", Height1 )
            print ("Height2 :", Height2 )
            print ("Breadth1 :", Breadth1 )
            print ("Perimeter of Triangle Formula : ", "Height1*+ Height2 + Breadth1")
            print ("Perimeter of Triangle : ", Perimeter_Of_Triangle)

    #areaTriangle()
    #perimeterTriangle()