from config import USER_ID

class ApiClient:
    def __init__(self, client):
        self.client = client

    def is_followed_by(self, user_id):
        return self.client.user_friendship_v1(user_id=user_id).followed_by

    def last_time(self, thread):
        last_time_msg = thread.last_seen_at.get(USER_ID).get('timestamp')

    
    def send_wait_messege(self, user_id):
        self.client.direct_send("لطفا چند لحظه صبر کنید ...", user_ids=[user_id])   

    
    def send_nonfollow_messege(self, user_id):
        self.client.direct_send("شما دنبال کننده این صفحه نیستید. اول این صفحه رو دنبال کنید.", user_ids=[user_id])

    def send_nontext_messege(self, user_id):
        self.client.direct_send("پیام ارسالی صحیح نمی باشد. لطفا رویای خود را به صورت متنی توضیج دهید..", user_ids=[user_id])    

    def handle_messege(self, messege):
        user_id = messege.user_id

        # check follower
        # if not self.is_followed_by(user_id=user_id):
        #     self.send_nonfollow_messege(user_id=user_id) 
        #     return False   

        # check not None and length 
        if messege.text is None or len(messege.text) < 10:
            self.send_nontext_messege(user_id=user_id)
            return False   
        
        return True    
