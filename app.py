import os
from dotenv import load_dotenv
load_dotenv()

os.environ["HUGGINGFACE_ACCESS_TOKEN"] = os.getenv("HUGGINGFACE_ACCESS_TOKEN")
from embedchain import App
app = App.from_config('./mistral.yaml')
app.add("https://www.forbes.com/profile/elon-musk")
app.add("https://en.wikipedia.org/wiki/Elon_Musk")
ans = app.query("What is the net worth of Elon Musk today?")
print(ans)
