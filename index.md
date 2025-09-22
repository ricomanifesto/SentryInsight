# Exploitation Report

Current exploitation activity reveals several critical security incidents across major platforms and services. A critical vulnerability in Microsoft Entra ID enabled complete tenant hijacking and Global Administrator impersonation across organizations worldwide, while a maximum severity command injection flaw in Fortra GoAnywhere MFT poses significant risks to exposed systems. Sophisticated threat actors continue leveraging social engineering tactics, with DPRK-linked groups deploying ClickFix lures for cryptocurrency theft, Iranian UNC1549 targeting telecommunications through LinkedIn job scams, and widespread malware campaigns targeting macOS users through fake GitHub repositories. Additionally, a zero-click vulnerability in OpenAI's ChatGPT Deep Research agent enables silent data exfiltration from Gmail accounts.

## Active Exploitation Details

### Microsoft Entra ID Token Validation Vulnerability
- **Description**: Critical token validation failure in Microsoft Entra ID (previously Azure Active Directory) that allowed attackers to impersonate any user across any tenant
- **Impact**: Complete tenant hijacking, Global Administrator impersonation, and unauthorized access to organizational resources
- **Status**: Patched by Microsoft

### Fortra GoAnywhere MFT Command Injection
- **Description**: Maximum severity vulnerability in GoAnywhere Managed File Transfer software enabling arbitrary command execution
- **Impact**: Remote code execution and system compromise
- **Status**: Critical patch available, exploitation highly dependent on Internet exposure
- **CVE ID**: CVE-2025-10035

### ShadowLeak ChatGPT Zero-Click Vulnerability
- **Description**: Zero-click flaw in OpenAI ChatGPT's Deep Research agent allowing Gmail data exfiltration
- **Impact**: Silent theft of sensitive email data with a single crafted email, leaving no trace on enterprise systems
- **Status**: Active exploitation possible through OpenAI's infrastructure

### Windows Error Reporting EDR Bypass
- **Description**: New evasion technique using Windows Error Reporting (WER) system to suspend security software from user mode
- **Impact**: Complete bypass of endpoint detection and response solutions
- **Status**: Proof-of-concept tool "EDR-Freeze" available

## Affected Systems and Products

- **Microsoft Entra ID**: All tenants globally were potentially vulnerable to hijacking
- **Fortra GoAnywhere MFT**: Managed File Transfer software with Internet-exposed instances at highest risk
- **OpenAI ChatGPT**: Deep Research agent functionality vulnerable to data exfiltration
- **Windows Systems**: All versions susceptible to WER-based EDR bypass technique
- **macOS Systems**: Targeted by widespread infostealer campaigns through fake GitHub repositories
- **Steam Platform**: Verified games used as malware distribution vectors
- **Salesforce Platform**: Third-party compromises affecting major clients like Stellantis
- **Airport Check-in Systems**: EU airports disrupted by third-party software provider attacks

## Attack Vectors and Techniques

- **ClickFix Social Engineering**: DPRK actors using fake error prompts to deliver BeaverTail and InvisLoader malware
- **LinkedIn Job Lures**: UNC1549 targeting telecommunications employees with fake recruitment offers
- **Fake GitHub Repositories**: macOS users targeted with malicious software impersonating legitimate tools
- **Phishing-as-a-Service**: Lighthouse and Lucid platforms operating 17,500+ phishing domains across 316 brands
- **Fraudulent Game Distribution**: Malware delivery through verified Steam games stealing cryptocurrency wallets
- **AI-Powered Malware**: MalTerminal leveraging GPT-4 capabilities for dynamic malware generation
- **Multi-Channel Phishing**: Attackers expanding beyond email to social media, chat apps, and malicious advertisements

## Threat Actor Activities

- **DPRK-Linked Groups**: Cryptocurrency-focused campaigns using ClickFix techniques and BeaverTail malware in job recruitment scams
- **UNC1549 (Iran-Nexus)**: Cyber espionage campaign targeting 11 European telecommunications companies, compromising 34 devices using MINIBIKE malware
- **ComicForm Group**: Previously undocumented threat actor conducting phishing campaigns against Belarus, Kazakhstan, and Russia since April 2025
- **SectorJ149**: Deploying Formbook malware in coordinated Eurasian cyberattacks
- **SystemBC Operators**: Managing REM Proxy network with 1,500 daily VPS victims across 80 command-and-control servers
- **Atomic Infostealer Campaign**: Large-scale macOS targeting through fake password manager and software repositories