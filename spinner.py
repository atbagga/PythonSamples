import itertools
import time
from humanfriendly import Spinner, Timer
import random 
import colorama

label = "downloading"
with Spinner(label=label, total=100) as spinner:
    colorama.init()   # Needed for humanfriendly spinner to display correctly
    progress = 0
    while progress < 100:
        colorama.init()   # Needed for humanfriendly spinner to display correctly
        # Do something useful here.
        time.sleep(0.1)
        # Advance the spinner.
        spinner.step(progress)
        # Determine the new progress value.
        progress += random.random() * 5
        if progress > 50:
            spinner.label = "Validating.."

# with Spinner(label="Downloading") as spinner:
#     for i in range(100):
#         # Do something useful here.
#         time.sleep(0.1) 
#         # Advance the spinner.
#         spinner.step()

# with Spinner(label="Downloading", timer=Timer()) as spinner:
#     for i in range(100):
#         # Do something useful here.
#         time.sleep(0.1)
#         # Advance the spinner.
#         spinner.step()