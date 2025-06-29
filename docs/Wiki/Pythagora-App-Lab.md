Welcome to the Pythagora App Lab! 

This page showcases apps built entirely with Pythagora; no human written code involved. View our [YouTube playlist Pythagora App Lab](https://www.youtube.com/playlist?list=PLbi3WiEeXr2zPfh2W734HMG3gX5lBgqj7) to see an overview of the apps created. Feel free to fork the projects below and customize them to your liking.

# App Lab

## #3: Personal budget app

* video: [Budget smart: Track your expenses with Pythagora](https://www.youtube.com/watch?v=2f64gvm0ck0)
* repo: [Budget app](https://github.com/westonludeke/budget_app)

Initial Project Description:

```
# Budget App

Budget App is a personal budget tracker tool, designed to track and monitor credit card transactions over time. The user will upload a list of transactions in CSV format to the website. Afterwards, the user will be able to categorize the transactions once uploaded and track expenses over time.

## Core Features

* The top of the website should contain a navbar with links for `Home`, `Reports`, `Upload`, as well the ability to logging in/logging out of the site.
* The website will have an `Upload` link on the top navbar for the user to click to upload a CSV file containing a list of transactions. 
* Any CSV file uploaded will contain the following headers: `Post Date`, `Transaction Date`, `Reference Number`, `Merchant Data`, and `Dollar Amount`.
* The website's homepage should display a list of the transactions after uploaded.
* For each transaction, there should be additional categories added that the user will manually edit:
  * `Close Date` which will be a form field where the user will be able to add the Month and Year (in the format MM/YYYY) of the close date for each transaction.
  * `Category` which will be a separate form field where the user will add in each transaction's category in order to track the transactions. For example: `Groceries`, `Gasoline`, `Eating Out`, etc.
* After the transactions are uploaded to the website, the user will then be able to manually be able to modify each individual transaction's `Close Date` and `Category` selection.
* Transactions should be grouped on the homepage by the `Close Date` category. For example, all transactions with the close date of `10/2024` should be grouped under a header for `10/2024`.
* In the header, under each `Close Date` add a subheader for `Number of Transactions` tracking how many transactions exist for that Close Date.
* Also, add a subheader under each Close Date for `Total` to track the dollar amount for all transactions for that Close Date, which will be a sum of all transactions containing that `Close Date`.
* As new transactions are uploaded to the website, they should be added to the database in addition to the existing transactions. i.e. they will not replace existing transactions.
* Each transaction should contain an `Edit` button to edit the individual transaction and a `Delete` button to delete the transaction and remove it from the database.

## Reporting

* When the user loads the `Reports` page, a page displaying the reports should load.
* The Reports page will contain a breakdown of expenses by category, grouped by each month
* For example, one report will be for all transactions with the `Close Date` category of `10/2024`.
* The report will display totals across each category for that close date.
* For example, if there are 5 transactions for `10/2024` with the `Category` of `gasoline`, the app should get the total amount for all 5 of those transactions and display them on the report.
* An example report may display:
  * Groceries: $250
  * Gas: $85
  * Eating Out: $215
```

## #1: AI-Powered Chatbot

* video: [Pythagora App Lab #1: Build Your Own AI-Powered Chatbot Without Code](https://www.youtube.com/watch?v=_VontX6ACuA)
* repo: [Pythagora Chatbots](https://github.com/Pythagora-io/custom-chat-bot)

Initial Project Description:

```
I want to build an app that allows users to design and build LLM-based support chatbots - with different personalities, cultures, etc. - to be added on the websites. Each user will have an API key dedicated to it and the chatbots can be injected into the websites using a script tag.
```

# Other Apps

## EchoSphere ([DEMO](https://echo-sphere.examples.pythagora.ai/auth/register))

EchoSphere is basically a Reddit clone and has ~5000 LOC. We created a [poll on Reddit](https://www.reddit.com/r/webdev/comments/1b1g4n4/what_kind_of_a_web_app_would_you_consider/) to see what kind of an app people would want to see that would demonstrate capabilities of AI coding agents. The results were very consistent and it did lead us to focus more on expanding GPT Pilot to create apps with more features rather than smaller apps with more complexity. Currently, this is an app with most features that we built internally.

- Time spent to create this: 60 hours
- [Github repo](https://github.com/Pythagora-io/echo-sphere)
- Video overview coming soon

---

## Code Chat ([DEMO](https://code-whisperer.examples.pythagora.ai/))

Code Chat is one fun project that we made up as an example to showcase. The idea is that you can use it to ask the LLM questions about your codebase. You paste in the link to a public Github repo; it scrapes the code from Github, chunks it, sends it to the LLM for analysis that creates a description about what the code does and saves the descriptions into the database. Then, you can ask the app a question about the codebase and the codebase shows you the response. In the demo, we’re using GPT-3.5.

- Time spent to create this: 7 hours
- [Github repo](https://github.com/Pythagora-io/code-chat)
- [Video overview](https://youtu.be/8qzq6F5DtyE)

---

## GPT Optimizely ([DEMO](https://gpt-optimizely.examples.pythagora.ai/))
This is a platform that enables users to do A/B testing for websites, allowing them to experiment with different versions of their web pages to determine which one performs better in terms of user engagement and conversions. For each user, it creates a JS snippet that the user adds to their website. Then, whenever the user creates a new test and picks which HTML elements they want to test, GPTOptimizely will inject A and B versions of the elements to half of the users. Then, it will track a click event on each version and display the results in the dashboard.

- Time spent to create this: \~3 days
- [Github repo](https://github.com/Pythagora-io/gpt-optimizely)
- [Video overview](https://www.youtube.com/watch?v=U2QXHyVY6Hw)

---

## Prompt Lab ([DEMO](https://prompt-lab.examples.pythagora.ai/))

OpenAI Playground on steroids – it enables you to load a conversation from a JSON array or enter it manually, run the conversation with the LLM an X number of times, save the conversation to the database, and load it back in. We actually use this app when we engineer a prompt and want to see how it behaves. The playground is not good enough because it’s time consuming to repetitively rerun a single prompt. Rather, we choose how many times we want to run it and let the app run the prompt repeatedly. Once it’s finished, we can go into analyzing the results. This might be useful for people who are building an AI app and need to optimize their prompts.

- Time spent to create this: \~2 days
- [Github repo](https://github.com/Pythagora-io/pythagora-prompt-lab)
- [Video overview](https://youtu.be/UXhC4nx0pvs)

---

## Star History ([DEMO](https://star-history.examples.pythagora.ai/))

I’ve been releasing open-source projects for years now, and I always wanted to check how fast is my Github repo growing by comparing it to some other successful repositories on https://star-history.com/. The problem is that on Star History, I’m not able to zoom into the graph, so a new repo that has 1000 stars cannot be compared with a big repo that has 50.000 because you can’t see how the bigger repo does in it’s beginning. So, I asked GPT Pilot to build this functionality. It scrapes Github repos for stargazers, saves them into the database, plots them on a graph, and enables the graph to be zoomed in and out.

- Time spent to create this: 6 hours
- [Github repo](https://github.com/Pythagora-io/star-history)
- [Overview video link](https://youtu.be/mjc4vnlLz3M)

---

## SQLite database looker ([DEMO](https://gpt-pilot-db-looker.examples.pythagora.ai/))

This is also one app we use internally to analyze a local SQLite database. It pulls the data from the database in a format that’s very specific to the GPT Pilot database structure, but it can easily be modified to fit other structures. It reads and uploads your SQLite database, splits the rows by the specific field, unpacks the rows into values, loads the LLM conversation data into a form, and enables you to simply change one of the messages and submit the LLM request to GPT-4 to see how the results will look like. This way, we can analyze the conversations that GPT Pilot’s agents have with the LLM and easily try what would happen if the prompts were different.

- Time spent to create this: \~2 days
- [Github repo](https://github.com/Pythagora-io/gpt-pilot-db-analysis-tool)
- [Video overview](https://youtu.be/gKgswTm5tFo)

---

## Vanish Talk ([DEMO](https://vanish-talk.examples.pythagora.ai/))

Vanish Talk is a sample app created to showcase real time messaging features but so it's not too easy, other features are added. It has the ability to authenticate the user, send verification email, create real time chatting room with or without a password, join any open room, and has a cronjob running that deletes all the messages every hour.

- Time spent to create this: 4 hours
- [Github repo](https://github.com/Pythagora-io/vanish-talk)
- [Video overview](https://youtu.be/ZOYsEzI8cjI)