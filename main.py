import argparse
from sms_manager import SMSManager
from wsdot_trafficflow import WSDOTTrafficFlow

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

    traffic_flow = WSDOTTrafficFlow(args.access_code, args.flow_data_id)
    sms = SMSManager(args.twilio_account_sid,
                     args.twilio_auth_token, args.to_phone_number, args.from_phone_number)

    flow_data = traffic_flow.flow_data()
    if flow_data.flow_reading_value > 1:
        sms.send_text_message(
            f"{flow_data.flow_station_location.description} Slow Traffic")
    else:
        print("No slow traffic: ", flow_data.flow_station_location.description)
