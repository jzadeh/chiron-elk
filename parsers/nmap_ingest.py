import logging

log = logging.getLogger(__name__)

class nmap_ingest(object):

  """Parse nmap related data

    Attributes:
        directory_to_parse: path to nmap data 
        move_files_after_parsing: set to false if we want to retain files after parsing
    """
    def __init__(self, directory_to_parse, move_files_after_parsing = True):
        self.directory = directory_to_parse
        self.flag = move_files_after_parsing

#    def parse_single_nmap_file(full_file_name):
#   	???

#	def move_data:
#		# excute an os command to read all files in directory and dlete