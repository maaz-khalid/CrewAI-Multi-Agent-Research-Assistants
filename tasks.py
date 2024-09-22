from crewai import Task
from tools import tool
from agents import news_researcher,news_writer

# Research task
research_task = Task(
  description=(
    "Identify the meaning in {topic}."
    "Focus on when, how and why was this technology introduced."
    "Talk about where it is used and how it has changed the world of AI."
    "its usecase, advantages and disadvantages."
  ),
  expected_output='A comprehensive 4 paragraphs long report which explains the topic.',
  tools=[tool],
  agent=news_researcher,
#   async_execution=True
)

# Writing task with language model configuration
write_task = Task(
  description=(
    "Compose an insightful article on {topic}."
    "This article should be easy to understand, engaging, and positive."
  ),
  expected_output='An article on {topic} in the form of 10 bullet points formatted as markdown.',
#   tools=[tool],
  context=[research_task],
  agent=news_writer,
  async_execution=False,
  output_file='new-blog-post.md'  # Example of output customization
)