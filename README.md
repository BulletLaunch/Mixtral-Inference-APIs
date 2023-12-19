# Mixtral Inference APIs
make the best out of the race to bottom

a convenience script we use internally having a collection of providers with cheap infra cost for LLM inference

if you like what we are doing  

Please leave a star on the repo

Support us on buymeacoffee  
<a href="https://www.buymeacoffee.com/bulletlaunch" target="_blank"><img src="https://github.com/BulletLaunch/.github/assets/62943847/9e97ec08-c4ab-4baa-8485-f3f543f247bb" alt="Buy Me A Coffee"></a>  
Checkout our socials and follow us there  
<a href="https://twitter.com/bulletlaunchhq" target="_blank"><img src="https://github.com/BulletLaunch/.github/assets/62943847/58075057-2502-4fe8-b2f8-c6e121194dd4" alt="Buy Me A Coffee" height="41" width="41"></a>
<a href="https://www.linkedin.com/company/bulletlaunch" target="_blank"><img src="https://github.com/BulletLaunch/.github/assets/62943847/e71c1e79-a287-4cfc-bad2-79ad41cd445b" alt="Buy Me A Coffee" height="41" width="41"></a>  

## Usage
1. Rename the `.env.template` file to `.env` and add the corresponding credentials for the providers you want to use (check pricing and performance comparison below)
2. You can either run the script directly for testing the endpoints or use the inference function in your program logic

To directly use the inference function copy the `.env` file and `llm_inference_script` to your project and import the function
  
example :
```python
from llm_inference_script import llm_inference
from dotenv import load_dotenv
import os

load_dotenv()

KEY = os.getenv("PROVIDER_API_KEY") # put correct provider name here
output = llm_inference(provider, prompt, KEY)
```

## Credits and Pricing
As of 19-12-2023

| Provider    | Run 1 Processing Time | Run 2 Processing Time |
|-------------|-----------------------|-----------------------|
| OpenRouter  | 4.353891372680664     | 3.521432638168335     |
| Anyscale    | 3.7671189308166504    | 3.727105140686035     |
| Together    | 2.8246912956237793    | 2.7198286056518555    |
| DeepInfra   | 19.719090700149536    | 18.043762922286987    |
| AbacusAI    | 11.183688879013062    | 14.28700041770935     |

| Provider   | Pricing per Million Tokens | Free Credits |
|------------|----------------------------|--------------|
| OpenRouter | 0.3 - 0.7                  | $1          |
| Anyscale   | 0.5                        | $10         |
| Together   | 0.6                        | $25         |
| DeepInfra  | 0.27                       | Unclear      |
| AbacusAI   | 0.3                        | Unclear      |

My recommendation use Together for latency ciritical inference and DeepInfra for latency non critical applications. These two provided me with the most flexibility in what I can run with reasonable pricing and a very good user experience

Also checkout [this](https://www.f6s.com/company-deals/deepinfra/150h-free-ai-ml-models-by-api-14180 ) idk if it works but seems interesting