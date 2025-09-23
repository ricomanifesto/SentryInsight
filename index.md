# Exploitation Report

Critical exploitation activity is currently dominated by sophisticated threat actors leveraging multiple attack vectors to compromise systems globally. A maximum-severity command injection vulnerability in Fortra GoAnywhere systems (CVE-2025-10035) represents one of the most urgent threats, while zero-click vulnerabilities in OpenAI's ChatGPT Deep Research agent enable data exfiltration without user interaction. Advanced persistent threat groups, including Iran-linked UNC1549 and North Korean actors, are conducting targeted campaigns against telecommunications and cryptocurrency sectors using enhanced malware variants and social engineering techniques. European airports experienced significant disruptions due to ransomware attacks targeting third-party check-in systems, demonstrating the cascading impact of supply chain compromises.

## Active Exploitation Details

### Fortra GoAnywhere Command Injection Vulnerability
- **Description**: A maximum-severity command injection flaw in Fortra GoAnywhere managed file transfer systems
- **Impact**: Allows attackers to execute arbitrary commands on vulnerable systems, potentially leading to complete system compromise
- **Status**: Active exploitation possible, patch available from Fortra
- **CVE ID**: CVE-2025-10035

### ShadowLeak ChatGPT Zero-Click Vulnerability
- **Description**: A zero-click flaw in OpenAI ChatGPT's Deep Research agent that allows data exfiltration through crafted emails
- **Impact**: Enables attackers to leak sensitive Gmail inbox data without user interaction, leaving no trace on enterprise systems
- **Status**: Actively exploitable, allows invisible data theft via OpenAI's infrastructure

### Microsoft Entra ID Token Validation Failure
- **Description**: Critical token validation failure in Microsoft Entra ID enabling cross-tenant privilege escalation
- **Impact**: Could allow attackers to impersonate any user, including Global Administrators, across any Microsoft tenant
- **Status**: Recently patched by Microsoft, previously exploitable across all tenants globally

### American Archive of Public Broadcasting Access Control Bypass
- **Description**: Vulnerability allowing unauthorized access to protected and private media content
- **Impact**: Enabled downloading of restricted media that should have been protected
- **Status**: Recently patched after years of exposure

## Affected Systems and Products

- **Fortra GoAnywhere**: Managed file transfer systems with Internet exposure particularly at risk
- **Microsoft Entra ID**: All tenants globally were potentially vulnerable to the token validation flaw
- **OpenAI ChatGPT**: Deep Research agent vulnerable to zero-click data exfiltration
- **Airport Check-in Systems**: European airports using third-party check-in kiosk software
- **macOS Systems**: Targeted by multiple malware campaigns through fake GitHub repositories
- **Steam Gaming Platform**: Verified games used as malware delivery vectors
- **Telecommunications Infrastructure**: 34 devices across 11 European telecom companies compromised
- **Cryptocurrency Platforms**: TradeOgre exchange seized with $40 million in assets
- **American Archive of Public Broadcasting**: Website with media access control vulnerabilities

## Attack Vectors and Techniques

- **Command Injection**: Exploitation of CVE-2025-10035 in GoAnywhere systems for arbitrary command execution
- **Zero-Click Exploitation**: ShadowLeak attacks against ChatGPT requiring no user interaction
- **Ransomware Deployment**: Targeting critical infrastructure including airport check-in systems
- **Social Engineering**: LinkedIn job lures targeting telecommunications employees
- **SEO Poisoning**: Large-scale campaigns directing users to malicious GitHub repositories
- **ClickFix Lures**: North Korean actors using fake error prompts to deliver malware
- **Supply Chain Attacks**: Compromising third-party service providers to impact multiple organizations
- **Cryptocurrency Theft**: Malicious Steam games draining cryptocurrency wallets
- **EDR Evasion**: New techniques using Windows Error Reporting system to suspend security software

## Threat Actor Activities

- **UNC1549 (Iran-linked)**: Successfully infiltrated 34 devices across 11 European telecommunications companies using LinkedIn job lures and MINIBIKE malware
- **Nimbus Manticore (Iran-linked)**: Targeting European entities with improved variants of flagship malware, expanding beyond usual focus areas
- **North Korean Actors**: Deploying BeaverTail and InvisibleFerret malware through cryptocurrency job scams using ClickFix techniques
- **ComicForm Group**: Conducting phishing campaigns against organizations in Belarus, Kazakhstan, and Russia using Formbook malware since April 2025
- **SectorJ149**: Collaborating in Eurasian cyberattacks deploying Formbook malware
- **Cryptocurrency Scammers**: Operating through verified Steam games to steal crypto wallet funds from vulnerable users
- **Airport Ransomware Group**: Disrupted major European airports including Heathrow through third-party provider compromise