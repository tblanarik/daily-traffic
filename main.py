import argparse
from message_manager import MessageManager
from wsdot_trafficflow import WSDOTTrafficFlow

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Retrieve traffic flow data from WSDOT API and send message to http endpoint')
    parser.add_argument('--access-code', type=str,
                        required=True, help='WSDOT API access code')
    parser.add_argument('--flow-data-id', type=int, required=True,
                        help='ID of traffic flow data to retrieve')
    parser.add_argument('--recipients', type=str, required=True,
                        help='Email recipients separated by commas')
    parser.add_argument('--post-url', type=str, required=True,
                        help='URL to send message to')
    args = parser.parse_args()

    traffic_flow = WSDOTTrafficFlow(args.access_code, args.flow_data_id)
    message_manager = MessageManager(args.post_url)

    flow_data = traffic_flow.flow_data()
    if flow_data.flow_reading_value > 1:
        message_manager.send_message(
            f"{flow_data.flow_station_location.description} Slow Traffic = ({flow_data.flow_reading_value})!",
            args.recipients)
    else:
        print("No slow traffic: ", flow_data.flow_station_location.description)
