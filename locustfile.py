from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
  wait_time = between(1, 2)

  @task
  def index(self):
    self.client.get("/")

if __name__ == "__main__":
  import os
  os.environ['LOCUST_HOST'] = 'http://localhost:5000'  # Replace with your app URL

