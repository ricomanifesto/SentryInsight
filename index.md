# Exploitation Report

Current security landscape reveals significant exploitation activity targeting enterprise infrastructure and consumer applications. CISA has flagged a critical vulnerability in Smartbedded Meteobridge devices (CVE-2025-4008) as actively exploited in the wild. Multiple attack campaigns are underway, including sophisticated reconnaissance efforts against Palo Alto Networks login portals showing a 500% spike in scanning activity, and novel attacks like CometJacking that exploit AI browser functionality. Threat actors including Scattered Lapsus$, ShinyHunters, and Detour Dog are actively conducting data theft operations, while new malware variants like SORVEPOTEL are spreading through messaging platforms and Rhadamanthys stealer continues evolving its capabilities.

## Active Exploitation Details

### Meteobridge Command Injection Vulnerability
- **Description**: High-severity security flaw affecting Smartbedded Meteobridge weather monitoring devices that allows remote code execution
- **Impact**: Attackers can execute arbitrary commands on affected devices, potentially gaining full system control
- **Status**: Actively exploited in the wild, flagged by CISA for immediate patching
- **CVE ID**: CVE-2025-4008

### CometJacking Attack Against Perplexity's Comet Browser
- **Description**: Novel attack technique that embeds malicious prompts within seemingly innocuous links to trick Comet AI browser into executing unauthorized actions
- **Impact**: Attackers can access sensitive data from connected services including email, calendars, and other integrated platforms
- **Status**: Newly disclosed attack method targeting AI browser functionality

### Palo Alto Networks Portal Reconnaissance
- **Description**: Massive surge in suspicious scanning activity targeting Palo Alto Networks login portals indicating coordinated reconnaissance efforts
- **Impact**: Potential precursor to credential stuffing attacks or exploitation attempts against network security infrastructure
- **Status**: Active scanning campaigns with 500% increase in activity observed

## Affected Systems and Products

- **Smartbedded Meteobridge**: Weather monitoring devices vulnerable to command injection attacks
- **Perplexity Comet Browser**: AI-powered browser susceptible to prompt injection attacks through malicious URLs
- **Palo Alto Networks Login Portals**: Enterprise security appliance interfaces under active reconnaissance
- **Salesforce Instances**: Multiple organizations affected by data theft campaigns conducted by cybercriminal groups
- **Discord Support Systems**: Third-party customer service provider compromised leading to data exposure
- **WhatsApp Messaging Platform**: Used as vector for SORVEPOTEL malware distribution targeting Brazilian users
- **Renault and Dacia UK Systems**: Customer data compromised through third-party provider breach

## Attack Vectors and Techniques

- **Command Injection**: Remote exploitation of Meteobridge devices through web interface vulnerabilities
- **Prompt Injection**: Malicious URL parameters used to manipulate AI browser behavior for data exfiltration
- **Credential Scanning**: Automated reconnaissance against enterprise login portals for authentication bypass attempts
- **DNS-Powered Malware Distribution**: Detour Dog using DNS infrastructure to deliver Strela Stealer payloads
- **PNG Steganography**: Rhadamanthys stealer hiding malicious payloads within image files for evasion
- **Social Engineering via Messaging**: SORVEPOTEL malware spreading through trusted WhatsApp communications
- **SEO Poisoning**: UAT-8099 hijacking legitimate websites for search engine manipulation and data theft

## Threat Actor Activities

- **Scattered Lapsus$ (ShinyHunters)**: Relaunched operations with new data leak site targeting 39 Salesforce breach victims, threatening data publication with October 10 deadline
- **Detour Dog**: Operating DNS-powered malware distribution infrastructure to deliver Strela Stealer information theft campaigns
- **UAT-8099**: Chinese-language threat actor conducting multi-stage attacks including web server infection, SEO spam injection, and organizational data theft
- **Cavalry Werewolf Campaign**: Targeting Russian public sector agencies with FoalShell and StallionRAT malware, showing operational overlaps with YoroTrooper group
- **Rhadamanthys Operators**: Enhanced stealer capabilities with device fingerprinting and steganographic payload delivery, expanding service offerings with proxy bots and crypting services
- **SORVEPOTEL Campaign**: Self-propagating malware targeting Brazilian users through WhatsApp social engineering tactics