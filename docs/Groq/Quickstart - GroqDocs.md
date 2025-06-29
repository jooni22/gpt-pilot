---
created: 2025-06-29T04:26:10
source: https://console.groq.com/docs/quickstart
---

# Quickstart - GroqDocs

> Documentation for Groq products and APIs.

---
[Quickstart](https://console.groq.com/docs/quickstart#quickstart)
-----------------------------------------------------------------

Get up and running with the Groq API in a few minutes.

### [Create an API Key](https://console.groq.com/docs/quickstart#create-an-api-key)

Please visit [here](https://console.groq.com/keys) to create an API Key.

### [Set up your API Key (recommended)](https://console.groq.com/docs/quickstart#set-up-your-api-key-recommended)

Configure your API key as an environment variable. This approach streamlines your API usage by eliminating the need to include your API key in each request. Moreover, it enhances security by minimizing the risk of inadvertently including your API key in your codebase.

#### [In your terminal of choice:](https://console.groq.com/docs/quickstart#in-your-terminal-of-choice)

```
export GROQ_API_KEY=<your-api-key-here>
```

### [Requesting your first chat completion](https://console.groq.com/docs/quickstart#requesting-your-first-chat-completion)

#### [Install the Groq Python library:](https://console.groq.com/docs/quickstart#install-the-groq-python-library)

#### [Performing a Chat Completion:](https://console.groq.com/docs/quickstart#performing-a-chat-completion)

```
1import os
2
3from groq import Groq
4
5client = Groq(
6    api_key=os.environ.get("GROQ_API_KEY"),
7)
8
9chat_completion = client.chat.completions.create(
10    messages=[
11        {
12            "role": "user",
13            "content": "Explain the importance of fast language models",
14        }
15    ],
16    model="llama-3.3-70b-versatile",
17)
18
19print(chat_completion.choices[0].message.content)
```

### [Using third-party libraries and SDKs](https://console.groq.com/docs/quickstart#using-thirdparty-libraries-and-sdks)

#### [Using AI SDK:](https://console.groq.com/docs/quickstart#using-ai-sdk)

[AI SDK](https://ai-sdk.dev/) is a Javascript-based open-source library that simplifies building large language model (LLM) applications. Documentation for how to use Groq on the AI SDK [can be found here](https://console.groq.com/docs/ai-sdk/).

First, install the `ai` package and the Groq provider `@ai-sdk/groq`:

  

Then, you can use the Groq provider to generate text. By default, the provider will look for `GROQ_API_KEY` as the API key.

  

```
1import { groq } from '@ai-sdk/groq';
2import { generateText } from 'ai';
3
4const { text } = await generateText({
5  model: groq('llama-3.3-70b-versatile'),
6  prompt: 'Write a vegetarian lasagna recipe for 4 people.',
7});
```

Now that you have successfully received a chat completion, you can try out the other endpoints in the API.

### [Next Steps](https://console.groq.com/docs/quickstart#next-steps)

*   Check out the [Playground](https://console.groq.com/playground) to try out the Groq API in your browser
*   Join our GroqCloud developer community on [Discord](https://discord.gg/groq)
*   Add a how-to on your project to the [Groq API Cookbook](https://github.com/groq/groq-api-cookbook)

### Was this page helpful?
