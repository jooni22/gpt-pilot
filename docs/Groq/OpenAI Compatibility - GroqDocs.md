---
created: 2025-06-29T04:26:10
source: https://console.groq.com/docs/openai
---

# OpenAI Compatibility - GroqDocs

> Documentation for Groq products and APIs.

---
[OpenAI Compatibility](https://console.groq.com/docs/openai#openai-compatibility)
---------------------------------------------------------------------------------

We designed Groq API to be mostly compatible with OpenAI's client libraries, making it easy to configure your existing applications to run on Groq and try our inference speed.

We also have our own [Groq Python and Groq TypeScript libraries](https://console.groq.com/docs/libraries) that we encourage you to use.

### [Configuring OpenAI to Use Groq API](https://console.groq.com/docs/openai#configuring-openai-to-use-groq-api)

To start using Groq with OpenAI's client libraries, pass your Groq API key to the `api_key` parameter and change the `base_url` to `https://api.groq.com/openai/v1`:

```
import os
import openai

client = openai.OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=os.environ.get("GROQ_API_KEY")
)
```

  

You can find your API key [here](https://console.groq.com/keys).

### [Currently Unsupported OpenAI Features](https://console.groq.com/docs/openai#currently-unsupported-openai-features)

Note that although Groq API is mostly OpenAI compatible, there are a few features we don't support just yet:

#### [Text Completions](https://console.groq.com/docs/openai#text-completions)

The following fields are currently not supported and will result in a 400 error (yikes) if they are supplied:

*   `logprobs`
    
*   `logit_bias`
    
*   `top_logprobs`
    
*   `messages[].name`
    
*   If `N` is supplied, it must be equal to 1.
    

#### [Temperature](https://console.groq.com/docs/openai#temperature)

If you set a `temperature` value of 0, it will be converted to `1e-8`. If you run into any issues, please try setting the value to a float32 `> 0` and `<= 2`.

#### [Audio Transcription and Translation](https://console.groq.com/docs/openai#audio-transcription-and-translation)

The following values are not supported:

*   `vtt`
*   `srt`

### [Feedback](https://console.groq.com/docs/openai#feedback)

If you'd like to see support for such features as the above on Groq API, please reach out to us and let us know by submitting a "Feature Request" via "Chat with us" located on the left. We really value your feedback and would love to hear from you! 🤩

[Next Steps](https://console.groq.com/docs/openai#next-steps)
-------------------------------------------------------------

Migrate your prompts to open-source models using our [model migration guide](https://console.groq.com/docs/prompting/model-migration), or learn more about prompting in our [prompting guide](https://console.groq.com/docs/prompting).

### Was this page helpful?
