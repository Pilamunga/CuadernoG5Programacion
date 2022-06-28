vector1=[1,2,3,4,5,6,7,8,9,10]
vector2=[1,2,3,4,5,6,7,8,9,10]
vector3=[0]*10
vector3[9]=vector1[9]+vector2[9]
for item in range (10):
    vector3[item]=vector1[item]+vector2[item]
    print(vector3[item],end= " ")  
    
print("\n")
print(vector3)
