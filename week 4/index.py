#1.File Read & Write Challenge
 #create a file and added 3 sentences
with open("index.txt","w") as f:
    f.write("this is week 3 assignment.")
    f.write(" I am expected to Create a program that reads a file and writes a modified version to a new file. ")
    f.write("For the seccond part, ask the user for a filename and handle errors if it doesn’t exist or can’t be read.")
    print("File 'index.txt' created\n")
#check if file is created with the contents   
with open("index.txt","r") as f:
   content=f.read()
print(content)

#mordify the file to uppercase  and content of the file while retaining the previous file
try:
    with open("index.txt","a") as task4_file:
        task4_file.write("\n \nSorry for that this is week 4 assignment not 3.")
        task4_file.write("\nNothing changes for the task assignment. you first  Create a program that reads a file and writes a modified version to a new file. ")
        task4_file.write("\nFor the second part, ask the user for a filename and handle errors if it doesn’t exist or can’t be read.")
        print ("\nfile successfully Mordified and saved to 'task4.txt'\n")
#check if file modificaions are done
    with open("index.txt","r") as task4_file:
        data=task4_file.read() .upper()
    print(data)

except FileNotFoundError:
    print(f"Error:file not found.Please try again")

# 2.Error handling
def valid_filename():
    while True:  # Keep asking until valid file is found
        filename = input("Enter valid filename: ").strip()
        
        try:
            with open(filename ,"r") as file2:
                content2 = file2.read()
                print(f"Successfully read the: {filename}")
                return content2
        except FileNotFoundError:
            print(f"Error:{filename} not found.Please try again")
        except Exception as e:
            print(f"Error reading file: {e}")
        
        return None