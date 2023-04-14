# daily-traffic

daily-traffic is a Python program that retrieves traffic flow data from the Washington State Department of Transportation (WSDOT) API. The program is designed to be run daily to collect the latest traffic flow data.

### Usage
To run daily-traffic, use the following command:

```python
usage: main.py [-h] --access-code ACCESS_CODE --flow-data-id FLOW_DATA_ID --twilio-account-sid TWILIO_ACCOUNT_SID --twilio-auth-token
               TWILIO_AUTH_TOKEN --to-phone-number TO_PHONE_NUMBER --from-phone-number FROM_PHONE_NUMBER
```

where <access_code> is your WSDOT API access code and <flow_data_id> is the ID of the traffic flow data to retrieve.

You can obtain an access code here: https://wsdot.wa.gov/traffic/api/


License
daily-traffic is licensed under the MIT License. See LICENSE for more information.