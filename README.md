# Tuna-ASyncio

Tuna-ASyncio is a Python project that generates questions and sarcastic answers based on provided text chunks using the OpenAI API. It utilizes asyncio for asynchronous processing and implements rate limiting mechanisms to ensure compliance with API usage limits.

## Features

- Generates a specified number of questions and sarcastic answers from text chunks
- Supports custom prompts and response formats for the OpenAI API
- Implements token bucket algorithm for rate limiting
- Uses asyncio for efficient asynchronous processing
- Handles API request retries and backoff mechanisms
- Outputs the generated questions and answers to a CSV file

## Prerequisites

- Python 3.7 or higher
- OpenAI API key (set as an environment variable `OPENAI_API_KEY`)

## Installation

1. Clone the repository:

```bash
git clone https://github.com/cypheroxide/Tuna-ASyncio.git
```

2. Navigate to the project directory:

```bash
cd Tuna-ASyncio
```

3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

1. Prepare a CSV file containing text chunks with the following columns: `ChunkIDs`, `ChunkTexts`.

2. Run the `main.py` script with the path to your CSV file as an argument:

```bash
python main.py chunks.csv
```

This will generate an `output.csv` file containing the questions, answers, and related information.

## Customization

You can customize various aspects of the question and answer generation process by modifying the following variables in `main.py`:

- `custom_system_message`: The system message for the OpenAI API prompt.
- `custom_json_format`: The desired format for the response JSON.
- `num_triplets`: The number of questions and answers to generate.
- `custom_prompt_prefix`: The custom prefix for the OpenAI API prompt.
- `model_choice`: The OpenAI model to be used.
- `num_chunks`: The number of text chunks to consider for generating questions and answers.

## Project Structure

- `main.py`: The main script that orchestrates the question and answer generation process.
- `format.py`: A utility script for converting a DataFrame to a JSONL format.
- `chunks.csv`: A sample input CSV file containing text chunks.
- `output.csv`: The output file containing the generated questions and answers (created after running `main.py`).
- `poetry.lock` and `pyproject.toml`: Files used for dependency management with Poetry.

## Contributing

Contributions are welcome! If you have any ideas, suggestions, or bug reports, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

This project makes use of the following libraries:

- [OpenAI API](https://openai.com/api/)
- [aiohttp](https://docs.aiohttp.org/en/stable/)
- [pandas](https://pandas.pydata.org/)
- [tqdm](https://github.com/tqdm/tqdm)
