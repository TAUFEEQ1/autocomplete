
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return False
class FileHandler:
    def __init__(self, filename):
        self.filename = filename
        self._names = []

    def _read_names(self):
        """Read names from the file and return as a list."""
        with open(self.filename, 'r') as f:
            names = f.readlines()
            names = [name.strip() for name in names]
        return names

    def get_names(self):
        """Return all names in the file."""
        if not self._names:
            self._names = self._read_names()
        return self._names
    
    def append_names(self, new_names):
        """Append new names to the file."""
        names = self.get_names()
        names.extend(new_names)
        names.sort()

        with open(self.filename, 'w') as f:
            for name in names:
                f.write(f"{name}\n")

        return f"New names have been appended to {self.filename}."
    
    def update(self,new_names:list):
        novel_names = []
        for name in new_names:
            if not binary_search(self.get_names(), name):
                novel_names.append(name)
        if novel_names:
            self.append_names(novel_names)
            return f"New names have been appended to {self.filename}."