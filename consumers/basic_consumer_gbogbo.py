"""
basic_consumer_gbogbo.py

Consume and process streaming buzz messages. 
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
    return_value: str = os.getenv("MESSAGE_INTERVAL_SECONDS", 2)
    interval: int = int(return_value)
    logger.info(f"Messages will be processed every {interval} seconds.")
    return interval


#####################################
# Define global variables
#####################################

# Define some sample messages for simulation (in real scenario, these would come from a queue/stream)
SAMPLE_MESSAGES: list = [
    "I just visited a hidden beach! It was breathtaking.",
    "Travel update: Just explored an ancient temple and it was absolutely magical!",
    "Amazing day! I hiked a mountain peak - so challenging.",
    "Can't believe I discovered a local café today. Totally peaceful!",
    "Latest adventure: wandered through a traditional village. Pretty cultural experience!",
    "Just photographed a scenic viewpoint. Words can't describe how stunning it was!",
    "Update from the road: sailed to a secret waterfall - incredibly adventurous.",
    "Travel diary: Today I climbed a historic castle. Simply unforgettable!"
]

# Define response templates for processing messages
RESPONSE_TEMPLATES: list = [
    "Processing message: '{message}' - Status: Received",
    "Consumed: '{message}' - Action: Logged",
    "Message handled: '{message}' - Result: Success",
    "Incoming: '{message}' - Processing: Complete",
    "Received buzz: '{message}' - Status: Processed"
]

#####################################
# Define a function to simulate consuming messages
#####################################


def consume_messages():
    """
    Simulate consuming a stream of buzz messages.

    This function uses a generator to simulate consuming messages from a queue or stream.
    In a real-world scenario, this would connect to a message broker like RabbitMQ,
    Apache Kafka, or similar streaming platform.

    Because this function uses a while True loop, it will run continuously 
    until we close the window or hit CTRL c (CMD c on Mac/Linux).
    """
    while True:
        # Simulate receiving a message (in real scenario, this would come from a queue/stream)
        message = random.choice(SAMPLE_MESSAGES)
        response_template = random.choice(RESPONSE_TEMPLATES)
        
        # Process the message and yield a response
        processed_response = response_template.format(message=message)
        yield processed_response


#####################################
# Define message processing functions
#####################################


def process_message(message: str) -> dict:
    """
    Process an individual message and return metadata.
    
    Args:
        message (str): The message to process
        
    Returns:
        dict: Message metadata including word count, timestamp, etc.
    """
    word_count = len(message.split())
    char_count = len(message)
    
    # Simple sentiment analysis based on keywords
    positive_words = ["amazing", "breathtaking", "stunning", "magical", "unforgettable", "peaceful"]
    sentiment = "positive" if any(word in message.lower() for word in positive_words) else "neutral"
    
    return {
        "word_count": word_count,
        "char_count": char_count,
        "sentiment": sentiment,
        "timestamp": time.time()
    }


#####################################
# Define main() function to run this consumer.
#####################################


def main() -> None:
    """
    Main entry point for this consumer.

    It doesn't need any outside information, so the parentheses are empty.
    It doesn't return anything, so we say the return type is None.   
    The colon at the end of the function signature is required.
    All statements inside the function must be consistently indented. 
    This is a multiline docstring - a special type of comment 
    that explains what the function does.
    """

    logger.info("START consumer...")
    logger.info("Consuming and processing buzz messages...")
    logger.info("Hit CTRL c (or CMD c) to close.")
    
    # Call the function we defined above to get the message interval
    # Assign the return value to a variable called interval_secs
    interval_secs: int = get_message_interval()
    
    message_count = 0

    for consumer_response in consume_messages():
        message_count += 1
        logger.info(f"[Message #{message_count}] {consumer_response}")
        
        # Extract the original message for processing
        # This is a simple extraction - in real scenarios, message format would be structured
        if "'" in consumer_response:
            start_idx = consumer_response.find("'") + 1
            end_idx = consumer_response.rfind("'")
            if start_idx < end_idx:
                original_message = consumer_response[start_idx:end_idx]
                metadata = process_message(original_message)
                logger.info(f"Message metadata: {metadata}")
        
        # Use the time module to pause execution for a specified number of seconds
        # The time.sleep() function takes a single argument: the number of seconds to pause
        time.sleep(interval_secs)

    logger.info("NOTE: See the `logs` folder to learn more.")
    logger.info("END consumer.....")


#####################################
# Conditional Execution
#####################################

# If this file is the one being executed, call the main() function
if __name__ == "__main__":
    # Call the main function by writing its name followed by parentheses.
    main()