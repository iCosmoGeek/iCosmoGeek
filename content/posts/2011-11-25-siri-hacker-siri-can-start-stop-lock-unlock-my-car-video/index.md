---
title: "Siri Hacker: Siri Can Start, Stop, Lock, Unlock My Car [Video]"
date: "2011-11-25"
categories: 
  - "apple"
---

Ever since Apple launched Siri along with iPhone 4S, hackers and enthusiasts around the globe implemented many magical things and endless possibilities.

Another hacker taking developments of others added something new allowing him to use voice commands to control his vehicle.

[![image](http://lh4.ggpht.com/-7xH-bP_yjKk/Ts71VGFRH_I/AAAAAAAAHvs/kAna1JxK_bY/image_thumb%25255B1%25255D.png?imgmax=800 "image")](http://lh3.ggpht.com/-zMl_dU4Zd3c/Ts71URWDdBI/AAAAAAAAHvk/RXhV7MHktwI/s1600-h/image%25255B3%25255D.png)

He mentioned on his [website](http://fiquett.com/?p=791), that he created a ruby plugin that is used by “Siri Proxy”, a proxy server for Apple’s Siri assistant. This proxy server allows for the creation of custom plugins that can intercept recognized speech and perform virtually any function.

> _“__The "Siri Proxy" plugin I wrote handles interaction with a php script that runs on my web server. The php script, which I developed months ago for personal use, allows me to send commands to my car which has a Viper SmartStart module installed._
> 
> _Current commands accepted are: "Vehicle Arm", "Vehicle Disarm", "Vehicle Start", "Vehicle Stop", "Vehicle Pop Trunk", and "Vehicle Panic"._
> 
> _\--UPDATE: Now it also responds to more conversational commands such as "Start my car", "Lock my car", "Pop my trunk", etc...”_

If you are technical enough to understand and analyze his code, here are some technical details for you:

**Technical Details:**

Siri Proxy / DNSMasq box - Ubuntu 11.04 Server VM  
Ruby 1.9.3  
Apache Web server - Ubuntu 10.04 LTS Server  
**Code:  
**[vipercontrol.rb](https://github.com/fiquett/SiriProxy/tree/master/plugins/vipercontrol) (placed in the plugins folder of "Siri Proxy")  
[viper\_control.php](https://github.com/fiquett/Viper_SmartStart_Control) (ran from a web server)

Watch out this video created by him for more closer impressions of these innovative attempt:

[![](http://lh4.ggpht.com/-5MaPjzxLM4Q/TtFrfimAI_I/AAAAAAAAHwY/Js8S14QCnok/videobc0881faa1f9%25255B3%25255D.jpg?imgmax=800)](http://www.youtube.com/watch?v=aPCpqXyFA8U)
