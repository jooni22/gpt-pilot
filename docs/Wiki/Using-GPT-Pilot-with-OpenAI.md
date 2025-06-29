_Note: This article is for using GPT Pilot locally via the terminal. For info on how to use your own API key via the Pythagora VS Code extension, [read this article](https://github.com/Pythagora-io/gpt-pilot/wiki/Using-the-Pythagora-VS-Code-extension-with-your-own-API-key)._

0 - Be sure to first follow the steps in [How to start using GPT Pilot](https://github.com/Pythagora-io/gpt-pilot?tab=readme-ov-file#how-to-start-using-gpt-pilot) from the GPT Pilot README to setup GPT Pilot via the terminal.

1 - Go to the [OpenAI website](https://platform.openai.com/api-keys) and get an API key.

2 - If you haven't already, in your cloned GPT Pilot repo, make a copy of the `example-config.json` file and name it `config.json`.

3 - Edit the new `config.json` file's `llm` section and also remove the other providers that you're not using:

```json
"llm": {
  "openai": {
    "base_url": "https://api.openai.com/v1/",
    "api_key": "sk-your-api-key",
```

4 - Update the `models` section of the `config.json` file for OpenAI (if not already set as `openai` by default). Note: This is example code, you'll need to double-check the [official OpenAI documentation](https://platform.openai.com/docs/models) for the most recent model info:

```json
"agent": {
    "default": {
      "provider": "openai",
      "model": "gpt-4o-2024-05-13",
      "temperature": 0.5
    },
```

5 - Remove any commented out code from the `config.json` file.

6 - After making changes to your `config.json` file, if you're using the VS Code extension, you will need to restart VS Code for the changes to be reflected in the settings page.

7 - That's it!