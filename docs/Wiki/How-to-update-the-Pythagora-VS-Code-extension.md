When a new version of the Pythagora VS Code extension is released you should update your extension to get the latest version. New releases typically include bug fixes and improvements to the application. 

Note: To find out which version of Pythagora is the most recent, you can see the history of all Pythagora versions including the release dates of each version on the [VS Code Marketplace](https://marketplace.visualstudio.com/items?itemName=PythagoraTechnologies.pythagora-vs-code) listing on the `Version History` tab.

## Updating the Extension

To update the Pythagora extension in VS Code, open the Extensions view by clicking the Extensions icon in the Activity Bar on the side of the window. Look for Pythagora, and if an update is available, you’ll see a reload icon or an `Update` button next to it. Click the button to update the extension, and then reload VS Code if prompted to apply the changes.

After updating the extension, we also recommend restarting VS Code as this will force the Pythagora extension to fetch any additional updates.

## New Installation of Pythagora

After updating the extension, inside the directory on your local machine where you chose to install Pythagora's files, you will see some changes. The previous directory `pythagora-core` will be renamed to to something like `pythagora-core-backup-xxx-xxx-xx` and a new  `pythagora-core` directory will be added.

This new `pythagora-core` directory is where the latest version of Pythagora is installed. Any directory titled `pythagora-core-backup-xxx-xxx-xx` is the previous version of the extension you were using before the update, to ensure previous versions of Pythagora are preserved.

Any projects you were previously working on before updating are automatically added to the new `pythagora-core` directory, under the `workspace` subdirectory.

## Migrating Old Projects 

After updating the extension to version `v1.2.x`, please follow the steps below to move over any applications you were previously working on:

1 - Go to the directory where you have Pythagora installed and open the directory. You can find where Pythagora is installed by going to Pythagora's Settings in the section `Pythagora Core path`.

2 - Go to the `pythagora-core-backup-xxx-xxx-xx` directory where you previously had Pythagora's core files installed

3 - Manually copy the `pythagora.db` file. 

Note: Depending on which version of Pythagora you have installed, this file might be in the parent `pythagora-core-backup-xxx-xxx-xx` directory. On later versions of the extension, this file will be inside `pythagora-core-backup-xxx-xxx-xx` -> `data`, `database`.

4 - Go to the `pythagora-core` directory.

5 - Go to the `data` directory.

6 - Go to the `database` directory.

7 - Paste the old `pythagora.db` file inside the `database` directory, replacing the default `pythagora.db` file.

Your applications should load now when you click the `Load App` button inside of Pythagora.


## Running Your App Locally via the Command Line

If you want to run your application locally via the command line, be sure to `cd` into the new `pythagora-core` directory, then `cd` into `workspace`, finally `cd` into your app's directory before running your application.

## Handling Errors When Running Application

After updating Pythagora, if you run into any errors when starting your application, you may need to delete `node_modules` directory inside the application's directory, then run `npm install` to reinstall the project's dependencies. This issue could occur due to mismatched dependencies after the update.
