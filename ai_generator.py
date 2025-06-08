# Standard library imports
import os
from typing import Dict

# Third-party imports
# Note: Mistral import is commented out as it's not currently in use
# from mistralai import Mistral, UserMessage, SystemMessage
from openai import OpenAI
from dotenv import load_dotenv
import logging

# Configure logging with INFO level for detailed debugging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load environment variables from .env file
load_dotenv()

# Debug print to verify NVIDIA API key is loaded
print("NVIDIA_API_KEY loaded:", os.getenv("NVIDIA_API_KEY") is not None)

# Initialize OpenAI client configured for NVIDIA's API
# This client will be used to interact with NVIDIA's AI models
client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key=os.getenv("NVIDIA_API_KEY")
)

def generate_blog_post(keyword: str, seo_data: Dict[str, float]) -> str:
    """
    Generate a blog post using NVIDIA Models API based on the keyword and SEO data.
    
    This function takes a keyword and SEO metrics as input and generates a well-structured,
    SEO-optimized blog post using AI. The generated content follows specific guidelines
    for formatting, tone, and structure.
    
    Args:
        keyword (str): The main keyword/topic for the blog post
        seo_data (Dict[str, float]): Dictionary containing SEO metrics:
            - search_volume: Number of monthly searches
            - keyword_difficulty: Score indicating competition level
            - avg_cpc: Average cost per click in USD
        
    Returns:
        str: Generated blog post in HTML format with proper formatting and structure
        
    Raises:
        Exception: If there's an error during blog post generation
    """
    # Construct a detailed prompt that guides the AI in generating structured content
    prompt = f"""Write an engaging and educational blog post about {keyword} that's perfect for learners and general audiences.
    
    SEO Metrics:
    - Search Volume: {seo_data['search_volume']}
    - Keyword Difficulty: {seo_data['keyword_difficulty']}
    - Average CPC: ${seo_data['avg_cpc']}
    
    Content Requirements:
    ### 1. Title Creation 
    Create a accurate, meaningful, and compelling title that:
        - Excatly matches the content
        - Contains catchy and attention grabbing words
        - Appeals to beginners and general audiences but not too simple
        - Incorporates the main keyword naturally and is not too long or too short

    ### 2. Introduction (2 paragraphs, ~5 lines each)
        - Start with a relatable hook or question
        - Clearly explain what the topic is in simple terms
        - Highlight why this matters to everyday readers
        - Give readers a clear idea of what they'll gain from reading

    ### 3. Main Content Structure 
    Instead of rigid sections, create a natural flow that might include:
        - **Simple explanations** using analogies and real-world comparisons
        - **Practical examples** that readers can relate to
        - **Detailed explanations** of the topic
        - **Step-by-step breakdowns** when explaining processes
        - **Common misconceptions** addressed clearly
        - **Benefits and challenges** explained in plain language
        - **Current trends** and why they matter

    *Note: Organize content based on what makes most sense for the topic, not a predetermined structure*

    ### 4. Future Outlook
        - Discuss emerging trends in accessible language
        - Explain potential challenges or opportunities
        - Help readers understand what to watch for

    ### 5. Conclusion
        - Summarize key takeaways in simple bullet points
        - Provide actionable next steps for interested readers
        - Include an engaging call-to-action

    ### 6. Sources (3-5 reputable sources)
    Research and verify each source link before including:
        - **Source Title**: Brief description (replacing {{AFF_LINK_n}} placeholders with dummy URLs.)
        - Prioritize reputable, accessible sources
        - Ensure all links are functional and lead to relevant content
        - Don't use any affiliate links in the sources

    ## Writing Guidelines:

        **Tone & Style:**
        - Conversational yet informative
        - Use "you" to address readers directly
        - Explain technical terms when first introduced
        - Include helpful analogies for complex concepts
        - Ask rhetorical questions to engage readers

        **Formatting:**
        - Use proper Markdown formatting
        - Break up text with relevant subheadings
        - Include bullet points for easy scanning
        - Bold key terms and important points
        - Use italics for emphasis sparingly

        **Content Quality:**
        - Target 1000-1500 words for comprehensive coverage
        - Include relevant statistics with proper context
        - Add practical tips or actionable insights
        - Ensure accuracy and avoid speculation
        - Make content shareable and bookmark-worthy

    ## Special Instructions:
        - If the keyword is ambiguous, choose the most commonly searched interpretation
        - Focus on providing genuine value to readers
        - Prioritize clarity over complexity
        - Include at least 2-3 data points or statistics where relevant
        - End with something memorable or thought-provoking

    **Return only the finished blog post content in proper format. Do not include meta-commentary or instructions."""

    try:
        # Log the start of blog post generation
        logger.info(f"Generating blog post for keyword: {keyword}")
        
        # Prepare the message for the AI model
        messages = [{"role": "user", "content": prompt}]
        
        # Make API call to NVIDIA's AI model
        response = client.chat.completions.create(
            model="mistralai/mistral-medium-3-instruct",  # Using Mistral Medium model
            messages=messages,
            temperature=0.7,  # Controls randomness in output
            top_p=0.7,       # Controls diversity via nucleus sampling
            max_tokens=2048,  # Maximum length of generated content
            stream=False     # Get complete response at once
        )
        
        # Extract the generated content from the response
        blog_post = response.choices[0].message.content
        logger.info(f"Successfully generated blog post for keyword: {keyword}")
        
        # Replace placeholder affiliate links with dummy URLs
        # This ensures the blog post has working links while maintaining security
        blog_post = blog_post.replace("{{AFF_LINK_1}}", "https://verified-working-link.com")
        blog_post = blog_post.replace("{{AFF_LINK_2}}", "https://verified-working-link.com")
        blog_post = blog_post.replace("{{AFF_LINK_3}}", "https://verified-working-link.com")
        blog_post = blog_post.replace("{{AFF_LINK_4}}", "https://verified-working-link.com")
        blog_post = blog_post.replace("{{AFF_LINK_5}}", "https://verified-working-link.com")
        
        # Read the SEO template
        try:
            with open('seo_template.html', 'r', encoding='utf-8') as template_file:
                seo_template = template_file.read()
            
            # Format the SEO template with the actual data
            seo_section = seo_template.format(
                keyword=keyword,
                search_volume=f"{seo_data['search_volume']:,.0f}",
                keyword_difficulty=seo_data['keyword_difficulty'],
                avg_cpc=f"{seo_data['avg_cpc']:.2f}"
            )
            
            # Append SEO data to the blog post
            blog_post += "\n\n" + seo_section
            
        except Exception as e:
            logger.error(f"Error formatting SEO template: {str(e)}")
            # Fallback to simple text format if template fails
            seo_section = f"""
## SEO Performance Metrics

Keyword Analysis: {keyword}

- Search Volume: {seo_data['search_volume']:,.0f} monthly searches
- Keyword Difficulty: {seo_data['keyword_difficulty']}/100
- Average CPC: ${seo_data['avg_cpc']:.2f}

*This content has been optimized based on current SEO metrics for better search engine visibility and user engagement.*
"""
            blog_post += "\n\n" + seo_section
        
        return blog_post
        
    except Exception as e:
        # Log any errors that occur during generation
        logger.error(f"Error generating blog post: {str(e)}")
        raise Exception(f"Error generating blog post: {str(e)}")



