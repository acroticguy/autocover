from google import genai
from google.genai import types
from tenacity import retry, stop_after_attempt, wait_exponential
from typing import Optional

from src.config import GEMINI_API_KEY, GEMINI_MODEL


class GeminiClient:
    """Wrapper for the Gemini API."""

    def __init__(self):
        self.client = genai.Client(api_key=GEMINI_API_KEY)
        self.model = GEMINI_MODEL

    @retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=1, min=2, max=10)
    )
    def generate(self, prompt: str, temperature: float = 0.7) -> str:
        """
        Generate text using Gemini.

        Args:
            prompt: The prompt to send to the model
            temperature: Controls creativity (0.0 = conservative, 1.0 = creative)

        Returns:
            Generated text response
        """
        response = self.client.models.generate_content(
            model=self.model,
            contents=prompt,
            config=types.GenerateContentConfig(
                temperature=temperature,
                max_output_tokens=2000,
            )
        )
        return response.text


# Singleton instance
_client: Optional[GeminiClient] = None


def get_gemini_client() -> GeminiClient:
    """Get or create the Gemini client instance."""
    global _client
    if _client is None:
        _client = GeminiClient()
    return _client
