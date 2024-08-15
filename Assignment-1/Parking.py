class Vehicle:
    def __init__(self, license_plate, vehicle_type):
        self.license_plate = license_plate
        self.vehicle_type = vehicle_type

class Car(Vehicle):
    def __init__(self, license_plate, vehicle_type, brand_name, name):
        super().__init__(license_plate, vehicle_type)
        self.brand_name = brand_name
        self.name = name

class Bike(Vehicle):
    def __init__(self, license_plate, vehicle_type, brand_name, name):
        super().__init__(license_plate, vehicle_type)
        self.brand_name = brand_name
        self.name = name

class ParkingSpot:
    def __init__(self, spot_id):
        self.spot_id = spot_id
        self.is_available = True
        self.vehicle = None

    def park_vehicle(self, vehicle):
        if self.is_available:
            self.vehicle = vehicle
            self.is_available = False
        else:
            raise Exception("Spot is already taken.")

    def retrieve_vehicle(self):
        if not self.is_available:
            vehicle = self.vehicle
            self.vehicle = None
            self.is_available = True
            return vehicle
        else:
            raise Exception("Spot is already empty.")

class ParkingLot:
    def __init__(self, num_of_spots):
        self.parking_spots = [ParkingSpot(i) for i in range(num_of_spots)]

    def park_vehicle(self, vehicle):
        for spot in self.parking_spots:
            if spot.is_available:
                spot.park_vehicle(vehicle)
                return spot.spot_id
        raise Exception("No available spots.")

    def retrieve_vehicle(self, spot_id):
        if 0 <= spot_id < len(self.parking_spots):
            return self.parking_spots[spot_id].retrieve_vehicle()
        else:
            raise Exception("Invalid spot ID.")

    def display_status(self):
        status = []
        for spot in self.parking_spots:
            if spot.is_available:
                status.append(f"Spot {spot.spot_id}: Available")
            else:
                vehicle = spot.vehicle
                status.append(f"Spot {spot.spot_id}: Occupied by {vehicle.vehicle_type} with license plate {vehicle.license_plate}")
        return "\n".join(status)

# Example usage
if __name__ == "__main__":
    lot = ParkingLot(10)
    
    c1 = Car("123ABC", "Car", "Toyota", "Camry")
    b1 = Bike("456XYZ", "Bike", "Yamaha", "MT-07")
    
    sp1 = lot.park_vehicle(c1)
    sp2 = lot.park_vehicle(b1)
    
    print("Parking Lot Status:")
    print(lot.display_status())
    
    print("\nRetrieving vehicle from spot:", sp1)
    lot.retrieve_vehicle(sp1)
    
    print("\nParking Lot Status after retrieval:")
    print(lot.display_status())
