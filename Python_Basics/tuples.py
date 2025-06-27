import sys

def main():

    coordinates = (42.376,-71.115)
    coordinates_list =[42.376,-71.115]
    #coordinates[0] = 56.454 error because we cant add or change any element in tuples
    #only use tuples if you are sure that data is fix it helps in dpace managing
    latitude,longitude = coordinates
    print(coordinates)
    print(f"Latitude : {coordinates[0]}")
    print(f"Longitude : {coordinates[1]}")   

    print(latitude,longitude) 

    print(f"{sys.getsizeof(coordinates)} bytes")
    print(f"{sys.getsizeof(coordinates_list)} bytes")
    
    
main()    