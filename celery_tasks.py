import time
import random 
from celery import Celery
from config import get_insta_client
from app.instagram.dm_format import dream_interpretation_parser
from app.llm.openai_client import get_llm_response

app = Celery("tasks", broker="redis://localhost:6379/0")
cl= get_insta_client()

@app.task(bind=True, acks_late=True, max_retries=3)
def send_wait_message(self, user_id):
    try:

        time.sleep(random.randint(1, 5))
        cl.direct_send("لطفا چند لحظه صبر کنید ...", user_ids=[user_id])   
    except Exception as e:
        print(f"Error: {e}. Retrying...")
        raise self.retry(exc=e)

@app.task(bind=True, acks_late=True, max_retries=2,)# rate_limit='100/h')
def send_llm_response(self, user_id, user_dream):
    try:
        response= get_llm_response(user_dream=user_dream)
        reply = dream_interpretation_parser(data=response)
        time.sleep(random.randint(3, 10))
        cl.direct_send(reply, [user_id])

    except Exception as e:
        print(f"Error: {e}")
        raise self.retry(exc=e)
