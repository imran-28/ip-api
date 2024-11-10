import requests
"""
api_url = ip api url
get_api = access url from requests module
get_json = get data from url
get_ip = get ip
"""
api_url = 'https://api.ipify.org?format=json'
get_api = requests.get(api_url)
get_json = get_api.json()
get_ip = get_json.get('ip')

if get_api.status_code == 200:
    get_geo_url = f'https://api.iplocation.net/?ip={get_ip}'
    get_geo_api = requests.get(get_geo_url)
    get_geo_json = get_geo_api.json()
    geo_country = get_geo_json.get('country_name')
    isp = get_geo_json.get('isp')
    full = f'Your IP address is : {get_ip}, Country name : {geo_country}, isp : {isp} '
    print(full)