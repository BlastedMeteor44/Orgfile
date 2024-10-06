import os
import shutil
import subprocess
import colorama



def banner():
    print(colorama.Fore.BLUE + r"""
________  ________  ________  ________ ___  ___       _______      
|\   __  \|\   __  \|\   ____\|\  _____\\  \|\  \     |\  ___ \     
\ \  \|\  \ \  \|\  \ \  \___|\ \  \__/\ \  \ \  \    \ \   __/|    
 \ \  \\\  \ \   _  _\ \  \  __\ \   __\\ \  \ \  \    \ \  \_|/__  
  \ \  \\\  \ \  \\  \\ \  \|\  \ \  \_| \ \  \ \  \____\ \  \_|\ \ 
   \ \_______\ \__\\ _\\ \_______\ \__\   \ \__\ \_______\ \_______|
    
    Made by BlastedMeteor44
    ╔Youtube: https://www.youtube.com/@BlastedMeteor44
    ║Discord: https://discord.gg/zGtynHphsX
    ╚Github: https://github.com/BlastedMeteor44

""" + colorama.Style.RESET_ALL)
def main():
    
    if os.name == "nt":
        os.system("cls")
        banner()
    else:
        os.system("clear")
        banner()
    
    root_directory = open("settings.txt", "r").readlines()[0].strip()
    directory = root_directory
    
    running = True
    while running:
        command = input(f"{directory}> ")
        
        if command == "exit":
            running = False
        
        elif command == "clear":
            if os.name == "nt":
                os.system("cls")
                banner()
            else:
                os.system("clear")
                banner()
        
        elif command == "help":
            print(colorama.Fore.BLUE + """
Commands:
  cd <directory>    - Change directory
  list              - List all files in current directory
  conjuref <file>   - Create an empty file
  conjure <folder>  - Create a new directory
  rmtree <folder>   - Remove a directory
  remove <file>     - Delete a file
  rename <old> <new>- Rename a file or directory
  open <file>       - Open a file in VS Code
  view <file>       - View the contents of a file
  clear             - Clear the screen and display the banner
  exit              - Exit the program
            """ + colorama.Style.RESET_ALL)
        
        elif command == "cd ..":
            if directory == root_directory:
                print(colorama.Fore.RED + "Already in root directory, no going back 🗿" + colorama.Style.RESET_ALL)
            else:
                directory = os.path.dirname(directory)
            
        elif command.startswith("cd "):
            new_dir = command.split(" ", 1)[1]
            if os.path.isabs(new_dir):
                if os.path.exists(new_dir):
                    directory = new_dir
                else:
                    print(colorama.Fore.RED + f"Directory '{new_dir}' does not exist." + colorama.Style.RESET_ALL)
            else:
                test_directory = os.path.join(directory, new_dir)
                if os.path.exists(test_directory):
                    directory = test_directory
                else:
                    print(colorama.Fore.RED + f"Directory '{test_directory}' does not exist." + colorama.Style.RESET_ALL)
        
        elif command == "list":
            try:
                for file in os.listdir(directory):
                    print(colorama.Fore.BLUE + file + colorama.Style.RESET_ALL)
            except FileNotFoundError:
                print(colorama.Fore.RED + f"Directory '{directory}' not found." + colorama.Style.RESET_ALL)
        
        elif command.startswith("conjuref "):
            file_name = command.split(" ", 1)[1]
            with open(os.path.join(directory, file_name), "w") as f:
                f.write("")
            print(colorama.Fore.GREEN + f"File '{file_name}' created." + colorama.Style.RESET_ALL)
        
        elif command.startswith("conjure "):
            directory_name = command.split(" ", 1)[1]
            os.makedirs(os.path.join(directory, directory_name), exist_ok=True)
            print(colorama.Fore.GREEN + f"Directory '{directory_name}' created." + colorama.Style.RESET_ALL)

        elif command.startswith("rmtree "):
            directory_name = command.split(" ", 1)[1]
            shutil.rmtree(os.path.join(directory, directory_name), ignore_errors=True)
            print(colorama.Fore.GREEN + f"Directory '{directory_name}' removed." + colorama.Style.RESET_ALL)
            
        elif command.startswith("remove "):
            file_name = command.split(" ", 1)[1]
            try:
                os.remove(os.path.join(directory, file_name))
                print(colorama.Fore.GREEN + f"File '{file_name}' removed." + colorama.Style.RESET_ALL)
            except FileNotFoundError:
                print(colorama.Fore.RED + f"File '{file_name}' not found." + colorama.Style.RESET_ALL)
        
        elif command.startswith("rename "):
            try:
                parts = command.split(" ", 2)
                old_name = parts[1]
                new_name = parts[2]
                os.rename(os.path.join(directory, old_name), os.path.join(directory, new_name))
                print(colorama.Fore.GREEN + f"File '{old_name}' renamed to '{new_name}'." + colorama.Style.RESET_ALL)
            except IndexError:
                print(colorama.Style.RESET_ALL + "Invalid rename command format. Use: rename <old> <new>")
            except FileNotFoundError:
                print(colorama.Style.RESET_ALL + f"File '{old_name}' not found.")
        
        elif command.startswith("open "):
            try:
                subprocess.run(['code', os.path.join(directory, command.split(" ", 1)[1])])
            except Exception as e:
                print(colorama.Fore.RED + f"Could not start file: {e}" + colorama.Style.RESET_ALL)
        
        elif command.startswith("view "):
            try:
                with open(os.path.join(directory, command.split(" ", 1)[1]), "r") as f:
                    lines = f.readlines()
                for line in lines:
                    print(colorama.Fore.BLUE + line, end='' + colorama.Style.RESET_ALL)
            except FileNotFoundError:
                print(colorama.Fore.RED + "File not found." + colorama.Style.RESET_ALL)
            except Exception as e:
                print(colorama.Fore.RED + f"Could not open file: {e}" + colorama.Style.RESET_ALL)
        
        else:
            print(colorama.Fore.RED + "Invalid command" + colorama.Style.RESET_ALL)

main()


