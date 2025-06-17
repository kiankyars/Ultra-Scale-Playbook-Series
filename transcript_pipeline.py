#!/usr/bin/env python3
"""
YouTube Transcript to Jupyter Notebook Pipeline
Extracts transcript from YouTube video and creates a prompt for LLM to generate notebook
"""

import sys
from youtube_transcript_api import YouTubeTranscriptApi
import yt_dlp


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
- **Title**: Use format "# Ultra-Scale Playbook: Part {episode_number}"
- **Overview section**: Bullet points explaining what will be covered
- **Educational content**: Mix of markdown explanations and code examples
- **2 Interactive Exercises**: Hands-on coding exercises that reinforce the concepts
- **Quiz section**: 3-4 questions with answers at the end

### 2. Code Standards
- Use PyTorch when applicable
- Include proper imports
- Add comments explaining complex concepts
- Use realistic examples that demonstrate scaling concepts

### 3. Educational Approach
- Important: Simple explanations
- Practical, runnable code examples
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

Package the notebook as a downloadable .ipynb file in the following format: `{episode_number}_episode_name.ipynb`
"""
    
    return prompt


def get_video_id_from_playlist(playlist_url, episode_number):
    """Use yt-dlp to get video ID by episode number in title from playlist"""
    ydl_opts = {'quiet': True, 'extract_flat': True, 'skip_download': True}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(playlist_url, download=False)
        for entry in info['entries']:
            title = entry.get('title', '')
            print(title)
            if title and str(episode_number) in title:
                return entry['id']
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