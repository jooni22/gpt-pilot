_Note: This article is for using GPT Pilot locally via the terminal. For info on how to use your own API key via the Pythagora VS Code extension, [read this article](https://github.com/Pythagora-io/gpt-pilot/wiki/Using-the-Pythagora-VS-Code-extension-with-your-own-API-key)._

0 - Be sure to first follow the steps in the [How to start using GPT Pilot](https://github.com/Pythagora-io/gpt-pilot?tab=readme-ov-file#how-to-start-using-gpt-pilot) article to setup GPT Pilot via the terminal.

1 - To use Anthropic, [get an API key from the Anthropic website](https://console.anthropic.com). 

2 - If you haven't already, in your cloned GPT Pilot repo, make a copy of the `example-config.json` file and name it `config.json`.

3 - Edit the new `config.json` file's `llm` section. If you're using Anthropic via a proxy or through AWS Bedrock, you'll also need to set `base_url` accordingly from the default `null`:

```json
"llm": {
  "anthropic": {
    "base_url": "https://api.anthropic.com/",
    "api_key": "your-anthropic-key",
    "connect_timeout": 60.0,
    "read_timeout": 10.0
  }
},
```

4 - Update the `agent` section of the `config.json` file for Anthropic. Note: This is an example, you'll need to double-check the [official Anthropic documentation](https://docs.anthropic.com/claude/docs/models-overview#model-recommendations) for the most recent model info:

```json
"agent": {
    "default": {
      "provider": "anthropic",
      "model": "claude-3-5-sonnet-20240620",
      "temperature": 0.5
    }
```

5 - Remove any commented out code from the `config.json` file.

6 - After making changes to your `config.json` file, if you're using the VS Code extension, you will need to restart VS Code for the changes to be reflected in the settings page.

7 - That's it! 
