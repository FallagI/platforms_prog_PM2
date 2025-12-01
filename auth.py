# Обновляем auth.py для исправления потенциальной ошибки
class User:
    def __init__(self, username, email):
        if not username:
            raise ValueError("Username cannot be empty")
        self.username = username
        self.email = email
        self.is_authenticated = False
    
    def authenticate(self, password):
        # Добавляем проверку пароля
        if not password:
            print("Error: Password cannot be empty")
            return False
        
        # В реальном проекте здесь была бы проверка пароля
        self.is_authenticated = True
        return True
    
    def logout(self):
        self.is_authenticated = False
        return True

def login(username, password):
    """Функция входа пользователя с проверкой входных данных"""
    try:
        user = User(username, f"{username}@example.com")
        if user.authenticate(password):
            print(f"User {username} logged in successfully")
            return user
    except ValueError as e:
        print(f"Login error: {e}")
    return None
EOF
