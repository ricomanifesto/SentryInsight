# Exploitation Report

The current threat landscape reveals several critical exploitation activities targeting diverse platforms and systems. CISA has flagged CVE-2025-4008, a high-severity vulnerability in Smartbedded Meteobridge devices, as actively exploited in the wild. Meanwhile, Oracle has linked ongoing Clop ransomware extortion campaigns to vulnerabilities in E-Business Suite that were patched in July 2025, though the specific vulnerabilities remain under investigation by Google Mandiant. DrayTek has warned of a remote code execution vulnerability affecting multiple Vigor router models, while new attack techniques like "CometJacking" are being used to exploit AI browser functionalities. Threat actors continue to evolve their tactics, with campaigns like SORVEPOTEL targeting WhatsApp users in Brazil, Confucius APT deploying new malware against Pakistani targets, and UAT-8099 conducting sophisticated SEO fraud operations.

## Active Exploitation Details

### Meteobridge Weather Station Vulnerability
- **Description**: A high-severity security flaw impacting Smartbedded Meteobridge weather station devices that allows unauthorized access and control
- **Impact**: Attackers can gain unauthorized access to weather monitoring systems and potentially use them as entry points into larger networks
- **Status**: Actively exploited in the wild, added to CISA's Known Exploited Vulnerabilities catalog
- **CVE ID**: CVE-2025-4008

### Oracle E-Business Suite Vulnerabilities
- **Description**: Security flaws in Oracle E-Business Suite (EBS) that were patched in July 2025, now being exploited in extortion campaigns
- **Impact**: Attackers are conducting data theft and extortion operations against organizations using vulnerable EBS systems
- **Status**: Actively exploited by Clop ransomware gang for ongoing extortion campaigns, patches available since July 2025

### DrayTek Vigor Router Remote Code Execution
- **Description**: A security vulnerability affecting several DrayTek Vigor router models that allows remote, unauthenticated code execution
- **Impact**: Attackers can execute arbitrary code remotely without authentication, potentially gaining full control of network infrastructure
- **Status**: Advisory released by DrayTek, exploitation status in the wild unclear

### CometJacking Browser Exploitation
- **Description**: A new attack technique that exploits URL parameters in Perplexity's Comet AI browser to pass hidden instructions
- **Impact**: Attackers can access sensitive data from connected services including email and calendar systems
- **Status**: Newly discovered attack method, exploitation capabilities demonstrated

## Affected Systems and Products

- **Smartbedded Meteobridge**: Weather station devices vulnerable to unauthorized access
- **Oracle E-Business Suite**: Enterprise resource planning systems targeted in extortion campaigns
- **DrayTek Vigor Routers**: Multiple router models affected by remote code execution vulnerability
- **Perplexity Comet Browser**: AI-powered browser vulnerable to parameter injection attacks
- **WhatsApp**: Messaging platform being used to spread SORVEPOTEL malware in Brazil
- **Salesforce Platforms**: 39 organizations impacted by ShinyHunters data breaches
- **Microsoft Outlook**: SVG image display functionality used in previous attacks (now mitigated)
- **Red Hat GitLab**: Private repositories allegedly compromised affecting 28,000 repositories

## Attack Vectors and Techniques

- **Parameter Injection**: CometJacking exploits URL parameters to inject hidden instructions into AI browsers
- **Social Engineering**: WhatsApp malware campaigns using trusted messaging platforms for distribution
- **Supply Chain Attacks**: Malicious PyPI packages like "soopsocks" targeting Python developers
- **SEO Poisoning**: UAT-8099 threat actor hijacking legitimate websites for search engine manipulation
- **Phishing Evolution**: Migration from email-based phishing to mobile platforms including SMS and QR codes
- **Repository Compromise**: Large-scale breaches of private code repositories for data theft
- **Network Infrastructure Targeting**: Exploitation of routers and network devices for persistent access

## Threat Actor Activities

- **Clop Ransomware Gang**: Conducting ongoing extortion campaigns against Oracle EBS users, leveraging July 2025 vulnerabilities for data theft operations
- **ShinyHunters**: Operating data leak site to extort 39 Salesforce breach victims, publicly releasing stolen data samples to pressure organizations
- **UAT-8099**: Chinese-language threat actor conducting comprehensive campaigns including web server infections, SEO spam injection, and organizational data theft
- **Confucius APT**: Long-running South Asian advanced persistent threat group targeting Pakistani organizations with new WooperStealer and Anondoor malware families
- **YoroTrooper-linked Actor**: "Cavalry Werewolf" campaign targeting Russian public sector with FoalShell and StallionRAT malware
- **SORVEPOTEL Campaign**: Self-propagating malware operation targeting Brazilian WhatsApp users through trusted messaging channels
- **Malicious Package Distributors**: Cybercriminals distributing "soopsocks" package on PyPI, successfully infecting 2,653 systems before takedown