import json
import os
import requests

API_KEY = 'eyJrIjoiV2RiaXlacmRpOUw5bkJNTHREanY1VjFUQ2w2bnozR1ciLCJuIjoiZ19hcGlfa2V5IiwiaWQiOjF9'
import_url='http://localhost:3000/api/dashboards/import'
headers_import={"Content-Type": 'application/json', "Authorization": "Bearer "+API_KEY}

def getData():
    headers = {'Authorization': 'Bearer %s' % (API_KEY,)}

    # Get all folders.
    folders_response = requests.get('http://localhost:3000/api/folders', headers=headers)
    folders_response.raise_for_status()
    folders = folders_response.json()
    print(folders)

    for folder in folders:
        folder_id=folder["id"]
        print("Folder_id: {}, title: {}".format(folder["id"], folder["title"]))

        #Get all dashboards belong to each folder.
        dashboards_response = requests.get('http://localhost:3000/api/search?folderIds='+str(folder_id), headers=headers)
        dashboards=dashboards_response.json()
        for dashboard in dashboards:
            dashboard_uid=dashboard["uid"]
            dashboard_title=dashboard["title"]
            print("Dashboard_id: {}, title: {}".format(dashboard_uid, dashboard_title))
            print("/n")

            #Get json rep. of all the dashbaords belong to each folder.
            dashboard_details=requests.get('http://localhost:3000/api/dashboards/uid/'+str(dashboard_uid), headers=headers)
            dashboard_json = dashboard_details.json()

            import_response = requests.post(import_url, data=json.dumps(dashboard_json),headers=headers_import)
            r=import_response.json()
            print(r)


            # dashboard_json=json.dumps(dashboard_json)
            # y=dashboard_json["dashboard"]
            # # print(y["panels"][0]["datasource"])
            # print(y["panels"][0]["targets"][0])
            # print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
            # print("/n")

if __name__ == '__main__':
    getData()
