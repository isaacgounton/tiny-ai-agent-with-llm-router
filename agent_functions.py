"""
Content Tweet Generator Script

This script demonstrates how to generate engaging tweets for X (formerly Twitter)
based on content from different sources (YouTube, blog, or text),
using templates and an LLM profile.

The script follows this flow:
1. Extract content from the source (YouTube, blog, or text)
2. Select the best templates using LLMRouter
3. Generate 3 tweets based on the content, templates, and LLM profile
"""

# Import necessary libraries
import re
import requests
from typing import List
from enum import Enum
from pydantic import BaseModel
from bs4 import BeautifulSoup

# Import SimplerLLM libraries
from SimplerLLM.language.llm_addons import generate_pydantic_json_model_async
from SimplerLLM.language.llm_router import LLMRouter

from templates import get_template_choices


SEARCH_IO_API_KEY = "XXX" # Replace with your actual API key



# Define source types
class SourceType(str, Enum):
    """
    Enum for different types of content sources.
    - YOUTUBE: Content from a YouTube video (will extract transcript)
    - BLOG: Content from a blog post (will scrape paragraphs)
    - TEXT: Direct text input
    """
    YOUTUBE = "youtube"
    BLOG = "blog"
    TEXT = "text"

# Define the tweet output model using Pydantic
class TweetOutput(BaseModel):
    """
    Pydantic model for generated tweets output.
    - tweets: List of generated tweets
    """
    tweets: List[str]


async def get_youtube_transcript(video_id: str) -> str:
    """
    Get the transcript of a YouTube video using searchapi.io.
    
    Parameters:
    - video_id: YouTube video ID
    
    Returns:
    - Video transcript as a string
    """
    # API endpoint and parameters
    api_url = "https://searchapi.io/api/v1/search"
    params = {
        "api_key": SEARCH_IO_API_KEY,  # Replace with your actual API key
        "engine": "youtube_transcripts",
        "video_id": video_id
    }

    try:
        # Make the API request
        response = requests.get(api_url, params=params)
        response.raise_for_status()  # Raise an exception for bad status codes

        # Parse the JSON response
        data = response.json()

        # Check if transcript is available
        if "transcripts" not in data or not data["transcripts"]:
            raise Exception("Transcript not available for this video")

        # Join sentences with a space, adding a period at the end of each sentence if needed
        transcript_text = " ".join(
            [line["text"].strip() + "." if not line["text"].strip().endswith('.') else line["text"].strip()
             for line in data["transcripts"]]
        )

        return transcript_text

    except Exception as e:
        # For simplicity, we'll return a placeholder in case of error
        print(f"Error getting transcript: {e}")
        return "Failed to get transcript. Please check the video ID and try again."

async def extract_content(source_type: SourceType, content: str) -> str:
    """
    Extract content from different sources.
    
    Parameters:
    - source_type: Type of content source (YouTube, blog, or text)
    - content: The content identifier (URL or text)
    
    Returns:
    - Extracted content as a string
    """
    # Case 1: If source is YouTube, extract the transcript
    if source_type == SourceType.YOUTUBE:
        # Extract the video ID from the YouTube URL
        match = re.search(r"(?:youtube\.com/watch\?v=|youtu\.be/|youtube\.com/shorts/)([\w-]+)", content)
        if not match:
            raise ValueError("Invalid YouTube URL format")
        
        video_id = match.group(1)
        # Get the transcript using the video ID
        transcript = await get_youtube_transcript(video_id)
        return transcript
    
    # Case 2: If source is a blog, scrape the paragraphs
    elif source_type == SourceType.BLOG:
        # Make a request to the blog URL
        response = requests.get(content)
        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')
        # Extract all paragraphs and join them
        return " ".join([p.text for p in soup.find_all('p')])
    
    # Case 3: If source is direct text, return it as is
    elif source_type == SourceType.TEXT:
        return content
    
    # Default case: If source type is not recognized, return the content as is
    return content

def select_best_templates(content: str, llm_instance) -> List[dict]:
    """
    Select the best templates for the given content using LLMRouter.
    
    Parameters:
    - content: The content to generate tweets from
    - llm_instance: The language model instance
    
    Returns:
    - List of selected templates with their metadata
    """
    # Create a new LLMRouter instance
    router = LLMRouter(llm_instance=llm_instance)
    
    # Add template choices to the router
    router.add_choices(get_template_choices())
    
    # Create a prompt that instructs the LLM to select appropriate templates
    selection_prompt = f"""
    Please analyze the following content and select the most appropriate tweet templates that would work well for creating engaging tweets about this topic:

    CONTENT:
    {content}

    Select templates that:
    1. Match the tone and subject matter of the content
    2. Would help highlight the key points effectively
    3. Would resonate with the target audience for this topic
    """

    # Get the best 3 templates using the router
    top_templates = router.route_top_k_with_metadata(
        selection_prompt,  # Using the instructional prompt
        k=3,  # Select top 3 templates
        metadata_filter={}  # No filtering
    )

    # Extract the selected templates with their metadata
    selected_templates = []
    for result in top_templates:
        template_index = result.selected_index
        template_content, template_metadata = router.get_choice(template_index)
        selected_templates.append({
            "template": template_content,
            "metadata": template_metadata
        })
    
    return selected_templates

def read_llm_profile(profile_path: str) -> str:
    """
    Read the LLM profile from a text file.
    
    Parameters:
    - profile_path: Path to the LLM profile text file
    
    Returns:
    - LLM profile as a string
    """
    try:
        with open(profile_path, 'r') as file:
            return file.read()
    except Exception as e:
        print(f"Error reading LLM profile: {e}")
        return "No profile available."

async def generate_tweets(content: str, templates: List[dict], llm_profile: str, llm_instance) -> TweetOutput:
    """
    Generate tweets based on content, templates, and LLM profile using SimplerLLM.
    
    Parameters:
    - content: The content to generate tweets from
    - templates: List of selected templates with their metadata
    - llm_profile: The LLM profile text
    - llm_instance: The language model instance
    
    Returns:
    - TweetOutput object with generated tweets
    """
    # Create a prompt for the LLM
    prompt = f"""
    # TASK: Generate 3 Viral X Tweets
    
    You are a social media expert specializing in creating high-engagement Twitter content.
    
    ## CONTENT TO Create Tweets based on:
    ```
    {content}
    ```
    
    ## TEMPLATES TO FOLLOW
    Use these templates as structural guides for your Tweets. Each Tweet should follow one of these templates:
    ```
    {templates[0]['metadata']['format']}
    
    {templates[1]['metadata']['format']}
    
    {templates[2]['metadata']['format']}
    ```
    
    ## LLM PROFILE (Your background and style)
    ```
    {llm_profile}
    ```
    
    ## REQUIREMENTS
    - Create exactly 3 Tweets, each following one of the provided templates
    - Each Tweet must be around 8-10 tweets under 280 characters each
    - Include relevant hashtags where appropriate (max 2-3)
    - Focus on providing value or insights that would make users want to share
    - Adapt the style to match the LLM profile
    
    ## OUTPUT FORMAT
    Provide 3 ready-to-post Tweets that follow the templates and capture the essence of the content.
    """
    
    # Generate tweets using SimplerLLM's pydantic model generation
    response = await generate_pydantic_json_model_async(
        model_class=TweetOutput,
        prompt=prompt,
        llm_instance=llm_instance
    )
    
    return response

async def main(source_type: SourceType, content: str, llm_profile_path: str, llm_instance):
    """
    Main function to demonstrate the tweet generation flow.
    
    Parameters:
    - source_type: Type of content source (YouTube, blog, or text)
    - content: The content identifier (URL or text)
    - llm_profile_path: Path to the LLM profile text file
    - llm_instance: The language model instance
    """
    # 1. Extract content from the source
    print(f"Step 1: Extracting content from {source_type.value} source...")
    extracted_content = await extract_content(source_type, content)
    print(f"Extracted content: {extracted_content[:100]}...")  # Show first 100 chars
    
    # 2. Select the best templates using LLMRouter
    print("\nStep 2: Selecting best templates with LLMRouter...")
    templates = select_best_templates(extracted_content, llm_instance)
    print(f"Selected templates: {[t['metadata']['id'] for t in templates]}")
    
    # 3. Read the LLM profile
    print("\nStep 3: Reading LLM profile...")
    llm_profile = read_llm_profile(llm_profile_path)
    print(f"LLM profile: {llm_profile[:100]}...")  # Show first 100 chars
    
    # 4. Generate tweets using SimplerLLM
    print("\nStep 4: Generating tweets with SimplerLLM...")
    tweet_output = await generate_tweets(extracted_content, templates, llm_profile, llm_instance)
    
    # 5. Display the results
    print("\nGenerated Tweets:")
    for i, tweet in enumerate(tweet_output.tweets, 1):
        print(f"\nTweet {i}:")
        print(tweet)

