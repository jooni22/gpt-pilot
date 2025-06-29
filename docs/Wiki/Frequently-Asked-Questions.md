# Pythagora FAQ

These are some of the most frequently asked questions about Pythagora. There's additional articles in [our wiki](https://github.com/Pythagora-io/gpt-pilot/wiki). If you're new to Pythagora, check out the YouTube playlist [How to use Pythagora Like a Pro](https://www.youtube.com/watch?v=HIIHx0kErPc&list=PLbi3WiEeXr2wdppQ575zSLbcORou-Lxd1). There's additional help videos on our [YouTube channel](https://www.youtube.com/@pythagoraa).

If you don't find an answer below, [try asking in our Discord community](https://discord.gg/HaqXugmxr9) or you can [contact us here](https://github.com/Pythagora-io/gpt-pilot/wiki/Contact-Us).

---

# Table of Contents

## General Information
- [What is the difference between Pythagora and GPT Pilot?](#what-is-the-difference-between-pythagora-and-gpt-pilot)
- [What is Pythagora v1 and how does it differ than the beta VS Code extension?](#what-is-pythagora-v1-and-how-does-it-differ-than-the-beta-vs-code-extension)
- [How do I get access to Pythagora v1?](#how-do-i-get-access-to-pythagora-v1)

## Pricing & Subscription
- [What is Pythagora Pro?](#what-is-pythagora-pro)
- [What is the pricing if I use my own API key?](#what-is-the-pricing-if-i-use-my-own-api-key)

## Technical Requirements & Compatibility
- [Which version of Python do I need?](#which-version-of-python-do-i-need)
- [Which LLMs and models can I use?](#which-llms-and-models-can-i-use)
- [Which language(s) does Pythagora support?](#which-languages-does-pythagora-support)

## Installation & Setup
- [The Pythagora VSCode extension asks me to log in? What am I logging into?](#the-pythagora-vscode-extension-asks-me-to-log-in-what-am-i-logging-into)
- [How do I set up Pythagora using third-party API keys?](#how-do-i-set-up-pythagora-using-third-party-api-keys)
- [I entered my API key but I get "you don't have access to gpt-4" or "openai model not found" error](#i-entered-my-api-key-but-i-get-you-dont-have-access-to-gpt-4-or-openai-model-not-found-error)
- [How do I upgrade from Pythagora beta to Pythagora v1?](#how-do-i-upgrade-from-pythagora-beta-to-pythagora-v1)
- [How do I get started with Pythagora?](#how-do-i-get-started-with-pythagora)
- [Developing locally vs. in the cloud with Pythagora](#developing-locally-vs-in-the-cloud-with-pythagora)
- [Using MongoDB with Pythagora](#using-mongodb-with-pythagora)
- [Changing Pythagora's installation directory](#changing-pythagoras-installation-directory)
- [How to update the Pythagora VS Code extension](#how-to-update-the-pythagora-vs-code-extension)

## Building Applications
- [How to write a good initial project description](#how-to-write-a-good-initial-project-description)
- [Initial project description examples](#initial-project-description-examples)
- [Pythagora App Lab](#pythagora-app-lab)

## Troubleshooting
- [How do I get help with my question/bug/issue?](#how-do-i-get-help-with-my-questionbugissue)
- [My old projects are missing under the `Load App` menu after updating the Pythagora extension](#my-old-projects-are-missing-under-the-load-app-menu-after-updating-the-pythagora-extension)
- [I start Pythagora/GPT Pilot and get an error like `TypeError: 'type' object is not subscriptable`](#i-start-pythagoragpt-pilot-and-get-an-error-like-typeerror-type-object-is-not-subscriptable)
- [I get the following error in the VSCode extension: "No module named dotenv"](#i-get-the-following-error-in-the-vscode-extension-no-module-named-dotenv)
- [Pythagora/GPT Pilot is very slow and eats tokens like there's no tomorrow, why?](#pythagoragpt-pilot-is-very-slow-and-eats-tokens-like-theres-no-tomorrow-why)
- [I got `TokenLimitError`, how to work around it?](#i-got-tokenlimiterror-how-to-work-around-it)

## Miscellaneous
- [This rocks! Can I buy you coffee?](#this-rocks-can-i-buy-you-coffee)

---

# General Information

## What is the difference between Pythagora and GPT Pilot?
Pythagora is our [VS Code extension](https://marketplace.visualstudio.com/items?itemName=PythagoraTechnologies.pythagora-vs-code) as well as the name of [our company](https://www.pythagora.ai). GPT Pilot is our [open source codebase](https://github.com/Pythagora-io/gpt-pilot) Pythagora is built on top of. GPT Pilot is licensed under a [Fair Source License](https://blog.pythagora.ai/2025/01/30/pythagora-supports-fair-source).

## What is Pythagora v1 and how does it differ than the beta VS Code extension?
Version 1 (v1) of the Pythagora VS Code extension was released in October 2024. v1 is a completely new VS Code extension, and the old beta version has been deprecated.

## How do I get access to Pythagora v1?
You can install the extension directly from the [VS Code Marketplace](https://marketplace.visualstudio.com/items?itemName=PythagoraTechnologies.pythagora-vs-code).

# Pricing & Subscription

## What is Pythagora Pro?
Pythagora Pro is our monthly subscription pricing model. You can view our [pricing info on our homepage](https://www.pythagora.ai). Pythagora Pro is optimized for builders and makers, offering a user-friendly experience without the need for manual configuration. With Pro, you also gain access to **Pythagora Chat**, which allows you to ask questions about your application, as the chat understands the context of your app.

## What is the pricing if I use my own API key?
If you’re using your own API key(s), the cost will depend on the LLM provider(s) and model(s) you choose. You can use your own API keys from providers like OpenAI, Anthropic, or local LLMs. If you run Pythagora using your own API keys, a Pythagora Pro subscription isn’t required; however, you may incur costs from your chosen LLM provider.

# Technical Requirements & Compatibility

## Which version of Python do I need?
Pythagora requires Python version between 3.9 and 3.13. Check your version by running:

```
python --version
python3 --version
```

## Which LLMs and models can I use?
For paid Pythagora users, we recommend not making any changes to the LLM providers and/or models used. Our team does extensive testing to ensure that Pythagora uses the best models currently available for all of Pythagora's agents. Modifying the configuration to use different models may cause Pythagora to underperform or not work as expected.

## Which language(s) does Pythagora support?
- **Backend:** Node.js, MongoDB, Express.
- **Frontend:** Vite, React, TypeScript, Shadcn, Tailwind CSS.

Our dev team rigorously tests using this stack, focusing on web app development. Once we’ve refined the experience with these technologies, we plan to expand support to other languages and frameworks.

# Installation & Setup

## The Pythagora VSCode extension asks me to log in? What am I logging into?
We're building a cloud version of Pythagora, so the extension requires a login for access control. This is separate from your OpenAI or Anthropic account. 

## How do I set up Pythagora using third-party API keys?
* [Using the Pythagora VS Code extension with your own API key](https://github.com/Pythagora-io/gpt-pilot/wiki/Using-the-Pythagora-VS-Code-extension-with-your-own-API-key)
* [Using GPT Pilot with OpenAI](https://github.com/Pythagora-io/gpt-pilot/wiki/Using-GPT-Pilot-with-OpenAI)
* [Using GPT Pilot with Anthropic](https://github.com/Pythagora-io/gpt-pilot/wiki/Using-GPT-Pilot-with-Anthropic-models)
* [Using GPT Pilot with local LLMs](https://github.com/Pythagora-io/gpt-pilot/wiki/Using-GPT%E2%80%90Pilot-with-Local-LLMs)

## I entered my API key but I get "you don't have access to gpt-4" or "openai model not found" error
Ensure you have a paid subscription to OpenAI's API and/or Anthropic's API. Check your access at [OpenAI API Playground](https://platform.openai.com/playground/).

## How do I upgrade from Pythagora beta to Pythagora v1?
To upgrade from the beta version to Pythagora v1, follow the instructions in our [wiki guide](https://github.com/Pythagora-io/gpt-pilot/wiki/How-to-upgrade-from-Pythagora-beta-to-Pythagora-v1).

## How do I get started with Pythagora?
For a step-by-step guide on getting started with Pythagora, check out our [wiki article](https://github.com/Pythagora-io/gpt-pilot/wiki/How-to-get-started-with-Pythagora).

## Developing locally vs. in the cloud with Pythagora
Learn about the differences between developing locally and in the cloud with Pythagora in our [wiki guide](https://github.com/Pythagora-io/gpt-pilot/wiki/Developing-locally-verses-in-the-cloud-with-Pythagora).

## Using MongoDB with Pythagora
For instructions on using MongoDB with Pythagora, refer to our [wiki guide](https://github.com/Pythagora-io/gpt-pilot/wiki/Using-MongoDB-with-Pythagora).

## Changing Pythagora's installation directory
To change the installation directory for Pythagora, follow the steps in our [wiki guide](https://github.com/Pythagora-io/gpt-pilot/wiki/Changing-Pythagora's-installation-directory).

## How to update the Pythagora VS Code extension
For instructions on updating the Pythagora VS Code extension, check out our [wiki guide](https://github.com/Pythagora-io/gpt-pilot/wiki/How-to-update-the-Pythagora-VS-Code-extension).

# Building Applications

## How to write a good initial project description
A well-written project description is key to getting the best results from Pythagora. Learn how to write a good initial project description in our [wiki guide](https://github.com/Pythagora-io/gpt-pilot/wiki/How-to-write-a-good-initial-project-description).

## Initial project description examples
For examples of good initial project descriptions, check out our [wiki article](https://github.com/Pythagora-io/gpt-pilot/wiki/Initial-project-description-examples).

## Pythagora App Lab
Explore example applications created with Pythagora in our [Pythagora App Lab](https://github.com/Pythagora-io/gpt-pilot/wiki/Pythagora-App-Lab).

# Troubleshooting

## How do I get help with my question/bug/issue?
If you encounter any issues or have questions, you can:
- Check our [wiki](https://github.com/Pythagora-io/gpt-pilot/wiki) for detailed guides and troubleshooting tips.
- Join our [Discord community](https://discord.gg/HaqXugmxr9) to ask questions and get support from other users and the Pythagora team.
- [Contact us directly](https://github.com/Pythagora-io/gpt-pilot/wiki/Contact-Us) for personalized assistance.

## My old projects are missing under the `Load App` menu after updating the Pythagora extension
If you’ve upgraded from an older version of Pythagora, you may need to migrate your old projects. Follow the steps in the [Migrating Old Projects](https://github.com/Pythagora-io/gpt-pilot/wiki/How-to-update-the-Pythagora-VS-Code-extension#migrating-old-projects) section of our wiki.

## I start Pythagora/GPT Pilot and get an error like `TypeError: 'type' object is not subscriptable`
Ensure you're using Python 3.9+. If you have multiple Python installations, make sure Pythagora is using the correct version.

## I get the following error in the VSCode extension: "No module named dotenv"
The Python virtual environment may not have been set up correctly. Try manually setting up the virtual environment as described in our [wiki](https://github.com/Pythagora-io/gpt-pilot/wiki).

## Pythagora/GPT Pilot is very slow and eats tokens like there's no tomorrow, why?
Pythagora slows down as the number of files in your project increases.

## I got `TokenLimitError`, how to work around it?
List large or unnecessary files in the `fs.ignore_paths` section of your `config.json` file.

# Miscellaneous

## This rocks! Can I buy you coffee?
Thanks! The best way to support us is to share Pythagora with others, star the [GPT Pilot repo](https://github.com/Pythagora-io/gpt-pilot), and participate in our [Discord community](https://discord.gg/HaqXugmxr9)!