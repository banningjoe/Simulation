class Location:
    def __init__(self, row, column):
        """Initialize a location.

        @type self: Location
        @type row: int
        @type column: int
        @rtype: None
        """
        # TODO
        self.location = [row,column]
        
    def __str__(self):
        """Return a string representation.

        @rtype: str
        """
        # TODO
        return str(self.location)

    def __eq__(self, other):
        """Return True if self equals other, and false otherwise.
        @type other: Location
        @rtype: bool
        """
        # TODO
        return self.location[0] == other.location[0] and self.location[1] == \
        other.location[1]
    


def manhattan_distance(origin, destination):
    """Return the Manhattan distance between the origin and the destination.

    @type origin: Location
    @type destination: Location
    @rtype: int
    """
    # TODO
    return abs(destination[0] - origin[0]) + abs(destination[1] - origin[1])



def deserialize_location(location_str):
    """Deserialize a location.

    @type location_str: str
        A location in the format 'row,col'
    @rtype: Location
    """
    # TODO
    temp_list = location_str.split(",")
    location = Location(int(temp_list[0]),int(temp_list[1]))
    return location