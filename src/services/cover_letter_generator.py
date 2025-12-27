from src.services.gemini_client import get_gemini_client


COVER_LETTER_PROMPT = """You are writing a motivation letter for a job application. This is a formal letter addressed to the company (not a personal message to a hiring manager). Your goal is to sound like a human wrote this - not an AI.

CRITICAL RULES - AVOID THESE AI GIVEAWAYS:
1. NEVER use these words: delve, pivotal, embark, invaluable, relentless, groundbreaking, utilize, spearhead, crucial, revolutionize, pertinent, leverage, synergy, holistic, robust, streamline, foster, facilitate, enhance, innovative, dynamic, proactive
2. NEVER use em dashes (—) or en dashes (–). Use commas, periods, or rewrite the sentence instead
3. NEVER start with "I am writing to express my interest" or "I am excited to apply"
4. NEVER use phrases like: "proven track record", "detail-oriented professional", "I believe I would be a great fit", "passion for excellence", "hit the ground running", "think outside the box", "results-driven"
5. NEVER use overly complex or perfectly structured sentences. Real people write with some variation
6. NEVER be too polished or flawless. Include natural human touches
7. Keep it SHORT: 250-350 words maximum, 3 paragraphs
8. LANGUAGE: Write the letter in the SAME LANGUAGE as the job description. If the job posting is in German, write in German. If in French, write in French. Match the language exactly.

FORMAT:
- This is a motivation letter to the COMPANY, not a personal message to a hiring manager
- Start with a proper salutation. Use the ACTUAL company name from the job description (e.g., "Dear Google Team," or "Dear Spotify Hiring Team,"). If the company name is unclear, use "Dear Hiring Team,"
- NEVER use placeholders like "[Hiring Manager Name]", "[Company Name]", or any brackets. Extract the real company name from the job posting.
- The tone should be professional but personable, presenting yourself as a candidate to the organization

STRUCTURE:
1. Opening (2-3 sentences): Present your motivation for applying. WHY does this role at THIS company interest you? What specifically about the company's mission, product, or this position caught your attention?

2. Body (1 paragraph): Explain why you're a strong fit. Pick 1-2 relevant experiences from the CV that directly match what they're looking for. Show how your background aligns with their needs. Be specific with examples or outcomes when possible.

3. Closing (2-3 sentences): Summarize what you'd bring to the company and express your enthusiasm for the opportunity. End professionally.

TONE GUIDELINES:
- Write like a confident professional presenting themselves to a company
- Use contractions naturally (I'm, I've, it's, that's)
- Vary sentence length. Some short. Some a bit longer to explain things
- Show personality from the "About Me" section
- Be specific, not generic. Reference actual details from the job posting
- Sound ambitious but not arrogant

ABOUT THE CANDIDATE (their personality, background, motivations):
{about_me}

CANDIDATE'S CV/RESUME:
{cv_text}

JOB THEY'RE APPLYING FOR:
{job_description}

CANDIDATE'S PERSONAL NOTES ABOUT THIS JOB (use this context to make the letter more personal and authentic - incorporate naturally if provided):
{job_notes}

Write the motivation letter now. Output ONLY the letter text. No headers, no subject lines, no explanations."""


def generate_cover_letter(
    about_me: str,
    cv_text: str,
    job_description: str,
    job_notes: str = "",
    temperature: float = 0.7
) -> str:
    """
    Generate a cover letter using Gemini.

    Args:
        about_me: Text describing the candidate's background, motivations, character
        cv_text: Extracted text from the candidate's CV
        job_description: The job posting description
        job_notes: Optional personal notes about the job/company
        temperature: Controls creativity (0.0-1.0)

    Returns:
        Generated cover letter text
    """
    prompt = COVER_LETTER_PROMPT.format(
        about_me=about_me,
        cv_text=cv_text,
        job_description=job_description,
        job_notes=job_notes if job_notes else "No additional notes provided."
    )

    client = get_gemini_client()
    return client.generate(prompt, temperature=temperature)
