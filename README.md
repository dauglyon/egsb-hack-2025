# Create paper summaries with ontogpt, langchain, and \<your choice of llm\>
The idea here is to "embed" the ontoGPT AUTO: terms into a summary of the paper to create a summary of the extracted terms in a natural-language format that LLM agents can further parse. The summaries could then be combined into a super-summary of similar terms and their respective contexts, along with references back to the original papers. A separate agent could then use these summaries of term contexts to orchestrate an effort to create an ontology from scratch from a large corpus of papers. This is one of many ideas to try to solve the "context window" size for processing a large corpus of documents into an ontology.

## main.py
generates summaries

## merge.py
attempts to merge summaries
