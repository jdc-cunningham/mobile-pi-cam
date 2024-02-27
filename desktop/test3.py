import bluetooth
def find_bt_address_by_target_name(name):
    # sometimes bluetooth.discover_devices() failed to find all the devices
    MAX_COUNT = 3
    count = 0
    while True:
        nearby_devices = bluetooth.discover_devices()

        for btaddr in nearby_devices:
            if name == bluetooth.lookup_name( btaddr ):
                return btaddr

        count += 1
        if count > MAX_COUNT:
            return None
        print("Try one more time to find target device..")           