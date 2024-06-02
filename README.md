# AI Agent Implementation Using Langchain, DuckDuckGo Search, and Wolfram Alpha API

This project demonstrates how to implement an AI agent using Langchain with integration of DuckDuckGo search and Wolfram Alpha API as tools. The AI agent is designed to answer general knowledge questions and solve mathematical problems.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Example Queries](#example-queries)
- [Acknowledgements](#acknowledgements)

## Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/da-ros/AgentLangchain.git
   cd AgentLangchain

2. **Create a virtual environment and activate it**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install the required packages**

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Set up environment variables**

   Create a `.env` file in the project root directory and add your OpenAI API key and Wolfram Alpha API key.

   ```
   OPENAI_API_KEY=your_openai_api_key
   WA_API_KEY=your_wolfram_alpha_api_key
   ```

2. **Run the application**

   ```bash
   python app.py
   ```

## Configuration

### Environment Variables

- `OPENAI_API_KEY`: Your OpenAI API key. You can obtain it from [OpenAI](https://beta.openai.com/signup/).
- `WA_API_KEY`: Your Wolfram Alpha API key. You can obtain it from [Wolfram Alpha](https://products.wolframalpha.com/api/).

## Example Queries

The agent can handle various types of queries. Below are some examples:

1. **General Information**

   ```python
   response = agent("What is lablab.ai?")
   print(f"Final answer: {response['output']}")
   ```

2. **Mathematical Problem Solving**

   ```python
   response = agent("Integral of x * (log(x)^2)")
   print(f"Final answer: {response['output']}")
   ```

## Acknowledgements

This project is based on the tutorial provided by [lablab.ai](https://lablab.ai/t/ai-agents-tutorial-how-to-use-and-create-them). It utilizes the following tools and libraries:

- [Langchain](https://github.com/hwchase17/langchain) for building language model chains.
- [DuckDuckGo](https://duckduckgo.com/) for web search functionality.
- [Wolfram Alpha](https://products.wolframalpha.com/api/) for solving complex mathematical problems.

For more details, please refer to the [tutorial](https://lablab.ai/t/ai-agents-tutorial-how-to-use-and-create-them).
