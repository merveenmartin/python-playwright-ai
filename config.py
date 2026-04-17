import anthropic
from dotenv import load_dotenv

load_dotenv()

MODEL = "claude-opus-4-7"
MAX_TOKENS = 16000
BASE_URL = "https://the-internet.herokuapp.com"

client = anthropic.Anthropic()
