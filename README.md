
### ChatGPT basic 
ChatGPT --> OpenAI --> GPT3.4/GPT4
- ChatGPT is an application & GPT3.4/GPT4 are LLM
- ChatGPT cost associated(1000 token 0.002c initial $5 credit)
- ChatGPT does not answer all question, knowlwdge is limited.
- ChatGPT does not access to private data etc.
- ChatGPT does not access to google/wikipedia/social media data etc!

### Langchain  
[Your application want to access bellow to get the details] 
- OpenAI
- Huggingface
- Bloom
- Company DB etc.

- LangChain platform uses OpnAI/Hugingface/Bloom/Google/wiki/Company DB etc 

- Langchain is a framework, that allow user to build LLM application.

### OpenAI setup

```bash
!pip install --upgrade pip
!pip install langchain
!pip install openai
!pip install streamlit 
# pip uninstall tensorflow
# pip install tensorflow==2.13
# pip list

import os
os.environ["OPENAI_API_KEY"] = 'sk---'

from langchain.llms import OpenAI
llm = OpenAI(temperature=0.6) # temperature means how creative/risk your model (1 highest 0 lowest) 
#llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
text = "What would be a good company to work as ML engineer in USA?"
print(llm(text))
```

### langchain 
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

### langchain - SimpleSequentialChain
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

### langchain - SequentialChain
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

### langchain -LLM Agent
- The core idea of agents is to use a language model to choose a sequence of actions to take
- LLM has Knowlwdge to understand and respond your request, but it has Reasoning to identify the request.
- configure google, wiki, math etc 

```bash
from langchain.agents import AgentType, Tool, initialize_agent, load_tools
from langchain.chat_models import ChatOpenAI
from langchain.utilities import SerpAPIWrapper

tools = load_tools(["wikipedia","llm-math"], llm=llm)
agent = initialize_agent(
    tools,
    llm,
    #llm=OpenAI(temperature=0, max_tokens=1000),
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True  # go step by step
)
agent.run('When Mark Zuckerberg born and what is the age on 2020')

```

### langchain - serp Api 

```bash
import os
os.environ["SERPAPI_API_KEY"] = ''

from langchain.utilities import SerpAPIWrapper
search = SerpAPIWrapper()
search.run("Obama's first name?")
```

### langchain - Memory

```bash
from langchain.memory import ConversationBufferMemory
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

prompt_template_name = PromptTemplate(
    input_variables = ['name'],
    template = 'Want to open a {name} company please suggest a fancy name?'
)
memory1 = ConversationBufferMemory()
chain = LLMChain(llm=llm, prompt=prompt_template_name, memory=memory1)
print(chain.memory)
names = chain.run('AI')
print(names)

print(chain.memory)
print(chain.memory.buffer)


### ConversationChain - 

from langchain.chains import ConversationChain
conversation = ConversationChain(llm=llm)
print(conversation.prompt)
print(conversation.prompt.template)
conversation.run("Translate this sentence from English to French: I love programming.")
conversation.run("What is 2+2?")

print(conversation.memory)
print(conversation.memory.buffer)

## ConversationBufferWindowMemory

from langchain.memory import ConversationBufferWindowMemory
memory = ConversationBufferWindowMemory(k=2) # k- remember last 2 conversation 
conversation = ConversationChain(llm=llm, memory=memory)

conversation.run("USA GDP 2023")
conversation.run(5+5)
conversation.run("Which city Barack Obama was born?")

```
