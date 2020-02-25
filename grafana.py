import json
import os
import requests

HOST = 'https://sonia123.grafana.net'
API_KEY = 'eyJrIjoicTBuSnRBRXUyRnh3RVc1TTlabmZBWXdaaDUzVWlSSE4iLCJuIjoiZ2V0X2Rhc2hiYW9yZHMiLCJpZCI6MX0='

DIR = 'exported-dashboards/'

def main():
    headers = {'Authorization': 'Bearer %s' % (API_KEY,)}
    response = requests.get('%s/api/dashboards/uid/6RD_NhwWk' % (HOST,), headers=headers)
    response.raise_for_status()
    dashboards = response.json()
    print(dashboards)
    print(dashboards["dashboard"])

    if not os.path.exists(DIR):
        os.makedirs(DIR)

    for d in dashboards:
        # print ("Saving: " + d['title'])
        response = requests.get('%s/api/dashboards/uid/6RD_NhwWk' % (HOST), headers=headers)
        data = response.json()['dashboard']
        dash = json.dumps(data, sort_keys=True, indent=4, separators=(',', ': '))
        name = data['title'].replace(' ', '_').replace('/', '_').replace(':', '').replace('[', '').replace(']', '')
        tmp = open(DIR + name + '.json', 'w')
        tmp.write(dash)
        tmp.write('\n')
        tmp.close()


if __name__ == '__main__':
    main()
