#!/usr/bin/python3
"""A module containing "Review" class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Implementation of "Review" objects"""

    place_id = ""
    user_id = ""
    text = ""
