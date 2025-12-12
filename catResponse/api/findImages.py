import requests

url = "https://http.cat/"

def get_target_response(code: int):
    try:
        response = requests.get(f'{url}/{code}')
        return response.json()
    except response.status_code == 500:
        print("Error: Server error accured, was not able to fetch image. A placeholder was returned to stop your api from crashing!")
        return {"Code": f"{code}"} 
    except response.status_code == 404:
        print("Error: Cat image was not found. A placeholder was returned to stop your api from crashing!")
        return {"Code": f"{code}"} 