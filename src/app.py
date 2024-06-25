import os
import pandas as pd
import seaborn as sns
from dotenv import load_dotenv
import spotipy

# load the .env file variables
load_dotenv()

import os
from dotenv import load_dotenv
load_dotenv()

client_id = os.environ.get('CLIENT_ID')
client_secret = os.environ.get('CLIENT_SECRET')
