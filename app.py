from Hotel import Hotel
from Room import Room

myHotel = Hotel('Rayyan', 'Malibu')
for i in range(11):
    if (i % 2 == 0):
        myHotel.addRoom(i, 'King', 'n', 199)
    else:
        myHotel.addRoom(i, 'Queen', 's', 259)
print(myHotel.addReservation('Ray','s','Queen'))
print(myHotel.addReservation('Anya','n','King'))
print(myHotel.addReservation('Yo','n','King'))
print(myHotel.addReservation('Van','s','Queen'))
print(myHotel.addReservation('Dylan','n','King'))
myHotel.printReservationList()
myHotel.printStr()