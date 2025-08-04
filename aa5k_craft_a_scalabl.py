import random
import time
from threading import Thread
from collections import deque

class IoTDevice:
    def __init__(self, device_id, device_type):
        self.device_id = device_id
        self.device_type = device_type
        self.sensor_data = deque(maxlen=100)  # store last 100 readings

    def readSensor(self):
        # simulate reading sensor data
        return random.uniform(0, 100)

    def send_data(self):
        while True:
            data = self.readSensor()
            self.sensor_data.append(data)
            print(f"Device {self.device_id} ({self.device_type}): {data}")
            time.sleep(5)  # send data every 5 seconds

class IoTDeviceSimulator:
    def __init__(self, num_devices):
        self.devices = [IoTDevice(f"Device {i}", "Sensor") for i in range(1, num_devices + 1)]
        self.threads = []

    def run_simulation(self):
        for device in self.devices:
            thread = Thread(target=device.send_data)
            thread.start()
            self.threads.append(thread)

    def stop_simulation(self):
        for thread in self.threads:
            thread.join()

if __name__ == "__main__":
    simulator = IoTDeviceSimulator(10)  # create 10 devices
    simulator.run_simulation()