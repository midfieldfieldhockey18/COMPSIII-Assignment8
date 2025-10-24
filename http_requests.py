import requests

class JSONPlaceholder:
    def __init__(self, base_url):
        self.base_url = base_url

    def get_request(self):
        response = requests.get(self.base_url)
        return {
            "status_code": response.status_code,
            "headers": dict(response.headers),
            "content": response.text[:500]
        }

    def post_request(self, data):
        response = requests.post(self.base_url, json=data)
        return {
            "status_code": response.status_code,
            "headers": dict(response.headers),
            "content": response.text[:500]
        }

    def update_user(self, userId, title, body):
        data = {
            "title": title,
            "body": body
        }
        url = f"{self.base_url}/{userId}"
        response = requests.put(url, json=data)
        return {
            "status_code": response.status_code,
            "headers": dict(response.headers),
            "content": response.text[:500]
        }

    def delete_user(self, userId):
        url = f"{self.base_url}/{userId}"
        response = requests.delete(url)
        return {
            "status_code": response.status_code
        }
