import requests,os,time,instaloader



BRed="\033[1;31m" # Red
BGreen="\033[1;32m" # Green
BYellow="\033[1;33m" # Yellow
BCyan="\033[1;36m" # Cyan
BPurple="\033[1;35m" # Purple

print(f"{BYellow}========================================\n {BPurple}-ππ·π΄ ππΎπΎπ» ππ°π π³π΄ππ΄π»πΎπΏπ΄π π±π: {BCyan}ALHAZIN ALMALAKIβ\n {BPurple}-π³π΄ππ΄π»πΎπΏπ΄π: {BCyan}@GGGGQU\n {BPurple}-π³π΄ππ΄π»πΎπΏπ΄π π²π·π°π½π½π΄π»: {BCyan}@GGGGQ3\n{BYellow}========================================\n")


user = input(f'{BGreen}- π΄π½ππ΄π πππ΄ππ½πΈπΌπ΄ > ')
aut =input(f"{BGreen}- π΄π½ππ΄π ππΎπΊπ΄π½ > ")
os.system('clear')


L = instaloader.Instaloader()
profile = str(instaloader.Profile.from_username(L.context,user))
idd=str(profile.split(')>')[0])
target=idd.split(' (')[1]

print(f"{BYellow}========================================\n {BPurple}-ππ·π΄ ππΎπΎπ» ππ°π π³π΄ππ΄π»πΎπΏπ΄π π±π: {BCyan}ALHAZIN ALMALAKIβ\n {BPurple}-π³π΄ππ΄π»πΎπΏπ΄π: {BCyan}@GGGGQU\n {BPurple}-π³π΄ππ΄π»πΎπΏπ΄π π²π·π°π½π½π΄π»: {BCyan}@GGGGQ3\n{BYellow}========================================\n")

def test():
	while True:
	
		url1 = f"https://speedfollow.herokuapp.com/"
		api= requests.get(url1).text
		dap = api
		

		script = dap.split('{"message":"success","user":{"follow_coin":')[1]
		
		s = (script.split('"}<hr class=')[0])
		
		try:
			nmb = int(s[0]+s[1]+s[2]+s[3])
		except ValueError:
			try:
				nmb = int(s[0]+s[1]+s[2])
			except ValueError:
				try:
					nmb = int(s[0]+s[1])
				except ValueError:
					try:
						nmb = int(s[0])
					except:
						pass
				
					
		if "success" in dap:
			print(f"\n     {BGreen}done sent 1 follow coin to ==> {BYellow}{user}\n     {BGreen}Your Follow Coin Now Is ==> {BYellow}{nmb}")
		else:
			print(f"\n     {BRed}error send follow coin to ==> {BYellow}{user}")
			
while True:
	try: test()
	except IndexError: pass
