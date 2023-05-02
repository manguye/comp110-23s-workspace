"""Reinforcing Class education."""


class PlaneTicket:
    """Defining the class."""

    departure_city: str
    arrival_city: str
    departure_time: int
    ticket_cost: float

    def __init__(self, city_a: str, city_b: str, depart: int, cost: float):
        """Makes a new ticket object."""
        self.departure_city = city_a
        self.arrival_city = city_b
        self.departure_time = depart
        self.ticket_cost = cost

    def __str__(self) -> str:
        """See a prettier ticket."""
        pretty_ticket: str = f"Depart from {self.departure_city} at {self.departure_time}. "
        pretty_ticket += f"Arrive at {self.arrival_city}. It costs ${round(self.ticket_cost, 2)}."
        return pretty_ticket

    def delay(self, delay_hours: int) -> None:
        """Add hours to departure time in military time."""
        self.departure_time += (delay_hours * 100)
        self.departure_time %= 2400

    def discount(self, discount: float) -> None:
        """Subtract discounts."""
        self.ticket_cost *= (1 - discount)


def compare_prices(ticket1: PlaneTicket, ticket2: PlaneTicket) -> PlaneTicket:
    if ticket1.ticket_cost < ticket2.ticket_cost:
        return ticket1
    else:
        return ticket2
    

nc_la_ticket: PlaneTicket = PlaneTicket("Raleigh", "New Orleans", 1000, 85.25)

print(nc_la_ticket)

nc_la_ticket.delay(2)
nc_la_ticket.discount(0.10)

fl_ca_ticket: PlaneTicket = PlaneTicket("Orlando", "San Francisco", 1100, 100.50)

print(compare_prices(nc_la_ticket, fl_ca_ticket))