import os

def search_opcode(directory, opcode):
    found_files = []
    
    # Walk through all files in the given directory
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".asm"):  # Check only .asm files
                file_path = os.path.join(root, file)
                
                # Read file and check for opcode
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    for line in f:
                        if opcode in line:
                            found_files.append(file_path)
                            break  # Stop checking once found in the file
    
    # Print results
    if found_files:
        print("OpCode found in:")
        for file in found_files:
            print(f" - {file}")
    else:
        print("OpCode not found in any .asm files.")

if __name__ == "__main__":
    project_dir = "../Debug"
    search_opcode(project_dir, "MCCNDD")
