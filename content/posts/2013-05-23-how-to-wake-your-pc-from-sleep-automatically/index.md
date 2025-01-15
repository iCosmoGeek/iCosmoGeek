---
title: "How To Wake Your PC From Sleep Automatically"
date: "2013-05-23"
categories: 
  - "best-of"
  - "how-to"
coverImage: "Sleep-PC.jpg"
---

Have you ever wondered whether you can wake up your PC automatically without actually pressing the power button? This can be useful in scenarios where you want to perform heavy downloads in off-peak hours or other similar actions before you wake up in the morning, without running your computer all the night!

[![Sleep PC](images/Sleep-PC.jpg)](http://iCosmoGeek.com/wp-content/uploads/2013/05/Sleep-PC.jpg)

\[[Credit](http://www.flickr.com/photos/strandell/2446408542/)\]

Follow these step by step procedure to wake your PC from sleep automatically:

Step 1: Open **Task Scheduler** by searching for it in Start Menu

Step 2: In the Task Scheduler window, click **Create Task**

[![1](images/1.jpg)](http://iCosmoGeek.com/wp-content/uploads/2013/05/1.jpg)

Step 3: Name the task as shown below or any other desired name. I prefer to select other options to run this task whether the user is logged in or not and run with higher privileges.

[![2](images/2.jpg)](http://iCosmoGeek.com/wp-content/uploads/2013/05/2.jpg)

Step 4: Click the **Triggers** tab and create a new trigger. Set options at your own desired schedule as below:

[![3](images/3.jpg)](http://iCosmoGeek.com/wp-content/uploads/2013/05/3.jpg)

Step 5: Click the **Conditions** tab, and check **'Wake the computer to run this task'.**

[![4](images/4.jpg)](http://iCosmoGeek.com/wp-content/uploads/2013/05/4.jpg)

Step 6: A scheduled task cannot run without at least one task. You could have any simple task like opening a notepad or any file-downloading program or torrent program. In this example, I am running a command prompt with the exit arguments so that it will open and immediately close it - doing nothing. To do this, type **cmd.exe** in Program/script and **/c "exit"** arguments as shown below:

[![5](images/5.jpg)](http://iCosmoGeek.com/wp-content/uploads/2013/05/5.jpg)

**Finally, save your task and close it.** 

If you want to disable this whole thing, just **delete** the above created task by right clicking on it, of course from **Task Scheduler.**

From next time, your PC will wake up automatically at your desired time. Now, this procedure will work only if you put your computer in sleep mode. That is , the computer won't wake up if it's shut down completely. You can also change power options from Control Panel to have PC automatically sleep after it hasn't been used for a while or when you press specific buttons.

The following are some of the screenshots to put your computer sleep instead of normal shutdown.

[![6](images/6.jpg)](http://iCosmoGeek.com/wp-content/uploads/2013/05/6.jpg)

[![7](images/7.jpg)](http://iCosmoGeek.com/wp-content/uploads/2013/05/7.jpg)

Wake On LAN is another method you can use to wake computers, but it works only over the network.
