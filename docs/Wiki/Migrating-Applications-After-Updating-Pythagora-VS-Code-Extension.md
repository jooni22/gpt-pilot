After updating your Pythagora VS Code extension, follow these steps to migrate any applications you were previously working on:

1. **Open Your Pythagora Core Installation Directory**  
   - Open VS Code and navigate to Pythagora's Settings page.  
   - Find the `Pythagora Core path` to identify the directory where the Pythagora core files are installed.  
   - *(Need help? [View Pythagora Settings](https://share.zight.com/QwuJmgx1))*  

2. **Locate the Backup Directory**  
   - Go to the `pythagora-core-backup-xxx-xxx-xx` directory where your previous Pythagora core files were installed.  

3. **Copy the Database File**  
   - Navigate to:  
     ```
     pythagora-core-backup-xxx-xxx-xx -> data -> database
     ```  
   - Copy the `pythagora.db` file.  

4. **Paste the Database File into the New Directory**  
   - Go to the new `pythagora-core` directory installed by the update.  
   - Navigate to:  
     ```
     pythagora-core -> data -> database
     ```  
   - Paste the `pythagora.db` file here, replacing the default file.  

## Verify Migration
- Your applications should now load when you click the `Load App` button in Pythagora.  

## Need Help?
If you encounter any issues, [contact our support team](https://github.com/Pythagora-io/gpt-pilot/wiki/Contact-Us).  