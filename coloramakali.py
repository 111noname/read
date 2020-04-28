from colorama import init, Fore, Back, Style
init()
init(autoreset=True)
print(Back.GREEN + "colorama console")
while True:
	init()
	init(autoreset=True)
	root = input(Fore.RED + "colorama@kali# ")
	if root == "":
		pass

	elif root == " ":
		print("tab error")

	elif root == "help":
		print("enter text")

	elif root == root:
		print(Fore.RED + root, Fore.GREEN + root, Fore.WHITE + root, Fore.YELLOW + root, Back.RED + root, Back.GREEN + root, Back.WHITE + root, Back.YELLOW + root)

	elif root == "clear":
		pass

	else:
		print(Fore.RED + "error")
