from Room import Room
class Hotel:
    theRooms = []
    __name = ' '
    __location = ' '
    occupiedCnt = 0
    numOfRooms = 0

    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.theRooms = []
        occupiedCnt = 0
        self.numOfRooms = 0

    def isFull(self):
        if self.occupiedCnt == self.numOfRooms:
            return True
        else:
            return False

    def isEmpty(self):
        if self.occupiedCnt == 0:
            return True
        else:
            return False

    def addRoom(self, roomNum, bedType, smoking, price):
        self.numOfRooms += 1
        self.theRooms.append(Room(roomNum, bedType, smoking, price))

    def addReservation(self, occupantName, smoking, bedtype):
        notFound = True
        for i in range(len(self.theRooms)):
            if (Room.get__BedType(self.theRooms[i]) == bedtype) and (
                    Room.get__Smoking(self.theRooms[i]) == smoking) and (Room.isOccupied(self.theRooms[i]) == False):
                Room.set_Occupied(self.theRooms[i], True)
                Room.set_Occupant(self.theRooms[i], occupantName)
                self.occupiedCnt += 1
                print(
                    f'Room is reserved for {occupantName}\nRoom# {i}\nbedType: {Room.get__BedType(self.theRooms[i])}\nSmoking: {smoking}\n')
                break
            if (len(self.theRooms) == i + 1):
                print('Sorry, There is no room available as per requirement')

    def cancelReservation(self, occupantName):
        found = self.findReservation(occupantName)
        if not (found == -1):
            print(f'Reservation of {occupantName} is succussfully cancelled {found}')
        else:
            print(f'{occupantName} name is not found')

    def findReservation(self, occupantName):
        NOT_FOUND = True
        i = 0
        while NOT_FOUND == True:
            if Room.get__Occupant(self.theRooms[i]) == occupantName:
                Room.set_Occupied(self.theRooms[i], False)
                NOT_FOUND = False
                return i
            else:
                i += 1
            if (len(self.theRooms) == i + 1):
                return -1

    def printReservationList(self):
        for i in range(len(self.theRooms)):
            if (Room.isOccupied(self.theRooms[i]) == True):
                print(
                    f'Room Number: {i}\nOccupant name: {Room.get__Occupant(self.theRooms[i])} \nSmoking room:{Room.get__Smoking(self.theRooms[i])}\nBed type: {Room.get__BedType(self.theRooms[i])} \nRate: {Room.get__RoomRate(self.theRooms[i])}')

                print('---------------------------')

    def getDailySales(self):
        price = 0
        for i in range(len(self.theRooms)):
            if (Room.isOccupied(self.theRooms[i])):
                price += Room.get__RoomRate(self.theRooms[i])

        print(f'Total cost for occupied rooms: ${price}')

    def occupancyPercentage(self):
        occ = 0
        for j in range(len(self.theRooms)):
            if (Room.isOccupied(self.theRooms[j])):
                occ += 1
        perc = len(self.theRooms) / occ
        print('{0:.2f} Percent'.format(round(perc, 2)))

    def set__name(self, name):
        self.name = name

    def get__name(self):
        return self.name

    def set__location(self, location):
        self.location = location

    def get__location(self):
        return self.location

    def printStr(self):
        print(
            f'Hotel Name: {self.name} \nNumber of rooms: {self.numOfRooms} \nNumber of occupied rooms: {self.occupiedCnt}\n\nRoom Details are:\n\n')
        for i in range(len(self.theRooms)):
            if (Room.isOccupied(self.theRooms[i])):
                print (
                    f'Room number:{Room.get__RoomNum(self.theRooms[i])} \nOccupant name: {Room.get__Occupant(self.theRooms[i])} \nSmoking room: {Room.get__Smoking(self.theRooms[i])} \nBed Type: {Room.get__BedType(self.theRooms[i])} \nRate: {float(Room.get__RoomRate(self.theRooms[i]))}\n')
            else:
                print (
                    f'Room number:{Room.get__RoomNum(self.theRooms[i])} \nOccupant name: Not Occupied \nSmoking room: {Room.get__Smoking(self.theRooms[i])} \nBed Type: {Room.get__BedType(self.theRooms[i])} \nRate: {float(Room.get__RoomRate(self.theRooms[i]))}\n')

#     def printStr(self):
#         print(Room.__str__(self.name, self.numOfRooms, self.occupiedCnt, self.theRooms))



