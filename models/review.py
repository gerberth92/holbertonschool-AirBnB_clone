#!/usr/bin/python3
"""
Modulo que define una clase Review.
"""
from models.base_model import BaseModel


class Review(BaseModel):
    place_id = ""
    user_id = ""
    text = ""