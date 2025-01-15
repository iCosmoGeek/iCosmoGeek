---
title: "What happened to Amazon yesterday?"
date: "2011-04-22"
categories: 
  - "best-of"
---

Yesterday was an interesting day for many (I mean many) sites around the world which rely on **[Amazon](http://www.cosmogeek.info/2010/10/amazon-web-services-aws-offers-free.html)** servers.

**Amazon EC2 (Elastic Compute Cloud),** an amazing implementation of Cloud Computing had a major network failure yesterday that triggered a re-mirror of all the **Elastic Block Storage (EBS)** volumes in the North Virginia data centre.

This re-mirror combined with a large number of customers trying to fire up new instances to recover from the network failure caused Amazon to hit a storage capacity problem.

[![image](http://lh4.ggpht.com/_40bmzDo_mBs/TbGae87LMdI/AAAAAAAAB8U/34M0yjiZHbk/image_thumb%5B1%5D.png?imgmax=800 "image")](http://lh6.ggpht.com/_40bmzDo_mBs/TbGad9b5QiI/AAAAAAAAB8Q/bd2waeis8F4/s1600-h/image%5B3%5D.png)  
Basically they didn’t have enough disk space to support the re-mirror and as the thousands upon thousands of customers they have tried to fire up new replacement images the problem compounded.

Amazon is still experiencing these issues and is updating the current status at [http://status.aws.amazon.com/rss/EC2.rss](http://status.aws.amazon.com/rss/EC2.rss "http://status.aws.amazon.com/rss/EC2.rss") and [http://status.aws.amazon.com/](http://status.aws.amazon.com/ "http://status.aws.amazon.com/")

Many big sites and their services are still down. Some of them are -

> About.me
> 
> Quora.com
> 
> Reddit.com
> 
> StarNews.in
> 
> RepositoryHosting.com
> 
> Foursquare.com
> 
> HootSuite.com

See [http://ec2disabled.com](http://ec2disabled.com) for the complete list.

**What companies can try in these scenarios?**

1. They should have strict disaster recovery process which can make the system up in not less than 30 minutes
2. They should try out the actual worst scenarios from their so called hourly (or minutely!) backups and thorough recovery process
3. As soon as Amazon admitted that they had severe performance issues in the [status page](http://status.aws.amazon.com/), you should start out disaster recovery process, in this case, move everything to a new availability zone to have everything up and running with full data integrity

Do you really believe that Amazon running out of disk space? But those are the details that Amazon published as of now. We may have to wait for full post mortem report.
