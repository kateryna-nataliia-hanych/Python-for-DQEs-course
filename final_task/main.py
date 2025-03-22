from my_classes.DBConnection import DBConnection
from my_classes.City import City

city1_name = input('Please write the first city: ').strip().lower().capitalize()
print(f'You\'ve entered: {city1_name}')
city2_name = input('Please write the second city: ').strip().lower().capitalize()
print(f'You\'ve entered the next one: {city2_name}')


db_name = 'cities.db'
db_table = 'city_table'
dbc = DBConnection(db_name)
dbc.create_table(db_table, ('city', 'TEXT'), ('lat', 'REAL'), ('lon', 'REAL'))


# result = dbc.cursor.fetchone()
# print(result)

# Function to safely convert to float
def get_float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError as e:
            print(f"An error occured {e}")


# Function to handle city data retrieval or insertion
def handle_city(city_name):
    city = City(city_name)

    # Check if city data already exists
    if res := dbc.select(db_table, ['lon', 'lat'], f'city="{city.name}"'):
        city.lon, city.lat = res[0]
        print(f'Coordinates of {city.name} - Lon: {city.lon}, Lat: {city.lat}')
    # If not, prompt the user to input the coordinates
    else:
        city.lon = get_float_input(f'Please write lon of {city.name}: ')
        city.lat = get_float_input(f'Please write lat of {city.name}: ')
        # Insert city data into the database
        dbc.insert(db_table, city=city.name, lon=city.lon, lat=city.lat)

    return city


# Handle first city
city1 = handle_city(city1_name)

# Handle second city
city2 = handle_city(city2_name)

distance = city1.distance_to_other_city(city2)
print(f"The distance between {city1.name} and {city2.name} is: {distance:.2f} kilometers")