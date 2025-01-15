---
title: "Google Wallet Has Been Hacked – Two Vulnerabilities Discovered"
date: "2012-02-10"
categories: 
  - "google"
---

The magic has been paused – [Google Wallet](http://www.cosmogeek.info/2011/09/google-wallet-future-innovative-mobile.html) which is an innovative way of payment technology from Google has been hacked today. Not with one vulnerability, but two.

The first hack is able to use brute-force attacks to reveal the Google Wallet PIN which keeps the application secure. The second hack allow access to Wallet app in your Android device and will add the ability to add the prepaid balance that is tied to the device.

[![Hacked Android](http://lh6.ggpht.com/-BE55idItnn0/TzSl_CDh_yI/AAAAAAAAIXU/n9KG5jmXV7Q/3188752624_35ca0694e6_o_thumb.jpg?imgmax=800 "Hacked Android")](http://lh6.ggpht.com/--wB4krklfYo/TzSl-QigKfI/AAAAAAAAIXQ/WJSEbzxVHdg/s1600-h/3188752624_35ca0694e6_o%25255B2%25255D.jpg) 

To those who are hearing Google Wallet for the first time, it lets you digitize your credit cards and the ability to pay things using near-field communication (NFC) technology. It means, you can just touch your phone to an NFC device and the item you are buying is automatically charged to your account. Currently, only Google has implemented this technology with Google Wallet in its Android powered Nexus S 4G available on Sprint.

The first vulnerability which was discovered by [Zvelo](https://zvelo.com/blog/entry/google-wallet-security-pin-exposure-vulnerability), reveals Google Wallet PIN in Android devices which are rooted. Wallet Cracker is a simple app developed by this team.

> _“The lynch-pin, however, was that within the PIN information section was a long integer “salt” and a SHA256 hex encoded string “hash”. Knowing that the PIN can only be a 4-digit numeric value, it dawned on us that a brute-force attack would only require calculating, at most, 10,000 SHA256 hashes. This is trivial even on a platform as limited as a smartphone. Proving this hypothesis took little time.”_

Watch the video below for more details -

[![](http://lh3.ggpht.com/-Obu1PNx6l3I/TzSl_1VX6UI/AAAAAAAAIXg/qbhRworeVT0/videod3b91d26dada%25255B22%25255D.jpg?imgmax=800)](http://www.youtube.com/watch?v=P655GXnE_ic&feature=player_embedded)

The second vulnerability which was discovered later today works on non-rooted devices as well and requires no special hacking skills. [TheSmartPhoneChamp](http://thesmartphonechamp.com/security-flaw-found-in-google-wallet/) uploaded a video demo that shows this hack. This is quite simple than earlier one. Someone who found your stolen device can easily access your digital money (funds) by just clearing the Google Wallet app data. Once the new PIN has been entered, the intruder can add your Google Prepaid Card that is tied to the device and access available money.

Second hack demo -

[![](http://lh5.ggpht.com/-k9fHVAIXkZQ/TzSmAQjPJGI/AAAAAAAAIXo/v3uOJG29bGM/video1937df09c17e%25255B5%25255D.jpg?imgmax=800)](http://www.youtube.com/watch?v=Rh1ytHrhj2E&feature=player_embedded)

Google has reportedly working on these two security flaws.
