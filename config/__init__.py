import os
from .settings import (USER_ID, USERNAME,
                        PASSWORD, MAX_INTERVAL,
                        OPENAI_API_KEY, MODEL_NAME
                        )
from .client import get_insta_client
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
os.environ["OPENAI_MODEL_NAME"] = MODEL_NAME
os.environ['HTTP_PROXY'] = "socks5h://127.0.0.1:10808"
os.environ['HTTPS_PROXY'] = "socks5h://127.0.0.1:10808"
