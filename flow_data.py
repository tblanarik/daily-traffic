class FlowStationLocation:
    """Represents a flow station location."""

    def __init__(self, description, direction, latitude, longitude, mile_post, road_name):
        self.description = description
        self.direction = direction
        self.latitude = latitude
        self.longitude = longitude
        self.mile_post = mile_post
        self.road_name = road_name

    @classmethod
    def from_json(cls, json_obj):
        """Create a FlowStationLocation object from a JSON object."""
        return cls(
            json_obj['Description'],
            json_obj['Direction'],
            json_obj['Latitude'],
            json_obj['Longitude'],
            json_obj['MilePost'],
            json_obj['RoadName']
        )


class FlowData:
    """Represents a traffic flow reading from WSDOT."""

    def __init__(self, flow_data_id, flow_reading_value, flow_station_location, region, station_name, time):
        self.flow_data_id = flow_data_id
        self.flow_reading_value = flow_reading_value
        self.flow_station_location = flow_station_location
        self.region = region
        self.station_name = station_name
        self.time = time

    @classmethod
    def from_json(cls, json_obj):
        """Create a FlowData object from a JSON object."""
        flow_station_location = FlowStationLocation.from_json(
            json_obj['FlowStationLocation'])
        return cls(
            json_obj['FlowDataID'],
            json_obj['FlowReadingValue'],
            flow_station_location,
            json_obj['Region'],
            json_obj['StationName'],
            json_obj['Time']
        )
