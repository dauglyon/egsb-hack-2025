import getpass
import os
from langchain.chat_models import init_chat_model
from langchain_community.document_loaders import PyPDFLoader
from glob import glob

summaries = []
for path in glob("./out/*.txt"):
    with open(path) as file: # OntoGPT Output of AUTO: terms
      summaries.append(file.read())
summaryText = "\n\n".join(summaries)

summaryPrompt = f"""
You are an Ontology Curation Assistant Agent. 
You are an expert in ontology generation from scientific papers. 
You will receive a set of summaries of papers prepared by another agent. 
Your task is to identify terms in the summaries which are similar or contradictory. 
As your response:
- First, provide a list of conceptually exact synoynms.
- Then, provide a list of terms that conceptually negate eachother or are opposite.
- Finally, excluding exact synonyms and negations, identify terms with possible hierarchical relationships.

For any of these lists, if there are no entries, state such. 
Be sure to investigate all provided terms. Terms are inlined in brackets "<>". Do your best to include every term provided, do not reformat them (for example, do not remove the url escaping).
SUMMARIES
```
{summaryText}
```

Give it a go, print your output and only your output. Do not include a preamble or commentary. Do not improvise or suggest your own terms. Do not introduce information other than the requested terms.
"""

def main():
    if not os.environ.get("ANTHROPIC_API_KEY"):
        os.environ["ANTHROPIC_API_KEY"] = getpass.getpass("Enter API key for Anthropic: ")
    model = init_chat_model("claude-3-5-sonnet-latest", model_provider="anthropic")
    out = model.invoke(summaryPrompt).text()
    print(out)

if __name__ == "__main__":
    main()
