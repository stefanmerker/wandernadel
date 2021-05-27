import requests


body = {"coordinates":[[8.681495,49.41461],[8.686507,49.41943],[8.687872,49.420318]],"elevation":"true","language":"de-de"}

headers = {
    'Accept': 'application/json, application/geo+json, application/gpx+xml, img/png; charset=utf-8',
    'Authorization': '5b3ce3597851110001cf6248902e12deed49439881d71b62e8948798',
    'Content-Type': 'application/json; charset=utf-8'
}
call = requests.post('https://api.openrouteservice.org/v2/directions/foot-hiking/geojson', json=body, headers=headers)

if call.status_code == 200:
    print("request success")
    result_file = open("result.geojson", "a")
    result_file.writelines(call.text)
else:
    output = "request failed ({})"
    print(output.format(call.status_code))
    print(call.reason)







#print(call.status_code, call.reason)
#print(call.text)