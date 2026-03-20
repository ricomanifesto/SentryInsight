# Exploitation Report

Critical exploitation activity is currently impacting organizations across multiple sectors, with several zero-day vulnerabilities being actively exploited in the wild. Most concerning is the DarkSword iOS exploit kit utilizing three zero-day vulnerabilities for complete device takeover, targeting users in Saudi Arabia, Turkey, Malaysia, and Ukraine. Simultaneously, the Interlock ransomware gang has been exploiting a maximum severity Cisco Secure Firewall Management Center zero-day vulnerability since January 2026. Additional active exploitation includes Russian APT28 targeting Ukrainian government systems through Zimbra vulnerabilities, while CISA has issued urgent warnings for multiple actively exploited flaws in Microsoft SharePoint and Zimbra Collaboration Suite systems.

## Active Exploitation Details

### DarkSword iOS Exploit Kit
- **Description**: A sophisticated exploit kit targeting Apple iOS devices using a combination of six vulnerabilities, including three zero-day flaws
- **Impact**: Enables complete device takeover and sensitive data theft from iOS devices
- **Status**: Actively exploited since at least November 2025 by multiple threat actors

### Cisco Secure Firewall Management Center Zero-Day
- **Description**: Maximum severity remote code execution vulnerability in Cisco FMC software
- **Impact**: Allows attackers to gain root access and deploy ransomware
- **Status**: Actively exploited by Interlock ransomware gang since January 2026
- **CVE ID**: CVE-2026-20131

### Microsoft SharePoint Critical Vulnerability
- **Description**: Critical vulnerability in Microsoft SharePoint patched in January
- **Impact**: Enables unauthorized access and potential system compromise
- **Status**: Now being actively exploited in attacks, prompting CISA warning

### Zimbra Collaboration Suite XSS Flaw
- **Description**: Cross-site scripting vulnerability in Zimbra Collaboration Suite
- **Impact**: Allows unauthorized access and potential data theft
- **Status**: Actively exploited by Russian APT28 in attacks against Ukrainian government

### PolyShell Magento Vulnerability
- **Description**: Newly disclosed vulnerability affecting all Magento Open Source and Adobe Commerce stable version 2 installations
- **Impact**: Allows unauthenticated remote code execution and complete account takeover
- **Status**: Newly disclosed with potential for widespread exploitation

### Ubiquiti UniFi Maximum Severity Flaw
- **Description**: Maximum severity vulnerability in UniFi Network Application
- **Impact**: May allow attackers to take over user accounts
- **Status**: Recently patched by Ubiquiti

### ConnectWise ScreenConnect Vulnerability
- **Description**: Cryptographic signature verification vulnerability in ScreenConnect
- **Impact**: Could lead to unauthorized access and privilege escalation
- **Status**: Recently patched by ConnectWise

## Affected Systems and Products

- **Apple iOS Devices**: All iOS versions targeted by DarkSword exploit kit
- **Cisco Secure Firewall Management Center**: FMC software vulnerable to zero-day exploitation
- **Microsoft SharePoint**: SharePoint installations vulnerable to critical flaw
- **Zimbra Collaboration Suite**: ZCS installations affected by XSS vulnerability
- **Magento E-commerce Platforms**: All Magento Open Source and Adobe Commerce version 2 installations
- **Ubiquiti UniFi Network Application**: Network management systems vulnerable to account takeover
- **ConnectWise ScreenConnect**: Remote access software affected by signature verification flaw
- **IoT Devices**: Over 3 million compromised devices used in massive botnets
- **Microsoft Intune Systems**: Endpoint management tools exploited in Stryker breach

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Multiple threat actors leveraging previously unknown vulnerabilities
- **Bring Your Own Vulnerable Driver (BYOVD)**: 54 EDR killers exploiting 34 signed vulnerable drivers
- **Cross-Site Scripting**: Web-based attacks targeting Zimbra installations
- **Remote Code Execution**: Unauthenticated RCE attacks against Magento stores
- **Ransomware Deployment**: Exploitation of Cisco vulnerabilities for ransomware distribution
- **Mobile Device Takeover**: iOS exploit chains for complete device compromise
- **Botnet Infrastructure**: IoT device compromise for large-scale DDoS attacks
- **Supply Chain Attacks**: Hijacking legitimate software infrastructure (Cobra DocGuard)
- **Prompt Injection**: Attacking AI systems through malicious prompts
- **Social Engineering**: Fake remote job schemes for IT worker infiltration

## Threat Actor Activities

- **APT28 (Russian GRU)**: Exploiting Zimbra vulnerabilities in attacks against Ukrainian government systems
- **Interlock Ransomware Gang**: Actively exploiting Cisco FMC zero-day since January 2026 for ransomware deployment
- **Lazarus Group (North Korean)**: Attributed to Bitrefill cryptocurrency platform attack
- **Bluenoroff Group**: Subgroup of Lazarus involved in financial cybercrime operations
- **Handala Hacktivist Group**: Conducted destructive cyberattack on Stryker medical technology company
- **Multiple Unknown Actors**: Operating DarkSword iOS exploit kit since November 2025
- **DPRK IT Worker Networks**: Using fake remote jobs to fund weapons of mass destruction programs
- **Various Cybercriminal Groups**: Deploying Perseus Android malware for financial fraud and device takeover
- **Speagle Malware Operators**: Hijacking legitimate Cobra DocGuard infrastructure for data theft