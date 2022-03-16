# import requests

# requests_client = requests.Session()
# requests_client.get("http://localhost:8000/users/signIn/")
# r = requests_client.post(
#     "http://localhost:8000/users/signIn/",
#     data={
#         "username": "mehdi",
#         "pass": "1",
#         "csrfmiddlewaretoken": requests_client.cookies["csrftoken"],
#     },
# )
# rr = requests_client.get(
#     "http://localhost:8000/todos/f42a2acd-f810-4efb-89eb-f78b260688e1.json",
# )
# print(rr.json())

