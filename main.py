from funcs import *


class Flight:
    def __init__(self, origin, destination, depdate, retdate, carrier, price):
        self.origin = origin
        self.destination = destination
        self.depdate = depdate
        self.retdate = retdate
        self.carrier = carrier
        self.price = '{:,}'.format(float(price))
        # price in EUR


###
# flight data
PAX = 2
DEP = 'FRA'
DEP_DATE = '2024-12-28'
ARR = 'JFK'
RET_DATE = '2025-01-07'
CLASS = 'ECONOMY'
###

rawdata = get_flight_data(origin=DEP,
                          destination=ARR,
                          depdate=DEP_DATE,
                          returndate=RET_DATE,
                          pax=PAX,
                          bookclass=CLASS)

try:
    offers = rawdata['data']
    flights = True
except KeyError:
    offers = []
    flights = False

if flights:

    flightlist = []

    for i in offers:
        flightlist.append(Flight(
            origin=i['itineraries'][0]['segments'][0]['departure']['iataCode'],
            destination=i['itineraries'][1]['segments'][0]['departure']['iataCode'],
            depdate=i['itineraries'][0]['segments'][0]['departure']['at'],
            retdate=i['itineraries'][1]['segments'][0]['departure']['at'],
            carrier=i['itineraries'][0]['segments'][0]['operating']['carrierCode'],
            price=i['price']['total']))

    # print(flightlist[0].carrier)

    for f in flightlist:
        output = (f"*********\n"
                  f"Flug {f.origin} -> {f.destination} von\n{f.depdate} bis {f.retdate}\nmit {f.carrier} "
                  f"kostet derzeit EUR {f.price} für {PAX} Personen."
                  f"\n"
                  f"*********")

        print(output)

        send_telegram(output)
else:
    print(f"Noch Keine Flüge für {DEP}->{ARR} gefunden")
