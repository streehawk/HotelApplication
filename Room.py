class Room:
    roomNum = 0
    bedType = " "
    rate = 0.0
    occupantName = " "
    smoking = ''

    def __init__(self, roomNum, bedType, smoking, rate):
        self.roomNum = roomNum
        self.bedType = bedType
        self.smoking = smoking
        self.rate = rate
        self.set_Occupied(False)

    #         print(self.__str__(Hotel))

    def get__BedType(self):
        return self.bedType

    def get__Smoking(self):
        return self.smoking

    def get__RoomNum(self):
        return self.roomNum

    def get__RoomRate(self):
        return self.rate

    def get__Occupant(self):
        return self.occupantName

    def set_Occupied(self, occupied):
        self.occupied = occupied

    def set_Occupant(self, occupantName):
        self.occupantName = occupantName

    def set_RoomNum(self, roomNum):
        self.roomNum = roomNum

    def setBedType(self, bedType):
        self.bedType = bedType

    def setRate(self, rate):
        self.rate = rate

    def setSmoking(self, smoking):
        self.smoking = smoking

    def isOccupied(self):
        return self.occupied

#     def __str__(hotelName, numOfRooms, occupiedCount, theRooms):
#         for i in range(len(theRooms)):
#             return ('Hotel Name: {}\nNumber of rooms: {}\nNumber of occupied rooms: {}\n\nRoom Details are:\n\nRoom number {} '.format(hotelName, numOfRooms, occupiedCount))
# #         return "{self.roomNum} {self.bedType} {self.smoking} {self.rate}".format(self=self)


#         r

