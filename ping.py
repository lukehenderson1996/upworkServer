import requests
from time import sleep
import upwork


# # url = "https://www.upwork.com/api/profiles/v2/search/jobs.json"
# # POST /api/auth/v1/oauth/token/request
# url = "https://www.upwork.com/api/auth/v1/oauth/token/request"
#
# # response = requests.request("GET", url)
# response = requests.request("POST", url)
#
# print(response.text)


public_key = "6cc64b61b06a6d9446d17daec5aef053"
secret_key = "b923e71b020a22ab"
credentials = {}
#Instantiating a client without an auth token
client = upwork.Client(public_key, secret_key)
# client = upwork.Client(public_key, secret_key, **credentials)
# client.auth.get_authorize_url()
client.auth.get_request_token()



# sleep(10000)



# #example code
#
# client.provider_v2.search_jobs(
#     data={PARAMS_DICT}, page_offset=0, page_size=20)
#
# #EXAMPLE REQUEST:
# import upwork
# client = upwork.Client(public_key, secret_key, **credentials)
# data = {'q': 'python', 'title': 'Web developer'}
# client.provider_v2.search_jobs(data=data)
