import polyline, numpy as np, matplotlib.pyplot as plt

class Activity(object):
    def __init__(self, json):
        '''
        Params:
        json: JSON dictionary returned by Strava API containing
        activity details
        '''
        self.__dict__.update(json)


    def plot(self):
        fig, ax = plt.subplots()
        ax.plot(*self.polyline(), 'k')
        ax.set_aspect('equal')
        plt.show()

    def polyline(self):
        '''
        Return numpy arrays of GPS coordinates for the activity.
        longitude, latitude
        '''
        pl = polyline.decode(self.map['summary_polyline'])  # list of tuples
        y, x = zip(*pl)  # two tuples
        return np.array(x), np.array(y)  # numpy
