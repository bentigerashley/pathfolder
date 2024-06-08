From: Support Team
Subject: Re: Issue Accessing Our Website

Hi Alice,

I have investigated the issue with your website `site.recruitment.shq.nz` and identified the problem. The DNS A record for `site.recruitment.shq.nz` is currently pointing to a private IP address `192.168.1.10`. This is why the site is inaccessible from the public internet.

To resolve this issue, you need to update the A record for `site.recruitment.shq.nz` to point to the correct public IP address `120.138.30.179`. Here are the steps you can follow:

1. Log in to your DNS management console.
2. Locate the DNS settings for the domain `recruitment.shq.nz`.
3. Find the A record for `site.recruitment.shq.nz`.
4. Update the IP address from `192.168.1.10` to `120.138.30.179`.
5. Save the changes.

Alternatively, for immediate access, you can modify your local `hosts` file to temporarily map `site.recruitment.shq.nz` to the IP address `120.138.30.179`. This will allow you to access the site from your local machine without changing the actual DNS record.

As proof of my investigation, I was able to access the site and found the following hidden code in the HTML source:

<!-- This is what you're looking for: SHIrNitsbU1SNzBJdXd4UEdDOUNPVFNHZWRrSWJ4U21QOVFnMGs4QlZ0NVE= -->

Best regards,
Support Team
