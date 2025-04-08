# AI Content Generation Pipeline

## Flowchart Overview
```mermaid
flowchart TD
    A[Trend Searcher\n<Google Trends/SerpAPI>] --> B[Trend Summarizer\n<Extract Key Points>]
    B --> C[Content Creator\n<NextaX1.1.5B>]
    C --> D[SEO Validator\n<Yoast/SEMrush Check>]
    D --> E[Image Prompt Generator\n<DALL-E/MidJourney Specs>]
    E --> F[Publisher\n<WordPress/Social APIs>]
    style A fill:#ff6b6b,stroke:#333
    style B fill:#feca57,stroke:#333
    style C fill:#5f27cd,stroke:#333,color:white
    style D fill:#1dd1a1,stroke:#333
    style E fill:#ff9ff3,stroke:#333
    style F fill:#54a0ff,stroke:#333,color:white
```

---

## Agent Specifications

### 1. Trend Searcher
- **Purpose**: Identify trending topics
- **Tools**: 
  ```python
  # Example API Call
  pytrends = GoogleTrends(geo='EG')  # Egypt-focused trends
  trends = pytrends.daily_searches()
  ```
- **Output**: List of 5 trending keywords with search volumes

### 2. Trend Summarizer
- **Input**: Raw trend data
- **Processing**:
  ```python
  def summarize(trend_data):
      return NextaX.generate(
          f"Summarize in 3 bullet points:\n{trend_data}",
          max_length=150
      )
  ```
- **Output**: Key insights (Markdown formatted)

### 3. Content Creator (NextaX)
- **Prompt Template**:
  ```text
  "Create {content_type} about {trend}:
  - Tone: {professional/casual}
  - Length: {300 words}
  - SEO Keywords: {kw1, kw2}
  - Include: Call-to-action"
  ```
- **Output**: Blog post/social media content

### 4. SEO Validator
- **Checks**:
  - ✅ Keyword density (2-3%)
  - ✅ Readability score (>80)
  - ✅ Meta description length (50-160 chars)
- **Tools**: 
  ```bash
  python -m seo_analyzer --text "content.txt" --lang ar
  ```

### 5. Image Prompt Generator


### 6. Publisher

