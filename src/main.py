import json
import requests
from flow_data import FlowData

TRAFFIC_FLOW_URL = ("http://wsdot.wa.gov/Traffic/api/TrafficFlow/"
                    "TrafficFlowREST.svc/GetTrafficFlowAsJson")


def get_flow_data(access_code, flow_data_id):
    """Get traffic flow data from WSDOT API"""
    url = f"{TRAFFIC_FLOW_URL}?AccessCode={access_code}&FlowDataID={flow_data_id}"
    response = requests.get(url, timeout=10)
    data = json.loads(response.text)
    flow_data = FlowData.from_json(data)
    return flow_data


if __name__ == "__main__":
    print("Hello World")