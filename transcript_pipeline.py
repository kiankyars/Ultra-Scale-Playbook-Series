#!/usr/bin/env python3
"""
YouTube Transcript to Jupyter Notebook Pipeline
Extracts transcript from YouTube video and creates a prompt for LLM to generate notebook
"""

import sys
from youtube_transcript_api import YouTubeTranscriptApi
import requests
from bs4 import BeautifulSoup
import re


def get_transcript(video_id):
    """Get transcript from YouTube video"""
    transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
    # Combine all text parts
    full_text = " ".join([entry['text'] for entry in transcript_list])
    return full_text


def generate_prompt(transcript, episode_number):
    """Generate a well-engineered prompt for creating a Jupyter notebook"""
    
    prompt = f"""# Ultra-Scale Playbook Jupyter Notebook Generation

You are an expert ML engineer and educator creating interactive Jupyter notebooks for the Ultra-Scale Playbook video series. Your task is to create an educational notebook based on the provided video transcript.

## Context
This is part of the Ultra-Scale Playbook series that teaches how to scale LLM training efficiently on GPUs and clusters. The series has a specific format and naming convention that must be followed.

## Requirements

### 1. Content Requirements
- **Title**: Use format "# Ultra-Scale Playbook: Part X" where X is the episode number
- **Overview section**: Bullet points explaining what will be covered
- **Educational content**: Mix of markdown explanations and code examples
- **2 Interactive Exercises**: Hands-on coding exercises that reinforce the concepts
- **Quiz section**: 3-4 questions with answers at the end

### 2. Code Standards
- Use PyTorch when applicable
- Include proper imports
- Add comments explaining complex concepts
- Use realistic examples that demonstrate scaling concepts
- Reference previous notebooks when relevant (e.g., "Building on what we learned in episode 1...")

### 3. Naming Convention
- This is episode {episode_number}
- Filename: `{episode_number}_episode_name.ipynb`
- Keep topic name concise but descriptive

### 4. Educational Approach
- Start with simple explanations
- Build complexity gradually
- Include visual analogies when helpful
- Provide practical, runnable code examples
- Connect concepts to real-world LLM training scenarios

## Video Transcript
```
{transcript}
```

## Your Task
Based on the above transcript, create a complete Jupyter notebook that:
1. Follows the exact format requirements above
2. Teaches the key concepts from the video
3. Includes 2 meaningful hands-on exercises
4. Maintains consistency with the existing notebook style
5. Uses appropriate episode numbering and naming

Please provide the complete notebook as a JSON structure that can be saved as a .ipynb file.
"""
    
    return prompt


def get_video_id_from_playlist(playlist_url, episode_number):
    """Fetch playlist and find video ID by episode number in aria-label of video links"""
    resp = requests.get(playlist_url)
    soup = BeautifulSoup(resp.text, 'html.parser')
    for a in soup.find_all('a', href=True):
        href = a['href']
        if '/watch?v=' in href:
            aria_label = a.get('aria-label')
            print(aria_label)
            if aria_label and str(episode_number) in aria_label:
                match = re.search(r'v=([\w-]+)', href)
                if match:
                    return match.group(1)
    raise ValueError(f"Episode {episode_number} not found in playlist")


def main():
    episode_number = sys.argv[1]
    playlist_url = "https://www.youtube.com/playlist?list=PLWVevi-n5pPy-Y9swxvs5AiTwA_QzUXsr"
    print(f"Finding video for episode {episode_number}...")
    video_id = get_video_id_from_playlist(playlist_url, episode_number)
    print(f"Video ID: {video_id}")
    print("Fetching transcript...")
    transcript = get_transcript(video_id)
    print(f"Transcript length: {len(transcript)} characters")
    print("Generating prompt...")
    prompt = generate_prompt(transcript, episode_number)
    with open(f"prompt.txt", "w") as f:
        f.write(prompt)
    print(f"Prompt saved to prompt.txt")


if __name__ == "__main__":
    main() 