def write_file(filename):
        
    # filename = input("Enter the file name: ")

    txt = open(filename, 'w')

    write_txt = input("Enter line to write to file: ")

    txt.write(write_txt)

    txt.close()

if __name__ == "__main__":      #to import in another file and not run the whole code(make module)

    filename = input("Enter the file name: ")

    write_file(filename)