GPT Pilot is developed primarily with OpeAI GPT-4 in mind. This is because it is currently the best model on the market for general programming tasks (not just writing code but also planning, debugging, and everything else related to the development).

This means that GPT Pilot uses OpenAI API (to access GPT-4), and also that the prompts are all optimized for GPT4.

While it is possible to run GPT Pilot with another LLM, **you will need to modify the prompts to make it work - expect a lot of trial and error there**.

## Command-line setup

That said, here's how you can use the command-line version of GPT Pilot with your local LLM of choice:

### GPT-Pilot configuration (0.2.x)

If you're using the latest version of GPT Pilot, it stores the configuration in `config.json` file. Follow these steps to set it up:

1. [Set up GPT-Pilot](https://github.com/Pythagora-io/gpt-pilot#how-to-start-using-gpt-pilot)
2. Install a local API proxy (see below for choices)
3. Edit `config.json` file in `gpt-pilot` directory (this is the file you'd edit to use your own OpenAI, Anthropic or Azure key), and update `llm.openai` section to something required by the local proxy, for example:

    ```
    "llm": {
      "openai": {
        "base_url": "http://0.0.0.0:8000/",
        "api_key": "dummy-key",
        "connect_timeout": 60.0,
        "read_timeout": 10.0
      },
      "agent": {
        "default": {
          "provider": "openai",
          "model": "your-local-model",
        },
        ...
      }
    }
    ```
4. Start the API Proxy in a separate terminal, then start GPT Pilot as usual (via the VSCode extension, or in command-line):
    ```
    cd /path/to/gpt-pilot
    source venv/bin/activate # (or venv\Scripts\activate on Windows)
    python main.py 
    ```

Note: the OpenAI client sets some settings (like usage tracking in streaming responses) that are not available on most OpenAI-compatible servers. Most servers have an option to "strip unrecognized options from requests" and you'll probably need to enable that to ignore non-supported OpenAI options.

### GPT Pilot 0.1 setup

If for some reason you're using gpt-pilot 0.1 and not the new 0.2.x version, follow these instructions instead:

1. Install a local API proxy (see below for choices)
2. Edit `.env` file in `gpt-pilot/pilot/` directory (this is the file you would have to set up with your OpenAI keys in step 1), to set `OPENAI_ENDPOINT` and `OPENAI_API_KEY` to something required by the local proxy; for example:
    ```
    # This differs for different local llm proxies, this is just an example
    OPENAI_ENDPOINT=http://0.0.0.0:8000/chat/completions
    OPENAI_API_KEY=dummy
    ```
3. Start the API Proxy in a separate terminal, then start GPT Pilot as usual:
    ```
    cd /path/to/gpt-pilot
    source pilot-env/bin/activate # (or pilot-env\Scripts\activate on Windows)
    cd pilot/
    python main.py
    ```

## Visual Studio Code extension

The extension currently doesn't allow changing the endpoint/key settings so it can't be used out of the box. However, it uses the command-line GPT Pilot under the hood so you can configure these settings in the same way.

1. Install [the VSCode GPT Pilot extension](https://marketplace.visualstudio.com/items?itemName=PythagoraTechnologies.gpt-pilot-vs-code)
2. Start the extension. On the first run, you will need to select an empty folder where the GPT Pilot will be downloaded and configured. This will take a few minutes.
3. Open a terminal and go to that folder. The `gpt-pilot/config.json` file should have already been created, and you can proceed with the same steps as for the command line version (see above).

## Local LLM routers

### LM Studio

[LM Studio](https://lmstudio.ai/) is an easy way to discover, download and run local LLMs, and is available for Windows, Mac and Linux. After selecting a downloading an LLM, you can go to the `Local Inference Server` tab, select the model and then start the server.

Then edit the `config.json` in GPT Pilot directory to set:

```
"llm": {
  "openai": {
    "base_url": "http://localhost:1234/v1/",
    "api_key": "dummy",
    "connect_timeout": 60.0,
    "read_timeout": 10.0
  }
},
"agent": {
  "default": {
    "provider": "openai",
    "model": "your-local-model",
   },
   ...
}
```

(The port 1234 is default in LM Studio, you can use any free port just make sure it's the same in LM Studio and the .env file).

### LiteLLM

[LiteLLM](https://github.com/BerriAI/litellm) can proxy for a lot of remote or local LLMs, including `ollama`, `vllm` and `huggingface` (meaning it can run most of the models that these programs can run. Here is [the full list of supported LLM providers](https://github.com/BerriAI/litellm#supported-provider-docs), with instructions how to set them up.

The full documentation to set up LiteLLM with a local proxy server is [here](https://docs.litellm.ai/docs/proxy/quick_start), but in a nutshell:

```
pip install litellm[proxy]
```

Test it with `litellm --test`

After you set it up (as per the quickstart above), run it with:

```
litellm --model yourmodel --drop_params
```

(The `--drop_params` flag is here to ignore OpenAI specific flags that wouldn't work for other LLMs).

Then edit the `config.json` in GPT Pilot directory to set:

```
"llm": {
  "openai": {
    "base_url": "http://0.0.0.0:8000/",
    "api_key": "dummy",
    "connect_timeout": 60.0,
    "read_timeout": 10.0
  },
},
"agent": {
  "default": {
    "provider": "openai",
    "model": "your-local-model",
   },
   ...
}
```

(if you change the default port in litellm configuration, be sure to also update your `config.json`).

## Tweaking the prompts

As you're using GPT Pilot, watch the output that LLM makes. It will probably get stuck in a loop, or producing nonsense output, and you'll need to tweak the prompts for the specific LLM you're using.

First, add a new prompt directory where GPT Pilot will search for your prompts, so you don't have to overwrite the original ones:

1. Open the terminal, go to GPT Pilot directory and activate the Python virtual environment (see above)
2. Run `python main.py --show-config` to see the current configuration
3. Notice there's a "prompt" section with the default directory (within GPT Pilot installation), copy-paste that into your existing `config.json` if it isn't there already. Then modify the section to insert your custom directory above the default one, like in this example:
  ```
  "prompt": {
    "paths": [
      "/Users/your-user/Projects/gpt-pilot/your-custom-prompts",
      "/Users/your-user/Projects/gpt-pilot/core/prompts"
    ]
  },
  ```
4. Check the prompt files and folders in `core/prompts`. To override a prompt, create the file with the same name in the same folder within your custom prompts directory.
5. (Re)start Pythagora

The initial setup is a bit tedious, but after this you can just open a text editor and tweak how Pythagora works - No programming knowledge needed!

## Credits

Thanks to our [Discord community](https://discord.gg/HaqXugmxr9) members `@HeliosPrime`, `@Kujila` and `@Limenarity` for diving into, researching, and hacking GPT Pilot to make work (communicate with) the local LLMs. This tutorial is mostly based on the work they shared on GPT Pilot Discord channels.
