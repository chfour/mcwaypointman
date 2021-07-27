#!/usr/bin/env python3
import pyperclip
import time

def wait(interval=0.5) -> str:
    """
        Block until a clipboard content change has been detected,
        and return the content.
    """
    current = ""
    previous = current
    while current == previous:
        current = pyperclip.paste()
        time.sleep(interval)
        previous = pyperclip.paste()
    return previous

if __name__ == "__main__":
    print(wait(), end="")
