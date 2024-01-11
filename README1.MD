
### Langchain 0.1.0

What is LangChain?
- LangChain is a python package that serve as a framework for developing application in large language model. 
- LangChain build llm application. 
- LangSmith trace your application. 
- LangServe serve your application. 

### project setup

- https://python.langchain.com/docs/get_started/installation

 ```bash
    conda create -p envlang python==3.11 -y 
    conda activate envlang/

    pip install --upgrade pip
    pip install -r requirement.txt
    #pip install faiss-cpu #Faiss is a library for efficient similarity search and clustering of dense vectors
 ```

### LLM Prompt

   ```bash
    from langchain_openai import ChatOpenAI
    from constants import OPENAI_KEY

    llm = ChatOpenAI(openai_api_key=OPENAI_KEY, temperature=0.7)
    llm.invoke("Where is Lord Ram Temple located?")

    ## Prompt templates are used to convert raw user input to a better input to the LLM.

    from langchain_core.prompts import ChatPromptTemplate

    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are world class technical documentation writer."),
        ("user", "{input}")
    ])

    # We can now combine these into a simple LLM chain
    chain = prompt | llm 

    chain.invoke({"input": "Where is Lord Ram Temple located?"})   
    
   ```

   ### LLM OutputParser

   ```bash
    ## Output parser to convert the chat message to a string.
    from langchain_core.output_parsers import StrOutputParser
    output_parser = StrOutputParser()

    # We can now combine these into a simple LLM chain
    chain = prompt | llm | output_parser
    chain.invoke({"input": "Where is Lord Ram Temple located?"})
   ```

   ### Driving Deeper 
   - So far llm only answer single questions, In order to update retrieval, we will create a new chain. This chain  will take in the most recent input (input) and the conversation history (chat_history) and use an LLM to generate a search query.