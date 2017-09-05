import logging

log = logging.getLogger(__name__)

class normalization_utils:
"""Normalize p0f, nmap and

  Attributes:
  bro_file:  maybe just data frame instead 
  nmap_file:
  p0f_file
  """

    def __init__(self, directory_to_parse, move_files_after_parsing = true):
        self.directory = directory_to_parse

    def normalize_data_frames(df1,df2,df3):
      
