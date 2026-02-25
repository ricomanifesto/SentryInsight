# Exploitation Report

Critical exploitation activity is currently centered around several high-impact vulnerabilities and threat actor campaigns. CISA has confirmed active exploitation of a FileZen vulnerability (CVE-2026-25108), while SolarWinds has patched four critical Serv-U flaws that enable root code execution. Meanwhile, sophisticated threat actors including the North Korean Lazarus Group are deploying Medusa ransomware in healthcare attacks, and Russian exploit brokers are actively purchasing stolen zero-day exploits from defense contractors. The threat landscape is further complicated by ATM jackpotting attacks that surged in 2025, costing banks over $20 million, and the emergence of new cybercrime services enabling malicious Google ads to evade detection for extended periods.

## Active Exploitation Details

### FileZen Vulnerability
- **Description**: A critical vulnerability in FileZen file transfer software that is being actively exploited in the wild
- **Impact**: Allows attackers to compromise file transfer systems and potentially gain unauthorized access to sensitive data
- **Status**: Added to CISA's Known Exploited Vulnerabilities (KEV) catalog with evidence of active exploitation
- **CVE ID**: CVE-2026-25108

### SolarWinds Serv-U Critical Flaws
- **Description**: Four critical security vulnerabilities in SolarWinds Serv-U 15.5 file transfer software that enable remote code execution
- **Impact**: Successful exploitation could result in root-level code execution on affected servers, providing complete system compromise
- **Status**: Patches have been released by SolarWinds to address these vulnerabilities

### GitHub Codespaces RoguePilot Flaw
- **Description**: A vulnerability in GitHub Codespaces that could be exploited through malicious Copilot instructions injected in GitHub issues
- **Impact**: Enables attackers to seize control of repositories by leaking GITHUB_TOKEN credentials
- **Status**: Vulnerability disclosed and addressed

### Zero-Day Exploit Trading
- **Description**: Active marketplace for zero-day exploits involving Russian brokers purchasing stolen vulnerabilities from defense contractors
- **Impact**: Eight zero-day exploits were sold to Russian entities, potentially compromising national security systems
- **Status**: US sanctions imposed on Russian broker; former L3Harris executive sentenced to over seven years in prison

## Affected Systems and Products

- **FileZen**: File transfer software with actively exploited vulnerability
- **SolarWinds Serv-U 15.5**: File transfer software with four critical RCE flaws
- **GitHub Codespaces**: Development environment vulnerable to token leakage
- **ATM Systems**: Widespread jackpotting attacks targeting banking infrastructure
- **Android Mental Health Apps**: 14.7 million installations affected by security vulnerabilities
- **Telecommunications Infrastructure**: Central Asian telecoms targeted by UnsolicitedBooker group
- **Healthcare Systems**: U.S. healthcare organizations targeted by Lazarus Group ransomware
- **Freight and Logistics Systems**: European and U.S. operators targeted by Diesel Vortex phishing

## Attack Vectors and Techniques

- **File Transfer Exploitation**: Attackers targeting critical vulnerabilities in file transfer solutions
- **Ransomware Deployment**: Lazarus Group using Medusa ransomware with Comebacker backdoor, Blindingcan RAT, and Infohook stealer
- **Social Engineering**: Russia-aligned UAC-0050 using spoofed domains and RMS malware against European financial institutions
- **Phishing Campaigns**: Diesel Vortex group using 52 domains to steal credentials from logistics organizations
- **Malicious Advertising**: 1Campaign platform enabling threat actors to run persistent malicious Google ads
- **ATM Jackpotting**: Physical and logical attacks causing ATMs to dispense cash, with losses exceeding $20 million
- **Backdoor Deployment**: UnsolicitedBooker using LuciDoor and MarsSnake backdoors against telecommunications targets

## Threat Actor Activities

- **Lazarus Group (Diamond Sleet/Pompilus)**: North Korean state-backed group conducting ransomware attacks against Middle East and U.S. healthcare organizations using Medusa ransomware
- **UAC-0050**: Russia-aligned threat actor targeting European financial institutions through social engineering attacks for intelligence gathering and financial theft
- **Diesel Vortex**: Financially motivated group conducting credential theft campaigns against freight and logistics operators in the U.S. and Europe
- **UnsolicitedBooker**: Threat cluster targeting telecommunications companies in Kyrgyzstan and Tajikistan with custom backdoors
- **ShinyHunters**: Extortion gang responsible for multiple data breaches including Wynn Resorts, CarGurus (12.4 million records), and Odido telecommunications provider
- **Russian Exploit Brokers**: Active procurement of zero-day exploits from compromised defense contractor personnel
- **ATM Criminal Networks**: Organized groups conducting jackpotting attacks across banking infrastructure using established tools and tactics