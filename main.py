import json

class Constants():
    one_lightyear_km = float(9.46) * pow(10, 12)
    Mile_to_Kilo = float(1.60934)
    Kilo_to_Mile = float(0.621371)

class StarSystem():
    with open('list of stars.json', 'r') as json_s:
        star_data = json.load(json_s)

class TravelVehicle():
    with open('list of vehicles.json', 'r') as json_v:
        vehicle_dict = json.load(json_v)

class DataViewer():
    def show_all_stars():
        stars = StarSystem.star_data.keys()
        i = 0
        starpreview = {}
        for star in stars:
            starpreview.update({i : star})
            i=i+1
        print("\n".join("{}\t{}".format(key, value) for key, value in starpreview.items()))
        return starpreview

    def show_all_vehicles():
        vehicles = TravelVehicle.vehicle_dict.keys()
        vehiclepreview = {}
        n = 0
        for vehicle in vehicles:
            vehiclepreview.update({n : vehicle})
            n=n+1
        print("\n".join("{}\t{}".format(key, value) for key, value in vehiclepreview .items()))
        return vehiclepreview

def take_user_inputs():
    starpreview = DataViewer.show_all_stars()
    destination = input("Enter stars index number: ")
    vehiclepreview = DataViewer.show_all_vehicles()
    transport = input("select transportation (type serial number):")
    return (destination, transport, starpreview, vehiclepreview)

def calculate_the_journey_time(destination, transport):
    travel_hour = StarSystem.star_data[starpreview[int(destination)]]['distance_ly'] * Constants.one_lightyear_km/TravelVehicle.vehicle_dict[vehiclepreview[int(transport)]]['Speed (km/h)']
    return travel_hour

if __name__ =='__main__':
    destination, transport, starpreview, vehiclepreview = take_user_inputs()
    travel_hour = calculate_the_journey_time(destination, transport)
    print('\nThe journey to ' + starpreview[int(destination)] + ' by ' + vehiclepreview[int(transport)] + ' will take '+ str((travel_hour/24)/365) + ' years\n')
