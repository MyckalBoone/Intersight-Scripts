#!! /usr/bin/env python

# URL format: "https://intersight.com/path[?query]| Example -> "https://intersight.com/api/v1/asset/DeviceRegistrations/"MOID"

from intersight.intersight_api_client import IntersightApiClient

from intersight.apis import equipment_device_summary_api

HOST = input('Enter the host: ') # Example -> "https://intersight.com/api/v1"
private_key = input('Enter the private key: ') # Example -> "/Path_to/SecretKey.txt"
api_key_id = input('Enter the api key id: ') 

# Create an Intersight API Client intstance
API_INSTANCE = IntersightApiClient( HOST, private_key, api_key_id)

# Create an equipment device handle
D_HANDLE = equipment_device_summary_api.EquipmentDeviceSummaryAPI(API_INSTANCE)

DEVICES = D_HANDLE.equipment_device_summaries_get().results

print ('{0:35s}{1:40s}{2:13s}{3:14s}'.format("DN", "MODEL", "SERIAL", "OBJECT TYPE"))
print ('-'*105)

# Loop through devices and extract data
for DEVICE in DEVICES:
    print('{0:35s}{1:40s}{2:13s}{3:14s}'.format( DEVICE.dn, DEVICE.model, DEVICE.serial, DEVICE.source_object_type))
