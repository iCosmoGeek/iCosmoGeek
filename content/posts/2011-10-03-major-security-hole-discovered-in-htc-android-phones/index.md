---
title: "Major Security Hole Discovered in HTC Android Phones"
date: "2011-10-03"
categories: 
  - "google"
---

A major security hole found in some HTC Android phones which could give apps with Internet permissions to information like user’s location and their text messages. In fact, this could happen with any third-party application. Some of the devices in this category identified as of now include **EVO 3D, 4G, Thunderbolt, EVO Shift 4G, MyTouch 4G Slide**, etc. The list could increase on further research.

[![image](http://lh6.ggpht.com/-Ie2EZ2Wuqvw/Ton1sZtjkuI/AAAAAAAAF24/1HCtFvG1L-Y/image_thumb.png?imgmax=800 "image")](http://lh6.ggpht.com/-qWEzjUqJ0H4/Ton1qySB6eI/AAAAAAAAF20/APM5_T2B0lk/s1600-h/image%25255B2%25255D.png)

After a quite extensive research, [Android Police](http://www.androidpolice.com/2011/10/01/massive-security-vulnerability-in-htc-android-devices-evo-3d-4g-thunderbolt-others-exposes-phone-numbers-gps-sms-emails-addresses-much-more/) has discovered a suite of logging tools called **HTCLoggers** which were added to some HTC devices during a recent software update. This HTCLoggers.apk has root-level access. Any app on affected devices that requests a single android.permission.INTERNET which is normal for any app that connects to Internet can get its hands on the following -

> _**\-the list of user accounts, including email addresses and sync status for each  
> \-last known network and GPS locations and a limited previous history of locations  
> \-phone numbers from the phone log  
> \-SMS data, including phone numbers and encoded text (not sure yet if it's possible to decode it, but very likely)  
> \-system logs (both kernel/dmesg and app/logcat), which includes everything your running apps do and is likely to include email addresses, phone numbers, and other private info**_

Even though there is no immediate fix for this security flaw, if your device is rooted, you can immediately delete Htcloggers.apk right away (you can find it at /system/app/HtcLoggers.apk).

Even though this is not the security vulnerability that is present in Android itself, but rather something that has been introduced by HTC team, this is serious issue. We have seen many instances in the [past](http://www.cosmogeek.info/2011/08/warning-new-android-malware-records.html) where Android devices are affected with [malware apps](http://www.cosmogeek.info/2011/03/google-removed-21-malware-apps-remotely.html), but this one is entirely different.

HTC has responded to this report - _"HTC takes our customers' security very seriously, and we are working to investigate this claim as quickly as possible. We will provide an update as soon as we're able to determine the accuracy of the claim and what steps, if any, need to be taken."_

**Proof of Concept for advanced Android users:**

[![](http://lh4.ggpht.com/-gOswyYOqWik/Ton1smsULcI/AAAAAAAAF28/k-DafTzi1Jg/videob917172b4542%25255B8%25255D.jpg?imgmax=800)](http://www.youtube.com/watch?v=YoTUkQ7SlNU&feature=player_embedded)
