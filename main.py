from urllib.request import urlopen
import json

url = 'https://usher2.club/d1_uniq_ip4.json'
response = urlopen(url)

string = response.read().decode('utf-8')
json_obj = json.loads(string)
tmp = ""
bit_count = 0;
print("==BEGIN==")
for obj in json_obj:

	if obj['x'] > 1525797543:
		sign = ''
		if obj['y'] > 48000 and obj['y'] < 53000:
			sign = '0'
			bit_count = bit_count + 1
		if obj['y'] > 53000:
			sign = '1'
			bit_count = bit_count + 1
		tmp = tmp + sign
		
		if bit_count == 8:
			print (tmp)
			print(chr(int(tmp, 2)))
			tmp = ''
			bit_count = 0
if len(tmp) != 0:
	print(tmp)
	prognoz = tmp
	while(len(tmp) < 8):
		prognoz = prognoz + '1'
		tmp = tmp + '0'
	prognoz_i = int(prognoz, 2)
	tmp_i = int(tmp, 2)
	prognoz_str = ''
	while(tmp_i <= prognoz_i):
		prognoz_str = prognoz_str + '|' + chr(tmp_i)
		tmp_i = tmp_i + 1
	print(prognoz_str)
			
print("===END===")
