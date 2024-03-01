import sys
import datetime
import csv
import os


def main():
    # filename= f"{datetime.datetime.now().strftime("%Y-%m-%d %H_%M_%S.%f")[:-3]}".md"
    
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H_%M_%S.%f")[:-3]
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    print(today)
    folder_path = "blog-entries"


    # Check if the folder exists, create it if it doesn't
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    
    filename = os.path.join(folder_path, f"{today}.md")
    #print(filename)
    try:
        inp = input("Type in an entry:  ")
        with open(filename, "a") as file:
            current_time = datetime.datetime.now().strftime("%H-%M-%S")
            file.write(f"{current_time} : {inp}\n")
    except FileNotFoundError:
        sys.exit("File not found.")




if __name__ == "__main__":
    main()
