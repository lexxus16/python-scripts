import os
import subprocess

# Step 1: List down shared network computers
def list_shared_computers():
    shared_computers = []
    try:
        output = subprocess.check_output('net view', shell=True, universal_newlines=True)
        lines = output.split('\n')
        for line in lines:
            if "\\" in line:
                shared_computers.append(line.strip())
        return shared_computers
    except subprocess.CalledProcessError:
        return []

# Step 2: Check if a folder is accessible on a computer
def check_folder_access(computer_name, folder_path):
    try:
        command = f'net use \\\\{computer_name}\\IPC$ /u:""'
        subprocess.check_output(command, shell=True)
        folder_path = folder_path.replace('/', '\\')  # Ensure folder_path uses backslashes
        command = f'net use \\\\{computer_name}\\{folder_path}'
        subprocess.check_output(command, shell=True)
        return True
    except subprocess.CalledProcessError:
        return False

if __name__ == "__main__":
    # Step 1: List down shared network computers
    shared_computers = list_shared_computers()
    
    if not shared_computers:
        print("No shared network computers found.")
    else:
        print("Shared network computers:")
        for computer in shared_computers:
            print(computer)
            
        # Step 2: Check folder access
        computer_name = input("Enter a computer name from the list: ")
        folder_path = input("Enter the folder path to check access: ")
        
        if computer_name not in shared_computers:
            print("Computer name is not in the list of shared computers.")
        else:
            if check_folder_access(computer_name, folder_path):
                print(f"You have access to '{folder_path}' on '{computer_name}'.")
            else:
                print(f"You do not have access to '{folder_path}' on '{computer_name}'.")
