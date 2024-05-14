import requests

image_path = "/Users/boshang/Desktop/joint/S1074750.png/straight_cracks/crack_45.png"

with open(image_path, "rb") as f:
    files = {"image": f}
    response = requests.post("http://localhost:5000/classify", files=files)

result = response.json()
print(result)  # {'class': '...', 'confidence': ...}
