import argparse
import json
import requests
from twilio.rest import Client
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


def send_text_message(account_sid, auth_token, to_phone_number, from_phone_number, flow_data):
    """Send text message with traffic flow data using Twilio API"""
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body=f"{flow_data.flow_station_location.description}: {flow_data.flow_reading_value}",
        from_=from_phone_number,
        to=to_phone_number
    )
    print(message.sid)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Retrieve traffic flow data from WSDOT API and send text message using Twilio API')
    parser.add_argument('--access-code', type=str,
                        required=True, help='WSDOT API access code')
    parser.add_argument('--flow-data-id', type=int, required=True,
                        help='ID of traffic flow data to retrieve')
    parser.add_argument('--twilio-account-sid', type=str,
                        required=True, help='Twilio account SID')
    parser.add_argument('--twilio-auth-token', type=str,
                        required=True, help='Twilio auth token')
    parser.add_argument('--to-phone-number', type=str, required=True,
                        help='Phone number to send traffic flow data to')
    parser.add_argument('--from-phone-number', type=str,
                        required=True, help='Phone number to send from')
    args = parser.parse_args()

    flow_data = get_flow_data(args.access_code, args.flow_data_id)
    send_text_message(args.twilio_account_sid, args.twilio_auth_token,
                      args.to_phone_number, args.from_phone_number, flow_data)
