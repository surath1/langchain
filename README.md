
### ChatGPT basic 
ChatGPT --> OpenAI --> GPT3.4/GPT4

- ChatGPT is an application & GPT3.4/GPT4 are LLM
- ChatGPT are cost associated(1000 token 0.002c, starting $5 credit)
- ChatGPT does not answer all question, knowlwdge is limited.
- ChatGPT does not access to your private data etc.
- ChatGPT does not access to google/wikipedia/social platform etc.

### Langchain  
[Your application want to access bellow to get the details] 
- OpenAI
- Huggingface
- Bloom
- Company DB etc.

LangChain platform uses OpnAI/Hugingface/Bloom/Google/wiki/Company DB etc 

Langchain is a framework allow user to build LLM application.

### OpenAI setup

```bash
!pip install --upgrade pip
!pip install langchain
!pip install openai

import os
os.environ["OPENAI_API_KEY"] = 'sk-v4HjJoJZm------------------'

from langchain.llms import OpenAI
llm = OpenAI(temperature=0.6) # temperature means how creative/risk your model (1 highest 0 lowest) 
text = "What would be a good company to work as ML engineer in USA?"
print(llm(text))
```

## langchain 
```bash
from langchain.prompts import PromptTemplate
prompt_template_name = PromptTemplate(
    input_variables = ['name'],
    template = 'Want to open a {name} company please suggest a fancy name?'
)
prompt_template_name.format(name='Machine Learning')

# ML Chain 
from langchain.chains import LLMChain
chain = LLMChain(llm=llm, prompt=prompt_template_name)
names = chain.run('AI')
print(names)
```

## langchain - SimpleSequentialChain
```bash
# Sequential Chain
# multiple --> input -> input --> output / Just give one output the final one 
from langchain.llms import OpenAI
llm = OpenAI(temperature=0.6)
prompt_template_nm = PromptTemplate(
    input_variables = ['name'],
    template = 'Want to open a {name} company please suggest a fancy name?'
)

nm_chain = LLMChain(llm=llm, prompt=prompt_template_nm)

prompt_template_soft = PromptTemplate(
    input_variables = ['software'],
    template = 'suggest locations {software} for this company, return as a list?'
)
software_chain = LLMChain(llm=llm, prompt=prompt_template_soft)

from langchain.chains import SimpleSequentialChain
chain = SimpleSequentialChain(chains = [nm_chain, software_chain])
response = chain.run('AI')
print(response)
```

## langchain - SequentialChain
```bash
# Sequential Chain (Multiple input/output)
prompt_template_nm = PromptTemplate(
    input_variables = ['name'],
    template = 'Want to open a {name} software company please suggest a fancy name?'
)

name_chain = LLMChain(llm=llm, prompt=prompt_template_nm, output_key='company_nm')

prompt_template_soft = PromptTemplate(
    input_variables = ['company_nm'],
    template = 'suggest {company_nm} locations for this company, return as a list?'
)
software_chain = LLMChain(llm=llm, prompt=prompt_template_soft, output_key='locations_details')

from langchain.chains import SequentialChain
chain = SequentialChain(
    chains = [name_chain, software_chain],
    input_variables = ['name'],
    output_variables = ['company_nm','locations_details']
)
chain({'name':'AI'})

```



