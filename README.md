

# buzzline-01-gbogbo

This project introduces streaming data with a travel theme. 
The Python language includes generators - we'll use this feature to generate some streaming travel buzzline messages. 
As the code runs, it will continuously update the log file with travel experiences and discoveries. 
We'll use a consumer to monitor the log file and alert us when special travel messages are detected. 

## Task 1. Set Up Your Machine & Sign up for GitHub

We practice professional Python. In each course that uses Python, we use a standard set of popular professional tools. 
This course uses advanced tools such as Apache Kafka that requires **Python 3.11**. 
You are encouraged to install and practice with multiple versions. 
If space is an issue, we only need Python 3.11 for this course. 

Follow instructions at [pro-analytics-01](https://github.com/denisecase/pro-analytics-01), **Part 1: Set Up Machine & Sign up for GitHub**.

**Setup is critical.** Follow all steps exactly and verify success before proceeding.  
Missing or incomplete setup steps can make the course impossible to complete.

## Task 2. Initialize a Project

Once your machine is ready, you'll copy this template repository into your own GitHub account  
and create your personal version of the project to run and explore. 
Named **buzzline-01-gbogbo** with custom travel-themed streaming messages.  

Follow instructions at [pro-analytics-01](https://github.com/denisecase/pro-analytics-01), **Part 2: Initialize a Project**.
This will get your project stored safely in the cloud - and ready for work on your machine. 

## Task 3. Generate Streaming Travel Data (Terminal 1)

Now we'll generate some streaming travel data with custom messages about destinations, adventures, and experiences. 
By the way - you've done 90% of the hard work before we even look at code. 
Congratulations!

In VS Code, open a terminal.
Use the commands below to activate .venv, and run the travel-themed generator as a module. 
To learn more about why we run our Python file as a module, see [PYTHON-PKG-IMPORTS](docs/PYTHON-PKG-IMPORTS.md) 

Windows PowerShell:

```shell
# Activate the virtual environment
.venv\Scripts\activate
# Run the travel producer
py -m producers.basic_producer_gbogbo
```

Mac/Linux:
```zsh
# Activate the virtual environment
source .venv/bin/activate
# Run the travel producer
python3 -m producers.basic_producer_gbogbo
```

## Task 4. Monitor an Active Travel Log File (Terminal 2)

A common streaming task is monitoring a log file as it is being written. 
This project has a consumer that reads and processes our travel log file as messages about adventures arrive. 
The consumer includes special alerts for breathtaking experiences, hidden beach discoveries, and ancient temple visits.

In VS Code, open a NEW terminal in your root project folder. 
Use the commands below to activate .venv, and run the travel log consumer as a module. 

Windows:
```shell
# Activate the virtual environment
.venv\Scripts\activate
# Run the travel consumer
py -m consumers.basic_consumer_gbogbo
```

Mac/Linux:
```zsh
# Activate the virtual environment
source .venv/bin/activate
# Run the travel consumer
python3 -m consumers.basic_consumer_gbogbo
```

## Project Features

### Travel-Themed Producer (`basic_producer_gbogbo.py`)
- Generates streaming travel messages with destinations, adventures, and experiences
- Uses adjectives like: breathtaking, adventurous, peaceful, magical, unforgettable
- Actions include: visited, explored, discovered, hiked, photographed, climbed
- Destinations feature: hidden beaches, ancient temples, mountain peaks, historic castles

### Travel Log Consumer (`basic_consumer_gbogbo.py`)
- Monitors the log file in real-time as travel messages are written
- Special alerts for:
  - **Breathtaking experiences** - Highlights amazing travel moments
  - **Hidden beach discoveries** - Alerts when secret beaches are found
  - **Ancient temple visits** - Notifications for historical site explorations
- Processes messages continuously until stopped with Ctrl+C

### Sample Messages
The system generates messages like:
- "Travel update: Just explored a hidden beach and it was absolutely breathtaking!"
- "Can't believe I climbed a mountain peak today. Totally challenging!"
- "Latest adventure: wandered through an ancient temple. Pretty magical experience!"

## Save Space
To save disk space, you can delete the .venv folder when not actively working on this project.
We can always recreate it, activate it, and reinstall the necessary packages later. 
Managing Python virtual environments is a necessary and valuable skill. 
We will get a good amount of practice. 

