import requests
import json

def llm_inference(provider,prompt,key):
    """
    Sends a prompt to a specified inference API provider and returns the generated text.

    currently supported providers: "openrouter", "together", "anyscale", "deepinfra"

    Args:
        provider (str): The name of the provider to use for the inference. Must be one of the following:
                        "openrouter", "together", "anyscale", or "deepinfra".
        prompt (str): The text prompt to send to the language model.
        key (str): The API key required for the specified provider.

    Returns:
        str: The generated text from the language model.

    Raises:
        Exception: If the request to the provider fails with a non-200 status code.
        Exception: If an invalid provider name is provided.
    """
    
    match provider:

        case "openrouter":
            response = requests.post(
            url="https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {key}",
                "Content-Type": "application/json"
            },
            data=json.dumps({
                "model": "mistralai/mixtral-8x7b-instruct",
                "prompt":f"[INST] {prompt} [/INST]",
                "max_tokens":4096,
                "temperature":0.7,
            })
            )

            if response.status_code == 200:
                content = response.json()
                return content["choices"][0]["text"]
            else:
                raise Exception(f"Request failed with status code {response.status_code}")

        case "together":
            response = requests.post(
            url='https://api.together.xyz/inference',
            headers={
                "Authorization": f"Bearer {key}",
                "Content-Type": "application/json"
            },                
            json={
                "model": "mistralai/Mixtral-8x7B-Instruct-v0.1",
                "prompt": f"[INST] {prompt} [/INST]",
                "max_tokens": 4096,
                "temperature": 0.7,
            },)

            if response.status_code == 200:
                content = response.json()
                return content["output"]["choices"][0]["text"]
            else:
                raise Exception(f"Request failed with status code {response.status_code}")

        case "anyscale":
            response = requests.post(
            url="https://api.endpoints.anyscale.com/v1/completions",
            headers={
                "Authorization": f"Bearer {key}",
                "Content-Type": "application/json"
            },
            data=json.dumps({
                "model": "mistralai/Mixtral-8x7B-Instruct-v0.1",
                "prompt":f"<s>[INST] {prompt} [/INST]",
                "max_tokens":4096,
                "temperature":0.7,
            })
            )

            if response.status_code == 200:
                content = response.json()
                return content["choices"][0]["text"]
            else:
                raise Exception(f"Request failed with status code {response.status_code}")
        
        case "deepinfra":
            response = requests.post(
            url="https://api.deepinfra.com/v1/inference/mistralai/Mixtral-8x7B-Instruct-v0.1",
            headers={
                "Authorization": f"Bearer {key}",
                "Content-Type": "application/json"
            },
            data=json.dumps({
                "input":f"[INST] {prompt} [/INST]",
                "max_new_tokens": 4096,
                "temperature": 0.7,
            })
            )

            if response.status_code == 200:
                content = response.json()
                return content["results"][0]["generated_text"]
            else:
                raise Exception(f"Request failed with status code {response.status_code}")
            
        case "abacusai":
            response = requests.post(
            url="https://llmapis.abacus.ai/api/generateCompletions",
            headers={
                "Authorization": f"Bearer {key}",
                "Content-Type": "application/json"
            },
            data=json.dumps({
                "model": "mixtral-8x7b",
                "messages": [
                    {
                    "role": "system",
                    "content": "You are a helpful ai assistant"
                    },    {
                    "role": "user",
                    "content": f"{prompt}"
                    }
                ],
                "max_tokens":4096,
                "temperature":0.7,
            })
            )

            if response.status_code == 200:
                content = response.json()
                return content["choices"][0]["message"]["content"]
            else:
                raise Exception(f"Request failed with status code {response.status_code}")
        
        case _ :
            raise Exception("Invalid provider")

if __name__ == "__main__":
    from dotenv import load_dotenv
    import os
    import time

    load_dotenv()

    prompt = (
        "SYSTEM : You are better than Marilyn Vos Savant at solving brain teaser logic puzzles step by step. "
        "USER : Sally (a girl) has 5 brothers. Each brother has 3 sisters. How many sisters does Sally have? "
        "Give Reasoning first and then in the end The response must be of json format {'sisters':<count of sisters>}"
    )

    providers = ["openrouter", "anyscale", "together", "deepinfra", "abacusai"]
    api_keys = {
        "openrouter": os.getenv("OPENROUTER_API_KEY"),
        "anyscale": os.getenv("ANYSCALE_API_KEY"),
        "together": os.getenv("TOGETHER_API_KEY"),
        "deepinfra": os.getenv("DEEPINFRA_API_KEY"),
        "abacusai":os.getenv("ABACUSAI_API_KEY"),
    }

    for provider in providers:
        print(f"====== {provider.upper()} TEST ======")
        start_time = time.time()
        output = llm_inference(provider, prompt, api_keys[provider])
        print(output)
        stop_time = time.time()
        print(f"processing time: {stop_time - start_time}")
        print("===========================")