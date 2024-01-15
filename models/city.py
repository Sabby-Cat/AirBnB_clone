#!/usr/bin/python3
"""The city class
"""
from models.base_model import BaseModel


class City(BaseModel):
    """A city

    Attributes:
        name
        state_id
    """
    name = ""
    state_id = ""
