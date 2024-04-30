import unittest
from app import app, conn, c  # Assuming these are defined in app.py

class TestApp(unittest.TestCase):

  def test_home_page(self):
    # Test home page route
    tester = app.test_client()
    response = tester.get("/")
    self.assertEqual(response.status_code, 200)
    self.assertIn(b"Flask Application", response.data)  # Check for presence of title

  def test_add_data(self):
    # Test data insertion (replace with your validation logic)
    name = "Test User"
    email = "test@example.com"
    c.execute("INSERT INTO your_table (name, email) VALUES (?, ?)", (name, email))
    conn.commit()

    c.execute("SELECT * FROM your_table WHERE email = ?", (email,))
    data = c.fetchone()
    self.assertEqual(data[1], email)  # Check if email matches

    # Remove test data after test
    c.execute("DELETE FROM your_table WHERE email = ?", (email,))
    conn.commit()

if __name__ == "__main__":
  unittest.main()
