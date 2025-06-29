---
created: 2025-06-29T04:26:10
source: https://console.groq.com/docs/reasoning
---

# Reasoning - GroqDocs

> Documentation for Groq products and APIs.

---
[Reasoning](https://console.groq.com/docs/reasoning#reasoning)
--------------------------------------------------------------

Reasoning models excel at complex problem-solving tasks that require step-by-step analysis, logical deduction, and structured thinking and solution validation. With Groq inference speed, these types of models can deliver instant reasoning capabilities critical for real-time applications.

### [Why Speed Matters for Reasoning](https://console.groq.com/docs/reasoning#why-speed-matters-for-reasoning)

Reasoning models are capable of complex decision making with explicit reasoning chains that are part of the token output and used for decision-making, which make low-latency and fast inference essential. Complex problems often require multiple chains of reasoning tokens where each step build on previous results. Low latency compounds benefits across reasoning chains and shaves off minutes of reasoning to a response in seconds.

[Supported Model](https://console.groq.com/docs/reasoning#supported-model)
--------------------------------------------------------------------------

[Reasoning Format](https://console.groq.com/docs/reasoning#reasoning-format)
----------------------------------------------------------------------------

Groq API supports explicit reasoning formats through the `reasoning_format` parameter, giving you fine-grained control over how the model's reasoning process is presented. This is particularly valuable for valid JSON outputs, debugging, and understanding the model's decision-making process.

**Note:** The format defaults to `raw` or `parsed` when JSON mode or tool use are enabled as those modes do not support `raw`. If reasoning is explicitly set to `raw` with JSON mode or tool use enabled, we will return a 400 error.

### [Options for Reasoning Format](https://console.groq.com/docs/reasoning#options-for-reasoning-format)

| `reasoning_format` Options | Description |
| --- | --- |
| `parsed` | Separates reasoning into a dedicated field while keeping the response concise. |
| `raw` | Includes reasoning within think tags in the content. |
| `hidden` | Returns only the final answer. |

### [Options for Reasoning Effort](https://console.groq.com/docs/reasoning#options-for-reasoning-effort)

The `reasoning_effort` parameter controls the level of effort the model will put into reasoning. This is only supported by [Qwen 3 32B](https://console.groq.com/docs/model/qwen3-32b).

| `reasoning_effort` Options | Description |
| --- | --- |
| `none` | Disable reasoning. The model will not use any reasoning tokens. |
| `default` | Enable reasoning. |

[Quick Start](https://console.groq.com/docs/reasoning#quick-start)
------------------------------------------------------------------

```
1from groq import Groq
2
3client = Groq()
4completion = client.chat.completions.create(
5    model="deepseek-r1-distill-llama-70b",
6    messages=[
7        {
8            "role": "user",
9            "content": "How many r's are in the word strawberry?"
10        }
11    ],
12    temperature=0.6,
13    max_completion_tokens=1024,
14    top_p=0.95,
15    stream=True,
16    reasoning_format="raw"
17)
18
19for chunk in completion:
20    print(chunk.choices[0].delta.content or "", end="")
```

[Quick Start with Tool use](https://console.groq.com/docs/reasoning#quick-start-with-tool-use)
----------------------------------------------------------------------------------------------

```
curl https://api.groq.com//openai/v1/chat/completions -s \
  -H "authorization: bearer $GROQ_API_KEY" \
  -d '{
    "model": "deepseek-r1-distill-llama-70b",
    "messages": [
        {
            "role": "user",
            "content": "What is the weather like in Paris today?"
        }
    ],
    "tools": [
        {
            "type": "function",
            "function": {
                "name": "get_weather",
                "description": "Get current temperature for a given location.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "location": {
                            "type": "string",
                            "description": "City and country e.g. Bogotá, Colombia"
                        }
                    },
                    "required": [
                        "location"
                    ],
                    "additionalProperties": false
                },
                "strict": true
            }
        }
    ]}'
```

[Recommended Configuration Parameters](https://console.groq.com/docs/reasoning#recommended-configuration-parameters)
--------------------------------------------------------------------------------------------------------------------

| Parameter | Default | Range | Description |
| --- | --- | --- | --- |
| `messages` | \- | \- | Array of message objects. Important: Avoid system prompts - include all instructions in the user message! |
| `temperature` | 0.6 | 0.0 - 2.0 | Controls randomness in responses. Lower values make responses more deterministic. Recommended range: 0.5-0.7 to prevent repetitions or incoherent outputs |
| `max_completion_tokens` | 1024 | \- | Maximum length of model's response. Default may be too low for complex reasoning - consider increasing for detailed step-by-step solutions |
| `top_p` | 0.95 | 0.0 - 1.0 | Controls diversity of token selection |
| `stream` | false | boolean | Enables response streaming. Recommended for interactive reasoning tasks |
| `stop` | null | string/array | Custom stop sequences |
| `seed` | null | integer | Set for reproducible results. Important for benchmarking - run multiple tests with different seeds |
| `response_format` | `{type: "text"}` | `{type: "json_object"}` or `{type: "text"}` | Set to `json_object` type for structured output. |
| `reasoning_format` | `raw` | `"parsed"`, `"raw"`, `"hidden"` | Controls how model reasoning is presented in the response. Must be set to either `parsed` or `hidden` when using tool calling or JSON mode. |
| `reasoning_effort` | `default` | `"none"`, `"default"` | Controls the level of effort the model will put into reasoning. This is only supported by [Qwen 3 32B](https://console.groq.com/docs/model/qwen3-32b). |

[Optimizing Performance](https://console.groq.com/docs/reasoning#optimizing-performance)
----------------------------------------------------------------------------------------

### [Temperature and Token Management](https://console.groq.com/docs/reasoning#temperature-and-token-management)

The model performs best with temperature settings between 0.5-0.7, with lower values (closer to 0.5) producing more consistent mathematical proofs and higher values allowing for more creative problem-solving approaches. Monitor and adjust your token usage based on the complexity of your reasoning tasks - while the default max\_completion\_tokens is 1024, complex proofs may require higher limits.

### [Prompt Engineering](https://console.groq.com/docs/reasoning#prompt-engineering)

To ensure accurate, step-by-step reasoning while maintaining high performance:

*   DeepSeek-R1 works best when all instructions are included directly in user messages rather than system prompts.
*   Structure your prompts to request explicit validation steps and intermediate calculations.
*   Avoid few-shot prompting and go for zero-shot prompting only.

### Was this page helpful?
