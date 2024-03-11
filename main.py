from dotenv import load_dotenv
import os
from app import App

environment=os.getenv('ENVIRONMENT')
print(f'Running in {environment} mode')

if __name__ == "__main__":
    App.start()
