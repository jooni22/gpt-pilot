If you have your own OpenAI API key, you can easily use it with Pythagora VisualStudio Code extension.

**NOTE: Your OpenAI API key must have access to GPT4 model, which means you need to make at least $5 payment to OpenAI to activate it. This is separate from your ChatGPT Plus subscription (if you have one). Read more here: https://bit.ly/openai-how-can-i-access-gpt-4**

Here's how you can use Pythagora VisualStudio Code extension with your own OpenAI API key:

1. Close VisualStudio Code
2. Edit `config.json` file in your GPT Pilot installation folder and in `llm.openai` section, change `api_key` from `null` to your API key. Then, change `base_url` for the LLM:

For OpenAI:

```
"llm": {
  "openai": {
    "base_url": "https://api.openai.com/v1/",
    "api_key": "sk-your-api-key",
```

For Anthropic:

```
"llm": {
  "anthropic": {
    "base_url": "https://api.anthropic.com/",
    "api_key": "sk-your-api-key",
```

3. If there's no `config.json` file, that means you're on an older version of GPT Pilot (0.1.x) and you'll need to modify `pilot/.env` file instead and set `OPENAI_API_KEY` to correct value)
3. Open VisualStudio Code, start Pythagora, go to settings and you should see the message *You're using your own OpenAI key*
4. That's it!

### Using Pythagora keys

If you're currently using your own keys and would like to subscribe to Pythagora and use its managed keys instead, just do the reverse:

1. Close VisualStudio Code
2. Edit the `config.json` file in your GPT Pilot installation folder and set `llm.openai.api_key` to `null`
3. Open VisualStudio Code, start Pythagora, go to settings and you should see the message *You're on free trial* or *Your free trial has expired*, and a *Subscribe to Pythagora* button
4. Clicking the button will send you an email with available plans. Once you subscribe to any of them, the settings panel in Pythagora extension will update to *You're using Pythagora Pro* or similar message (depending on the exact plan you choose)

*NOTE*: Your GPT Pilot installation folder is the folder you selected to install GPT Pilot in when you set up Pythagora. It is visible in Pythagora settings. For example if this folder is `/Users/me/Projects/`, then there should be a GPT Pilot installation in `/users/me/Projects/gpt-pilot`, and the `config.json` file you need to modify is in `/Users/me/Projects/gpt-pilot/config.json`.