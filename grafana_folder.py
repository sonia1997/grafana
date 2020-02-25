import json
import os
import requests

HOST = 'https://sonia123.grafana.net'
API_KEY = 'eyJrIjoicTBuSnRBRXUyRnh3RVc1TTlabmZBWXdaaDUzVWlSSE4iLCJuIjoiZ2V0X2Rhc2hiYW9yZHMiLCJpZCI6MX0='
DIR = 'exported-dashboards/'

def main():
    headers = {'Authorization': 'Bearer %s' % (API_KEY,)}

    # Get all folders
    folders_response = requests.get('%s/api/folders' % (HOST,), headers=headers)
    folders_response.raise_for_status()
    folders = folders_response.json()

    for folder in folders:
        folder_id=folder["id"]
        print(folder_id)

        dashbaords_response = requests.get('https://sonia123.grafana.net/api/search?folderIds='+str(folder_id), headers=headers)
        dashboards=dashbaords_response.json()
        for dashboard in dashboards:
            dashboard_uid=dashboard["uid"]
            print(dashboard_uid)

            dashboard_details=requests.get('https://sonia123.grafana.net/api/dashboards/uid/'+str(dashboard_uid), headers=headers)
            dashboard_json = dashboard_details.json()['dashboard']
            print(dashboard_json)

if __name__ == '__main__':
    main()
