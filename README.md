# Valorant Scoreboard Reader 🎮📊
Valorant Scoreboard Reader is an innovative OCR (Optical Character Recognition) application that processes in-game scoreboards from the popular first-person shooter, Valorant. With the power of Python, OpenCV, Tesseract, and the OpenAI GPT-3.5 API, we bring an entertaining and personalized experience to your gaming sessions! 🕹️🚀

## Features 🌟
* **OCR Integration:** Capture screenshots and extract player information using Tesseract OCR 🔍
* **Image Processing:** Enhance and manipulate images with OpenCV for improved OCR accuracy 🔧
* **GPT-3.5 API:** Generate personalized greetings and light-hearted jokes for each player using OpenAI's GPT-3.5 API 🤖📝
* **Regular Expressions:** Extract and process player names and statistics with Python regex 🧩
* **Environment Management:** Manage API keys and configurations using python-dotenv 🗝️🔐

## How to Install Dependencies 📦
Before running the project, make sure you have Python 3.6 or later installed on your system. Then, follow these steps to install the required libraries:

1. Clone the repository and navigate to the project folder:
```
git clone https://github.com/your_username/valorant-scoreboard-reader.git
cd valorant-scoreboard-reader
```
2. It is recommended to create a virtual environment to keep the project's dependencies isolated:
```
python -m venv venv
```
3. Activate the virtual environment:

* **Windows:**
```
venv\Scripts\activate
```

* **macOS/Linux:**
```
source venv/bin/activate
```
4. Install the required dependencies using pip:
```
pip install -r requirements.txt
```
Now you're ready to run the script and enjoy the features! Follow the instructions in the "How to Use" section of the README.

## How to Use 📘
1. Clone the repository and navigate to the project folder.
2. Install the required dependencies using pip install -r requirements.txt.
3. Set up a .env file in the project directory with your OpenAI API key:
```
OPENAI_API_KEY=your_api_key_here
```
4. Run the script using python scoreboard_reader.py.
5. Enjoy personalized greetings and jokes for you and your fellow players! 😄🎉
