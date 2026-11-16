class File:

  def __init__(self, name: str, extension: str, size: int):
    """Конструктор класу File"""
    self._name = name
    self._extension = extension
    self._size = size
    self._parent = (
        None
    )
    print(f"[Створено файл]: {self.full_name}")

  def __del__(self):
    print(f"[Видалено файл]: {self.full_name}")

  #гетери сетери
  @property
  def name(self):
    return self._name

  @name.setter
  def name(self, value: str):
    self._name = value

  @property
  def extension(self):
    return self._extension

  @extension.setter
  def extension(self, value: str):
    self._extension = value

  @property
  def size(self):
    return self._size

  @size.setter
  def size(self, value: int):
    if value >= 0:
      self._size = value
    else:
      raise ValueError("Розмір файлу не може бути від'ємним.")

  @property
  def full_name(self):
    return f"{self._name}.{self._extension}"

  def get_path(self):
    if self._parent:
      return f"{self._parent.get_path()}/{self.full_name}"
    return self.full_name

  def display(self, indent=""):
    print(f"{indent}📄 Файл: {self.full_name} (Розмір: {self._size} байт)")


class Folder:

  def __init__(self, name: str):
    self._name = name
    self._items = []  #об'єкти File або Folder
    self._parent = None
    print(f"[Створено папку]: {self._name}")

  def __del__(self):
    print(f"[Видалено папку]: {self._name}")


  @property
  def name(self):
    return self._name

  @name.setter
  def name(self, value: str):
    self._name = value

  @property
  def items(self):
    return self._items

  def add_item(self, item):
    item._parent = self
    self._items.append(item)

  def get_path(self):
    if self._parent:
      return f"{self._parent.get_path()}/{self._name}"
    return self._name

  def display(self, indent=""):
    print(f"{indent}📁 Папка: {self._name}")
    for item in self._items:
      item.display(indent + "    ")

  def get_all_paths(self):
    paths = [self.get_path()]
    for item in self._items:
      if isinstance(item, Folder):
        paths.extend(item.get_all_paths())
      else:
        paths.append(item.get_path())
    return paths

  def get_longest_path(self):
    all_paths = self.get_all_paths()
    if not all_paths:
      return self.get_path()
    return max(all_paths, key=len)


def main():
  print("Створення файлової системи")
  root = Folder("Root")


  documents = Folder("Documents")
  work = Folder("Work")
  photos = Folder("Photos")


  file1 = File("resume", "pdf", 1250)
  file2 = File("todo", "txt", 150)
  file3 = File("report", "docx", 4500)
  file4 = File("avatar", "jpg", 204800)

  # Побудова вкладеності
  work.add_item(file3)
  documents.add_item(file1)
  documents.add_item(file2)
  documents.add_item(work)

  photos.add_item(file4)

  root.add_item(documents)
  root.add_item(photos)

  print("\n--- 2. Виведення дерева файлів і папок ---")
  root.display()

  print("\n--- 3. Демонстрація функцій доступу (гетерів/сетерів) ---")
  print(
      f"Початкове ім'я та розмір файлу: {file2.full_name}, {file2.size} байт"
  )

  # Зміна значень через сетери
  file2.name = "important_notes"
  file2.size = 320
  print(f"Змінене ім'я та розмір файлу: {file2.full_name}, {file2.size} байт")

  print("\n--- 4. Пошук найдовшого шляху (path) до об'єкта ---")
  longest_path = root.get_longest_path()
  print(
      f"Найдовший шлях у файловій системі: '{longest_path}'"
      f" (довжина: {len(longest_path)} символів)"
  )

  print("\n--- 5. Завершення програми ---")


if __name__ == "__main__":
  main()