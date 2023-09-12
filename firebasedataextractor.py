import firebase_admin
from firebase_admin import credentials, db

cred = credentials.Certificate(r'    ')   #give json file between the ' '
firebase_admin.initialize_app(cred, {
    'databaseURL': '  '   #your url
})

def read_all_drone_data():
    all_drone_data = {}
    for drone_number in range(1, 5):
        drone_data = read_drone_data(drone_number)
        if drone_data:
            all_drone_data[f'Drone {drone_number}'] = drone_data
    return all_drone_data

def read_drone_data(drone_number):
    try:
        # Replace '/drone1', '/drone2', '/drone3', '/drone4' with the appropriate paths for your database
        ref = db.reference(f'/drone{drone_number}')
        drone_data = ref.get()

        if drone_data:
            return drone_data
        else:
            print(f"Drone {drone_number} data not found in the database.")
            return None
    except Exception as e:
        print(f"Error reading data for Drone {drone_number}: {e}")
        return None
def print_drone_data(drone_data):
    for key, value in drone_data.items():
        if isinstance(value, dict):
            print(f"{key}:")
            for sub_key, sub_value in value.items():
                print(f"  {sub_key}: {sub_value}")
        else:
            print(f"{key}: {value}")

if __name__ == "__main__":
    all_data = read_all_drone_data()
    for drone_number, drone_data in all_data.items():
        print(f"Data for {drone_number}:")
        print_drone_data(drone_data)
        print()
