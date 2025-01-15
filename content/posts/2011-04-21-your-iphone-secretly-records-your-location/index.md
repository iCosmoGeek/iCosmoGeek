---
title: "Your iPhone Secretly Records Your Location"
date: "2011-04-21"
categories: 
  - "apple"
  - "best-of"
---

We are know that iPhone can track user location. But, how many of knew that the iPhone **constantly tracks your location and records your coordinates** alongside a time stamp to a secret file?

This secret file is also copied to owner’s computer when the two are synchronised.

[![image](images/image%5B8%5D.png "image")![image](http://lh5.ggpht.com/_40bmzDo_mBs/TbAuyR-3KuI/AAAAAAAAB70/HW1PgRhxz-4/image_thumb%5B4%5D.png?imgmax=800 "image")](http://lh4.ggpht.com/_40bmzDo_mBs/TbAuva12ijI/AAAAAAAAB7o/vmR5OptojiU/s1600-h/image%5B3%5D.png)

**What’s so bad about this?**

The most immediate problem is that this data is stored in an easily-readable form on your machine. Any other program you run or user with access to your machine can look through it.

The more fundamental problem is that Apple are collecting this information at all. Cell-phone providers collect similar data almost inevitably as part of their operations, but it’s kept behind their firewall. It normally requires a court order to gain access to it, whereas this is available to anyone who can get their hands on your phone or computer.

By passively logging your location without your permission, Apple have made it possible for anyone from a jealous spouse to a private investigator to get a detailed picture of your movements.

**Want to see the hidden data for yourself?** The secret information is actually stored inside \\Users\\<your user>\\AppData\\Roaming\\Apple Computer\\MobileSync\\Backup \[_in Windows\]._ The names of the folders and the files within them are mostly random strings, but there are some index files like Info.plist and Manifest.mbdb. Load the most recent Info.plist into notepad to see what device it's for. You should see a 'Device Name' value in the XML, make sure that it matches your iPhone.

The Manifest.mbdb and Manifest.mbdx files contain a listing of the real names of the files represented by random strings in that folder. You need a Python script to decrypt this one.

To simplify, there is an app already which does it for you - **[iPhone Tracker](http://petewarden.github.com/iPhoneTracker/#1)**. It’s just a simple app that pulls the location data out of your saved iPhone files and displays the coordinates on a map.

However, users can opt-out of the tracking by turning off global Location Services on the device. That will, however, impact any third-party app like Facebook that wants to use location services.
