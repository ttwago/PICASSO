from locust import HttpUser, task, between

class MyUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def upload_file(self):
        self.client.post("/upload/", files={"file": ("test_file.txt", open("test_file.txt", "rb"))})

    @task
    def get_files(self):
        self.client.get("/files/")
