import unittest
from unittest.mock import patch, MagicMock
from apim import GeminiAI

class TestGeminiAI(unittest.TestCase):
    def setUp(self):
        self.test_prompt = "What is Python?"
        
    @patch('google.generativeai.GenerativeModel')
    def test_azure_response_success(self, mock_genai):
        # Arrange
        mock_response = MagicMock()
        mock_response.status_code = 200
        
        mock_model = MagicMock()
        mock_model.generate_content.return_value = mock_response
        mock_genai.return_value = mock_model

        # Act
        ai = GeminiAI('gemini-1.5-flash', use_azure=True)
        response = ai.generate_response(self.test_prompt)

        # Assert
        self.assertEqual(mock_response.status_code, 200)

    @patch('google.generativeai.GenerativeModel')
    def test_non_azure_response_success(self, mock_genai):
        # Arrange
        mock_response = MagicMock()
        mock_response.status_code = 200
        
        mock_model = MagicMock()
        mock_model.generate_content.return_value = mock_response
        mock_genai.return_value = mock_model

        # Act
        ai = GeminiAI('gemini-1.5-flash', use_azure=False)
        response = ai.generate_response(self.test_prompt)

        # Assert
        self.assertEqual(mock_response.status_code, 200)

if __name__ == '__main__':
    unittest.main()