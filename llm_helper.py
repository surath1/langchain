from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain
import os
os.environ["OPENAI_API_KEY"] = ''

llm = OpenAI(temperature=0.6)
#llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

def get_company_name_and_location(name):
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

    chain = SequentialChain(
        chains = [name_chain, software_chain],
        input_variables = ['name'],
        output_variables = ['company_nm','locations_details']
    )
    response = chain({'name': name})

    return response


if __name__ == "__main__":
    print(get_company_name_and_location("AI"))
