"""
basic_producer_gbogbo.py

Generate some streaming travel buzz messages. 
"""

#####################################
# Import Modules
#####################################

# Import packages from Python Standard Library
import os
import random
import time

# Import external packages (must be installed in .venv first)
from dotenv import load_dotenv

# Import functions from local modules
from utils.utils_logger import logger

#####################################
# Load Environment Variables
#####################################

# Load environment variables from .env
load_dotenv()

#####################################
# Define Getter Functions for .env Variables
#####################################

# Define a function to fetch the message interval from the environment
def get_message_interval() -> int:
    """
    Fetch message interval from environment or use a default value.

    It doesn't need any outside information, so the parentheses are empty.
    It returns an integer, so we specify that in the function signature.

    The colon at the end of the function signature is required.
    All statements inside the function must be consistently indented.

    Define a local variable to hold the value of the environment variable
    os.getenv() is a function that fetches the value of an environment variable
    os.getenv() always returns a string 
    We convert the return value to an integer using the built-in Python int() function
    To use handy functions like this, import the os module 
    from the Python Standard Library (see above).
    """
    return_value: str = os.getenv("MESSAGE_INTERVAL_SECONDS", 3)
    interval: int = int(return_value)
    logger.info(f"Messages will be sent every {interval} seconds.")
    return interval


#####################################
# Define global variables
#####################################

# Define some lists for generating travel buzz messages
ADJECTIVES: list = ["breathtaking", "crowded", "peaceful", "adventurous", "cultural", "stunning", "relaxing", "challenging", "magical", "unforgettable"]
ACTIONS: list = ["visited", "explored", "discovered", "hiked", "photographed", "experienced", "wandered through", "climbed", "sailed to", "flew over"]
DESTINATIONS: list = ["a hidden beach", "an ancient temple", "a bustling market", "a mountain peak", "a local café", "a historic castle", "a scenic viewpoint", "a traditional village", "a famous landmark", "a secret waterfall"]

#####################################
# Define a function to generate travel messages
#####################################


def generate_messages():
    """
    Generate a stream of travel buzz messages.

    This function uses a generator, which yields one buzz at a time.
    Generators are memory-efficient because they produce items on the fly
    rather than creating a full list in memory.

    Because this function uses a while True loop, it will run continuously 
    until we close the window or hit CTRL c (CMD c on Mac/Linux).
    """
    
    # Multiple message templates for variety
    message_templates = [
        "I just {action} {destination}! It was {adjective}.",
        "Travel update: Just {action} {destination} and it was absolutely {adjective}!",
        "Amazing day! I {action} {destination} - so {adjective}.",
        "Can't believe I {action} {destination} today. Totally {adjective}!",
        "Latest adventure: {action} {destination}. Pretty {adjective} experience!",
        "Just {action} {destination}. Words can't describe how {adjective} it was!",
        "Update from the road: {action} {destination} - incredibly {adjective}.",
        "Travel diary: Today I {action} {destination}. Simply {adjective}!"
    ]
    
    while True:
        template = random.choice(message_templates)
        adjective = random.choice(ADJECTIVES)
        action = random.choice(ACTIONS)
        destination = random.choice(DESTINATIONS)
        yield template.format(action=action, destination=destination, adjective=adjective)


#####################################
# Define main() function to run this producer.
#####################################


def main() -> None:
    """
    Main entry point for this travel producer.

    It doesn't need any outside information, so the parentheses are empty.
    It doesn't return anything, so we say the return type is None.   
    The colon at the end of the function signature is required.
    All statements inside the function must be consistently indented. 
    This is a multiline docstring - a special type of comment 
    that explains what the function does.
    """

    logger.info("START travel producer...")
    logger.info("Generating travel buzz messages...")
    logger.info("Hit CTRL c (or CMD c) to close.")
    
    # Call the function we defined above to get the message interval
    # Assign the return value to a variable called interval_secs
    interval_secs: int = get_message_interval()

    for message in generate_messages():
        logger.info(message)
        # Use the time module to pause execution for a specified number of seconds
        # The time.sleep() function takes a single argument: the number of seconds to pause
        time.sleep(interval_secs)

    logger.info("NOTE: See the `logs` folder to learn more.")
    logger.info("END travel producer.....")


#####################################
# Conditional Execution
#####################################

# If this file is the one being executed, call the main() function
if __name__ == "__main__":
    # Call the main function by writing its name followed by parentheses.
    main()