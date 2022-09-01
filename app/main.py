from datetime import datetime
from fastapi import FastAPI, Body, Response, status, HTTPException, Depends, Query
from models import PostBase, PostCreate, PostOut
from typing import Optional, List

app = FastAPI()

# Hardcoded posts for API demonstration
post_numb_one = {'id': 1, 'title': 'My first post', 'content': 'My first content', 'created_at': datetime.now()}
post_numb_two = {'id': 2, 'title': 'My second post', 'content': 'My second content', 'created_at': datetime.now()}
posts = [post_numb_one, post_numb_two]


@app.get("/")
def root():
    return {"message": "Welcome to my API!"}


@app.get("/posts", status_code=status.HTTP_200_OK, response_model=List[PostOut])
def get_posts():
        return posts

@app.get("/posts/", status_code=status.HTTP_200_OK, response_model=PostOut)
def get_posts(post_id: Optional[int] = None):
    for post in posts:
        if post['id'] == post_id:
            return post
    if post_id not in posts:
        raise HTTPException(status_code=404)


@app.get("/posts/{post_id}", status_code=status.HTTP_200_OK, response_model=PostOut)
def get_posts_id(post_id: int):
    for post in posts:
        if post['id'] == post_id:
            return post
    if post_id not in posts:
        raise HTTPException(status_code=404)


@app.post("/posts", status_code=status.HTTP_201_CREATED, response_model=PostOut)
def create_posts(post: PostCreate):
    post_id = posts[-1]['id'] + 1  # Creating a new ID that increases from the previous ID value in posts
    new_post = dict(post)
    new_post.update(id=post_id, created_at=datetime.now())
    print(new_post)
    posts.append(new_post)  # Puts new post in posts list
    return new_post
