import os, sys
try:
    __import__("trone").menu_apikey()
except Exception as e:
    exit(str(e))
