#!/usr/bin/python
"""
Calculate the total cost of tile it would take to cover a floor plan of width 
and height, using a cost entered by the user.
"""

def calc_tile_cost(width, length, cost):
    """
    Calculates tile cost. 

    Assumes cost is in units of "$/(width unit * length unit)"
    """
    return width * length * cost

def main():
    """
    Asks for width, length, cost of floor tile

    Prints total cost
    """
    width = float(input("Width of floor (in m): "))
    length = float(input("Length of floor (in m): "))
    cost = float(input("Cost of floor (in $/m^2): "))

    print("Total cost: ${0:.2f}".format(calc_tile_cost(width, length, cost)))

if __name__ == '__main__':
    main()
