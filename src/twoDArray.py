
rRow = ["r1","r2","r3","r4","r5","r6"]
yRow =  ["y1","y2","y3","y4","y5","y6"]
xRow = ["x1","x2","x3","x4","x5","x6"]

movieHall = [["r1","r2","r3","r4","r5","r6"],
             ["y1","y2","y3","y4","y5","y6"],
             ["x1","x2","x3","x4","x5","x6"]]

# print(movieHall[0][1])

for rowNumber in range(len(movieHall)):
    eachRow = movieHall[rowNumber]
    for seatNumber in range(len(eachRow)):
        print(movieHall[rowNumber][seatNumber])

for row in movieHall:
    print(row)
    for seat in row:
        print(seat)







# rRowVar = movieHall[0]

# print(movieHall[1][2])
# print(movieHall[2][4])










# dilshara_details = [22,"Dila","Engineer","Kotte",True,98.5]
# print(len(dilshara_details))
# town = dilshara_details[3]
# print(town)
#
# for i in range(len(dilshara_details)):
#     print(dilshara_details[i])
# #
# # for i in dilshara_details:
# #     print(i)
# #
name = " Dilshara"
city = "Ethul kotte"
age =16

# description = "My Name is " + name + ". And I live in " + city + " My age is " + age
description2 = f"My name is {name}. And I live in {city}. My age is {age}"

print(description2)

