import requests
import json
import csv

all_states = ['Andaman_&_Nicobar_Islands','Andhra_Pradesh','Arunachal_Pradesh','Assam','Bihar','Chhattisgarh','Chandigarh','Daman_&_Diu','Delhi','Dadra_Nagar_&_Haveli','Goa','Gujarat','Himachal_Pradesh','Haryana','Jharkhand','Jammu_&_Kashmir','Karnataka','Kerala','Manipur','Madhya_Pradesh','Meghalaya','Maharashtra','Mizoram','Nagaland','Odisha','Punjab','Puducherry','Rajasthan','Sikkim','Tamil_Nadu','Tripura','Uttarakhand','Uttar_Pradesh','West_Bengal','Lakshadweep','Telangana','Mysore']

url = "https://lokdhaba.ashoka.edu.in/api/data/api/v1.0/DataDownload"
payload = {
	"ElectionType":"AE",
	"StateName":"DUMMY",
	"AssemblyNo":"all",
	"Filters":[]
}

for state in all_states:
	print('Processing: ', state)
	# Add state here
	payload["StateName"] = state
	headers = {
							"accept": "*/*",
							"accept-language": "en-US,en;q=0.9",
							"content-type": "application/json",
							"sec-ch-ua": "\"Google Chrome\";v=\"93\", \" Not;A Brand\";v=\"99\", \"Chromium\";v=\"93\"",
							"sec-ch-ua-mobile": "?0",
							"sec-ch-ua-platform": "\"macOS\"",
							"sec-fetch-dest": "empty",
							"sec-fetch-mode": "cors",
							"sec-fetch-site": "same-origin",
							"cookie": "_ga=GA1.3.1048836088.1632791623; _gid=GA1.3.911628931.1632791623"
							}


	print('Downloading data for:', state)
	r = requests.post(url, data=json.dumps(payload), headers=headers)

	json_data = json.loads(r.text)
	data_to_write = json_data["data"]

	print('Writing to CSV file for: ', state)
	output_file_name =  state + '.csv'

	with open(output_file_name, 'w+') as file:
		for row in data_to_write:
			for index, item in enumerate(row):
				row[index] = str(item)
				row[index] = row[index].replace(',', '')
			string = ','.join(row)
			file.write(string + '\n')
		
	print('Done producing CSV for:', state)