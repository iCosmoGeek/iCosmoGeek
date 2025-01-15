---
title: "Remove Windows 7 SP1 Backup Files and Reclaim Disk Space"
date: "2011-02-23"
categories: 
  - "how-to"
  - "microsoft"
---

Now that everybody are excited about today’s [**Service Pack 1 Final**](http://www.microsoft.com/downloads/en/details.aspx?FamilyID=c3202ce6-4056-4059-8a1b-3a9b77cdfdda&displaylang=en) Release for Windows 7 and Windows Server 2008 R2, how many of you know that Windows 7 keeps traces in your machine of the previous updates? These backup files are necessary for the operating system in case if you want to remove the update later.

The size of these backup files will be huge in size (more than 1 GB) which you may not require in future.

[![image](http://lh4.ggpht.com/_40bmzDo_mBs/TWUakHRSnpI/AAAAAAAABzU/3iGDPifmKLs/image_thumb%5B1%5D.png?imgmax=800 "image")](http://lh3.ggpht.com/_40bmzDo_mBs/TWUajBtxAqI/AAAAAAAABzQ/yPaDj23IfrU/s1600-h/image%5B3%5D.png)

Perform following steps only if you do not plan to uninstall SP1 later.

1. In your Windows 7 machine, open Command Prompt with administrative privileges (Run as Administrator)
2. Run the command: **DISM /online /cleanup-Image /spsuperseded**

Alternatively, you can also achieve this task by opening Disk Clean-up utility of your system drive. In the Disk Cleanup window, you may have to select ‘Clean up system files’ button to show the service pack backup files.
