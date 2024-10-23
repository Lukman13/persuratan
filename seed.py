import requests
import json

url = "http://127.0.0.1:8000/surat/api/surat/"

payload = json.dumps({
  "id": 1,
  "created_at": "2024-10-23T06:43:27Z",
  "prihal": "Undangan Rapat Bulanan",
  "status": "Menunggu",
  "jenis": 2,
  "kategori": 3,
  "user": 1
})
headers = {
  'Content-Type': 'application/json'
}



for i in range(100):
    response = requests.request("POST", url, headers=headers, data=payload)
    print(f'ini data ke {i}') 
    
