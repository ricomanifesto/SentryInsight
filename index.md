# Exploitation Report

The current threat landscape reveals several critical exploitation activities across enterprise infrastructure and cybercrime operations. Most notably, HPE OneView is experiencing active exploitation of a maximum severity vulnerability (CVE-2025-37164) that enables remote code execution with devastating consequences. Chinese-speaking threat actors are leveraging VMware ESXi zero-day vulnerabilities to escape virtual machine environments, while Iranian MuddyWater operators have deployed a new Rust-based RAT called RustyWater through targeted spear-phishing campaigns across Middle Eastern sectors. Additionally, threat actors are systematically targeting misconfigured proxy servers to gain unauthorized access to commercial large language model services, and WhatsApp is being weaponized to distribute the Astaroth banking trojan across Brazil through automated contact messaging.

## Active Exploitation Details

### HPE OneView Remote Code Execution Vulnerability
- **Description**: A maximum severity vulnerability in HPE's IT infrastructure management platform that allows remote code execution
- **Impact**: Remote attackers can execute arbitrary code on affected systems, leading to complete system compromise
- **Status**: Currently being exploited in the wild
- **CVE ID**: CVE-2025-37164

### VMware ESXi Zero-Day Virtual Machine Escape
- **Description**: Zero-day vulnerabilities in VMware ESXi that allow attackers to escape virtual machine environments
- **Impact**: Virtual machine escape leading to hypervisor compromise and potential lateral movement across virtualized infrastructure
- **Status**: Actively exploited by Chinese-speaking threat actors using exploits potentially developed years ago

### Trend Micro Apex Central Remote Code Execution
- **Description**: Critical vulnerability in Trend Micro Apex Central on-premise Windows versions scoring 9.8 on CVSS scale
- **Impact**: Arbitrary code execution with SYSTEM privileges on affected security management consoles
- **Status**: Patched by Trend Micro, exploitation status in wild unknown

### Misconfigured Proxy Server Exploitation
- **Description**: Systematic targeting of misconfigured proxy servers to gain unauthorized access to commercial LLM services
- **Impact**: Unauthorized access to paid AI services, potential data exfiltration and service abuse
- **Status**: Ongoing systematic exploitation campaign

## Affected Systems and Products

- **HPE OneView**: IT infrastructure management platform with maximum severity RCE vulnerability
- **VMware ESXi**: Hypervisor platform affected by zero-day virtual machine escape vulnerabilities
- **Trend Micro Apex Central**: On-premise Windows versions vulnerable to critical RCE with SYSTEM privileges
- **SonicWall VPN Appliances**: Used as initial access vector in VMware ESXi exploitation campaigns
- **Chrome Browser Extensions**: Fake AI extensions targeting 900,000 users for data theft
- **WhatsApp Messaging Platform**: Weaponized for automated malware distribution in Brazil
- **ChatGPT Memory Feature**: Vulnerable to "ZombieAgent" prompt injection exploits
- **Misconfigured Proxy Servers**: Targeted for unauthorized LLM service access

## Attack Vectors and Techniques

- **Spear-Phishing Campaigns**: MuddyWater deploying RustyWater RAT targeting Middle Eastern diplomatic, maritime, financial, and telecom entities
- **Virtual Machine Escape**: Chinese threat actors exploiting VMware ESXi zero-days to break out of virtualized environments
- **WhatsApp Worm Distribution**: Automated contact messaging spreading Astaroth banking trojan across Brazilian users
- **Malicious QR Codes**: North Korean hackers using QR codes in targeted spear-phishing campaigns
- **Fake Browser Extensions**: Threat actors creating fraudulent AI Chrome extensions to steal ChatGPT and DeepSeek data
- **Credential Harvesting**: Russian APT28 running campaigns against Turkish energy agencies and strategic policy organizations
- **Proxy Server Misconfiguration Abuse**: Systematic hunting for improperly configured proxies to access paid LLM services
- **Prompt Injection Attacks**: ZombieAgent exploit leveraging ChatGPT's memory feature for persistent compromise

## Threat Actor Activities

- **MuddyWater (Iranian APT)**: Conducting spear-phishing campaigns with RustyWater RAT across Middle Eastern sectors including diplomatic, maritime, financial, and telecommunications organizations
- **Chinese-Speaking Threat Actors**: Exploiting VMware ESXi zero-day vulnerabilities for virtual machine escape, using compromised SonicWall VPN appliances as initial access vectors
- **Russian APT28 (Fancy Bear)**: Running credential-stealing campaigns targeting Turkish energy and nuclear research agencies, as well as strategic policy organizations
- **North Korean State-Sponsored Groups**: Deploying malicious QR codes in spear-phishing operations targeting cryptocurrency and financial sectors
- **Black Axe Criminal Organization**: 34 members arrested in Spain for €5.9M fraud operations and organized cybercrime activities
- **Brazilian Cybercriminals**: Operating WhatsApp worm campaigns to distribute Astaroth banking trojan through automated contact messaging
- **Chrome Extension Fraudsters**: Creating fake AI extensions to harvest data from 900,000 users and exfiltrate ChatGPT and DeepSeek information