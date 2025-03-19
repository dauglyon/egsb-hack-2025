import getpass
import os
from langchain.chat_models import init_chat_model
from langchain_community.document_loaders import PyPDFLoader

outputText = "" 
with open('./ontoGPTOut/ijsem006633.txt') as file: # OntoGPT Output of AUTO: terms
    outputText = file.read()

loader = PyPDFLoader('./papers/ijsem006633.pdf') # Paper these terms were pulled from
pages = []
for page in loader.lazy_load():
    pages.append(page.page_content)
inputPaperText = "\n".join(pages)
summaryPrompt = f"""
You are an Ontology Curation Assistant Agent. You are an expert in concise and accurate summarization of scientific papers. You will receive the text from a paper, and the outputs from ontogpt (https://monarch-initiative.github.io/ontogpt/operation/). Your task is to summarize the paper in as minimal way as possible, while being sure to include all provided terms and their importance to the paper. You should inline the terms in brackets "<>". Include the AUTO: prefix. E.G. "<AUTO:non-motile>". You may use exact phrasing from the paper. 

TERMS
```
{outputText}
```

PAPER
```
{inputPaperText}
```

Give it a go, print your output and only your output. Do not include a preamble or commentary. Do not improvise or suggest your own terms. Do not introduce information other than the requested terms.
"""

categoryPrompt = f"""
You are an Ontology Curation Agent. You will receive multiple lists of term outputs from ontogpt (https://monarch-initiative.github.io/ontogpt/operation/). Your goal is to group each AUTO:* term into categories. Ideally, these categories would be the first level of nodes in a hierarchical ontology containing these terms.
Give it a go, print your output and only your output. Do not include a preamble or commentary. Print terms as they appear in the input, no need to format. Do not improvise or suggest your own terms. Do not introduce information other than the requested categories.
```
{outputText}
```
"""


def main():
    if not os.environ.get("ANTHROPIC_API_KEY"):
        os.environ["ANTHROPIC_API_KEY"] = getpass.getpass("Enter API key for Anthropic: ")
    model = init_chat_model("claude-3-5-sonnet-latest", model_provider="anthropic")
    print(model.invoke(summaryPrompt).text())

if __name__ == "__main__":
    main()
