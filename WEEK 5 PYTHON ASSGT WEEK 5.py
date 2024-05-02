# File Creation
def create_file():
    try:
        with open("my_file.txt", "w") as file:
            file.write("This is line 1\n")
            file.write("31415\n")  # Mix of string and number
            file.write("Another line with some text and numbers: 10000\n")
    except PermissionError:
        print("Permission denied. Unable to create the file.")
    except Exception as e:
        print("An error occurred:", e)
    finally:
        print("File creation process completed.")


# File Reading and Display
def read_file():
    try:
        with open("my_file.txt", "r") as file:
            print("Contents of my_file.txt:")
            for line in file:
                print(line.strip())  # Strip removes the newline character at the end
    except FileNotFoundError:
        print("File not found. Unable to read the file.")
    except Exception as e:
        print("An error occurred:", e)
    finally:
        print("File reading process completed.")


# File Appending
def append_to_file():
    try:
        with open("my_file.txt", "a") as file:
            file.write("Appending line 1\n")
            file.write("Appending line 2\n")
            file.write("Appending line 3\n")
    except PermissionError:
        print("Permission denied. Unable to append to the file.")
    except Exception as e:
        print("An error occurred:", e)
    finally:
        print("File appending process completed.")


# Main function to execute the tasks
def main():
    create_file()
    read_file()
    append_to_file()


if __name__ == "__main__":
    main()
