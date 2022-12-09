from typing import List, Optional, Dict

def main():
    fname = "puzzle_data.txt"
    lines = ingest_file(fname)

    root = process_shell_output(lines)
    directory_sizes = find_directory_sizes(root)

    print("-------- Part 1 --------")
    size_sum = 0
    for k, v in directory_sizes.items():
        if v <= 100000:
            # print(f"Directory {k} has a size of {v}")
            size_sum += v

    print(f"Sum sizes of directories <= 100000: {size_sum}")

    print("-------- Part 2 --------")
    total_available_space = 70000000
    needed_unused_space = 30000000
    current_used_space = directory_sizes["/"]
    current_unused_space = total_available_space - current_used_space
    minimum_deletion_size = needed_unused_space - current_unused_space

    possible_deletions = {k:v for k, v in directory_sizes.items() if v >= minimum_deletion_size}

    min_dir = min(possible_deletions, key=possible_deletions.get)
    min_dir_size = possible_deletions[min_dir]
    print(f"Directory {min_dir} is the smallest directory (size: {min_dir_size}) that can be deleted to free up space.")

class File(object):
    """A simple class representing a file.

    Attributes:
        name (str): The name of the file.
        size (int): The size of the file in elf-units.
    """

    def __init__(self, name, size):
        """Initializes a new instance of the File class.

        Args:
            name (str): The name of the file.
            size (int): The size of the file in elf-units.
        """

        self.name = name
        self.size = size

    def get_name(self) -> str:
        """Returns the name of the file.

        Returns:
            str: The name of the file.
        """

        return self.name

    def get_size(self) -> int:
        """Returns the size of the file in elf-units.

        Returns:
            int: The size of the file in elf-units.
        """

        return self.size

    def __str__(self):
        """Returns a string representation of the file.

        Returns:
            str: A string representation of the file.
        """

        return f"File `{self.name}`: {self.size}"

class Directory(object):
    """A simple class representing a directory.

    A directory can contain files and subdirectories.

    Attributes:
        name (str): The name of the directory.
        files (List[File]): The list of files in the directory.
        subdirectories (Dict[str, Directory]): The dictionary of subdirectories in the directory, where the keys are the names of the subdirectories.
    """

    def __init__(self, name):
        """Initializes a new instance of the Directory class.

        Args:
            name (str): The name of the directory.
        """

        self.name = name
        self.files: List[File] = []
        self.subdirectories: Dict[str, Directory] = {}

    def get_name(self) -> str:
        """Returns the name of the directory.

        Returns:
            str: The name of the directory.
        """

        return self.name

    def get_size(self) -> int:
        """Returns the total size of the directory in bytes.

        This includes the sizes of all files in the directory and all of its subdirectories.

        Returns:
            int: The total size of the directory in elf-units.
        """

        total_size = 0

        for f in self.files:
            total_size += f.get_size()

        for d in self.subdirectories:
            total_size += d.get_size()

        return total_size

    def add_file(self, f: File) -> None:
        """Adds a file to the directory.

        Args:
            f (File): The file to add.
        """

        self.files.append(f)

    def add_subdirectory(self, d: "Directory") -> None:
        """Adds a subdirectory to the directory.

        Args:
            d (Directory): The subdirectory to add.
        """

        name = d.get_name()
        self.subdirectories[name] = d

    def __str__(self) -> str:
        """Returns a string representation of the directory.

        Returns:
            str: A string representation of the directory.
        """

        n = self.name
        f = ", ".join(map(str, self.files))
        d = ", ".join(map(str, self.subdirectories))
        return f"Directory {n}:\n\tFiles: {f}\n\tSubdirectories: {d}"


def find_directory_sizes(root: Directory) -> Dict[str, int]:
    """Finds the sizes of each directory in a directory tree.

    This function traverses a directory tree and returns a dictionary mapping the names of each directory to its size in bytes. The size of a directory includes the sizes of all files in the directory and all of its subdirectories.

    Args:
        root (Directory): The root of the directory tree.

    Returns:
        Dict[str, int]: A dictionary mapping directory names to their sizes in bytes.
    """

    file_sizes = 0
    for f in root.files:
        file_sizes += f.get_size()

    subdir_sizes = {}
    for s in root.subdirectories:
        size = find_directory_sizes(root.subdirectories[s])
        subdir_sizes.update(size)

    current_size = file_sizes
    for k, v in subdir_sizes.items():
        if k in root.subdirectories:
            current_size += v

    curname = root.get_name()
    directory_sizes = {}
    for k, v in subdir_sizes.items():
        directory_sizes[f"{curname}/{k}"] = v


    directory_sizes[root.get_name()] = current_size
    return directory_sizes


def ingest_file(fname: str) -> List[str]:
    """Ingests a file and returns a list of its lines.

    This function reads a file with the given name and returns a list of strings, where each string is a line from the file. Leading and trailing whitespace is removed from each line.

    Args:
        fname (str): The name of the file to ingest.

    Returns:
        List[str]: The list of lines from the file.
    """

    with open(fname, "r") as f:
        lines = f.readlines()

    lines = [l.strip() for l in lines]

    return lines

def process_shell_output(lines: List[str]) -> Directory:
    """Processes a list of lines of shell output and returns a directory tree.

    This function processes a list of strings, where each string is either a command or output from a command.
    Lines with commands are begin with a '$'. The function builds a tree of directories based on the commands
    and outputs of the commands, and returns the root of the tree.

    Args:
        lines (List[str]): The list of lines of shell output.

    Returns:
        Directory: The root of the directory tree.
    """
    dir_track: List[str]= []
    root = Directory("/")

    curdir = root
    for line in lines:
        input = line.split(" ")
        if input[0] == "$":
            if input[1] == "cd":
                if input[2] == "/":
                    dir_track = []
                elif input[2] == "..":
                    # navigate up one directory
                    dir_track.pop(-1)
                else:
                    dir_track.append(input[2])

                curdir = root
                for d in dir_track:
                    curdir = curdir.subdirectories[d]

        else:
            # if line does not start with "$", then we can assume
            # it is listing the contents of a directory

            if input[0] == "dir":
                curdir.add_subdirectory(Directory(input[1]))
            else:
                curdir.add_file(File(input[1], int(input[0])))

    return root


if __name__ == "__main__":
    main()