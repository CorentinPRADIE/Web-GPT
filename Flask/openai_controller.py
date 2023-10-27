from flask import jsonify, request
import openai

from bing_controller import requires_web_search, get_bing_search_results


def interactive_chat_with_bing_search(data, use_log=False):
        user_message = data['messages'][-1]['value'].strip()  
        conversation = ''
        for i in range(len(data['messages'])):
            conversation += data['messages'][i]['value'].strip() + '\n'  

        bing_search_used = False
        bing_response = ""

        # Check if web search is required for the user's message
        if not data['messages'][-1]['isAi'] and requires_web_search(conversation):
            # Perform the Bing search and get results
            bing_results = get_bing_search_results(user_message)

            if bing_results[0]:
                bing_response = ""
                for i in range(len(bing_results[0])):
                    # With link
                    # bing_response += f"{bing_results[0][i]}\n{bing_results[1][i]}\n{bing_results[2][i]}\n\n"
                    # Without link
                    bing_response += f"{i+1}.{bing_results[0][i]}\n{bing_results[2][i]} ...\n\n"
            else:
                bing_response = "Bing search did not return any results."

            bing_search_used = True

        # Convert input format to OpenAI format
        messages = []
        for item in data['messages']:
            role = "assistant" if item['isAi'] else "user"
            messages.append({
                "role": role,
                "content": item['value'].strip()
            })
        
        

        if bing_search_used:
            messages[-1]['content'] =  messages[-1]['content'] + 'To answer the question, use the results from the web :' + bing_response

        if use_log:
            print(messages[-1]['content'])

        # Call the OpenAI API
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )

       
        assistant_response = response.choices[0].message['content']

        # Include the Bing search results in the assistant's response if a search was performed
        if bing_search_used:
            assistant_response = "\n I have found the following articles to help answer your question:\n\n" + bing_response + '\n\n' +assistant_response

        # Add a note at the end of the assistant's response if a Bing search was used
        if bing_search_used:
            assistant_response += "\n(Bing search was performed)"
        else:
            assistant_response += "\n(No Bing search was performed)"

        return jsonify({'response': assistant_response})
