"""
Enum for type of redis channel

"""
import enum


class Type(enum.Enum):
    storageCheck = 1
    storageStatus = 2
