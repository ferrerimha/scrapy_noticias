import os, dotenv

dotenv.load_dotenv()

EVOLUTION_API_URL = os.getenv('EVOLUTION_API_URL')
EVOLUTION_API_TOKEN = os.getenv('EVOLUTION_API_TOKEN')
EVOLUTION_INSTANCE = os.getenv('EVOLUTION_INSTANCE')