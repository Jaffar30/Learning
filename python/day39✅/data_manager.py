import requests
from requests.auth import HTTPBasicAuth

sheety_endpoit = "https://api.sheety.co/a915b0c78ee4d2aa068707542720d773/copyOfFlightDeals/prices"


class DataManager:

    def __init__(self):
        self._user = 
        self._password =
        self._authorization = HTTPBasicAuth(self._user, self._password)
        self.destination_data = {}

    def get_destination_data(self):
        # 2. Use the Sheety API to GET all the data in that sheet and print it out.
        response = requests.get(url=sheety_endpoit, auth=self._authorization)
        data = response.json()
        self.destination_data = data["prices"]
        # 3. Try importing pretty print and printing the data out again using pprint() to see it formatted.
        # pprint(data)
        return self.destination_data

    # 6. In the DataManager Class make a PUT request and use the row id from sheet_data
    # to update the Google Sheet with the IATA codes. (Do this using code).
    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{sheety_endpoit}/{city['id']}",
                json=new_data,
                auth=self._authorization
            )
            print(response.text)