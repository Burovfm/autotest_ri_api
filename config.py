import os
from pathlib import Path

from dotenv import load_dotenv

environment = os.environ.get('TEST_ENV', 'test')
env_path = Path('.') / f'.env.{environment}'
load_dotenv(dotenv_path=env_path)

# RI_BASE_URL = os.getenv('RI_BASE_URL')
RI_BASE_URL='http://resource-inventory.resource.test.oliwio.rnd.mtt/api'
