from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()


@app.get('/')
async def main() -> str:
    return 'Главная страница'


@app.get('/user/admin')
async def admin() -> str:
    return 'Вы вошли как администратор'


@app.get('/user/{user_id}')
async def user(user_id: int = Path(ge=1, le=100, description='Enter User ID', example=1)) -> str:
    return f'Вы вошли как пользователь № {user_id}'


@app.get('/user/{username}/{age}')
async def user_info(
    username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username', example='User1')],
    age: int = Path(ge=18, le=120, description='Enter age', example=20)
) -> str:
    return f'Информация о пользователе. Имя: {username}, возраст: {age}.'
