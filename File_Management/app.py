import os   

def creat_file(file_name):
    try:
        with open(file_name , "x") as f:    # with open garda no need to close manually 
            print(f"File '{file_name}' created successfully")  
    except FileExistsError:
        print(f"File '{file_name}' already exists") 
    except Exception as E:
        print("An error occurred:", E)  

def view_all_files():  
    files = os.listdir()  
    if not files:
        print("No files found")
    else:
        print("File list:")  
        print("---------------")  
        for file in files:
            print(file)  
        print("---------------")  

def delete_file(file_name):
    try:
        os.remove(file_name)
        print(f"'{file_name}' has been deleted successfully") 
    except FileNotFoundError:
        print(f"File '{file_name}' not found")
    except Exception as E:
        print("An error occurred:", E) 

def read_file(file_name):
    try:
        with open(file_name, "r") as f:  
            content = f.read()
            print(f"Content of '{file_name}':\n{content}") 
    except FileNotFoundError:
        print(f"File '{file_name}' not found") 
    except Exception as E:
        print("An error occurred:", E)

def edit_file(file_name):
    try:
        with open(file_name, "a") as f: 
            content = input("Enter data to add: ")
            f.write(content + "\n") 
            print(f"Content added to '{file_name}' successfully")  
    except FileNotFoundError:
        print(f"File '{file_name}' not found")  
    except Exception as E:
        print("An error occurred:", E)

def main():
    while True: 
        print("\n===== FILE MANAGEMENT APP =====")  
        print("1: Create file")
        print("2: View all files")  
        print("3: Delete a file")
        print("4: Read file")
        print("5: Edit file")  
        print("6: Exit")
        print("===============================\n")  
        choice = input("Enter your choice (1-6): ")

        match choice:
            case "1":  
                file_name = input("Enter file name to create: ")
                creat_file(file_name)
            case "2":
                view_all_files()  
            case "3":
                file_name = input("Enter file name to delete: ")
                delete_file(file_name)
            case "4":
                file_name = input("Enter file name to read: ")
                read_file(file_name)
            case "5":
                file_name = input("Enter file name to edit: ")
                edit_file(file_name)
            case "6":
                print("Closing app...")
                break
            case _:  
                print("Please enter a valid number (1-6)")

if __name__ == "__main__":  # dunder main idiom 
    main()
