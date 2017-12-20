import re

class FileNameExtractor:
    @staticmethod
    def extract_file_name(s):
        return re.search(r"_(\w+.\w+).", s).group(1)