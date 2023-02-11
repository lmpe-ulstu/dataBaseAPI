from weather.stations.davis import VantagePro
from pprint import pprint


class DataScrapper:

    def getData(self):
        device = VantagePro('COM3', 0)
        device.parse()
        data = device.fields

        return data['HumOut']
