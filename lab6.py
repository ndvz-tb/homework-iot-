import logging
import os


class FileNotFound(Exception):
    """
    Custom exception raised when the file does not exist
    during the creation of a TextFileHandler object.
    """


class FileCorrupted(Exception):
    """
    Custom exception raised when an error occurs during reading,
    writing, or accessing the file.
    """
    pass

def logged(exception, mode="console"):
    """
    Decorator for logging exceptions.

    Parameters:
    exception — the exception type that should be logged.
    mode — logging mode: 'console' or 'file'.
    """

    def decorator(func):
        """
        Internal decorator that takes a function
        and returns its wrapped version.
        """

        def wrapper(*args, **kwargs):
            """
            Wrapper that executes the function and intercepts the
            specified exception type for logging.
            """
            try:
                return func(*args, **kwargs)
            except exception as e:
                logger = logging.getLogger(func.__name__)
                logger.setLevel(logging.ERROR)

                if mode == "file":
                    handler = logging.FileHandler("log.txt", mode="a", encoding="utf-8")
                else:
                    handler = logging.StreamHandler()

                formatter = logging.Formatter(
                    "%(asctime)s - %(levelname)s - %(message)s"
                )
                handler.setFormatter(formatter)
                logger.addHandler(handler)

                logger.error(str(e))

                logger.removeHandler(handler)

                raise e

        return wrapper

    return decorator 


class TextFileHandler:
    """
    A class for working with a text file.
    Provides reading, writing, and appending with error logging.
    """

    def __init__(self, path: str):
        """
        Constructor.

        Accepts the path to a file and checks its existence.
        If the file does not exist, raises FileNotFound.
        """
        self.path = path

        if not os.path.exists(path):
            raise FileNotFound(f"File '{path}' does not exist!")


    @logged(FileCorrupted, mode="file")
    def read(self):
        """
        Reads the content of the text file.
        If an error occurs, raises FileCorrupted
        and logs the exception into a file.
        """
        try:
            with open(self.path, "r", encoding="utf-8") as f:
                return f.read()
        except Exception:
            raise FileCorrupted("Unable to read the file!")

    @logged(FileCorrupted, mode="console")
    def write(self, text: str):
        """
        Fully rewrites the file content with the given text.
        If an error occurs, raises FileCorrupted
        and logs the exception to the console.
        """
        try:
            with open(self.path, "w", encoding="utf-8") as f:
                f.write(text)
        except Exception:
            raise FileCorrupted("Unable to write to the file!")

    @logged(FileCorrupted, mode="file")
    def append(self, text: str):
        """
        Appends the given text to the end of the file.
        If an error occurs, raises FileCorrupted
        and logs the exception into a file.
        """
        try:
            with open(self.path, "a", encoding="utf-8") as f:
                f.write(text)
        except Exception:
            raise FileCorrupted("Unable to append to the file!")

if __name__ == "__main__":
    """
    Entry point of the program.
    Demonstrates the functionality of TextFileHandler.
    """

    file_path = "data_corrupted.txt"

    try:
        with open(file_path, "w") as f:
            f.write("test")

        handler = TextFileHandler(file_path)

        # Artificially breaking the path to trigger an error.
        handler.path = "/invalid/path/to/force/error.txt"

        print("Attempting to read (should cause an error and be logged to file)...")

        handler.read()

    except FileNotFound as e:
        print(f"[{type(e).__name__}] {e}")

    except FileCorrupted as e:
        print(f"\n[{type(e).__name__}] {e}")

    if os.path.exists("log.txt"):
        print("\n File 'log.txt' successfully created!")
        with open("log.txt", "r", encoding="utf-8") as f:
            print("--- log.txt content ---")
            print(f.read())
            print("-----------------------")
    else:
        print("\n File 'log.txt' was not created.")
