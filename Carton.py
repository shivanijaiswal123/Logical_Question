N=int(input("Enter any number less than 1000"))
total=0
if(N<1000):

    if(N>=48):
        fourth_box=N/48
        print(fourth_box)
        print("48*" + str(fourth_box) + "="),48*fourth_box
        N=N%48
        total=total+fourth_box

    if(N>=24):
        third_box=N/24
        print("24*" + str(third_box) + "="),24*third_box
        N=N%24
        total=total+third_box

    if(N>=12):
        second_box=N/12
        print("12*" + str(second_box) + "="),12*second_box
        N=N%12
        total=total+second_box


    if(N>=6):
        first_box=N/6
        print("6*" + str(first_box) + "="),6*first_box
        N=N%12
        total=total+first_box

    if(N>0 and N<6):
        first_box=first_box+1
        print("6*"+str(first_box))
        total=total+first_box

else:
    print "invalid input"

print "The total no of cartons=",total