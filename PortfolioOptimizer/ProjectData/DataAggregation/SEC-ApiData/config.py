'''
SEC Edgar - API Credentials

API Type: DataFi Hackpack
Created On: 2019-07-04
Expiration: 2019-18-04
Status: Active

Credentials:
Registered Email: Tamashiroryan@gmail.com
Account Password: Standard Login -- Main
Application: UCI-DataAnalytics-Final
Key: eb5c9d9f7df6f14e3b523b587c793304
Datafi: HackPack

Limitations:
    - 2 API Calls/Second
    - Maximum 5000 Calls/Day

Documentation Resources:
[ Main | URL ] https://developer.edgar-online.com/docs

** API URI Example:
[ Syntax ] {Protocol}://datafied.api.edgar-online.com/{Version}/{Endpoints}{Format}?{Parameters}appkey={API Key}

    Protocol: [ HTTP | HTTPS ]
    Version: [ v1 | v2 ]
    Endpoints: [ corefinancials | insiders |]
    Format:  [ JSON | XML ]
    API Key: eb5c9d9f7df6f14e3b523b587c793304

Error Codes:
    400 - Bad Request
    403 - Forbidden (Failed Authentication)
    503 - Service Unavailable
    596 - Service Not Found (Resource Not Found)
'''
sec_api_login = "RTamashiro88"
sec_api_key = "eb5c9d9f7df6f14e3b523b587c793304"

sec_api_credentials = {
    "email": "Tamashiroryan@gmail.com",
    "login": "RTamashiro88",
    "key": "eb5c9d9f7df6f14e3b523b587c793304",
    "DataFi": "HackPack"
}
