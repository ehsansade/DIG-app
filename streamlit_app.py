import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns
#from fuzzywuzzy import process  
import re
import numpy as np
from fuzzywuzzy import fuzz
from difflib import SequenceMatcher
st.title("NLP-Powered Data Insights Generator")
