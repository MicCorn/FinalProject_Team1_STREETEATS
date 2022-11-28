import googlemaps
from datetime import datetime
gmaps = googlemaps.Client(key='AIzaSyDlf5AW-SAArmbJNIQieRH84zv_I2Iugr4')

def search(customer_location):
  foodDic = {}
  if customer_location == len(customer_location)*" " or customer_location == "here":
    locTuple = (41.38843845116738, 2.170912691748747)
  else:
    geocode_result = gmaps.geocode(customer_location)
    if geocode_result == []:
      raise NameError("Could not find " + customer_location)
    locTuple = (geocode_result[0]["geometry"]["location"]["lat"], geocode_result[0]["geometry"]["location"]["lng"])
  awful_dict = gmaps.places_nearby(location = locTuple, radius = 15000, keyword = "kebab", open_now = True, type = "restaurant")
  rest = 0
  for item in awful_dict["results"]:
    rest +=1
    try:
      foodDic["r" + str(rest)] = item["name"], item["rating"], item["price_level"]
    except KeyError:
      foodDic["r" + str(rest)] = item["name"], item["rating"]
  
  return foodDic
"""
print(item["name"], "--- Rating:", item["rating"], "--- Price Rating:", item["price_level"])
print(item["name"], "--- Rating:", item["rating"])

# Look up an address with reverse geocoding
reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))

gmaps.places("resturaunt",)

# Request directions via public transit
now = datetime.now()
directions_result = gmaps.directions("Sydney Town Hall",
                                     "Parramatta, NSW",
                                     mode="transit",
                                     departure_time=now)

# Validate an address with address validation
addressvalidation_result =  gmaps.addressvalidation(['1600 Amphitheatre Pk'], 
                                                    regionCode='US',
                                                    locality='Mountain View', 
                                                    enableUspsCass=True)
  """

  
  