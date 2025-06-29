_Note: This is only applicable to users who want to use Pythagora with their own API key. Pythagora users with a monthly subscription do not need to follow the steps below, as no API key is required for paid users._

To setup the Pythagora VS Code extension using your own API key:

1 - Open the directory where you installed the Pythagora core files. 

* In Local development mode, this directory will be specified by you inside of [Pythagora's settings](https://share.zight.com/QwuJmgx1) underneath `Pythagora Core path`.

* In Cloud development mode, open a new `Terminal` tab directly inside of VS Code (as opposed to using a separate command line application). Navigate to `/pythagora/pythagora-core`.

2 - Open the `config.json` file.

3 - Edit the `config.json` file to include the LLM you want to use and remove the other LLMs that you won't use. 

4 - Add your own API keys and update the `base_url` to the `config.json` file:

* For OpenAI, the `llm` section of the `config.json` file should have:  

```json
"llm": {
  "openai": {
    "base_url": "https://api.openai.com/v1/",
    "api_key": "sk-your-api-key",
```

* For Anthropic:

```json
"llm": {
  "anthropic": {
    "base_url": "https://api.anthropic.com/",
    "api_key": "sk-your-api-key",
    "connect_timeout": 60,
    "read_timeout": 60,
    "extra": null
```

5 - Update the all of the agents in the `agent` section of the `config.json` file so the `provider` and `model` properties contain the correct LLM and model. An example of one agent using Anthropic (note: there may be more than one agent):

```json
"agent": {
    "default": {
      "provider": "anthropic",
      "model": "claude-3-5-sonnet-20240620",
      "temperature": 0.5
      "connect_timeout": 60,
      "read_timeout": 60,
      "extra": null
    },
```

Note: Double-check the LLM's official documentation to ensure you have the correct model number. [Click here for the OpenAI documentation](https://platform.openai.com/docs/models). And [ here for Anthropic's docs](https://docs.anthropic.com/claude/docs/models-overview#model-recommendations). The wiki's [Integrations Guides section](https://github.com/Pythagora-io/gpt-pilot/wiki#integration-guides) has additional config examples for local LLM's, etc.

6 - Remove any commented out code from the `config.json` file.

7 - That's it! Pythagora's settings page should show that you're using your own API key.

# Example config file using both OpenAI and Anthropic:

Note: In your own `config.json` file, be sure to only edit the `llm` and `agent` sections. The remaining sections contain data unique to your installation, such as the installation directory in the `prompt` section, etc.

**If you copy/paste the entire example code into your own `config.json` file it will not work properly.**

```json
{
  "llm": {
    "openai": {
      "base_url": "https://api.openai.com/v1/",
      "api_key": "open_ai_api_key_here",
      "connect_timeout": 60.0,
      "read_timeout": 60.0,
      "extra": null
    },
    "anthropic": {
      "base_url": "https://api.anthropic.com/",
      "api_key": "anthropic_api_key_here",
      "connect_timeout": 60.0,
      "read_timeout": 60.0,
      "extra": null
    }
  },
  "agent": {
    "default": {
      "provider": "openai",
      "model": "gpt-4o-2024-05-13",
      "temperature": 0.5
    },
    "BugHunter.check_logs": {
      "provider": "anthropic",
      "model": "claude-3-7-sonnet-20250219",
      "temperature": 0.5
    },
    "CodeMonkey": {
      "provider": "anthropic",
      "model": "claude-3-7-sonnet-20250219",
      "temperature": 0.0
    },
    "CodeMonkey.code_review": {
      "provider": "anthropic",
      "model": "claude-3-5-sonnet-20240620",
      "temperature": 0.0
    },
    "CodeMonkey.describe_files": {
      "provider": "openai",
      "model": "gpt-4o-mini-2024-07-18",
      "temperature": 0.0
    },
    "Frontend": {
      "provider": "anthropic",
      "model": "claude-3-5-sonnet-20241022",
      "temperature": 0.0
    },
    "get_relevant_files": {
      "provider": "openai",
      "model": "gpt-4o-2024-05-13",
      "temperature": 0.5
    },
    "Developer.parse_task": {
      "provider": "anthropic",
      "model": "claude-3-5-sonnet-20241022",
      "temperature": 0.0
    },
    "SpecWriter": {
      "provider": "openai",
      "model": "gpt-4-0125-preview",
      "temperature": 0.0
    },
    "Developer.breakdown_current_task": {
      "provider": "anthropic",
      "model": "claude-3-7-sonnet-20250219",
      "temperature": 0.5
    },
    "TechLead.plan_epic": {
      "provider": "anthropic",
      "model": "claude-3-5-sonnet-20240620",
      "temperature": 0.5
    },
    "TechLead.epic_breakdown": {
      "provider": "anthropic",
      "model": "claude-3-5-sonnet-20241022",
      "temperature": 0.5
    },
    "Troubleshooter.generate_bug_report": {
      "provider": "anthropic",
      "model": "claude-3-7-sonnet-20250219",
      "temperature": 0.5
    },
    "Troubleshooter.get_run_command": {
      "provider": "anthropic",
      "model": "claude-3-7-sonnet-20250219",
      "temperature": 0.0
    }
  },
  "prompt": {
    "paths": [
      "/Users/Py-example-user/pythagora-core/core/prompts"
    ]
  },
  "log": {
    "level": "DEBUG",
    "format": "%(asctime)s %(levelname)s [%(name)s] %(message)s",
    "output": "pythagora.log"
  },
  "db": {
    "url": "sqlite+aiosqlite:///data/database/pythagora.db",
    "debug_sql": false
  },
  "ui": {
    "type": "plain"
  },
  "fs": {
    "type": "local",
    "workspace_root": "/Users/Py-example-user/pythagora-core/workspace",
    "ignore_paths": [
      ".git",
      ".gpt-pilot",
      ".idea",
      ".vscode",
      ".next",
      ".DS_Store",
      "__pycache__",
      "site-packages",
      "node_modules",
      "package-lock.json",
      "venv",
      ".venv",
      "dist",
      "build",
      "target",
      "*.min.js",
      "*.min.css",
      "*.svg",
      "*.csv",
      "*.log",
      "go.sum",
      "migration_lock.toml"
    ],
    "ignore_size_threshold": 50000
  }
}
```