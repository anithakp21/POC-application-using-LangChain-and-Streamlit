import os
from langchain.llms import OpenAI
from langchain.chains import LLMChain, SequentialChain
from langchain.prompts import PromptTemplate

# Set your OpenAI API key
os.environ['OPENAI_API_KEY'] = ''
llm = OpenAI(temperature=0.7)
def generate_restaurant_name_and_items(cuisine):
    # Chain 1: Restaurant Name generator
    prompt_template_name = PromptTemplate(
        input_variables=['cuisine'],
        template='I want to open a restaurant for {cuisine} food. Suggest a fancy name.'
    )

    name_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key='restaurant_name')
    # Chain 2: Menu Generator
    prompt_template_items = PromptTemplate(
        input_variables=['restaurant_name'],  # Change input variable to 'restaurant_name'
        template='Suggest me some food items for the {restaurant_name} menu and return it as a comma-separated list.'
    )

    food_items_chain = LLMChain(llm=llm, prompt=prompt_template_items, output_key='menu_items')

    chain = SequentialChain(
        chains=[name_chain, food_items_chain],
        input_variables=['cuisine'],
        output_variables=['restaurant_name', 'menu_items']
    )

    response = chain({'cuisine': cuisine})
    return response

if __name__ == "__main__":
    response = generate_restaurant_name_and_items('Italian')
    print(response)
