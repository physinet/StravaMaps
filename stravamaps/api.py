import requests

with open('access_token', 'r') as f:
    access_token = f.read().rstrip()

with open('secret', 'r') as f:
    secret = f.read().rstrip()

print(access_token, secret)

headers = {'Authorization' : 'Bearer %s' % access_token}

api_base_url = 'https://www.strava.com/api/v3/'
api_activities = api_base_url+'activities/'

def get_activities(per_page=30):
    assert per_page <= 200  # API max
    page = 1
    activities = []

    while True:
        params = {'page': page, 'per_page': per_page}
        r = requests.get(api_activities, headers=headers, params=params)
        activities += r.json()
        page += 1
        if len(r.json()) == 0:
            break

    return activities
