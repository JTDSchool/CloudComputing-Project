import torch
from transformers import T5ForConditionalGeneration, T5Tokenizer


class Summarizer:
    def __init__(self, model_path, model_file, tokenizer_path):
        """Initializes the Summarizer class with model and tokenizer paths."""
        self.model_path = model_path
        self.model_file = model_file
        self.tokenizer_path = tokenizer_path
        self.model, self.tokenizer = self.load_model_and_tokenizer()

    def load_tokenizer(self):
        """Loads a T5 tokenizer from the provided path."""
        tokenizer = T5Tokenizer.from_pretrained(self.tokenizer_path)
        return tokenizer

    def load_model_and_tokenizer(self):
        """Loads PyTorch model and T5 tokenizer from local paths."""
        tokenizer = self.load_tokenizer()
        model = T5ForConditionalGeneration.from_pretrained("t5-small")
        model.load_state_dict(
            torch.load(self.model_file, map_location=torch.device("cpu"))
        )
        return model, tokenizer

    def generate_summary(self, text):
        """Generates summary for given text using loaded model and tokenizer."""
        inputs = self.tokenizer.encode(
            "summarize: " + text, return_tensors="pt", max_length=512, truncation=True
        )
        summary_ids = self.model.generate(
            inputs,
            max_length=150,
            min_length=40,
            length_penalty=2.0,
            num_beams=4,
            early_stopping=True,
        )
        summary = self.tokenizer.decode(summary_ids[0], skip_special_tokens=True)
        return summary

    def call_model(self, text):
        """Generates summary for the given text using pre-trained model and tokenizer."""
        summary = self.generate_summary(text)
        return summary
