You may first want to read the article on [how to write a good initial project description](https://github.com/Pythagora-io/gpt-pilot/wiki/How-to-write-a-good-initial-project-description).

# Examples of good project descriptions:

## Personal budget app with reporting

[Watch the demo here](https://www.youtube.com/watch?v=2f64gvm0ck0)

[Fork the repo here](https://github.com/westonludeke/budget_app)

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

## SQLite db analysis tool
> I want to create an app that will enable the user to view and analyze the data stored in an SQLite database. On the frontend, the user should first either select the previously uploaded database from the dropdown or upload a new SQLite database by selecting the file from the disk that they want to load. If they choose a new database file from the disk, they should be able to name this database, and the database file should be sent to the backend and stored for later so that the user doesn’t have to upload the database every time they want to analyze it. Once the database is uploaded, the user should be able to interact with it. Specifically, the user should be able to see all apps from the database. Once they choose an app, they should see all development tasks of that app and be able to select one. Once they select a development task, they should see all development steps within the selected development task. Finally, once they select the development step, they should see all the step data from the database.
> 
> The SQLite database will always be structured like this:
> Table “app” contains all apps stored in the database. Every app has multiple development tasks that are stored as an array in the table “development_planning” under the key “development_plan”. Each array item is a JSON object that has 3 key-value pairs: “description”, “user_review_goal” and “programming_goal”.
> Finally, each development task contains many development steps that are stored in the table “development_steps” and are linked to the app table by the key “app_id”. The problem is that there is no connection between the development task and development step so what needs to be done is take all development steps from the database and split the list of steps by the field “prompt_path”. Every development task begins with the prompt path with the value “development/task/breakdown.prompt” so you can connect development steps to development tasks by splitting development steps list in multiple smaller lists in which every smaller list begins with the step that has “prompt_path” equal to “development/task/breakdown.prompt”. That way, you will get development steps for each development task.
> Finally, each development step contains the following values that need to be shown on the frontend to the user: “prompt_path” which is a string, “messages” which is an array of JSON objects, “llm_response” which is a JSON object and “prompt_data” which is JSON object. “messages” array will always contain JSON objects with keys “content” and “role” so the user should see on the frontend a big text field for the value of “content” and a label for the value “role”. “llm_response” will always have a key “text” that should be shown on the frontend as a text area - it will contain a large string. “prompt_data” can have different keys and each key-value pair should be shown to the user.

***

## Prompt Engineering App
> I want to create an app that will enable me to analyse different responses from OpenAI API. The interface should contain an LLM conversation one main list of messages to the LLM. Each list item should contain a text field where I can add a big text message and a dropdown that selects if the message is from Assistant or User. There can be infinite number of these list items so there can be only one when the app loads and a button to add new list item. Other than the list, there should be a field that contains a number that the user can edit but it can go only from 0 to 100 and also there should be a button SUBMIT. When I click on the SUBMIT button, the LLM conversation should be sent to the OpenAI API, in parallel, X number of times which is the 0 - 100 number that the user added on the frontend. When the responses are fetched from the OpenAI API, there should be a list of expandable elements that, when expanded, show that particular response from the OpenAI API. For example, if I set the number of requests to 10, when the responses start coming, 10 elements should appear that have just the number of the request as a label and when expanded, they should show that specific response. Keep in mind that the OpenAI API returns a stream so it should stream to the frontend as well. Use Tailwind for styling but don’t install it - instead use the CDN version.

***

## Credits Billing System
> I have an app that enables people to scrape the web and now, I want to create an account management system for my app. Here are the parts of the system I need you to create:
> 1. Authentication. I need the users to be able to register and log in. Make sure that they can reset their password, log out and when a user logs in, that they are logged in for 1 year (use JWT for session management and make sure that the user stays logged in after the server restarts).
> 2. Credit-based billing with Stripe. The user should be able to add a credit card that can be charged. The billing system will incorporate three pricing tiers: a free tier for 0-5000 credits, a Small Business tier priced at $0.0018 per credit for the following 500,000 credits, and an Enterprise tier at $0.0009 per credit for subsequent usage. Billing will be prepaid so that the user will purchase a certain number of credits that will be used up until there are no more credits in the user account - then, the user needs to top up their credits to continue using our service.
> 3. Once the user logs in, they should see their account management with the following pages:
>     - “Dashboard” page that shows their API key and the credits that they used up in the last 1 day, last 7 days and last 30 days. Create an endpoint that will enable another microservice (the one that scrapes the web) to update the used credits for a user. Also, on 
>     - “Billing” page that shows the past invoices and a form that enables user to set up auto-replenish feature. If this feature is turned on, the user will automatically be billed once they go below a certain number of credits. This form should have one toggle that enables or disables this feature and 2 input fields. One input field shows the number of credits to automatically purchase (default to 5000) and the second input field shows a threshold of available credits under which the automatic top up will be triggered. For example, if the threshold is 30000 and the number of credits to automatically purchase is 5000, user will be automatically billed for 5000 credits once their account has less than 30000 credits available. Also, on this page, show a list of all purchases that the user has made and next to each purchase, there should be a button to download a receipt for that purchase.
>     - “Contact” page that shows only an email where users can send their inquiries.
>     - “API Info” page that only shows the API key of the user.
>     - “Buy credits” page that enables users to purchase more credits. This page should have 4 buttons with some common number of credits that users purchase (5000, 25000, 50000, and 100000 credits) and an input field where users can set a custom number of credits to purchase. Below, there should be a field that shows the total price for the selected credits and a button “Confirm” that will trigger a purchase. When the button is clicked, the user is sent to a Stripe page where they can enter their credit card details and pay.
> 4. Frontend styling - use bootstrap for the styling and make sure that there is a sidebar with links to each of the pages listed and a header that shows the user that is logged in and a button to log out.

***

## Time tracker

> Time-tracking web app for freelancers in node/express using MongoDB. For the UI, use Bootstrap and vanilla JS.
>
> Users must register (username + password, no email verification, no password recovery). Use session-based auth (no JWT).
>
> When user logs in, the home page shows "start" button and input field for task description. When the user enters the description and presses "start", the timer starts, the timer button switches to "stop" and elapsed time (0h0m0s, updated every second) is shown. When the user hits "stop", the time entry is saved to the database, the description field and elapsed time are reset and the timer button switches back to "start". There should be no simultaneous multiple entries for the same user.
>
> The home page also shows 10 most recent time entries and a "Show all" link to the separate "Reports" page.
>
> The reports page has a list of all time entries for a specific date range. The user can select start and stop date (assume from midnight to midnight, time zones can be ignored, always assume local time), default is current month (month to date). When the user changes the time entries and clicks "show", the list of entries is updated as per the selection. The reports page should also show a simple bar chart of time per day, with days in the selected range on the X axis, and total time per day on the Y axis. The reports page should also support downloading the list of time entries in CSV format with "date", "start_time", "stop_time", and "description" columns.  Use 24h format for start-time and end time, and use "YYYY-MM-DD" format for the date.  Always assume local timezone (ignore timezones).
>
> Different users are completely separate (each only sees their own data), no need for multiple roles, admins, etc. Users can edit and delete time entries after they're saved to the database (only on the main page, not in the Reports page).
>
> Use the following project structure:
> 
> * main file should be called `server.js`
> * all database models should be in `models/` directory
> * all routes that respond with HTML should be in `routes/` directory
> * all API endpoints (routes that take and/or respond with JSON and are used by frontend JS) should be in `routes/api/` directory.
> * all templates should be in `views/` directory - use EJS as a template language.
> * all configuration parameters (port, session secret, database url) should be defined in `env` file and loaded via `dotenv`.
> 
> The UI must be simple, responsive, have header (with text logo, and navbar for page navigation and logout). Use Boostrap for styling.
