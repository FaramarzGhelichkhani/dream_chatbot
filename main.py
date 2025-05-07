import time
from app.instagram.api_client import ApiClient
from celery_tasks import send_wait_message, send_llm_response
from config import get_insta_client, USER_ID

cl= get_insta_client()
api = ApiClient(client=cl)

while True:
    threads = cl.direct_threads(
        amount=1, selected_filter="unread", thread_message_limit=2)

    for thread in threads:

        if len(thread.users) != 1:  # not group
            cl.direct_send_seen(thread_id=thread.pk)  # seen thread
            continue
        messages = thread.messages

        if not messages:
            cl.direct_send_seen(thread_id=thread.pk)
            continue

        latest_msg = messages[0]
        if latest_msg.user_id == USER_ID:
            cl.direct_send_seen(thread_id=thread.pk)
            continue
            
        if not api.handle_messege(messege=latest_msg):
            continue
        
        # Queue background tasks
        send_wait_message.delay(user_id=latest_msg.user_id)
        send_llm_response.delay(user_id=latest_msg.user_id, user_dream=latest_msg.text)

        cl.direct_send_seen(thread_id=thread.pk)

    time.sleep(1)
