When you start using Pythagora, you'll be prompted to choose between developing your application locally or in the cloud. This guide explains both options, their workflows, and how to manage your development environment.

---

## Local Development

Local development means building and running your application directly on your computer. Here’s what to expect:

- **Traditional Approach**: Local development has been Pythagora’s default method until recently.
- **Dependencies**: You'll need to install MongoDB, Python, Node.js, and other dependencies on your machine.
- **File Storage**: All Pythagora core files and your application will be stored locally in a directory you specify.
  - To set this up, go to [Pythagora's Settings](https://share.zight.com/QwuJmgx1) page. Under `Pythagora Core path`, click `Change` and select a new, empty directory. This will house all of Pythagora's Core files and your projects.

<img src="https://p135.p2.n0.cdn.zight.com/items/geuDewGg/f874b64c-21e7-4220-adc9-ab8f2fce4d38.jpg" width="800">

---

## Cloud Development

Cloud development allows Pythagora to handle everything for you in a managed environment:

- **Hassle-Free Setup**: Only the Pythagora VS Code extension is required. No need to install MongoDB, Python, or Node.js locally.
- **Cloud-Managed**: All packages, dependencies, and your application are built and managed by Pythagora in the cloud.
- **Convenience**: Ideal for those who want a quick, streamlined setup without configuring local environments.

Note: In cloud development mode, you don't need to set `Pythagora Core path` as it will be set to the cloud by default and will look like this in Pythagora's settings:

<img src="https://p135.p2.n0.cdn.zight.com/items/DOuLmZvk/978988c4-b01a-4e5b-94c9-c6e48feba171.jpg?v=9ec72034a7b5cec12956ccb53744498d" width="800">

---

## Accessing Application Files

### Local Development
- When developing locally, all files are stored in the directory specified under `GPT Pilot path` in the Pythagora settings.
- File hierarchy:
  - The main folder: `pythagora-core`
  - Within `pythagora-core`, a subfolder called `workspace` contains your projects:

<a href="https://p135.p2.n0.cdn.zight.com/items/YEu6B0E9/6e00ab53-0ba2-40b1-857a-fafdd2c93ccb.gif?source=viewer&v=e537edf84e8f1a2a3cacbd03f3ffb554"><img src="https://p135.p2.n0.cdn.zight.com/items/YEu6B0E9/6e00ab53-0ba2-40b1-857a-fafdd2c93ccb.gif?v=e537edf84e8f1a2a3cacbd03f3ffb554" width="800"></a>

[click to see this gif in a larger window](https://p135.p2.n0.cdn.zight.com/items/YEu6B0E9/6e00ab53-0ba2-40b1-857a-fafdd2c93ccb.gif?source=viewer&v=e537edf84e8f1a2a3cacbd03f3ffb554")

### Cloud Development
- When developing in the cloud, all files are managed by Pythagora’s cloud infrastructure.
- To access them:
  1. With the Cloud running, open a terminal in VS Code and you will be connected to your instance of Pythagora in the cloud.
  2. Use command-line commands to navigate the directory structure. 
  3. Your applications will be stored in the directory `pythagora/pythagora-core/workspace`.

<a href="https://p135.p2.n0.cdn.zight.com/items/Wnu5qPQW/50ee5c9a-48c3-4cdc-882a-184fd775185b.gif?source=viewer&v=43dd8cf1e5626a8f730c3bd4fc992840"><img src="https://p135.p2.n0.cdn.zight.com/items/Wnu5qPQW/50ee5c9a-48c3-4cdc-882a-184fd775185b.gif?v=43dd8cf1e5626a8f730c3bd4fc992840" width="800"></a>

[click to see this gif in a larger window](https://p135.p2.n0.cdn.zight.com/items/Wnu5qPQW/50ee5c9a-48c3-4cdc-882a-184fd775185b.gif?source=viewer&v=43dd8cf1e5626a8f730c3bd4fc992840)

---

## Switching Between Local and Cloud Development

Switching between local and cloud development is simple:
- **Switch to Cloud**: Go to [Pythagora's Settings](https://share.zight.com/QwuJmgx1) page and click `Use Pythagora on cloud`.
- **Switch to Local**: Go to the [Settings page](https://share.zight.com/QwuJmgx1) and click `Use Pythagora locally`.

---

## Databases

When building an application with Pythagora, MongoDB is used to manage application data. Database handling varies based on your development setup:

### Local Development
- By default, you can run MongoDB directly on your machine and access it via the command line.
- Alternatively, you can use [MongoDB Atlas](https://www.mongodb.com/products/platform/atlas-database) to host your database in the cloud (separate from Pythagora's cloud).
- Pythagora will prompt you to provide your MongoDB database URL during development. This can also be updated in your application's `.env` file.

### Cloud Development
- Pythagora manages a MongoDB instance in Pythagora's cloud by default.
- Access the database via VS Code’s terminal using the command `mongosh`.
- You can also modify your application's `.env` file to point to:
  1. A MongoDB instance on your local machine.
  2. A MongoDB Atlas database you manage in the cloud (separate from Pythagora's cloud).

---

## Summary

| Feature                | Local Development                       | Cloud Development                      |
|------------------------|-----------------------------------------|----------------------------------------|
| **Setup**             | Requires installation of dependencies.  | Requires only the VS Code extension.  |
| **File Storage**      | On your local machine.                  | Managed in Pythagora’s cloud.          |
| **Database Options**  | Local MongoDB or MongoDB Atlas.         | Pythagora-managed MongoDB (default) or custom URL. |
| **Best For**          | Advanced users comfortable with setups. | Users seeking quick and hassle-free environments. |

---

If you have any questions, feel free to reach out to us on [Discord](https://discord.gg/HaqXugmxr9) or check our [FAQ](https://github.com/Pythagora-io/gpt-pilot/wiki/Frequently-Asked-Questions).
