import openai
import os
from random import choice
import cv2
import numpy as np
import pytesseract
from PIL import ImageGrab
from PIL import Image
from pynput import keyboard
import re
from dotenv import load_dotenv

load_dotenv()

# Set up pytesseract executable path (if necessary)
#pytesseract.pytesseract.tesseract_cmd = r"/usr/local/Cellar/tesseract/4.1.1/bin/tesseract"  # Change this to your Tesseract OCR path
openai.api_key = os.environ["OPENAI_API_KEY"]

# Define the function to capture a screenshot when the "Tab" key is pressed
def capture_screenshot_on_tab():
    screenshot_container = [None]

    def on_press(key):
        if key == keyboard.Key.tab:
            screenshot_container[0] = np.array(ImageGrab.grab())
            screenshot_img = Image.fromarray(screenshot_container[0])
            screenshot_img.save("screenshot.png")  # Save the screenshot as a PNG file
            return False  # Stop the listener

    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

    return screenshot_container[0]

# Define the function to process the scoreboard screenshot
def process_scoreboard(screenshot):
    # Convert the screenshot to grayscale
    gray_screenshot = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)
    # print("Gray Screenshot Resolution:", gray_screenshot.shape)
    # Define the region of interest (ROI) for the scoreboard
    # (You may need to adjust these values based on your screen resolution)
    _, thresh_screenshot = cv2.threshold(gray_screenshot, 127, 255, cv2.THRESH_BINARY)
    
    roi = thresh_screenshot[600:1200, 950:1240]
    cv2.imwrite("roi.png", roi)

    # Use pytesseract to recognize player information
    custom_config = r"--oem 3 --psm 6"
    raw_data = pytesseract.image_to_string(roi, config=custom_config).split("\n")

    # Process raw data into dictionaries
    player_data = []
    # print(raw_data)
        # Define a function to clean up the numerical values
    def clean_number(value):
        cleaned_value = re.sub(r"[^0-9]", "", value)
        return cleaned_value

    name_pattern = re.compile(r"^\w+")

    player_data = []
    player_count = 0

    for row in raw_data:
        # Search for the name in the row using regex
        name_match = name_pattern.search(row)

        # If a name is found, add it to the player_data
        if name_match:
            player_name = name_match.group()
            player_dict = {"name": player_name}
            player_data.append(player_dict)
            player_count += 1

            # Break the loop once all 10 player names are collected
            if player_count == 10:
                break

    return player_data

def generate_greeting(player_names):
    start_chat_log = 'Greet all these players by name, in a 500 character paragraph. I am kAreN. Add a good valorant joke. be cheaky. The player names are: '
    for name in player_names:
        start_chat_log += f'\n- {name}'

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=start_chat_log,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.8,
    )

    message = response.choices[0].text.strip()
    return message
# Main loop
if __name__ == "__main__":
    while True:
        # Capture a screenshot when the "Tab" key is pressed
        screenshot = capture_screenshot_on_tab()

        # Process the scoreboard screenshot
        player_data = process_scoreboard(screenshot)

        # Print player data
        player_names = [player["name"] for player in player_data]

        # Generate a greeting with a bad joke for all player names
        greeting = generate_greeting(player_names)
        print(greeting)