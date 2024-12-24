# YouTube Timestamps Generator

A web-based tool to generate highlights from YouTube videos by extracting key timestamps and their descriptions. This project allows users to enter a YouTube video URL and get timestamps with short descriptions of important moments in the video.

## Features

- **Generate Highlights:** Input a YouTube video URL and generate a list of highlights with timestamps.
- **Copy Highlights:** Easily copy the generated highlights to your clipboard.
- **Responsive Design:** The app is designed to work well on both desktop and mobile devices.

![Image Alt](https://github.com/TheWestFace/timestamps-generator/blob/main/screenshot.png)

## Technologies Used

- **Python (Flask):** The backend is built using Flask to handle the web server and API requests.
- **HTML/CSS:** The frontend is built with HTML and CSS to provide a simple, user-friendly interface.
- **JavaScript:** Used for dynamic functionality, such as copying the highlights to the clipboard.

## Installation

### Clone the Repository

Clone this repository to your local machine:

```bash
git clone https://github.com/TheWestFace/youtube-timestamp-generator.git
```

### Set Up the Environment

1. Navigate to the project directory:

   ```bash
   cd youtube-timestamp-generator
   ```

2. Set Up a virtual environment (optional, but recommended)

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the app (ensure the virtual environment is activated if used)

   ```bash
   python app.py
   ```
