# A project that prompts the user to ask a question and answers 
# the question using the openAI API.

# API set up

import openai

api_key = '' # removed key for public github

openai.api_key = api_key



# A function that will send the question provided by the user to openAI and return a response

def ask_openai(question):
    response = openai.Completion.create(
        engine = "davinci",
        prompt = question,
        max_tokens = 300  # I made this a big number so that big questions won't have issues
    )
    return response.chocies[0].text.strip()


# Get input from user

#loop

while True:
    question = input("Ask me a question (or type 'quit' to quit) : ")

    if question.lower() == 'quit':
        break 


    # Sending input to function to get response

    response = ask_openai(question)

    # Display response

    print("Answer: ", response)






