# Exploitation Report

Current threat landscape shows significant exploitation activity across multiple attack vectors. Chinese-speaking threat actors are leveraging VMware ESXi zero-day vulnerabilities to achieve virtual machine escapes, while HPE OneView faces maximum severity exploitation enabling remote code execution. State-sponsored groups including Russian APT28 and Iranian MuddyWater continue aggressive credential harvesting campaigns, with North Korean actors adopting novel QR code-based phishing techniques. Additional threats include widespread misconfigured proxy exploitation for unauthorized LLM access and sophisticated social engineering campaigns targeting financial institutions through messaging platforms.

## Active Exploitation Details

### VMware ESXi Zero-Day Vulnerabilities
- **Description**: Critical zero-day vulnerabilities in VMware ESXi hypervisor allowing virtual machine escape
- **Impact**: Attackers can escape virtual machine confines and potentially gain access to hypervisor infrastructure
- **Status**: Active exploitation by Chinese-speaking threat actors, exploiting compromised SonicWall VPN appliances as initial access vector

### HPE OneView Remote Code Execution Flaw
- **Description**: Maximum severity vulnerability in HPE's IT infrastructure management platform
- **Impact**: Remote code execution capabilities leading to potential complete system compromise
- **Status**: Currently being exploited in the wild with devastating potential consequences
- **CVE ID**: CVE-2025-37164

### Trend Micro Apex Central RCE Vulnerability
- **Description**: Critical security flaw in on-premise Trend Micro Apex Central for Windows
- **Impact**: Arbitrary code execution with SYSTEM privileges
- **Status**: Recently patched by vendor, CVSS score of 9.8

### Misconfigured Proxy Server Exploitation
- **Description**: Systematic targeting of misconfigured proxy servers to access commercial LLM services
- **Impact**: Unauthorized access to paid AI services and potential data theft
- **Status**: Ongoing active exploitation campaign

## Affected Systems and Products

- **VMware ESXi**: Hypervisor platforms vulnerable to zero-day exploits enabling VM escape
- **HPE OneView**: IT infrastructure management platform with maximum severity RCE vulnerability
- **Trend Micro Apex Central**: On-premise Windows versions affected by critical RCE flaw
- **SonicWall VPN Appliances**: Used as initial access vector in VMware ESXi attacks
- **Proxy Servers**: Misconfigured instances providing unauthorized LLM access
- **WhatsApp**: Messaging platform exploited for banking trojan distribution in Brazil
- **ChatGPT**: Memory feature exploited through "ZombieAgent" prompt injection techniques
- **Chrome Extensions**: Fake AI extensions compromising 900,000 users' data

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: VMware ESXi vulnerabilities leveraged for hypervisor compromise
- **VPN Compromise**: SonicWall appliances used as entry points for advanced attacks
- **Spear-Phishing**: Multiple campaigns using email and QR codes for credential harvesting
- **Social Engineering**: WhatsApp worm campaigns distributing Astaroth banking trojan
- **Prompt Injection**: ChatGPT memory feature exploitation through ZombieAgent techniques
- **Malicious Browser Extensions**: Fake AI Chrome extensions harvesting user data
- **Proxy Exploitation**: Systematic hunting for misconfigured proxy servers
- **Credential Harvesting**: Targeted phishing against energy and policy organizations

## Threat Actor Activities

- **Chinese-Speaking Groups**: Deploying VMware ESXi exploits developed as early as possible, using SonicWall VPN compromise for initial access
- **APT28 (Fancy Bear)**: Russian state-sponsored credential stealing campaigns targeting Turkish energy agencies and strategic policy organizations
- **MuddyWater**: Iranian threat actor launching RustyWater RAT via spear-phishing across Middle East diplomatic, maritime, financial, and telecom sectors
- **North Korean State Actors**: FBI-warned campaigns using malicious QR codes in spear-phishing operations
- **Black Axe**: 34 members arrested in Spain for organized cybercrime involving €5.9M fraud operations
- **Brazilian Cybercriminals**: WhatsApp worm campaigns spreading Astaroth banking trojan through contact auto-messaging
- **AI Extension Fraudsters**: Creating fake Chrome extensions to harvest ChatGPT and DeepSeek user data affecting 900,000 users