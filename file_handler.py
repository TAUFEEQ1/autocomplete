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
            f.writelines(names)
            
        return f"New names have been appended to {self.filename}."