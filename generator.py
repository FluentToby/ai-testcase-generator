import os
from openai import  OpenAI
from dotenv import load_dotenv


load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_test_cases(user_input: str, context: str) -> str:
    is_bdd = "Given, When, Then" in context
    prompt = f"""
    You are a QA engineer. {context}
    
    Input:
    \"\"\"
    {user_input}
    \"\"\"
    """
    if is_bdd:
        prompt += "\nGenerate acceptance criteria using the BDD format:\n- Given\n- When\n- Then\n"
    else:
        prompt += "\nGenerate test cases in this format:\n- Title\n- Type (Positive / Negative / Edge)\n- Steps\n- Expected Result\n"

    response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3,
        )
    return response.choices[0].message.content.strip()
    