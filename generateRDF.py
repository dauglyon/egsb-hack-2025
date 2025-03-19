import getpass
import os
from langchain.chat_models import init_chat_model
from langchain_community.document_loaders import PyPDFLoader
from glob import glob



summaryPrompt = f"""
You are an Ontology Curation Assistant Agent. 
You are an expert in ontology generation from scientific papers. 
You will recieve a document describing a set of relationships between terms.
Terms are inlined in brackets "<>".
Please create an RDF XML file representing the contents of the following term relationships:

```
Identical Terms:
- <AUTO:can utilize d-cellobiose> and <AUTO:able to utilize d-cellobiose>
- <AUTO:can utilize d-galactose> and <AUTO:able to utilize d-galactose>
- <AUTO:can utilize d-glucose> and <AUTO:able to utilize d-glucose>
- <AUTO:can utilize d-mannose> and <AUTO:able to utilize d-mannose>

Similar Terms:
- Habitat grouping:
  - <AUTO:saline soils>
  - <AUTO:drought-affected soils>
  - <AUTO:chemically contaminated and polluted soils of the North Aral Sea Region>
  - <AUTO:rhizosphere soil of Camellia oleifera>
  - <AUTO:naturally found in soil environments, specifically rhizosphere soil associated with Camellia oleifera>

- Sugar utilization inability grouping:
  - <AUTO:cannot utilize sucrose>
  - <AUTO:unable to utilize sucrose>

Contradictory Terms:
- Sugar utilization:
  - <AUTO:can utilize d-ribose> vs <AUTO:unable to utilize d-ribose>
  - <AUTO:can utilize l-arabinose> vs <AUTO:unable to utilize l-arabinose>
  - <AUTO:can utilize d-xylose> vs <AUTO:unable to utilize d-xylose>

Terms Unique to Single Summary:
Summary 1:
- All terms related to S. meliloti AK21's symbiotic associations, stress tolerance, and genetic characteristics

Summary 2:
- All clinical isolate characteristics, enzymatic activities, and genetic measurements

Summary 3:
- All terms specific to Kitasatospora camelliae's morphology, cell wall composition, and growth conditions

Exact Synonyms:
- <AUTO:human peritoneal cavity (isolated from a peritoneal abscess)> = <AUTO:clinical isolate obtained from the peritoneal swab of a patient with ruptured appendicitis>
- <AUTO:cbb3-type terminal oxidase–based respiration> = <AUTO:fixNOQP cbb3-oxidase for microaerobic respiration>
- <AUTO:saline soils> = <AUTO:saline, drought-affected, and polluted soils>
- <plasmid mobilization genes (traG, VirB9-like)> = <AUTO:capacity for conjugative plasmid transfer (traG, VirB9-like system)>

Opposing Terms:
- <AUTO:can utilize d-maltose> vs <AUTO:cannot utilize d-maltose>
- <AUTO:can utilize sucrose> vs <AUTO:cannot utilize sucrose>
- <AUTO:motile> vs <AUTO:non-motile>

Hierarchical Relationships:
- <AUTO:symbiotic association with Medicago spp. (forms nodules)> is a specific type of <AUTO:broad metabolic adaptation to multiple C, N, P, and S sources>
- <AUTO:salt tolerance> and <AUTO:drought tolerance> are types of <AUTO:greater substrate-use versatility under stress>
- <AUTO:trehalose biosynthesis for osmotolerance> is a specific mechanism of <AUTO:salt tolerance>
- <AUTO:production of capsular polysaccharide> is enabled by <AUTO:intact expR allele>
- <AUTO:produces urease>, <AUTO:produces cholinesterase>, <AUTO:produces beta-glucuronidase> etc. are specific instances of enzymatic capabilities
- <AUTO:aerial hyphae form rectiflexible spore chains> is a specific type of <AUTO:reproduces via formation of aerial mycelia that differentiate into rectiflexible chains of spherical or cylindrical spores>
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
