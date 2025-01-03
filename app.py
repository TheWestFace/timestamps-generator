from flask import Flask, render_template, request
from youtube_transcript_api import YouTubeTranscriptApi
import google.generativeai as genai
import os

app = Flask(__name__)

# Add your API Key for Gemini model
YOUR_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=YOUR_API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")


# Step 1: Extract Transcript
def get_transcript(video_id):
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        return transcript
    except Exception as e:
        print(f"Error fetching transcript: {e}")
        return []


# Generate highlights using the Gemini model
def generate_highlights(transcript_text):
    """
    Function to generate highlights
    """
    try:
        response = model.generate_content(
            f"Given the following transcript of a YouTube video, identify the key highlights that are most relevant to the main topic or theme of the video. Ensure that the highlights are very short, concise sentences that capture the core ideas. Make sure the highlights cover different, non-overlapping sections of the transcript, and that each highlight is associated with a distinct starting time. Provide the highlights in chronological order based on their timestamps in the video. Here's the transcript:\n{transcript_text}"
        )

        highlights = response.text.split("\n")
        highlight_dict = {}

        print(highlights, "\n")

        for highlight in highlights:
            if highlight.strip():
                try:
                    # Attempt to split by ":**"
                    time, text = highlight.split(":**", 1)
                    time = time.replace("*", "").strip()

                    # Clean up the time to remove any unwanted characters, keeping only numbers and colon
                    time = "".join(c for c in time if c.isdigit() or c == ":")

                    text = text.strip()  # Clean up the text
                    highlight_dict[time] = text  # Add to dictionary with time as key

                except ValueError:
                    # If split fails, print the problematic highlight for debugging
                    print(f"Skipping malformed highlight: {highlight}")

        return highlight_dict
    except Exception as e:
        print(f"Error generating highlights: {e}")
        return {}


@app.route("/", methods=["GET", "POST"])
def index():
    highlights = {}
    if request.method == "POST":
        url = request.form["url"]
        print("URL:", url)

        # Extract video ID from the URL
        video_id = url.replace("https://www.youtube.com/watch?v=", "")
        print("Video ID:", video_id)

        # Retrieve the transcript
        transcript = get_transcript(video_id)
        if transcript:
            # Combine transcript text for input to the model
            transcript_text = " ".join([entry["text"] for entry in transcript])

            # Generate the highlights
            highlights = generate_highlights(transcript_text)

    return render_template("index.html", highlights=highlights)


if __name__ == "__main__":
    app.run(debug=True)
