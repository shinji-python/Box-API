import requests

url = "https://upload.box.com/api/2.0/files/content"

payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"file\"; filename=\"Shinji Homawoo Resume_updated_10_2 copy\"\r\nContent-Type: application/vnd.openxmlformats-officedocument.wordprocessingml.document\r\n\r\n\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"name\"\r\n\r\nResume.pdf\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"parent.id\"\r\n\r\n93036385137\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"
headers = {
    'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
    'Content-Type': "application/json",
    'Authorization': "Bearer Ccx0R2D5iYtkFJbVNV34gyrJ6Qf3medd"
}

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)
