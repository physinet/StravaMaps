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


# Elevation heatmap
fig, ax = plt.subplots()

points = np.array([x, y]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)

lc = LineCollection(segments, cmap=plt.get_cmap('hot'),
    norm=plt.Normalize(z.min(), z.max()))
lc.set_array(z)
lc.set_linewidth(3)

ax.add_collection(lc)
ax.autoscale_view()
ax.set_aspect('equal')
plt.show()
