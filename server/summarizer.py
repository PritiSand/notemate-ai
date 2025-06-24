import re

def summarize_text(text):
    # Break the full text into sentences
    sentences = re.split(r'(?<=[.!?]) +', text)

    # Take the first 3 sentences as a basic summary
    summary = ' '.join(sentences[:3])

    return f"Key Takeaways:\n{summary}"

