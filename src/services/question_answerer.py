from src.services.gemini_client import get_gemini_client


QUESTION_ANSWER_PROMPT = """You are helping a job candidate answer a recruiter's question. Your goal is to craft a natural, authentic response that sounds human.

CRITICAL RULES - AVOID THESE AI GIVEAWAYS:
1. NEVER use these words: delve, pivotal, embark, invaluable, relentless, groundbreaking, utilize, spearhead, crucial, revolutionize, pertinent, leverage, synergy, holistic, robust, streamline, foster, facilitate, enhance, innovative, dynamic, proactive
2. NEVER use em dashes (--) or en dashes (-). Use commas, periods, or rewrite the sentence instead
3. NEVER be overly formal or perfectly structured. Real people speak naturally
4. Keep responses conversational but professional
5. Be specific, reference actual experiences from the CV when relevant
6. Show personality from the About Me section
7. LANGUAGE: Write your answer in the SAME LANGUAGE as the job description. If the job posting is in German, answer in German. If in French, answer in French. Match the language exactly.

THE QUESTION:
{question}

ABOUT THE CANDIDATE (personality, background, motivations):
{about_me}

CANDIDATE'S CV/RESUME:
{cv_text}

JOB THEY'RE APPLYING FOR:
{job_description}

CANDIDATE'S PERSONAL NOTES ABOUT THIS JOB (use this context to make answers more personal and authentic - incorporate naturally if provided):
{job_notes}

GUIDELINES:
- Answer the specific question asked
- Use concrete examples from the CV when relevant
- Keep it concise (2-4 paragraphs typically)
- Sound confident but genuine
- Match the formality level of the question
- If the question asks about motivation/interest in the company, reference specific things from the job posting and the candidate's personal notes

Write the answer now. Output ONLY the answer text, no explanations or metadata."""


def generate_answer(
    question: str,
    about_me: str,
    cv_text: str,
    job_description: str,
    job_notes: str = "",
    temperature: float = 0.7
) -> str:
    """
    Generate an answer to a recruiter question.

    Args:
        question: The recruiter's question
        about_me: Candidate's background and motivations
        cv_text: Candidate's CV content
        job_description: The job posting description
        job_notes: Optional personal notes about the job/company
        temperature: Creativity level

    Returns:
        Generated answer text
    """
    prompt = QUESTION_ANSWER_PROMPT.format(
        question=question,
        about_me=about_me,
        cv_text=cv_text,
        job_description=job_description,
        job_notes=job_notes if job_notes else "No additional notes provided."
    )

    client = get_gemini_client()
    return client.generate(prompt, temperature=temperature)
