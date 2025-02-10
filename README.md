# Chat-PDF

**Chat-PDF** is a Python application that enables users to interact with PDF documents using Google's Gemini AI model. Users can interact with PDF file and ask questions about its content, receiving intelligent responses.

## Features

- Upload and chat with PDF documents.
- Utilizes **Google Gemini AI** for natural language understanding.
- Secure API key storage using environment variables.

## Setup Instructions

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/nipulrathod/Chat-PDF.git
   cd Chat-PDF
   ```

2. **Install Dependencies:**
   Ensure you have Python installed. Install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up Environment Variables:**
   - Create a `.env` file in the root directory.
   - Add your API key:
     ```plaintext
     GEMINI_API_KEY=your_api_key_here
     ```
     Replace `your_api_key_here` with your actual Google Gemini API key.

4. **Run the Application:**
   ```bash
   python main.py
   ```
