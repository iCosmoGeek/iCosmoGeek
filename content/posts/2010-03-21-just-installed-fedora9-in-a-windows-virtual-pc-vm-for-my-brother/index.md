---
title: "Just installed Fedora9 in a Windows Virtual PC VM for my brother"
date: "2010-03-21"
categories: 
  - "best-of"
  - "how-to"
coverImage: "Capture.jpg"
---

Just installed Fedora9 in a Windows Virtual PC VM for my brother.

  

Will it install out of the box if you have .iso Fedora image. The answer is no. When I booted the VM after inserting .iso Fedora image, VPC turned off with error - 'An unrecoverable processor error has been encountered.  The virtual machine will reset now.'

  

Fortunately, after googling sometime, I came to know that I have to add some parameters **noreplace-paravirt** to the end of the boot parameters.

  

I'll tell you how to do that. While the VPC window is at main boot screen, hit \[Tab\] to edit the option. Add **noreplace-paravirt** to the end of the boot parameters, and hit enter.

  

[![](images/Capture.JPG)](http://4.bp.blogspot.com/_40bmzDo_mBs/S6UOAA4g64I/AAAAAAAABDA/P5hQ_9ecIg0/s1600-h/Capture.JPG)

  

  

  

  

  

  

  

  

  

  

  

  

  

  

  

  

  

The installation process is relatively plain, until you get the hard drive partitioning screen where you have options to format in its file system. I have formatted the drive in a whole single partition as it is virtual hard drive where I hardly care.

  

The installation took around 30min and after rebooting you will have to enter above mentioned parameters again. You need to hit any key and then 'a' at the initial boot screen (before it throws an error). Add **noreplace-paravirt** parameters again and hit enter to continue booting.

  

This is the welcome screen:

  

[![](images/Capture.JPG)](http://4.bp.blogspot.com/_40bmzDo_mBs/S6URBu5W3mI/AAAAAAAABDI/fryat4xlxSs/s1600-h/Capture.JPG)

  

  

  

  

  

  

  

  

  

  

  

  

  

  

  

One final thing, if you add **noreplace-paravirt** into grub.config file, there is no need to enter this everytime you boot Fedora. Go to grub.config file located at filesystem\\etc folder and edit it in a text editor and add above mentioned parameter at the end of the line that looks something like **kernel /vmlinuz-2.6.25-14.fc9.i686 ro root=UUID= rhgb quiet**

Save this file and reboot to verify Fedora booting without adding any extra parameters.

  

Now that I have successfully installed Fedora9 in a Windows VM, I came to know that there is Fedora12 available  http://fedoraproject.org/en/index. I kept for download this new file and will experiment tomorrow. May be Fedora 12 will fix above issue of adding extra parameters.
