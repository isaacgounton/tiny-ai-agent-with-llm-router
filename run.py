"""
Example Usage of Content Tweet Generator

This script demonstrates how to use the Content Tweet Generator
with different source types (YouTube, blog, or text).
"""

import asyncio
from SimplerLLM.language.llm import LLM, LLMProvider
from agent_functions import main as generate_tweets_main, SourceType

OPEN_AI_API_KEY = "sk-proj-XXX" # Replace with your actual API key





async def run_example():
    """
    Run examples of the Content Tweet Generator with different source types.
    """
    # Initialize LLM instance
    # In a real application, you would configure this with your API key and model
    llm_instance = LLM.create(
        provider=LLMProvider.OPENAI,  
        model_name="gpt-4o", 
        api_key=OPEN_AI_API_KEY  
    )
    
    # Path to the LLM profile text file
    llm_profile_path = "llm_profile.txt"
    
    # Example 1: Generate tweets from YouTube content
    print("\n=== EXAMPLE 1: YOUTUBE CONTENT ===\n")
    youtube_url = "https://www.youtube.com/shorts/rz-z3nIqvsw"  # Replace with your YouTube URL
    await generate_tweets_main(SourceType.YOUTUBE, youtube_url, llm_profile_path, llm_instance)
    
    # Example 2: Generate tweets from Blog content
    # print("\n=== EXAMPLE 2: BLOG CONTENT ===\n")
    # blog_url = "https://example.com/blog-post"  # Replace with a real blog URL
    # await generate_tweets_main(SourceType.BLOG, blog_url, llm_profile_path, llm_instance)
    
    # Example 3: Generate tweets from Text content
    # print("\n=== EXAMPLE 3: TEXT CONTENT ===\n")
    # text_content = """
    # Artificial intelligence is transforming how we work and live. It's important to understand 
    # both the benefits and challenges of this technology. AI can automate repetitive tasks, 
    # analyze vast amounts of data, and provide insights that humans might miss. However, it 
    # also raises concerns about privacy, bias, and job displacement.
    # """
    # await generate_tweets_main(SourceType.TEXT, text_content, llm_profile_path, llm_instance)



if __name__ == "__main__":
    # Run the examples
    asyncio.run(run_example())
