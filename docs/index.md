# Exploitation Report

Critical exploitation activity is currently dominated by supply chain attacks and zero-day vulnerabilities being actively exploited in the wild. The most significant development is the first confirmed case of hackers using AI to develop a zero-day exploit for a two-factor authentication bypass, marking a new milestone in threat actor capabilities. Simultaneously, multiple supply chain compromises are affecting major development platforms including npm, PyPI, Jenkins, and Hugging Face repositories. The cPanel vulnerability CVE-2026-41940 is under active exploitation with threat actors deploying backdoors, while the Canvas learning management system has been compromised through an undisclosed vulnerability affecting educational institutions globally.

## Active Exploitation Details

### cPanel Critical Vulnerability
- **Description**: A critical flaw in cPanel that allows attackers to exploit the web hosting control panel
- **Impact**: Deployment of "Filemanager" backdoor on compromised environments, providing persistent access to hosting infrastructure
- **Status**: Under active exploitation by threat actor Mr_Rot13
- **CVE ID**: CVE-2026-41940

### AI-Generated Zero-Day 2FA Bypass
- **Description**: First known zero-day exploit developed using artificial intelligence to bypass two-factor authentication mechanisms
- **Impact**: Mass exploitation capability allowing attackers to circumvent 2FA protections on web administration tools
- **Status**: Active exploitation detected by Google Threat Intelligence Group

### Canvas Learning Management System Vulnerability
- **Description**: Security flaw in Instructure's Canvas platform allowing unauthorized access and modification
- **Impact**: Portal defacement, data theft of 3.65TB including sensitive educational data, and extortion demands
- **Status**: Exploited by ShinyHunters group, agreement reached to stop data leak

### Dirty Frag Linux Privilege Escalation
- **Description**: Privilege escalation vulnerability affecting enterprise Linux distributions, similar to Copy Fail and Dirty Pipe
- **Impact**: Local privilege escalation allowing attackers to gain root access
- **Status**: Under limited exploitation with potential for broader impact

### Ollama Out-of-Bounds Read
- **Description**: Critical vulnerability in Ollama allowing remote process memory leakage
- **Impact**: Remote, unauthenticated attackers can extract entire process memory contents
- **Status**: Disclosed vulnerability requiring immediate patching

## Affected Systems and Products

- **cPanel/WHM**: Web hosting control panels vulnerable to critical exploitation
- **Canvas LMS**: Educational technology platform used by numerous institutions globally
- **Jenkins Marketplace**: Checkmarx AST plugin compromised with malicious versions
- **npm/PyPI Packages**: TanStack, UiPath, Mistral AI, OpenSearch, and Guardrails AI packages compromised
- **Hugging Face**: Fake OpenAI Privacy Filter repository delivering malware
- **JDownloader**: Official website compromised to distribute Python RAT malware
- **Enterprise Linux**: Multiple distributions affected by Dirty Frag vulnerability
- **Ollama**: AI model management platform vulnerable to memory leakage
- **macOS Systems**: Targeted through Google Ads and Claude.ai chat abuse campaigns

## Attack Vectors and Techniques

- **Supply Chain Poisoning**: Compromise of legitimate software repositories and package managers
- **AI-Assisted Exploit Development**: First confirmed use of AI to create zero-day exploits
- **Website Compromise**: Direct compromise of official software distribution sites
- **Malvertising**: Abuse of Google Ads and legitimate AI chat platforms to distribute malware
- **Repository Impersonation**: Creation of fake repositories mimicking legitimate projects
- **Plugin Marketplace Abuse**: Uploading malicious versions of legitimate software plugins
- **Blockchain C2 Communication**: Use of TON blockchain for covert command and control

## Threat Actor Activities

- **ShinyHunters**: Breached Canvas LMS, demanded ransom, reached agreement with Instructure to prevent data leak
- **TeamPCP**: Responsible for multiple supply chain attacks including Mini Shai-Hulud worm, compromised Checkmarx Jenkins plugin and npm/PyPI packages
- **Mr_Rot13**: Actively exploiting cPanel CVE-2026-41940 to deploy Filemanager backdoors
- **Unknown AI-Using Actor**: First threat actor confirmed to use AI for zero-day exploit development targeting 2FA systems
- **TrickMo Operators**: Enhanced Android banking malware with TON blockchain communication capabilities
- **Aviation-Targeting Group**: Cyber espionage campaign focused on stealing GIS files, terrain models, and GPS data from aerospace companies
- **macOS Malware Distributors**: Using sophisticated social engineering through legitimate platforms to distribute Mac malware