#!/usr/bin/env python3
from waypoint import NotACopiedLocation, Waypoint
import clipboard
import logging

logging.basicConfig(format="[%(asctime)s] %(levelname)s: %(message)s", level=logging.DEBUG)

OUTPUT = "test.txt"

while True:
    logging.debug("listening for clipboard changes")
    clip = clipboard.wait()
    logging.debug(repr(clip))
    try:
        waypoint = Waypoint.from_copied(clip)
    except NotACopiedLocation:
        logging.debug("not a copied location")
        continue
    logging.info(repr(waypoint))

    with open(OUTPUT, "a") as f:
        f.write(str(waypoint) + "\n\n")
