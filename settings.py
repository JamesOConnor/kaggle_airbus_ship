import os
from pathlib import Path

###################################################################################
# PROJECT SETTINGS
###################################################################################
PROJ_ROOT = str(Path(__file__).parents[0].resolve().absolute())

###################################################################################
# PROJECT PATHS
###################################################################################

RAW = "raw"
INTERMEDIATE = "intermediate"
PREPARED = "prepared"
EXTERNAL = "external"
MASTER = "master"

# DATA
DATA_ROOT = "/".join([PROJ_ROOT, "data"])
RAW_DATA = "/".join([DATA_ROOT, RAW])
INTERMEDIATE_DATA = "/".join([DATA_ROOT, INTERMEDIATE])
PREPARED_DATA = "/".join([DATA_ROOT, PREPARED])
EXTERNAL_DATA = "/".join([DATA_ROOT, EXTERNAL])
