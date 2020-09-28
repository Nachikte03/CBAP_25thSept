# -*- coding: utf-8 -*-
#https://treyhunner.com/2016/04/how-to-loop-with-indexes-in-python/
#for loop


teamA = ['India', 'Australia','Pakistan', 'England']   # 4elements   list index 0-3

teamA

teamA[0]
teamA[1]
teamA[2]
teamA[3]

#for varname in list:
#   statements

for var in teamA :
    print(var)



lenteamA= len(teamA)
lenteamA


#LT= range(lenteamA)
#LT 

r1= range(1, 11)

for i in r1:
    print(2*i)


lenteamA= len(teamA)
lenteamA
teamA
teamB=[]
teamB

teamA = ['India', 'Australia','Pakistan', 'England']   # 4elements   list index 0-3

for i in range(lenteamA):
    #    teamB.append(teamA[i])
    teamA[i]=str(teamA[i]) +"_A"
    
    
teamA


#team names
for i in teamA : print(i)

#characters of the word
for i in teamA[0]: print(i)



for i in teamA:
    if i == 'India' :
        print('India is in Team A', '\t : ' , i)        
    else:
        print("India is not in Team A")

    
#x = 'Pakistan'
x = 'Bangladesh'
teamA

for i in teamA:
    if i == x :
        print(x , " is in Team A", '\t : ' , i)
        break   #exit if x is found otherwise loop over
    else:
        print(x , " is not in Team A")

#


range(6)
for x in range(6) : 
    print("\t ABC \n\n")



range(6)
for x in range(6) : 
    print(x)

range(6)
for x in range(6) : 
    print(x, end = ' ')



a=range(2,6)

La = list(a)

La


for x in range(2,6) : 
    print('x=', x, end = '  ' )




a=range(1, 50, 3)

La = list(a)

La



for x in range(2,10,2) : 
    print(x, end = ' ')



#While Loop

# -*- coding: utf-8 -*-
#Loop - while
#execute set of statements as long as the condition is true





while (False):    
    print('Vikas')


print("i =",1)
print("i =",2)
print("i =",3)
print("i =",4)
print("i =",5)
print("i =",6)
print("i =",7)
print("i =",8)
print("i =",9)


i = 1

while (i <= 10):
    print("i =",i)
    i = i + 1  #import to increment
    
    
    

#break the loop in between

i = 1
while (i < 10):
    
    if i == 5 : #end here
        print('Exiting Loop at this point')
        break
    print(i )
    i += 1



#use of continue - continue with loop
i = 0
while (i < 10):
    i += 1
    if i == 5 : #continue with loop
        continue
    print(i, end = '\t')
    



arr= list(range(100, 200))
arr

i = 0

arr[80]


while(i<len(arr)):
    if(i==80):
        print(arr[i])
    i=i+1
    
    
    
i=0
while(i<10):
    i=i+1
    if i==5:
        continue
    else:
        print(i)
        
        
        
L1=[10,20,30]    
L2=L1
L1
L2

L2[0]=40
L2
L1 

L3=L1.copy()
L3[0]=40
L3
L1 
   






