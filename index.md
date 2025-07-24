# Exploitation Report

Recent reporting highlights a resurgence of high-impact exploitation targeting enterprise collaboration platforms, edge VPN appliances, and widely deployed CMS installations. Chinese state-aligned actors are chaining three new Microsoft SharePoint zero-days in live attacks, while separate Chinese groups continue to harvest credentials and drop webshells on unpatched Ivanti Connect Secure gateways six months after fixes were released. Concurrently, WordPress administrators are facing a covert persistence mechanism that hides a PHP backdoor inside the rarely scrutinized “mu-plugins” directory, and Brazilian financial institutions are battling the new “Coyote” banking trojan that abuses Windows UI Automation (UIA) to bypass security controls. The blend of zero-day abuse, post-patch exploitation, and novel tradecraft underscores the need for accelerated patching, continuous monitoring of web-facing assets, and defense-in-depth controls across endpoint and server fleets.

## Active Exploitation Details

### Microsoft SharePoint Server Zero-Day Chain
- **Description**: Three previously unknown SharePoint flaws are being chained to gain initial access, elevate privileges, and execute arbitrary code on on-premises SharePoint farms. Microsoft attributed the activity to three distinct Chinese nation-state groups.  
- **Impact**: Full compromise of SharePoint servers, lateral movement with stolen service tokens, potential exfiltration of sensitive collaboration data.  
- **Status**: Two flaws are patched in the latest cumulative update; one remains unaddressed with mitigations provided (blocking specific API endpoints and tightening firewall rules).  
- **CVE ID**: *[Not listed in provided articles]*

### Ivanti Gateway Remote Code Execution Vulnerabilities
- **Description**: Legacy RCE bugs in Ivanti Connect Secure and Ivanti Policy Secure gateways remain weaponized long after patches. Attackers scan for appliances that failed to receive or fully apply updates, uploading webshells and tunneling traffic.  
- **Impact**: Device takeover, credential harvesting, network pivoting, and deployment of second-stage implants inside Japanese corporate networks.  
- **Status**: Official patches available since last year; exploitation remains widespread due to complex multi-step remediation and patch failures.  
- **CVE ID**: *[Not listed in provided articles]*

### WordPress Mu-Plugin Stealth Backdoor
- **Description**: Threat actors upload a malicious “must-use” plugin (mu-plugin) that WordPress autoloads on every request, creating a hidden backdoor for command execution, database manipulation, and account creation. The payload evades normal plugin dashboards and leverages obfuscated PHP.  
- **Impact**: Persistent administrator-level access, data theft, SEO poisoning, and ransomware staging.  
- **Status**: Actively exploited in the wild; site owners must manually inspect the /wp-content/mu-plugins/ directory and harden upload permissions.  

### Windows UI Automation Abuse by “Coyote” Banking Trojan
- **Description**: Coyote leverages the Windows UI Automation (UIA) framework to programmatically read and manipulate banking session windows, bypassing anti-fraud protections and enabling stealth credential theft. This is the first documented malware family abusing UIA at scale.  
- **Impact**: Real-time hijacking of online banking and cryptocurrency exchange sessions, fraudulent transactions, and account takeover.  
- **Status**: Campaigns active against dozens of Brazilian financial entities; no Microsoft patch required, but endpoint detection heuristics are being updated.  

## Affected Systems and Products

- **Microsoft SharePoint Server (2019, 2016, Subscription Edition)**  
  - **Platform**: On-premises Windows Server deployments

- **Ivanti Connect Secure / Ivanti Policy Secure Gateways**  
  - **Platform**: Hardened Linux-based VPN appliances exposed to the Internet

- **WordPress Core installations (all supported versions) with file-upload capability**  
  - **Platform**: Linux/Windows hosting running PHP and MySQL

- **Windows 10 & 11 Endpoints**  
  - **Platform**: Desktops and laptops targeted by the Coyote banking trojan

## Attack Vectors and Techniques

- **Zero-Day Exploit Chain (SharePoint)**  
  - **Vector**: Crafted HTTP requests targeting unpatched REST and SOAP endpoints, followed by privilege escalation via token manipulation.

- **Post-Patch Exploitation (Ivanti)**  
  - **Vector**: Mass scanning for outdated firmware, upload of /tmp/ webshells via vulnerable CGI scripts, persistence through cron jobs.

- **Mu-Plugin Backdoor Injection (WordPress)**  
  - **Vector**: Authenticated admin upload or compromised credential reuse to place obfuscated PHP in /mu-plugins, auto-executed on every page load.

- **Windows UI Automation Hijacking (Coyote)**  
  - **Vector**: Malicious installer drops DLLs that hook UIA APIs, capturing GUI elements of banking applications to scrape credentials.

## Threat Actor Activities

- **Chinese Nation-State Groups (Unnamed)**  
  - **Campaign**: Coordinated SharePoint exploitation to steal intellectual property from Western government and tech organizations.

- **Chinese APT Targeting Japan (Ivanti)**  
  - **Campaign**: Long-tail exploitation of Ivanti gateways; focus on credential harvesting and strategic webshell placement for later access.

- **Unattributed WordPress Intrusion Set**  
  - **Campaign**: Global smash-and-grab operation inserting mu-plugin backdoors on small-to-medium business sites for SEO fraud and malware hosting.

- **“Coyote” Operators (Brazilian Crimeware)**  
  - **Campaign**: Financially motivated attacks on Brazilian banks and crypto exchanges, leveraging UIA to automate fraudulent transfers.

- **XSS.is Administrator (Arrested)**  
  - **Activity**: Ran a major cybercrime marketplace facilitating exploit and malware trade for 12 years; takedown may temporarily disrupt illicit tooling supply.