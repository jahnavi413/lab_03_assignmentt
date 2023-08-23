class Flight:
    def __init__(self, f_id, source, destination, price):
        self.f_id = f_id
        self.source = source
        self.destination = destination
        self.price = price

class FlightTable:
    def __init__(self):
        self.flights = []
    
    def add_flight(self, flight):
        self.flights.append(flight)
    
    def search_by_id(self, f_id):
        for flight in self.flights:
            if flight.f_id == f_id:
                return flight
        return None
    
    def search_by_source(self, source):
        result = []
        for flight in self.flights:
            if flight.source == source:
                result.append(flight)
        return result
    
    def search_by_destination(self, destination):
        result = []
        for flight in self.flights:
            if flight.destination == destination:
                result.append(flight)
        return result

def main():
    table = FlightTable()
    table.add_flight(Flight("AI161E90", "BLR", "BOM", 5600))
    table.add_flight(Flight("BR161F91", "BOM", "BBI", 6750))
    table.add_flight(Flight("AI161F99", "BBI", "BLR", 8210))
    table.add_flight(Flight("VS171E20", "JLR", "BBI", 5500))
    table.add_flight(Flight("AS171G30", "HYD", "JLR", 4400))
    table.add_flight(Flight("AI131F49", "HYD", "BOM", 3499))
    
    user_input = input("Enter 1) Flight ID, 2) Source city, or 3) Destination city: ")
    
    if user_input == "1":
        flight_id = input("Enter Flight ID: ")
        flight = table.search_by_id(flight_id)
        if flight:
            print(f"Flight ID: {flight.f_id}, From: {flight.source}, To: {flight.destination}, Price: {flight.price}")
        else:
            print("Flight not found.")
    elif user_input == "2":
        source = input("Enter Source city: ")
        flights = table.search_by_source(source)
        if flights:
            print("Flights from", source)
            for flight in flights:
                print(f"Flight ID: {flight.f_id}, To: {flight.destination}, Price: {flight.price}")
        else:
            print("No flights found from", source)
    elif user_input == "3":
        destination = input("Enter Destination city: ")
        flights = table.search_by_destination(destination)
        if flights:
            print("Flights to", destination)
            for flight in flights:
                print(f"Flight ID: {flight.f_id}, From: {flight.source}, Price: {flight.price}")
        else:
            print("No flights found to", destination)
    else:
        print("Invalid input. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
