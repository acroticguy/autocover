# AutoCover

An AI-powered cover letter generator that creates personalized cover letters based on your profile and the job you're applying to. Built with Streamlit and Google's Gemini AI.

## Features

- **Profile Management**: Store your personal information, skills, and experience for reuse across multiple applications
- **CV/Resume Parsing**: Upload your CV as a PDF and automatically extract relevant information
- **Job Description Import**: Paste a job description or provide a LinkedIn URL to automatically parse job requirements
- **AI-Powered Generation**: Uses Google's Gemini AI to create tailored cover letters that match your experience to job requirements
- **Application Questions**: Get AI-generated answers to common application questions based on your profile

## Prerequisites

Before you begin, ensure you have:

- **Python 3.10 or higher** installed on your system
- **A Google Gemini API key** (free tier available)

### Getting a Gemini API Key

1. Go to [Google AI Studio](https://aistudio.google.com/apikey)
2. Sign in with your Google account
3. Click "Create API Key"
4. Copy the generated API key (you'll need this during setup)

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/autocover.git
cd autocover
```

### 2. Create a Virtual Environment

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the project root directory:

```bash
cp .env.example .env
```

Open the `.env` file and replace `your_api_key_here` with your actual Gemini API key:

```
GEMINI_API_KEY=your_actual_api_key_here
```

## Usage

### Starting the Application

With your virtual environment activated, run:

```bash
streamlit run app.py
```

The application will open in your default web browser at `http://localhost:8501`.

### Step 1: Set Up Your Profile

1. Click the **"Set up your profile"** button in the top-right corner
2. Fill in your personal information:
   - Name and contact details
   - Professional summary
   - Skills and experience
3. Optionally, upload your CV/Resume as a PDF to auto-populate fields
4. Save your profile

### Step 2: Add a Job Description

On the main page, you have two options:

**Option A: Paste Job Description**
- Copy the job description from any job posting
- Paste it into the text area

**Option B: LinkedIn URL**
- Paste a LinkedIn job posting URL
- The app will automatically scrape and parse the job details

### Step 3: Generate Your Cover Letter

1. After adding the job description, click **"Generate Cover Letter"**
2. Wait for the AI to analyze the job requirements and your profile
3. Review the generated cover letter
4. Copy or download the result

### Step 4: Answer Application Questions (Optional)

If the job application has additional questions:

1. Navigate to the Questions section
2. Enter the question text
3. Get AI-generated answers tailored to your profile and the specific job

## Project Structure

```
autocover/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── .env.example          # Environment variables template
├── .env                  # Your local environment variables (not tracked)
├── data/                 # Local data storage
│   └── profiles/         # Saved user profiles
└── src/
    ├── components/       # Streamlit UI components
    │   ├── main_page.py
    │   ├── profile_page.py
    │   ├── cover_letter.py
    │   └── questions_page.py
    ├── services/         # Business logic
    │   ├── gemini_client.py
    │   ├── cover_letter_generator.py
    │   ├── linkedin_scraper.py
    │   └── pdf_extractor.py
    └── storage/          # Data persistence
        ├── models.py
        └── profile_manager.py
```

## Troubleshooting

### "API key not configured" error
- Make sure you've created a `.env` file with your Gemini API key
- Verify the API key is correct and has no extra spaces
- Restart the Streamlit application after updating the `.env` file

### LinkedIn scraping not working
- Some LinkedIn job postings may require authentication
- Try copying and pasting the job description directly instead

### Virtual environment issues
- Make sure you've activated the virtual environment before running commands
- On Windows, you may need to run `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser` in PowerShell first

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the [MIT License](LICENSE).

## Disclaimer

This tool is meant to assist in writing cover letters, not replace thoughtful application preparation. Always review and personalize the generated content before submitting job applications.
