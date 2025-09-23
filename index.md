# Exploitation Report

Critical exploitation activity is currently targeting multiple platforms and industries through sophisticated campaigns. The most severe threats include a maximum-severity command injection vulnerability in Fortra GoAnywhere systems, zero-click attacks against ChatGPT's Deep Research agent that can leak Gmail data, and a critical Microsoft Entra ID flaw that allowed tenant hijacking. Nation-state actors, particularly Iran-linked groups, are actively targeting European telecommunications and other sectors using advanced malware and social engineering techniques. Additionally, widespread malware campaigns are targeting macOS users through fake GitHub repositories and Steam gaming platforms, while ransomware attacks continue to disrupt critical infrastructure including major European airports.

## Active Exploitation Details

### Fortra GoAnywhere Command Injection Vulnerability
- **Description**: A maximum-severity command injection flaw in Fortra GoAnywhere managed file transfer systems
- **Impact**: Allows remote command execution and complete system compromise
- **Status**: Patch available, exploitation highly dependent on Internet exposure
- **CVE ID**: CVE-2025-10035

### ShadowLeak Zero-Click ChatGPT Vulnerability
- **Description**: Zero-click flaw in OpenAI ChatGPT's Deep Research agent that can leak sensitive data
- **Impact**: Attackers can exfiltrate Gmail inbox data with a single crafted email without user interaction
- **Status**: Active exploitation technique disclosed, allows invisible data theft via OpenAI infrastructure

### Microsoft Entra ID Token Validation Flaw
- **Description**: Critical token validation failure in Microsoft Entra ID (Azure Active Directory)
- **Impact**: Could allow attackers to impersonate any user including Global Administrators across any tenant
- **Status**: Patched by Microsoft, previously allowed complete tenant hijacking

### American Archive of Public Broadcasting Access Control Bypass
- **Description**: Vulnerability allowing unauthorized access to protected and private media content
- **Impact**: Permitted downloading of restricted media files for years
- **Status**: Quietly patched this month

### Windows Error Reporting (WER) EDR Evasion
- **Description**: New technique using Windows Error Reporting system to suspend security software
- **Impact**: Allows attackers to evade endpoint detection and response solutions from user mode
- **Status**: Proof-of-concept tool "EDR-Freeze" demonstrates active exploitation method

## Affected Systems and Products

- **Fortra GoAnywhere**: Managed file transfer systems exposed to the Internet
- **Microsoft Entra ID**: All Azure Active Directory tenants globally
- **OpenAI ChatGPT**: Deep Research agent functionality
- **macOS Systems**: Users targeted through fake GitHub repositories and Steam platform
- **European Airport Systems**: Check-in and boarding systems affected by ransomware
- **Telecommunications Infrastructure**: 34 devices across 11 European telecom companies
- **American Archive of Public Broadcasting**: Website media access systems
- **Windows Systems**: Error Reporting (WER) functionality exploitable for EDR evasion
- **Stellantis North America**: Customer data via third-party Salesforce platform

## Attack Vectors and Techniques

- **ClickFix-Style Lures**: Used by DPRK hackers to deliver BeaverTail malware in cryptocurrency job scams
- **Fake GitHub Repositories**: Large-scale SEO poisoning campaigns delivering Atomic infostealers to Mac users
- **LinkedIn Job Lures**: Iranian UNC1549 group using professional networking for initial access
- **Malicious Steam Games**: Verified games like "BlockBlasters" stealing cryptocurrency wallets
- **Phishing Campaigns**: ComicForm group targeting Belarus, Kazakhstan, and Russia with Formbook malware
- **Social Media and Chat Apps**: Multi-channel phishing beyond traditional email vectors
- **AI-Powered Malware**: MalTerminal using GPT-4 capabilities for ransomware and reverse shell creation
- **Zero-Click Email Attacks**: ShadowLeak technique requiring no user interaction for data theft

## Threat Actor Activities

- **UNC1549 (Iran-linked)**: Successfully infiltrated 34 devices across 11 European telecommunications companies using LinkedIn job lures and MINIBIKE malware
- **Nimbus Manticore (Iran-linked)**: Targeting European organizations with improved malware variants outside usual focus areas
- **ComicForm Group**: Conducting phishing campaigns against organizations in Belarus, Kazakhstan, and Russia since April 2025, deploying Formbook malware
- **SectorJ149**: Collaborating with ComicForm in Eurasian cyberattacks using Formbook malware
- **DPRK-linked Actors**: Leveraging ClickFix techniques to deliver BeaverTail and InvisibleFerret malware in cryptocurrency-themed job scams
- **Unknown Ransomware Groups**: Disrupting major European airports including Heathrow through attacks on check-in system providers
- **Cryptocurrency Thieves**: Exploiting Steam's verified game system to distribute wallet-draining malware to unsuspecting gamers