   
r1=[1,2,3,4,5,6,7,8,9,10,11,12,
    13,14,15,16,17,18,19,20,21,22,23,24,
    25,26,27,28,29,30,31,32,33,34,35,36,
    37,38,39,40,41,42,43,44,45,46,47,48,
    49,50,51,52,53,54,55,56,57,58,59,60,
    61,62,63,64,65,66,67,68,69,70,71,72,
    73,74,75,76,77,78,79,80,81,82,83,84,
    85,86,87,88,89,90,91,92,93,94,95,96,
    97,98,99,100,101,102,103,104,105,106,107,108,
    109,110,111,112,113,114,115,116,117,118,119,120]

r2=[1,2,3,4,5,6,7,8,9,10,11,12,
    13,14,15,16,17,18,19,20,21,22,23,24,
    25,26,27,28,29,30,31,32,33,34,35,36,
    37,38,39,40,41,42,43,44,45,46,47,48,
    49,50,51,52,53,54,55,56,57,58,59,60]
      
y= 0
count = 0
while y < 180:
    print("---------------------------------")
    print("Divadlo-sedadla")
    print("---------------------------------\n")
    num = 1
    print("Spodní Patro")
    for x in r1:
        print(x, end =' ')
        if(num%12 ==0):
            print('\n')
        num+=1
    num =1
    print("\nHorní Patro")
    for x in r2:
        print(x, end =' ')
        if(num%12 ==0):
            print('\n')
        num+=1
    
    print("Celkem obsazeno míst:",end= ' ')
    print(count)
    rada = input("\nvyber řadu-(D nebo H)")
    if(rada == "d"):
        i = int(input("\nvyber sedadlo:"))
        r1[i-1] = 'X'
        count+=1
    if(rada == "h"):
        i = int(input("\nvyber sedadlo:"))
        r2[i-1] = 'X'
        count+=1

    print("....................................................")
    y+= 1

    

