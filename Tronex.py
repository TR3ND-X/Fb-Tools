import os, sys
try:
    __import__("trone").menu()
except Exception as e:
    exit(str(e))
