from fastapi import FastAPI, Path, HTTPException
from pydantic import BaseModel
from typing import Annotated, List

app = FastAPI()
users = []


class User(BaseModel):
    id: int = None
    username: str
    age: int = 18


@app.get('/users')
async def get_users() -> List[User]:
    return users


@app.post('/user/{username}/{age}')
async def create_user(
    username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username', example='User1')],
    age: int = Path(ge=18, le=120, description='Enter age', example=20)
) -> User:
    user = User(
        id=users[-1].id + 1 if len(users) > 0 else 1,
        username=username,
        age=age
    )
    users.append(user)
    return user


@app.put('/user/{user_id}/{username}/{age}')
async def update_user(
    user_id: Annotated[int, Path(ge=1, le=100, description='Enter User ID', example=1)],
    username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username', example='User1')],
    age: int = Path(ge=18, le=120, description='Enter age', example=20)
) -> User:
    for user in users:
        if user.id == user_id:
            user.username = username
            user.age = age
            return user
    raise HTTPException(404, 'User was not found.')


@app.delete('/user/{user_id}')
async def delete_user(user_id: int = Path(ge=1, le=100, description='Enter User ID', example=1)) -> User:
    for i in range(len(users)):
        if users[i].id == user_id:
            return users.pop(i)
    raise HTTPException(404, 'User was not found.')
