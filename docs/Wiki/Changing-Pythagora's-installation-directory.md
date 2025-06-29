If you need to change the directory where Pythagora's Core files are installed, follow the steps below to seamlessly move your Pythagora setup to a new location without losing your current configurations and projects:

1. Create a new empty, directory on your computer.

2. Go to [Pythagora's settings page](https://share.zight.com/QwuJmgx1) and find the `Pythagora Core path` section. Click `Change` and select the new directory created in step #1: 

<img src="https://p135.p2.n0.cdn.zight.com/items/geuDewGg/f874b64c-21e7-4220-adc9-ab8f2fce4d38.jpg" width="800">

3. This action will trigger the installation of the Pythagora core files to the new directory.

4. After finishing the installation, the directory you selected in step #2 will contain a new directory called `pythagora-core` with all of the Pythagora core files.

5. To ensure continuity of your existing projects, inside the old `pythagora-core` directory where you previously had Pythagora core installed, manually copy the `pythagora.db` file. Paste the old `pythagora.db` file inside the new `pythagora-core` directory, replacing the existing `pythagora.db` file in the new `pythagora-core` directory.

6. A new `config.json` file will be created in the new `pythagora-core` directory with the default settings.

Note: The steps in this article refer to the Pythagora core files, which is separate from the location where VS Code installs the underlying extension files. These files are usually in a directory called `.vscode`, inside an `extensions` directory. We don't recommend modifying this directory's location or the files inside this directory. 
