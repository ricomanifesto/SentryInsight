# Exploitation Report

Current threat landscape shows significant exploitation activity across multiple vectors, with state-sponsored actors leading sophisticated campaigns targeting critical infrastructure and enterprise systems. Chinese-linked threat actors are exploiting VMware ESXi zero-day vulnerabilities to achieve virtual machine escape capabilities, while Russian APT28 (Fancy Bear) continues credential harvesting operations against energy and policy organizations globally. Critical vulnerabilities in enterprise platforms like Trend Micro Apex Central and HPE OneView are being actively exploited, with attackers leveraging both zero-day exploits and recently disclosed flaws to gain remote code execution capabilities. Additionally, threat actors are increasingly targeting misconfigured proxy servers to gain unauthorized access to commercial AI services and deploying sophisticated social engineering campaigns using malicious QR codes and AI-powered Chrome extensions.

## Active Exploitation Details

### **VMware ESXi Zero-Day Vulnerabilities**
- **Description**: Multiple zero-day vulnerabilities in VMware ESXi hypervisor allowing virtual machine escape
- **Impact**: Attackers can break out of virtual machine isolation and gain access to the underlying hypervisor, potentially compromising entire virtualized environments
- **Status**: Actively exploited by Chinese-speaking threat actors; exploit may have been developed as early as previous years

### **HPE OneView Critical Vulnerability**
- **Description**: Maximum severity vulnerability in HPE's IT infrastructure management platform
- **Impact**: Remote code execution capabilities leading to complete compromise of infrastructure management systems
- **Status**: Actively exploited in the wild with devastating potential consequences
- **CVE ID**: CVE-2025-37164

### **Trend Micro Apex Central Remote Code Execution**
- **Description**: Critical vulnerability in on-premise Windows versions of Trend Micro Apex Central security management platform
- **Impact**: Arbitrary code execution on security management infrastructure, potentially compromising entire enterprise security posture
- **Status**: Security updates released; vulnerability scores 9.8 CVSS rating

### **Instagram Password Reset Bug**
- **Description**: Vulnerability allowing mass automated password reset email requests
- **Impact**: Threat actors exploited the bug to scrape data from over 17 million Instagram accounts
- **Status**: Fixed by Instagram; data allegedly leaked online

## Affected Systems and Products

- **VMware ESXi Hypervisor**: Multiple versions affected by zero-day exploits enabling VM escape
- **HPE OneView Platform**: IT infrastructure management systems vulnerable to maximum severity RCE flaw
- **Trend Micro Apex Central**: On-premise Windows versions susceptible to critical RCE vulnerability
- **Instagram Platform**: Social media accounts targeted through password reset functionality abuse
- **Commercial Proxy Servers**: Misconfigured proxy infrastructure providing unauthorized LLM service access
- **Chrome Browser Extensions**: Fake AI-powered extensions targeting 900,000+ users
- **WhatsApp Messaging**: Platform used as distribution vector for banking trojans
- **SonicWall VPN Appliances**: Compromised devices serving as initial access vectors

## Attack Vectors and Techniques

- **Virtual Machine Escape**: Exploitation of VMware ESXi zero-days to break hypervisor isolation
- **Proxy Server Abuse**: Systematic hunting for misconfigured proxies to access paid AI services
- **Spear-Phishing with QR Codes**: North Korean actors using malicious QR codes in targeted campaigns
- **WhatsApp Worm Distribution**: Auto-messaging functionality exploited to spread Astaroth banking trojan
- **Fake Browser Extensions**: AI-themed Chrome extensions harvesting ChatGPT and DeepSeek user data
- **Social Media Scraping**: Automated exploitation of platform bugs for mass data collection
- **Credential Harvesting**: Targeted phishing campaigns against energy and policy organizations
- **Initial Access via VPN**: Compromised SonicWall appliances as entry points for advanced attacks

## Threat Actor Activities

- **Chinese-Linked Groups**: Exploiting VMware ESXi zero-days through compromised SonicWall VPNs for VM escape attacks
- **Russian APT28 (Fancy Bear)**: Conducting credential-stealing campaigns targeting Turkish energy agencies and strategic organizations globally
- **Iranian MuddyWater**: Deploying RustyWater RAT via spear-phishing against Middle East diplomatic, maritime, financial, and telecom sectors
- **North Korean State Actors**: Using malicious QR codes in spear-phishing campaigns as warned by FBI
- **Black Axe Criminal Network**: 34 members arrested in Spain for €5.9M fraud operations and organized cybercrime activities
- **Brazilian Cybercriminals**: Spreading Astaroth banking trojan through WhatsApp worm campaigns
- **Chrome Extension Threat Actors**: Deploying fake AI extensions to harvest data from 900,000+ users