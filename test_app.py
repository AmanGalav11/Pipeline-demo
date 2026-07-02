from app import welcome_message

def test_welcome_message():
    assert welcome_message() == "Welcome to CI/CD Pipeline"

