# Exploitation Report

Current threat activity reveals significant exploitation campaigns targeting enterprise systems and infrastructure. The Clop ransomware gang is actively exploiting recently patched Oracle E-Business Suite vulnerabilities from July 2025, while CISA has flagged CVE-2025-4008 affecting Smartbedded Meteobridge as actively exploited in the wild. Multiple threat actors including Scattered Lapsus$, ShinyHunters, and state-sponsored groups are conducting sophisticated campaigns against major organizations, with particular focus on Salesforce customer data theft and supply chain attacks. Additionally, emerging attack vectors like CometJacking are targeting AI browsers, while traditional malware families continue to evolve with advanced evasion techniques.

## Active Exploitation Details

### Oracle E-Business Suite Vulnerabilities
- **Description**: Security flaws in Oracle's E-Business Suite that were patched in July 2025
- **Impact**: Enables attackers to conduct extortion campaigns and compromise enterprise data
- **Status**: Actively exploited by Clop ransomware gang in ongoing campaign

### Meteobridge Authentication Bypass
- **Description**: High-severity security flaw in Smartbedded Meteobridge weather monitoring systems
- **Impact**: Allows unauthorized access to weather monitoring infrastructure
- **Status**: Added to CISA's Known Exploited Vulnerabilities catalog for active exploitation
- **CVE ID**: CVE-2025-4008

### CometJacking Browser Vulnerability
- **Description**: Attack vector exploiting URL parameters in Perplexity's Comet AI browser
- **Impact**: Allows access to sensitive data from connected services including email and calendar
- **Status**: Newly discovered attack method affecting AI browser implementations

### DrayTek Vigor Router Remote Code Execution
- **Description**: Security vulnerability affecting multiple DrayTek Vigor router models
- **Impact**: Enables remote, unauthenticated attackers to execute arbitrary code
- **Status**: Advisory released by vendor for immediate patching

## Affected Systems and Products

- **Oracle E-Business Suite**: Enterprise resource planning system affected by July 2025 security patches
- **Smartbedded Meteobridge**: Weather monitoring and data logging devices
- **Perplexity Comet Browser**: AI-powered browser vulnerable to parameter injection attacks
- **DrayTek Vigor Routers**: Multiple router models susceptible to remote code execution
- **Salesforce**: Customer data targeted in multiple breach campaigns
- **Red Hat GitLab**: Private repositories reportedly compromised in widespread breach
- **Asahi Group**: Japanese brewery giant hit by ransomware disrupting factory operations
- **Renault and Dacia UK**: Customer data compromised through third-party provider breach

## Attack Vectors and Techniques

- **DNS-Powered Malware Distribution**: Detour Dog threat actor using DNS infrastructure to distribute Strela Stealer
- **PNG Steganography**: Rhadamanthys Stealer incorporating image-based payload delivery with device fingerprinting
- **WhatsApp Self-Propagation**: SORVEPOTEL malware spreading through messaging platform in Brazil
- **SEO Fraud and Site Hijacking**: UAT-8099 group infecting web servers for spam injection and data theft
- **Phishing Evolution**: Attack methods transitioning from email to mobile platforms including SMS and QR codes
- **Supply Chain Targeting**: Multiple campaigns focusing on third-party providers to reach end customers

## Threat Actor Activities

- **Clop Ransomware Gang**: Actively exploiting Oracle EBS vulnerabilities in extortion campaigns
- **Scattered Lapsus$**: Reemerged with new Salesforce data leak site threatening customer data publication
- **ShinyHunters**: Launched dedicated leak site to extort 39 companies affected by Salesforce breaches
- **Detour Dog**: Operating DNS-powered malware distribution network for Strela Stealer campaigns
- **UAT-8099**: Chinese-language group conducting SEO fraud and data theft through website hijacking
- **Confucius Group**: Targeting Pakistan with WooperStealer and Anondoor malware in phishing campaigns
- **YoroTrooper-affiliated Actor**: Conducting "Cavalry Werewolf" attacks against Russian agencies with FoalShell and StallionRAT
- **Pro-Russian Operatives**: Dutch authorities arrested two teenagers for alleged espionage activities