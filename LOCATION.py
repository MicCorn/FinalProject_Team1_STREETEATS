import googlemaps
from datetime import datetime
gmaps = googlemaps.Client(key='AIzaSyDlf5AW-SAArmbJNIQieRH84zv_I2Iugr4')

def search(customer_location):
  foodDic = {}
  #Get customer location, use Google Maps to grab its coordinates
  if customer_location == len(customer_location)*" " or customer_location == "here":
    locTuple = (41.38843845116738, 2.170912691748747)
  else:
    geocode_result = gmaps.geocode(customer_location)
    if geocode_result == []:
      raise NameError("Could not find " + customer_location)
    #Add coordinates to a tuple
    locTuple = (geocode_result[0]["geometry"]["location"]["lat"], geocode_result[0]["geometry"]["location"]["lng"])
  #Search for nearby kebab resturaunts
  unformatted_dict = gmaps.places_nearby(location = locTuple, radius = 15000, keyword = "kebab", open_now = True, type = "restaurant")
  #Add all results to a dictionary
  rest = 0
  for item in unformatted_dict["results"]:
    rest +=1 #Resturaunt incrementing variable
    #Get resturaunt location
    restTuple = (item['geometry']['location']['lat'], item['geometry']['location']['lng'])
    #Calculate biking directions (some deliveries on foot, gives an approximate answer)
    directions_result = gmaps.directions(restTuple,
                                     locTuple,
                                     mode="bicycling",
                                     departure_time=datetime.now())
    #Add all info to dictionary, with appropriate key names
    try:
      foodDic["r" + str(rest)] = {"name": item["name"], 'rating': item["rating"], 'price_level': item["price_level"], 'distance': directions_result[0]['legs'][0]['distance']['text'], 'duration': directions_result[0]['legs'][0]['duration']['text']}
    except KeyError:
      foodDic["r" + str(rest)] = {"name": item["name"], 'rating': item["rating"], 'distance': directions_result[0]['legs'][0]['distance']['text'], 'duration': directions_result[0]['legs'][0]['duration']['text']}
  
  return foodDic

#Example format for a single item returned dictionary, "foodDic":
  """
  'r12': {
  'name': 'NAME OF RESTURAUNT'
  'rating': ''
  }
  """
  
  