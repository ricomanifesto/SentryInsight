# Exploitation Report

Critical exploitation activity is currently targeting enterprise infrastructure and communication platforms worldwide. Chinese-speaking threat actors are actively exploiting VMware ESXi zero-day vulnerabilities to escape virtual machine environments, while Russian APT28 conducts credential-stealing campaigns against energy and policy organizations. North Korean hackers have escalated their tactics by incorporating malicious QR codes into spear-phishing operations. Additionally, a maximum severity vulnerability in HPE OneView is being actively exploited in the wild, and threat actors are systematically targeting misconfigured proxy servers to gain unauthorized access to paid LLM services.

## Active Exploitation Details

### VMware ESXi Zero-Day Vulnerabilities
- **Description**: Multiple zero-day vulnerabilities in VMware ESXi being exploited by Chinese-speaking threat actors to escape virtual machine environments
- **Impact**: Allows attackers to break out of virtual machine isolation and gain control over the hypervisor infrastructure
- **Status**: Active exploitation detected, patch status unknown

### HPE OneView Critical Vulnerability
- **Description**: Maximum severity vulnerability in HPE's IT infrastructure management platform
- **Impact**: Remote code execution capabilities leading to devastating consequences on enterprise infrastructure
- **Status**: Active exploitation confirmed in the wild
- **CVE ID**: CVE-2025-37164

### Trend Micro Apex Central Critical RCE Flaw
- **Description**: Critical vulnerability in on-premise Windows versions of Trend Micro Apex Central
- **Impact**: Could result in arbitrary code execution on affected systems
- **Status**: Security updates released by vendor

### Instagram Password Reset Bug
- **Description**: Bug in Instagram's password reset functionality that allowed mass-requesting of password reset emails
- **Impact**: Enabled threat actors to scrape and leak data from over 17 million Instagram accounts
- **Status**: Fixed by Instagram

## Affected Systems and Products

- **VMware ESXi**: Hypervisor environments targeted by Chinese threat actors for virtual machine escape attacks
- **HPE OneView**: IT infrastructure management platform with maximum severity vulnerability under active exploitation
- **Trend Micro Apex Central**: On-premise Windows versions affected by critical RCE vulnerability with 9.8 CVSS score
- **Instagram**: Social media platform affected by password reset bug leading to mass data scraping
- **SonicWall VPN Appliances**: Used as initial access vectors in attacks targeting VMware ESXi infrastructure
- **Misconfigured Proxy Servers**: Systematically targeted to access commercial large language model services
- **WhatsApp**: Messaging platform being exploited as distribution vector for Astaroth banking trojan
- **Chrome Extensions**: Fake AI-powered extensions stealing data from 900,000 users
- **Snapchat**: Platform targeted by phishing operations affecting nearly 600 accounts

## Attack Vectors and Techniques

- **Virtual Machine Escape**: Chinese actors exploiting VMware ESXi zero-days to break out of VM isolation
- **Spear-Phishing with QR Codes**: North Korean hackers incorporating malicious QR codes into targeted phishing campaigns
- **Credential Harvesting**: Russian APT28 conducting systematic credential theft campaigns
- **WhatsApp Worm Distribution**: Auto-messaging contacts to spread Astaroth banking trojan across Brazil
- **Proxy Server Exploitation**: Systematic hunting for misconfigured proxies to access paid LLM services
- **Malicious Browser Extensions**: Fake AI Chrome extensions designed to harvest ChatGPT and DeepSeek data
- **SonicWall VPN Compromise**: Using compromised VPN appliances as initial access vectors
- **Prompt Injection**: ZombieAgent exploit targeting ChatGPT's memory feature for enhanced attacks

## Threat Actor Activities

- **Chinese-Speaking Threat Actors**: Actively exploiting VMware ESXi zero-days and using SonicWall VPN compromise as initial access vector
- **Russian APT28 (Fancy Bear)**: Running credential-stealing campaigns targeting Turkish energy and nuclear research agencies, as well as strategic think tanks
- **North Korean State-Sponsored Groups**: Leveraging malicious QR codes in spear-phishing campaigns targeting cryptocurrency and DeFi sectors
- **Iranian MuddyWater APT**: Launching RustyWater RAT via spear-phishing across Middle East diplomatic, maritime, financial, and telecom sectors
- **Black Axe Criminal Organization**: 34 members arrested in Spain for €5.9 million fraud operations and organized cybercrime
- **Illinois-Based Threat Actor**: Charged with orchestrating Snapchat phishing operation affecting nearly 600 women's accounts
- **Brazilian Banking Trojan Operators**: Using WhatsApp worm to distribute Astaroth banking malware through contact auto-messaging