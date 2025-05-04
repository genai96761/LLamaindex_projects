##testing how to load  the environment variables 
import os 
from dotenv import load_dotenv 

load_dotenv()

print(f'loading the api key ')
print(f'goole api key {os.environ['GOOGLE_API_KEY']}')