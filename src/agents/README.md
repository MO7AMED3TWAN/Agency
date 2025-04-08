# Agents

This folder contains the implementation of various agents used in the AI Content Agency project. Each agent is responsible for a specific task in the content generation pipeline.

## Agents List

1. **Researcher**
   - Performs targeted searches using provided keywords.
   - Tools: Google Search API, Serper API.

2. **Extractor**
   - Analyzes collected pages to extract core information.
   - Tools: BeautifulSoup, Readability-lxml.

3. **Content Creator**
   - Generates original, SEO-optimized content with image descriptions.
   - Tools: NextaX1.1.5B, Grammarly API.

4. **SEO Validator**
   - Verifies content meets search engine requirements.
   - Tools: Yoast SEO, Moz API.

5. **Image Generator**
   - Creates visuals based on content descriptions.
   - Tools: Stable Diffusion API, DALL-E.
