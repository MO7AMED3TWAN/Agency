# AI Content Agency

The AI Content Agency project automates the process of content generation, including research, extraction, creation, validation, and image generation. This repository is structured to ensure modularity and ease of use.

## Project Structure

```
/Agency
├── apis.py               # API keys and configurations
├── Main.ipynb            # Main notebook for experimentation
├── README.md             # Project overview and documentation
├── requirements.txt      # Project dependencies
├── RunAgents.ipynb       # Notebook to run all agents
├── src/                  # Source code
│   ├── __init__.py       # Makes src a package
│   ├── agents/           # Contains agent implementations
│   │   ├── __init__.py   # Makes agents a package
│   │   ├── Researcher.py # Researcher agent
│   │   ├── Extractor.py  # Extractor agent
│   │   ├── ContentCreator.py # Content Creator agent
│   │   ├── SEOValidator.py  # SEO Validator agent
│   │   ├── ImageGenerator.py # Image Generator agent
│   ├── tools/            # Contains tool implementations
│   │   ├── __init__.py   # Makes tools a package
│   │   ├── GoogleSearchTool.py # Google Search tool
│   │   ├── SerperTool.py      # Serper API tool
│   │   ├── BeautifulSoupTool.py # BeautifulSoup tool
│   │   ├── ReadabilityTool.py   # Readability tool
│   │   ├── StableDiffusionTool.py # Stable Diffusion tool
```

## How to Use

1. Clone the repository.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Add your API keys to `apis.py`.
4. Run the `RunAgents.ipynb` notebook to execute the pipeline.

## Features

- **Researcher**: Performs targeted searches using keywords.
- **Extractor**: Extracts and summarizes content from URLs.
- **Content Creator**: Generates SEO-optimized content.
- **SEO Validator**: Validates content for SEO compliance.
- **Image Generator**: Creates images based on descriptions.