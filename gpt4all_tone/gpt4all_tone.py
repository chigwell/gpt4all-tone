import os
import re
import json
import argparse
from gpt4all import GPT4All

DEFAULT_MODEL_NAME = "orca-mini-3b.ggmlv3.q4_0.bin"
DEFAULT_CHAR_LIMIT = 2000

class ToneAnalyzer:
    def __init__(self, model_name, input, char_limit=DEFAULT_CHAR_LIMIT):
        self.model_name = model_name
        self.input = input
        self.model = GPT4All(model_name)
        self.char_limit = char_limit
        self.SYSTEM_TEMPLATE = 'Please respond with a numerical value indicating the sentiment of the following text: use 1 for positive tone, 0 for negative, 0.5 for neutral, 0.75 for more positive, or 0.25 for more negative.'
        self.prompt_template = 'Evaluate the tone of the following text: "{input}". Respond with "1" for positive, "0" for negative, "0.5" for neutral, "0.75" for more positive, or "0.25" for more negative.'

    def get_prompt_char_count(self):
        prompt_without_input = self.prompt_template.replace("{input}", "")
        return len(prompt_without_input)

    def analyze_chunk(self, chunk):
        prompt = self.prompt_template.replace("{input}", chunk)
        res = self.model.generate(prompt=prompt, max_tokens=50, temp=0.3)
        if 'positive' in res:
            if 'more positive' in res:
                return "0.75"
            else:
                return "1"
        elif 'negative' in res:
            if 'more negative' in res:
                return "0.25"
            else:
                return "0"
        elif 'neutral' in res:
            return "0.5"

        match = re.search(r"\b(1|0|0\.5|0\.75|0\.25)\b", res)
        if match:
            return match.group(1)
        else:
            return "-1"

    def run(self):
        prompt_char_count = self.get_prompt_char_count()
        input_char_limit = self.char_limit - prompt_char_count  # Use the instance variable char_limit
        chunks = [self.input[i:i+input_char_limit] for i in range(0, len(self.input), input_char_limit)]

        scores = []
        with self.model.chat_session(self.SYSTEM_TEMPLATE):
            for chunk in chunks:
                score = self.analyze_chunk(chunk)
                if score.startswith("-1"):
                    print(f"Error analyzing chunk: {chunk}")
                else:
                    scores.append(float(score))
        if scores:
            average_score = sum(scores) / len(scores)
            return str(average_score)
        else:
            return "Error: No scores obtained"

def parse_arguments():
    parser = argparse.ArgumentParser(description="gpt4all_tone")
    parser.add_argument("--model", help="Specifies the model name. Default is orca-mini-3b.ggmlv3.q4_0.bin", default=DEFAULT_MODEL_NAME)
    parser.add_argument("--char-limit", type=int, help=f"Specifies the character limit for the prompt. Default is {DEFAULT_CHAR_LIMIT}", default=DEFAULT_CHAR_LIMIT)
    parser.add_argument("input", help="Specifies the input text to analyze.")
    return parser.parse_args()

def main():
    args = parse_arguments()
    analyzer = ToneAnalyzer(args.model, args.input)
    result = analyzer.run()
    print(result)

if __name__ == "__main__":
    main()