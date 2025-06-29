---
created: 2025-06-29T04:26:11
source: https://console.groq.com/docs/text-chat
---

# Text Generation - GroqDocs

> Documentation for Groq products and APIs.

---
[Text Generation](https://console.groq.com/docs/text-chat#text-generation)
--------------------------------------------------------------------------

Generating text with Groq's Chat Completions API enables you to have natural, conversational interactions with Groq's large language models. It processes a series of messages and generates human-like responses that can be used for various applications including conversational agents, content generation, task automation, and generating structured data outputs like JSON for your applications.

[On This Page](https://console.groq.com/docs/text-chat#on-this-page)
--------------------------------------------------------------------

*   [Chat Completions](https://console.groq.com/docs/text-chat#chat-completions)
*   [Basic Chat Completion](https://console.groq.com/docs/text-chat#performing-a-basic-chat-completion)
*   [Streaming Chat Completion](https://console.groq.com/docs/text-chat#streaming-a-chat-completion)
*   [Using Stop Sequences](https://console.groq.com/docs/text-chat#performing-a-chat-completion-with-a-stop-sequence)
*   [JSON Mode](https://console.groq.com/docs/text-chat#json-mode)
*   [JSON Mode with Schema Validation](https://console.groq.com/docs/text-chat#json-mode-with-schema-validation)

[Chat Completions](https://console.groq.com/docs/text-chat#chat-completions)
----------------------------------------------------------------------------

Chat completions allow your applications to have dynamic interactions with Groq's models. You can send messages that include user inputs and system instructions, and receive responses that match the conversational context.

Chat models can handle both multi-turn discussions (conversations with multiple back-and-forth exchanges) and single-turn tasks where you need just one response.

For details about all available parameters, [visit the API reference page.](https://console.groq.com/docs/api-reference#chat-create)

### [Getting Started with Groq SDK](https://console.groq.com/docs/text-chat#getting-started-with-groq-sdk)

To start using Groq's Chat Completions API, you'll need to install the [Groq SDK](https://console.groq.com/docs/libraries) and set up your [API key](https://console.groq.com/keys).

### [Performing a Basic Chat Completion](https://console.groq.com/docs/text-chat#performing-a-basic-chat-completion)

The simplest way to use the Chat Completions API is to send a list of messages and receive a single response. Messages are provided in chronological order, with each message containing a role ("system", "user", or "assistant") and content.

```
1from groq import Groq
2
3client = Groq()
4
5chat_completion = client.chat.completions.create(
6    messages=[
7        # Set an optional system message. This sets the behavior of the
8        # assistant and can be used to provide specific instructions for
9        # how it should behave throughout the conversation.
10        {
11            "role": "system",
12            "content": "You are a helpful assistant."
13        },
14        # Set a user message for the assistant to respond to.
15        {
16            "role": "user",
17            "content": "Explain the importance of fast language models",
18        }
19    ],
20
21    # The language model which will generate the completion.
22    model="llama-3.3-70b-versatile"
23)
24
25# Print the completion returned by the LLM.
26print(chat_completion.choices[0].message.content)
```

### [Streaming a Chat Completion](https://console.groq.com/docs/text-chat#streaming-a-chat-completion)

For a more responsive user experience, you can stream the model's response in real-time. This allows your application to display the response as it's being generated, rather than waiting for the complete response.

To enable streaming, set the parameter `stream=True`. The completion function will then return an iterator of completion deltas rather than a single, full completion.

```
1from groq import Groq
2
3client = Groq()
4
5stream = client.chat.completions.create(
6    #
7    # Required parameters
8    #
9    messages=[
10        # Set an optional system message. This sets the behavior of the
11        # assistant and can be used to provide specific instructions for
12        # how it should behave throughout the conversation.
13        {
14            "role": "system",
15            "content": "You are a helpful assistant."
16        },
17        # Set a user message for the assistant to respond to.
18        {
19            "role": "user",
20            "content": "Explain the importance of fast language models",
21        }
22    ],
23
24    # The language model which will generate the completion.
25    model="llama-3.3-70b-versatile",
26
27    #
28    # Optional parameters
29    #
30
31    # Controls randomness: lowering results in less random completions.
32    # As the temperature approaches zero, the model will become deterministic
33    # and repetitive.
34    temperature=0.5,
35
36    # The maximum number of tokens to generate. Requests can use up to
37    # 2048 tokens shared between prompt and completion.
38    max_completion_tokens=1024,
39
40    # Controls diversity via nucleus sampling: 0.5 means half of all
41    # likelihood-weighted options are considered.
42    top_p=1,
43
44    # A stop sequence is a predefined or user-specified text string that
45    # signals an AI to stop generating content, ensuring its responses
46    # remain focused and concise. Examples include punctuation marks and
47    # markers like "[end]".
48    stop=None,
49
50    # If set, partial message deltas will be sent.
51    stream=True,
52)
53
54# Print the incremental deltas returned by the LLM.
55for chunk in stream:
56    print(chunk.choices[0].delta.content, end="")
```

### [Performing a Chat Completion with a Stop Sequence](https://console.groq.com/docs/text-chat#performing-a-chat-completion-with-a-stop-sequence)

Stop sequences allow you to control where the model should stop generating. When the model encounters any of the specified stop sequences, it will halt generation at that point. This is useful when you need responses to end at specific points.

```
1from groq import Groq
2
3client = Groq()
4
5chat_completion = client.chat.completions.create(
6    #
7    # Required parameters
8    #
9    messages=[
10        # Set an optional system message. This sets the behavior of the
11        # assistant and can be used to provide specific instructions for
12        # how it should behave throughout the conversation.
13        {
14            "role": "system",
15            "content": "You are a helpful assistant."
16        },
17        # Set a user message for the assistant to respond to.
18        {
19            "role": "user",
20            "content": "Count to 10.  Your response must begin with \"1, \".  example: 1, 2, 3, ...",
21        }
22    ],
23
24    # The language model which will generate the completion.
25    model="llama-3.3-70b-versatile",
26
27    #
28    # Optional parameters
29    #
30
31    # Controls randomness: lowering results in less random completions.
32    # As the temperature approaches zero, the model will become deterministic
33    # and repetitive.
34    temperature=0.5,
35
36    # The maximum number of tokens to generate. Requests can use up to
37    # 2048 tokens shared between prompt and completion.
38    max_completion_tokens=1024,
39
40    # Controls diversity via nucleus sampling: 0.5 means half of all
41    # likelihood-weighted options are considered.
42    top_p=1,
43
44    # A stop sequence is a predefined or user-specified text string that
45    # signals an AI to stop generating content, ensuring its responses
46    # remain focused and concise. Examples include punctuation marks and
47    # markers like "[end]".
48    # For this example, we will use ", 6" so that the llm stops counting at 5.
49    # If multiple stop values are needed, an array of string may be passed,
50    # stop=[", 6", ", six", ", Six"]
51    stop=", 6",
52
53    # If set, partial message deltas will be sent.
54    stream=False,
55)
56
57# Print the completion returned by the LLM.
58print(chat_completion.choices[0].message.content)
```

### [Performing an Async Chat Completion](https://console.groq.com/docs/text-chat#performing-an-async-chat-completion)

For applications that need to maintain responsiveness while waiting for completions, you can use the asynchronous client. This lets you make non-blocking API calls using Python's asyncio framework.

```
1import asyncio
2
3from groq import AsyncGroq
4
5
6async def main():
7    client = AsyncGroq()
8
9    chat_completion = await client.chat.completions.create(
10        #
11        # Required parameters
12        #
13        messages=[
14            # Set an optional system message. This sets the behavior of the
15            # assistant and can be used to provide specific instructions for
16            # how it should behave throughout the conversation.
17            {
18                "role": "system",
19                "content": "You are a helpful assistant."
20            },
21            # Set a user message for the assistant to respond to.
22            {
23                "role": "user",
24                "content": "Explain the importance of fast language models",
25            }
26        ],
27
28        # The language model which will generate the completion.
29        model="llama-3.3-70b-versatile",
30
31        #
32        # Optional parameters
33        #
34
35        # Controls randomness: lowering results in less random completions.
36        # As the temperature approaches zero, the model will become
37        # deterministic and repetitive.
38        temperature=0.5,
39
40        # The maximum number of tokens to generate. Requests can use up to
41        # 2048 tokens shared between prompt and completion.
42        max_completion_tokens=1024,
43
44        # Controls diversity via nucleus sampling: 0.5 means half of all
45        # likelihood-weighted options are considered.
46        top_p=1,
47
48        # A stop sequence is a predefined or user-specified text string that
49        # signals an AI to stop generating content, ensuring its responses
50        # remain focused and concise. Examples include punctuation marks and
51        # markers like "[end]".
52        stop=None,
53
54        # If set, partial message deltas will be sent.
55        stream=False,
56    )
57
58    # Print the completion returned by the LLM.
59    print(chat_completion.choices[0].message.content)
60
61asyncio.run(main())
```

### [Streaming an Async Chat Completion](https://console.groq.com/docs/text-chat#streaming-an-async-chat-completion)

You can combine the benefits of streaming and asynchronous processing by streaming completions asynchronously. This is particularly useful for applications that need to handle multiple concurrent conversations.

```
1import asyncio
2
3from groq import AsyncGroq
4
5
6async def main():
7    client = AsyncGroq()
8
9    stream = await client.chat.completions.create(
10        #
11        # Required parameters
12        #
13        messages=[
14            # Set an optional system message. This sets the behavior of the
15            # assistant and can be used to provide specific instructions for
16            # how it should behave throughout the conversation.
17            {
18                "role": "system",
19                "content": "You are a helpful assistant."
20            },
21            # Set a user message for the assistant to respond to.
22            {
23                "role": "user",
24                "content": "Explain the importance of fast language models",
25            }
26        ],
27
28        # The language model which will generate the completion.
29        model="llama-3.3-70b-versatile",
30
31        #
32        # Optional parameters
33        #
34
35        # Controls randomness: lowering results in less random completions.
36        # As the temperature approaches zero, the model will become
37        # deterministic and repetitive.
38        temperature=0.5,
39
40        # The maximum number of tokens to generate. Requests can use up to
41        # 2048 tokens shared between prompt and completion.
42        max_completion_tokens=1024,
43
44        # Controls diversity via nucleus sampling: 0.5 means half of all
45        # likelihood-weighted options are considered.
46        top_p=1,
47
48        # A stop sequence is a predefined or user-specified text string that
49        # signals an AI to stop generating content, ensuring its responses
50        # remain focused and concise. Examples include punctuation marks and
51        # markers like "[end]".
52        stop=None,
53
54        # If set, partial message deltas will be sent.
55        stream=True,
56    )
57
58    # Print the incremental deltas returned by the LLM.
59    async for chunk in stream:
60        print(chunk.choices[0].delta.content, end="")
61
62asyncio.run(main())
```

[JSON Mode](https://console.groq.com/docs/text-chat#json-mode)
--------------------------------------------------------------

JSON mode is a specialized feature that guarantees all chat completions will be returned as valid JSON. This is particularly useful for applications that need to parse and process structured data from model responses.

For more information on ensuring that the JSON output adheres to a specific schema, jump to: [JSON Mode with Schema Validation](https://console.groq.com/docs/text-chat#json-mode-with-schema-validation).

### [How to Use JSON Mode](https://console.groq.com/docs/text-chat#how-to-use-json-mode)

To use JSON mode:

1.  Set `"response_format": {"type": "json_object"}` in your chat completion request
2.  Include a description of the desired JSON structure in your system prompt
3.  Process the returned JSON in your application

### [Best Practices for JSON Generation](https://console.groq.com/docs/text-chat#best-practices-for-json-generation)

*   **Choose the right model**: Llama performs best at generating JSON, followed by Gemma
*   **Format preference**: Request pretty-printed JSON instead of compact JSON for better readability
*   **Keep prompts concise**: Clear, direct instructions produce better JSON outputs
*   **Provide schema examples**: Include examples of the expected JSON structure in your system prompt

### [Limitations](https://console.groq.com/docs/text-chat#limitations)

*   JSON mode does not support streaming responses
*   Stop sequences cannot be used with JSON mode
*   If JSON generation fails, Groq will return a 400 error with code `json_validate_failed`

### [Example System Prompts](https://console.groq.com/docs/text-chat#example-system-prompts)

Here are practical examples showing how to structure system messages that will produce well-formed JSON:

#### [Data Analysis API](https://console.groq.com/docs/text-chat#data-analysis-api)

The Data Analysis API example demonstrates how to create a system prompt that instructs the model to perform sentiment analysis on user-provided text and return the results in a structured JSON format. This pattern can be adapted for various data analysis tasks such as classification, entity extraction, or summarization.

```
1from groq import Groq
2
3client = Groq()
4
5response = client.chat.completions.create(
6    model="llama-3.1-8b-instant",
7    messages=[
8        {
9            "role": "system",
10            "content": "You are a data analysis API that performs sentiment analysis on text. Respond only with JSON using this format: {\"sentiment_analysis\": {\"sentiment\": \"positive|negative|neutral\", \"confidence_score\": 0.95, \"key_phrases\": [{\"phrase\": \"detected key phrase\", \"sentiment\": \"positive|negative|neutral\"}], \"summary\": \"One sentence summary of the overall sentiment\"}}"
11        },
12        {
13            "role": "user",
14            "content": "Analyze the sentiment of this customer review: 'I absolutely love this product! The quality exceeded my expectations, though shipping took longer than expected.'"
15        }
16    ],
17    response_format={"type": "json_object"}
18)
19
20print(response.choices[0].message.content)
```

These examples show how to structure system prompts to guide the model to produce well-formed JSON with your desired schema.

Sample JSON output from the sentiment analysis prompt:

```
1{
2     "sentiment_analysis": {
3       "sentiment": "positive",
4       "confidence_score": 0.84,
5       "key_phrases": [
6          {
7             "phrase": "absolutely love this product",
8             "sentiment": "positive"
9          },
10          {
11             "phrase": "quality exceeded my expectations",
12             "sentiment": "positive"
13          }
14       ],
15       "summary": "The reviewer loves the product's quality, but was slightly disappointed with the shipping time."
16    }
17}
```

In this JSON response:

*   `sentiment`: Overall sentiment classification (positive, negative, or neutral)
*   `confidence_score`: A numerical value between 0 and 1 indicating the model's confidence in its sentiment classification
*   `key_phrases`: An array of important phrases extracted from the input text, each with its own sentiment classification
*   `summary`: A concise summary of the sentiment analysis capturing the main points

Using structured JSON outputs like this makes it easy for your application to programmatically parse and process the model's analysis. For more information on validating JSON outputs, see our dedicated guide on [JSON Mode with Schema Validation](https://console.groq.com/docs/text-chat#json-mode-with-schema-validation).

### [Code Examples](https://console.groq.com/docs/text-chat#code-examples)

The following Python example demonstrates how to use JSON mode with the Groq Chat Completions API. It sets up a request with a system prompt instructing the model to generate a JSON summary of a restaurant, then processes and displays the structured JSON response.

```
1from typing import List, Optional
2import json
3
4from pydantic import BaseModel
5from groq import Groq
6
7groq = Groq()
8
9
10# Data model for LLM to generate
11class Ingredient(BaseModel):
12    name: str
13    quantity: str
14    quantity_unit: Optional[str]
15
16
17class Recipe(BaseModel):
18    recipe_name: str
19    ingredients: List[Ingredient]
20    directions: List[str]
21
22
23def get_recipe(recipe_name: str) -> Recipe:
24    chat_completion = groq.chat.completions.create(
25        messages=[
26            {
27                "role": "system",
28                "content": "You are a recipe database that outputs recipes in JSON.\n"
29                # Pass the json schema to the model. Pretty printing improves results.
30                f" The JSON object must use the schema: {json.dumps(Recipe.model_json_schema(), indent=2)}",
31            },
32            {
33                "role": "user",
34                "content": f"Fetch a recipe for {recipe_name}",
35            },
36        ],
37        model="meta-llama/llama-4-scout-17b-16e-instruct",
38        temperature=0,
39        # Streaming is not supported in JSON mode
40        stream=False,
41        # Enable JSON mode by setting the response format
42        response_format={"type": "json_object"},
43    )
44    return Recipe.model_validate_json(chat_completion.choices[0].message.content)
45
46
47def print_recipe(recipe: Recipe):
48    print("Recipe:", recipe.recipe_name)
49
50    print("\nIngredients:")
51    for ingredient in recipe.ingredients:
52        print(
53            f"- {ingredient.name}: {ingredient.quantity} {ingredient.quantity_unit or ''}"
54        )
55    print("\nDirections:")
56    for step, direction in enumerate(recipe.directions, start=1):
57        print(f"{step}. {direction}")
58
59
60recipe = get_recipe("apple pie")
61print_recipe(recipe)
```

[JSON Mode with Schema Validation](https://console.groq.com/docs/text-chat#json-mode-with-schema-validation)
------------------------------------------------------------------------------------------------------------

Schema validation allows you to ensure that the response conforms to a schema, making them more reliable and easier to process programmatically.

While JSON mode ensures syntactically valid JSON, schema validation adds an additional layer of type checking and field validation to guarantee that the response not only parses as JSON but also conforms to your exact requirements.

### [Using Zod (or Pydantic in Python)](https://console.groq.com/docs/text-chat#using-zod-or-pydantic-in-python)

[Zod](https://zod.dev/) is a TypeScript-first schema validation library that makes it easy to define and enforce schemas. In Python, [Pydantic](https://pydantic.dev/) serves a similar purpose. This example demonstrates validating a product catalog entry with basic fields like name, price, and description.

```
1import os
2import json
3from groq import Groq
4from pydantic import BaseModel, Field, ValidationError # pip install pydantic
5from typing import List
6
7client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
8
9# Define a schema with Pydantic (Python's equivalent to Zod)
10class Product(BaseModel):
11    id: str
12    name: str
13    price: float
14    description: str
15    in_stock: bool
16    tags: List[str] = Field(default_factory=list)
17    
18# Prompt design is critical for structured outputs
19system_prompt = """
20You are a product catalog assistant. When asked about products,
21always respond with valid JSON objects that match this structure:
22{
23  "id": "string",
24  "name": "string",
25  "price": number,
26  "description": "string",
27  "in_stock": boolean,
28  "tags": ["string"]
29}
30Your response should ONLY contain the JSON object and nothing else.
31"""
32
33# Request structured data from the model
34completion = client.chat.completions.create(
35    model="llama-3.3-70b-versatile",
36    response_format={"type": "json_object"},
37    messages=[
38        {"role": "system", "content": system_prompt},
39        {"role": "user", "content": "Tell me about a popular smartphone product"}
40    ]
41)
42
43# Extract and validate the response
44try:
45    response_content = completion.choices[0].message.content
46    # Parse JSON
47    json_data = json.loads(response_content)
48    # Validate against schema
49    product = Product(**json_data)
50    print("Validation successful! Structured data:")
51    print(product.model_dump_json(indent=2))
52except json.JSONDecodeError:
53    print("Error: The model did not return valid JSON")
54except ValidationError as e:
55    print(f"Error: The JSON did not match the expected schema: {e}")
```

### [Benefits of Schema Validation](https://console.groq.com/docs/text-chat#benefits-of-schema-validation)

*   **Type Checking**: Ensure fields have the correct data types
*   **Required Fields**: Specify which fields must be present
*   **Constraints**: Set min/max values, length requirements, etc.
*   **Default Values**: Provide fallbacks for missing fields
*   **Custom Validation**: Add custom validation logic as needed

[Using Instructor Library](https://console.groq.com/docs/text-chat#using-instructor-library)
--------------------------------------------------------------------------------------------

The [Instructor library](https://useinstructor.com/) provides a more streamlined experience by combining API calls with schema validation in a single step. This example creates a structured recipe with ingredients and cooking instructions, demonstrating automatic validation and retry logic.

```
1import os
2from typing import List
3from pydantic import BaseModel, Field # pip install pydantic
4import instructor # pip install instructor
5from groq import Groq
6
7# Set up instructor with Groq
8client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
9# Patch the client with instructor
10instructor_client = instructor.patch(client)
11
12# Define your schema with Pydantic
13class RecipeIngredient(BaseModel):
14    name: str
15    quantity: str
16    unit: str = Field(description="The unit of measurement, like cup, tablespoon, etc.")
17
18class Recipe(BaseModel):
19    title: str
20    description: str
21    prep_time_minutes: int
22    cook_time_minutes: int
23    ingredients: List[RecipeIngredient]
24    instructions: List[str] = Field(description="Step by step cooking instructions")
25    
26# Request structured data with automatic validation
27recipe = instructor_client.chat.completions.create(
28    model="llama-3.3-70b-versatile",
29    response_model=Recipe,
30    messages=[
31        {"role": "user", "content": "Give me a recipe for chocolate chip cookies"}
32    ],
33    max_retries=2  # Instructor will retry if validation fails
34)
35
36# No need for try/except or manual validation - instructor handles it!
37print(f"Recipe: {recipe.title}")
38print(f"Prep time: {recipe.prep_time_minutes} minutes")
39print(f"Cook time: {recipe.cook_time_minutes} minutes")
40print("\nIngredients:")
41for ingredient in recipe.ingredients:
42    print(f"- {ingredient.quantity} {ingredient.unit} {ingredient.name}")
43print("\nInstructions:")
44for i, step in enumerate(recipe.instructions, 1):
45    print(f"{i}. {step}")
```

### [Advantages of Instructor](https://console.groq.com/docs/text-chat#advantages-of-instructor)

*   **Retry Logic**: Automatically retry on validation failures
*   **Error Messages**: Detailed error messages for model feedback
*   **Schema Extraction**: The schema is translated into prompt instructions
*   **Streamlined API**: Single function call for both completion and validation

[Prompt Engineering for Schema Validation](https://console.groq.com/docs/text-chat#prompt-engineering-for-schema-validation)
----------------------------------------------------------------------------------------------------------------------------

The quality of schema generation and validation depends heavily on how you formulate your system prompt. This example compares a poor prompt with a well-designed one by requesting movie information, showing how proper prompt design leads to more reliable structured data.

```
1import os
2import json
3from groq import Groq
4
5# Set your API key
6client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
7
8# Example of a poorly designed prompt
9poor_prompt = """
10Give me information about a movie in JSON format.
11"""
12
13# Example of a well-designed prompt
14effective_prompt = """
15You are a movie database API. Return information about a movie with the following 
16JSON structure:
17
18{
19  "title": "string",
20  "year": number,
21  "director": "string",
22  "genre": ["string"],
23  "runtime_minutes": number,
24  "rating": number (1-10 scale),
25  "box_office_millions": number,
26  "cast": [
27    {
28      "actor": "string",
29      "character": "string"
30    }
31  ]
32}
33
34The response must:
351. Include ALL fields shown above
362. Use only the exact field names shown
373. Follow the exact data types specified
384. Contain ONLY the JSON object and nothing else
39
40IMPORTANT: Do not include any explanatory text, markdown formatting, or code blocks.
41"""
42
43# Function to run the completion and display results
44def get_movie_data(prompt, title="Example"):
45    print(f"\n--- {title} ---")
46    
47    completion = client.chat.completions.create(
48        model="llama-3.3-70b-versatile",
49        response_format={"type": "json_object"},
50        messages=[
51            {"role": "system", "content": prompt},
52            {"role": "user", "content": "Tell me about The Matrix"}
53        ]
54    )
55    
56    response_content = completion.choices[0].message.content
57    print("Raw response:")
58    print(response_content)
59    
60    # Try to parse as JSON
61    try:
62        movie_data = json.loads(response_content)
63        print("\nSuccessfully parsed as JSON!")
64        
65        # Check for expected fields
66        expected_fields = ["title", "year", "director", "genre", 
67                          "runtime_minutes", "rating", "box_office_millions", "cast"]
68        missing_fields = [field for field in expected_fields if field not in movie_data]
69        
70        if missing_fields:
71            print(f"Missing fields: {', '.join(missing_fields)}")
72        else:
73            print("All expected fields present!")
74            
75    except json.JSONDecodeError:
76        print("\nFailed to parse as JSON. Response is not valid JSON.")
77
78# Compare the results of both prompts
79get_movie_data(poor_prompt, "Poor Prompt Example")
80get_movie_data(effective_prompt, "Effective Prompt Example")
```

### [Key Elements of Effective Prompts](https://console.groq.com/docs/text-chat#key-elements-of-effective-prompts)

1.  **Clear Role Definition**: Tell the model it's an API or data service
2.  **Complete Schema Example**: Show the exact structure with field names and types
3.  **Explicit Requirements**: List all requirements clearly and numerically
4.  **Data Type Specifications**: Indicate the expected type for each field
5.  **Format Instructions**: Specify that the response should contain only JSON
6.  **Constraints**: Add range or validation constraints where applicable

### [Working with Complex Schemas](https://console.groq.com/docs/text-chat#working-with-complex-schemas)

Real-world applications often require complex, nested schemas with multiple levels of objects, arrays, and optional fields. This example creates a detailed product catalog entry with variants, reviews, and manufacturer information, demonstrating how to handle deeply nested data structures.

```
1import os
2from typing import List, Optional, Dict, Union
3from pydantic import BaseModel, Field # pip install pydantic
4from groq import Groq
5import instructor # pip install instructor
6
7# Set up the client with instructor
8client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
9instructor_client = instructor.patch(client)
10
11# Define a complex nested schema
12class Address(BaseModel):
13    street: str
14    city: str
15    state: str
16    zip_code: str
17    country: str
18
19class ContactInfo(BaseModel):
20    email: str
21    phone: Optional[str] = None
22    address: Address
23
24class ProductVariant(BaseModel):
25    id: str
26    name: str
27    price: float
28    inventory_count: int
29    attributes: Dict[str, str]
30
31class ProductReview(BaseModel):
32    user_id: str
33    rating: float = Field(ge=1, le=5)
34    comment: str
35    date: str
36
37class Product(BaseModel):
38    id: str
39    name: str
40    description: str
41    main_category: str
42    subcategories: List[str]
43    variants: List[ProductVariant]
44    reviews: List[ProductReview]
45    average_rating: float = Field(ge=1, le=5)
46    manufacturer: Dict[str, Union[str, ContactInfo]]
47
48# System prompt with clear instructions about the complex structure
49system_prompt = """
50You are a product catalog API. Generate a detailed product with ALL required fields.
51Your response must be a valid JSON object matching the following schema:
52
53{
54  "id": "string",
55  "name": "string",
56  "description": "string",
57  "main_category": "string",
58  "subcategories": ["string"],
59  "variants": [
60    {
61      "id": "string",
62      "name": "string",
63      "price": number,
64      "inventory_count": number,
65      "attributes": {"key": "value"}
66    }
67  ],
68  "reviews": [
69    {
70      "user_id": "string",
71      "rating": number (1-5),
72      "comment": "string",
73      "date": "string (YYYY-MM-DD)"
74    }
75  ],
76  "average_rating": number (1-5),
77  "manufacturer": {
78    "name": "string",
79    "founded": "string",
80    "contact_info": {
81      "email": "string",
82      "phone": "string (optional)",
83      "address": {
84        "street": "string",
85        "city": "string", 
86        "state": "string",
87        "zip_code": "string",
88        "country": "string"
89      }
90    }
91  }
92}
93"""
94
95# Use instructor to create and validate in one step
96product = instructor_client.chat.completions.create(
97    model="llama-3.3-70b-versatile",
98    response_model=Product,
99    messages=[
100        {"role": "system", "content": system_prompt},
101        {"role": "user", "content": "Give me details about a high-end camera product"}
102    ],
103    max_retries=3
104)
105
106# Print the validated complex object
107print(f"Product: {product.name}")
108print(f"Description: {product.description[:100]}...")
109print(f"Variants: {len(product.variants)}")
110print(f"Reviews: {len(product.reviews)}")
111print(f"Manufacturer: {product.manufacturer.get('name')}")
112print("\nManufacturer Contact:")
113contact_info = product.manufacturer.get('contact_info')
114if isinstance(contact_info, ContactInfo):
115    print(f"  Email: {contact_info.email}")
116    print(f"  Address: {contact_info.address.city}, {contact_info.address.country}")
```

### [Tips for Complex Schemas](https://console.groq.com/docs/text-chat#tips-for-complex-schemas)

*   **Decompose**: Break complex schemas into smaller, reusable components
*   **Document Fields**: Add descriptions to fields in your schema definition
*   **Provide Examples**: Include examples of valid objects in your prompt
*   **Validate Incrementally**: Consider validating subparts of complex responses separately
*   **Use Types**: Leverage type inference to ensure correct handling in your code

### [Best Practices](https://console.groq.com/docs/text-chat#best-practices)

*   Start simple and add complexity as needed.
*   Make fields optional when appropriate.
*   Provide sensible defaults for optional fields.
*   Use specific types and constraints rather than general ones.
*   Add descriptions to your schema definitions.

### Was this page helpful?
