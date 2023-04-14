import json
import requests
from flow_data import FlowData

TRAFFIC_FLOW_URL = ("http://wsdot.wa.gov/Traffic/api/TrafficFlow/"
                    "TrafficFlowREST.svc/GetTrafficFlowAsJson")


class WSDOTTrafficFlow:
    """Represents a WSDOT traffic flow."""

    def __init__(self, access_code, flow_data_id):
        self.access_code = access_code
        self.flow_data_id = flow_data_id

    def flow_data(self):
        """Get traffic flow data from WSDOT API"""
        url = f"{TRAFFIC_FLOW_URL}?AccessCode={self.access_code}&FlowDataID={self.flow_data_id}"
        response = requests.get(url, timeout=10)
        data = json.loads(response.text)
        flow_data = FlowData.from_json(data)
        return flow_data
