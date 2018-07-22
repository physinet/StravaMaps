from stravalib import Client
import matplotlib.pyplot as plt, numpy as np
import api

client = Client(access_token=api.access_token)

activities = list(client.get_activities()) # Get current athlete details

id = activities[0].id

types = ['time', 'altitude', 'latlng', 'moving', 'distance']

s = client.get_activity_streams(id, types=types)
distance = s['distance']
altitude = s['altitude']
latlng = s['latlng']
y, x = zip(*latlng.data)

fig, ax = plt.subplots(2)
ax[0].plot(distance.data, altitude.data, 'k')  # elevation profile
ax[1].plot(x, y, 'k')  # route overview
ax[1].set_aspect('equal')
plt.show()
