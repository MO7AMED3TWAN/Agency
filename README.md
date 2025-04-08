# AI Content Agency

## Agents

### 1. Researcher
- **Role**: Performs targeted searches using provided keywords
- **Description**: 
  - Receives exact keywords from user input
  - Searches Google and other approved sources
  - Filters results by relevance and recency
  - Returns clean list of URLs with metadata
- **Tools**: Google Search API, Serper API

### 2. Extractor
- **Role**: Analyzes collected pages to extract core information
- **Description**:
  - Visits each URL from Researcher
  - Identifies and extracts main content
  - Detects primary keywords and key phrases
  - Creates standardized summaries
  - Removes duplicate information
- **Tools**: BeautifulSoup, Readability-lxml

### 3. Content Creator
- **Role**: Generates original, SEO-optimized content with image description
- **Description**:
  - Takes extracted summaries as input
  - Produces completely original content
  - Ensures logical flow and accuracy
  - Optimizes for search engines
  - Creates detailed image description
  - Maintains consistent tone
- **Tools**: NextaX1.1.5B, Grammarly API

### 4. SEO Validator
- **Role**: Verifies content meets search engine requirements
- **Description**:
  - Checks keyword usage and density
  - Verifies proper heading structure
  - Ensures mobile-friendliness
  - Validates readability score
  - Confirms meta elements
  - Flags any potential issues
- **Tools**: Yoast SEO, Moz API

### 5. Image Generator
- **Role**: Creates visuals based on content descriptions
- **Description**:
  - Receives detailed image description
  - Generates multiple style options
  - Ensures proper dimensions
  - Maintains brand consistency
  - Optimizes file size
  - Delivers in required formats
- **Tools**: Stable Diffusion API, DALL-E

## Workflow

```mermaid
flowchart LR
    A[Researcher] --> B[Extractor]
    B --> C[Content Creator]
    C --> D[SEO Validator]
    D --> E[Image Generator]