from importlib import import_module

from . import e2e
from .all import objects

for k, v in objects.items():
    path, name = v.rsplit(".", 1)
    objects[k] = getattr(import_module(path), name)