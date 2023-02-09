from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS


# класс API для работы с бд
class DataBaseAPI:
    def __init__(self,bucket,url,token,organization):
        """
        :param bucket: Название нашей БД
        :param url: Адрес для подключения к БД
        :param token: Токен, генерируется в UI InfluxDB
        :param organization: Созданная организация в UI InfluxDB

        Метод подключения к клиенту
        """
        self.bucket = bucket

        self.client = InfluxDBClient(url=url,token=token,organization=organization)

    #добавление
    def addData(self,sensorData):
        write_api = self.client.write_api(write_options=SYNCHRONOUS)
        query_api = self.client.query_api()

        p = [Point("my_measurement").tag("location", "Prague").field("val", 25.3)]

        write_api.write(bucket=self.bucket, record=p)

    #чтение

