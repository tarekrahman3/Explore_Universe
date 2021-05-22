import json

class constants():
    one_lightyear_km = float(9.46) * pow(10, 12)
    Mile_to_Kilo = float(1.60934)
    Kilo_to_Mile = float(0.621371)

class StarSystem():
    with open('list of stars.json', 'r') as json_s:
        star_data = json.load(json_s)

class TravelVehicle():
    with open('list of vehicles.json', 'r') as json_v:
        vehicle_dict = json.load(json_v)

stars = StarSystem.star_data.keys()
i = 0
starpreview = {}
for star in stars:
    starpreview.update({i : star})
    i=i+1
print("\n".join("{}\t{}".format(key, value) for key, value in starpreview.items()))

vehicles = TravelVehicle.vehicle_dict.keys()
vehiclepreview = {}
n = 0
for vehicle in vehicles:
    vehiclepreview.update({n : vehicle})
    n=n+1

destination = input("Enter stars index number: ")
print("\n".join("{}\t{}".format(key, value) for key, value in vehiclepreview .items()))
transport = input("select transportation (type serial number):")

travel_hour = StarSystem.star_data[starpreview[int(destination)]]['distance_ly'] * constants.one_lightyear_km/TravelVehicle.vehicle_dict[vehiclepreview[int(transport)]]['Speed (km/h)']

print('\nThe journey to ' + starpreview[int(destination)] + ' by ' + vehiclepreview[int(transport)] + ' will take '+ str((travel_hour/24)/365) + ' years\n')
