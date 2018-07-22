from api import get_activities
from activity import Activity

activities = get_activities()
a = Activity(activities[0])
a.plot()
