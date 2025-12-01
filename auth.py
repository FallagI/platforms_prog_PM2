# Создаем новый файл для фичи
cat > auth.py << 'EOF'
"""
Модуль аутентификации пользователей
"""

class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.is_authenticated = False
    
    def authenticate(self, password):
        # В реальном проекте здесь была бы проверка пароля
        self.is_authenticated = True
        return True
    
    def logout(self):
        self.is_authenticated = False
        return True

def login(username, password):
    """Функция входа пользователя"""
    user = User(username, f"{username}@example.com")
    if user.authenticate(password):
        print(f"User {username} logged in successfully")
        return user
    return None

if __name__ == "__main__":
    # Тестовый код
    test_user = login("testuser", "password123")
EOF

# Обновляем main.py
cat > main.py << 'EOF'
"""
Главный модуль приложения
"""

from auth import login

def main():
    print("=== Демонстрация GitHub Flow ===")
    print("1. Инициализация проекта")
    print("2. Создание feature ветки")
    print("3. Разработка новой функциональности")
    print("4. Создание pull request")
    print("5. Code review и мерж")
    
    # Демонстрация новой функциональности
    user = login("demo_user", "demo_pass")
    if user:
        print(f"\nПользователь {user.username} успешно аутентифицирован!")
    else:
        print("\nОшибка аутентификации")

if __name__ == "__main__":
    main()
EOF
