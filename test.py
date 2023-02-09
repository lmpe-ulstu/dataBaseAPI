from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS

bucket = "wind"

client = InfluxDBClient(url="http://localhost:8086",
                        token="IkRV5NlnRp_fTHR5x4mgMzi_coQ31ILQBaQUf5wZfXIJ9iwCZBH9qiHnSREgdu_bdsmAjUisUTmqoMvpXDXUOA==",
                        org="nikitaOrganization")

write_api = client.write_api(write_options=SYNCHRONOUS)
query_api = client.query_api()

p = Point("my_measurement").tag("location", "Prague").field("val", 25.3)

write_api.write(bucket=bucket, record=p)

tables = query_api.query('from(bucket:"wind") |> range(start: -1h)')

for table in tables:
    print(table)
    for row in table.records:
        print (row.values)