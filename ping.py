import requests

url = "https://www.upwork.com/api/profiles/v2/search/jobs.json"

response = requests.request("GET", url)

print(response.text)



sleep(10000)



#example code

client.provider_v2.search_jobs(
    data={PARAMS_DICT}, page_offset=0, page_size=20)

#EXAMPLE REQUEST:
import upwork
client = upwork.Client(public_key, secret_key, **credentials)
data = {'q': 'python', 'title': 'Web developer'}
client.provider_v2.search_jobs(data=data)
