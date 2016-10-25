import requests

url = "http://123.56.46.244:5011/article"

data = "{\"text\":[[{\"w\":\"His\",\"e\":3,\"b\":0}, {\"w\":\"name\",\"e\":8,\"b\":4}, {\"w\":\"is\",\"e\":11,\"b\":9}, {\"w\":\"the\",\"e\":18,\"b\":12}, {\"w\":\"apple\",\"e\":1,\"b\":12}, {\"w\":\"States\",\"e\":25,\"b\":19}, {\"w\":\".\",\"e\":26,\"b\":25}]]\n}"
headers = {
    'cache-control': "no-cache",
    'content-type': "application/json"
    }

response = requests.request("POST", url, data=data, headers=headers)

print(response.text)
