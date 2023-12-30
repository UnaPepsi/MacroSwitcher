import keyboard, win32api, time, pyautogui, pyfiglet

print(pyfiglet.figlet_format("MacroSwitcher :v"))

if input("Do you have any custom settings.txt? y/n: ") == "y":
	with open("settings.txt","r") as file:
		for line in file:
			exec(line.replace("\n",""))
else:
	hotkeys = []
	file = open("settings.txt","w")
	print("Press your hotkeys for 1-4 hotbar slots")
	while len(hotkeys) < 4:
		key = keyboard.read_key()
		if key not in hotkeys:
			hotkeys.append(keyboard.read_key())
	file.write(f"hotkeys = {hotkeys}\n")
	hotbar = []

	print("Click your 1-4 hotbar slots")
	while len(hotbar) < 4:
		pos = (pyautogui.position().x,pyautogui.position().y)
		if win32api.GetKeyState(0x01) < 0 and pos not in hotbar:	
			hotbar.append(pos)
			time.sleep(0.3)
	file.write(f"hotbar = {hotbar}\n")


	armor = []

	print("Click your armor slots")
	while len(armor) < 4:
		pos = (pyautogui.position().x,pyautogui.position().y)
		if win32api.GetKeyState(0x01) < 0 and pos not in armor:	
			armor.append(pos)
			time.sleep(0.3)
	file.write(f"armor = {armor}\n")
	second_armor = []
	print("Click your secondary slots")
	while len(second_armor) < 4:
		pos = (pyautogui.position().x,pyautogui.position().y)
		if win32api.GetKeyState(0x01) < 0 and pos not in second_armor:	
			second_armor.append(pos)
			time.sleep(0.3)
	file.write(f"second_armor = {second_armor}\n")

	try:
		delay = float(input("Delay in miliseconds (too little delay may cause glitches): "))/1000
	except ValueError:
		print("Invalid input, using default delay")
		delay = 1
	file.write(f"delay = {delay}\n")

	time.sleep(0.3)
	print("Macro hotkey?")
	toggle_key = keyboard.read_key()
	file.write(f"toggle_key = '{toggle_key}'\n")
	file.close()
	print("Settings saved to settings.txt")

print("Running")
def on_key_event(key):
	try:
		if key.event_type == keyboard.KEY_DOWN and key.name == toggle_key:
			keyboard.send("e")
			time.sleep(0.3)
			for i in range(4):
				pyautogui.moveTo(second_armor[i][0],second_armor[i][1])
				keyboard.send(hotkeys[i])
				time.sleep(delay/12)
			for i in range(4):
				pyautogui.moveTo(armor[i][0],armor[i][1])
				keyboard.send(hotkeys[i])
				time.sleep(delay/12)
			for i in range(4):
				pyautogui.moveTo(second_armor[i][0],second_armor[i][1])
				keyboard.send(hotkeys[i])
				time.sleep(delay/12)
			keyboard.send("e")
	except Exception:
		print("Could not run properly, perhaps corrupt/incorrectly made settings.txt")
keyboard.hook(on_key_event)
keyboard.wait()
# print(hotkeys)