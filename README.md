# daily-traffic

[![Check Traffic](https://github.com/tblanarik/daily-traffic/actions/workflows/get-traffic.yml/badge.svg)](https://github.com/tblanarik/daily-traffic/actions/workflows/get-traffic.yml) [![CodeQL](https://github.com/tblanarik/daily-traffic/actions/workflows/github-code-scanning/codeql/badge.svg)](https://github.com/tblanarik/daily-traffic/actions/workflows/github-code-scanning/codeql)

daily-traffic is a Python program that retrieves traffic flow data from the Washington State Department of Transportation (WSDOT) API and sends a text message to the configured phone number if traffic is slow (`FlowReadingValue > 1`).

### Usage
To run daily-traffic, use the following command:

```python
usage: main.py [-h] --access-code ACCESS_CODE --flow-data-id FLOW_DATA_ID --twilio-account-sid TWILIO_ACCOUNT_SID --twilio-auth-token
               TWILIO_AUTH_TOKEN --to-phone-number TO_PHONE_NUMBER --from-phone-number FROM_PHONE_NUMBER
```

where `<access_code>` is your WSDOT API access code and `<flow_data_id>` is the ID of the traffic flow data to retrieve.

You can obtain an access code here: https://wsdot.wa.gov/traffic/api/

See the usage for the [TrafficFlow API here](https://wsdot.wa.gov/traffic/api/TrafficFlow/TrafficFlowREST.svc/Help).

To find the list of available `flow_data_id` numbers:

```bash
curl --location --request GET 'http://wsdot.wa.gov/Traffic/api/TrafficFlow/TrafficFlowREST.svc/GetTrafficFlowsAsJson?AccessCode={ACCESS CODE}'
```

which returns a list of objects:
```
    {
        "FlowDataID": 2532,
        "FlowReadingValue": 1,
        "FlowStationLocation": {
            "Description": "14th",
            "Direction": "NB",
            "Latitude": 47.032581343,
            "Longitude": -122.891744891,
            "MilePost": 105.38,
            "RoadName": "005"
        },
        "Region": "Olympic",
        "StationName": "005es10538",
        "Time": "/Date(1681453282000-0700)/"
    }
```

#### License
daily-traffic is licensed under the MIT License. See LICENSE for more information.

#### Note 
95% of this application was written with [Copilot X](https://github.com/features/preview/copilot-x)