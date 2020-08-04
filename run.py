import os
import json
import time
import shutil

def printDirectory(dir):
	print("\n")
	print("--- Printing 'Downloads' Directory! ---")
	print("\n")
	for file in os.listdir(dir):
		print(file)
	print("\n")
	print("--- Finished! ---")
	print("\n")

def moveDirectory(dir):
	print("\n")
	print("--- Moving Files! ---")
	print("\n")
	new_folder = "/mnt/c/Users/Noahj/Documents/College/CSCI1933TA/Misc/Download_Route"
	i = 1
	for file in os.listdir(dir):
		filename, file_extension = os.path.splitext(file)
		new_name = filename + "_" + str(i) + file_extension
		print("NEWNAME: " + new_name)
		file_exists = os.path.isfile(new_folder + "/" + new_name)
		while(file_exists):
			i += 1
			print(i)
			new_name = filename + "_" + str(i) + file_extension
			file_exists = os.path.isfile(new_folder + "/" + new_name)
		print("--- OLD FILENAME: " + file + " | New FILENAME: " + new_name + " ---\n")
		shutil.move(dir + "/" + file, new_folder + "/" + new_name)
	print("\n")
	print("--- Finished! ---")
	print("\n")

def main():
	file='/mnt/c/Users/Noahj/Downloads'
	print("--- Welcome to Downloads folder cleanup --- \n")
	while True:
		cmd=input("Please enter a command: 'print', 'move', or 'exit' \n")
		if(cmd == "Print" or cmd == "print"):
			try:
				printDirectory(file)
			except FileNotFoundError:
				print("File Not Found")
		elif(cmd == "Move" or cmd == "move"):
			try:
				moveDirectory(file)
			except FileNotFoundError:
				print("File Not Found: " + file)
		elif(cmd == "Exit" or cmd == "exit"):
			print("\n")
			print("--- Ending Program ---")
			print("\n")
			break
		else:
			print("\n")
			print("--- Invalid Input! ---")
			print("\n")


if __name__ == '__main__':
	main()
