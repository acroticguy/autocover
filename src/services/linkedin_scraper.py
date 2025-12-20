import re
import requests
from bs4 import BeautifulSoup
from typing import Tuple, Optional


def extract_job_id(url: str) -> Optional[str]:
    """Extract job ID from LinkedIn URL."""
    # Pattern: https://www.linkedin.com/jobs/view/XXXXXXXXXX
    match = re.search(r"/jobs/view/(\d+)", url)
    if match:
        return match.group(1)
    return None


def fetch_job_description(url: str) -> Tuple[str, bool]:
    """
    Fetch job description from LinkedIn using the Guest API.

    Args:
        url: LinkedIn job URL (e.g., https://www.linkedin.com/jobs/view/XXXXXXXXXX)

    Returns:
        Tuple of (job_description, success)
    """
    job_id = extract_job_id(url)
    if not job_id:
        return "Invalid LinkedIn job URL. Expected format: https://www.linkedin.com/jobs/view/[job_id]", False

    api_url = f"https://www.linkedin.com/jobs-guest/jobs/api/jobPosting/{job_id}"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
    }

    try:
        response = requests.get(api_url, headers=headers, timeout=15)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        # Find the job description div
        description_div = soup.find("div", class_="show-more-less-html__markup")

        if description_div:
            # Get text content, preserving some structure
            job_description = description_div.get_text(separator="\n", strip=True)
            return job_description, True
        else:
            return "Could not find job description in the response.", False

    except requests.exceptions.Timeout:
        return "Request timed out. Please try again.", False
    except requests.exceptions.RequestException as e:
        return f"Failed to fetch job posting: {str(e)}", False
