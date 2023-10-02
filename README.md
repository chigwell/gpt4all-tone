# GPT4ALL-Tone Analyzer

A comprehensive tool for sentiment analysis and tone review, empowered by GPT4ALL.

## Installation

Use the following command to install `gpt4all-tone`:

```bash
pip install gpt4all-tone
```

or

```bash
pip3 install gpt4all-tone
```

## Usage

You can use the `ToneAnalyzer` class to perform sentiment analysis on a given text. Here's a basic example of how you might use the `ToneAnalyzer` class:

```python
from gpt4all_tone import ToneAnalyzer

# Create an instance of the ToneAnalyzer class
analyzer = ToneAnalyzer("orca-mini-3b.ggmlv3.q4_0.bin", "Wow it is great!")

# Run the analyzer
result = analyzer.run()

# Print the result
print(result)  # 1.0
```

In this example, we're analyzing the text "Wow it is great!" and the result is `1.0`, indicating a positive sentiment.

## Command Line Interface

You can also use the `gpt4all-tone` command line interface to analyze text:

```bash
gpt4all_tone "Wow it is great!"
```

## Contact

- Author: [Evgenii Evstafev](https://www.linkedin.com/in/eugene-evstafev-716669181/)
- Email: [chigwel@gmail.com](mailto:chigwel@gmail.com)

## License

[MIT License](LICENSE)