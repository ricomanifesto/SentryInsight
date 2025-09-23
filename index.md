# Exploitation Report

Current cybersecurity landscape reveals significant exploitation activity across multiple attack vectors, with threat actors deploying sophisticated malware campaigns, leveraging zero-click vulnerabilities, and exploiting critical infrastructure systems. Notable incidents include ransomware attacks disrupting European airports, Iran-linked groups deploying new malware variants targeting European telecommunications, and North Korean threat actors using advanced social engineering techniques to deliver information stealers. Additionally, a critical Microsoft Entra ID vulnerability (CVE-2025-10035) has been patched after allowing potential Global Administrator impersonation across any tenant, while a zero-click flaw in OpenAI's ChatGPT Deep Research agent enables Gmail data exfiltration without user interaction.

## Active Exploitation Details

### ShadowLeak Zero-Click Vulnerability in ChatGPT
- **Description**: A zero-click flaw in OpenAI ChatGPT's Deep Research agent that allows attackers to leak sensitive Gmail inbox data through a single crafted email
- **Impact**: Enables data exfiltration via OpenAI's infrastructure without leaving traces on enterprise systems
- **Status**: Currently being exploited, allowing invisible email theft

### Microsoft Entra ID Token Validation Flaw
- **Description**: Critical token validation failure in Microsoft Entra ID that could allow attackers to impersonate any user, including Global Administrators, across any tenant
- **Impact**: Complete access to Microsoft Entra ID tenants of any company worldwide
- **Status**: Patched by Microsoft
- **CVE ID**: CVE-2025-10035

### Fortra GoAnywhere Command Injection
- **Description**: Maximum severity vulnerability allowing command injection in Fortra GoAnywhere systems
- **Impact**: Remote command execution capabilities for attackers
- **Status**: Patch available, exploitation highly dependent on Internet exposure
- **CVE ID**: CVE-2025-10035

### American Archive of Public Broadcasting Access Control Bypass
- **Description**: Vulnerability allowing unauthorized downloading of protected and private media content
- **Impact**: Exposure of restricted broadcast media and archives
- **Status**: Quietly patched after years of exposure

## Affected Systems and Products

- **European Airport Check-in Systems**: Weekend disruptions caused by ransomware targeting check-in and boarding systems at major European airports including Heathrow
- **Microsoft Entra ID**: All global tenants potentially affected by token validation vulnerability
- **Fortra GoAnywhere**: Systems exposed to the Internet at highest risk for command injection attacks
- **OpenAI ChatGPT Deep Research Agent**: Gmail integration vulnerable to zero-click data exfiltration
- **Steam Gaming Platform**: Verified game "BlockBlasters" used as cryptocurrency wallet drainer
- **macOS Systems**: Targeted by multiple malware campaigns through fake GitHub repositories
- **Stellantis North American Operations**: Customer data compromised through Salesforce platform breach
- **American Archive of Public Broadcasting**: Years of exposure of restricted media content

## Attack Vectors and Techniques

- **ClickFix Social Engineering**: North Korean groups using fake error messages to deliver BeaverTail and InvisibleFerret malware
- **GitHub Repository Spoofing**: Large-scale campaigns using fake repositories to distribute Atomic infostealer to Mac users
- **SEO Poisoning**: Attackers manipulating search results to redirect users to malicious GitHub pages
- **LinkedIn Job Lures**: UNC1549 using professional networking platform to target telecommunications employees
- **EDR Evasion via Windows Error Reporting**: New EDR-Freeze tool abusing Microsoft's WER system to suspend security software
- **Multi-Channel Phishing**: Expansion beyond email to social media, chat applications, and malicious advertisements
- **GPT-4 Powered Malware**: MalTerminal malware incorporating Large Language Model capabilities for dynamic attack generation
- **Third-Party Service Exploitation**: Attacks targeting service providers to compromise multiple downstream organizations

## Threat Actor Activities

- **Iran-Linked UNC1549**: Successfully infiltrated 34 devices across 11 European telecommunications companies using LinkedIn job lures and MINIBIKE malware
- **Nimbus Manticore**: Iran-linked group targeting Europe with improved malware variants outside their usual focus areas
- **North Korean DPRK Groups**: Deploying ClickFix-style lures in cryptocurrency job scams to deliver BeaverTail malware
- **ComicForm Group**: Previously undocumented hacking group targeting organizations in Belarus, Kazakhstan, and Russia with Formbook malware since April 2025
- **SectorJ149**: Collaborating with ComicForm in Eurasian cyberattacks using phishing campaigns
- **Cryptocurrency Threat Actors**: Sophisticated campaigns targeting crypto enthusiasts through verified Steam games and fake trading platforms
- **Multi-Platform Malware Distributors**: Coordinated campaigns across GitHub, social media, and legitimate platforms to distribute infostealers and ransomware