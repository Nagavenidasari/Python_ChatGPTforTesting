import openai


openai.api_key='sk-ezDGZ0I5co5pjcXXXXXXXXXXXXXXXXXXX'
def ask_chatbot(prompt):
    response = openai.Completion.create(
        engine='text-davinci-003',  #specifies the language model to use.davinci refers to GPT-3 model
        prompt=prompt,  # the question or prompt that you want to provide to chatbot.
        max_tokens=1500,  # number of words/chars
        temperature=0.5,  #controls the randomness of the generated response
        n=1,  #number of responses
        stop=None,  #specifies an optional stopping sequence to indicate the end.None means theresponse of any length

    )
    return response.choices[0].text.strip()
def generate_test_case():
    requirement = "The web application should allow users to search for a product by entering a keyword in the search field."
    prompt = f"Generate testcase for the following software requirement:\n\n{requirement}"
    return ask_chatbot(prompt)
def generate_user_Story():
    requirement = "The web application should allow users to login."
    prompt = f"Generate userstory/userstories for the following software requirement that covers both positive and negative scenario:\n\n{requirement}"
    return ask_chatbot(prompt)
def generate_test_plan():
    requirement = "Email Web Application"
    prompt = f"Generate a testplan for the following software requirement \n\n{requirement}"
    return ask_chatbot(prompt)
def generate_test_scenarios():
    requirement = "Email Web Application"
    prompt = f"Generate a testscenarios for the following software requirement \n\n{requirement}"
    return ask_chatbot(prompt)


#answer = ask_chatbot(requirement)
#answer = generate_test_case()
#answer=generate_user_Story()
#print(answer)
#testplan=generate_test_plan()
#print(testplan)
testscenarios=generate_test_scenarios()
print(testscenarios)
