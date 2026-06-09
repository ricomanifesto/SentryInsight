# Exploitation Report

This report identifies critical active exploitation across multiple platforms and products. Most significantly, Google Chrome's V8 engine has been targeted through a zero-day vulnerability that has been exploited in the wild, representing the fifth Chrome zero-day patched this year. Russian-aligned threat actors continue to exploit a previously patched WinRAR vulnerability in targeted campaigns against Ukrainian organizations. Multiple zero-day vulnerabilities are being actively exploited, including flaws in Check Point VPN systems by ransomware groups, and critical vulnerabilities in various enterprise software platforms. Supply chain attacks have intensified with multiple campaigns targeting Python Package Index repositories, while threat actors are leveraging social engineering and advanced persistent techniques to compromise high-value targets including government systems and enterprise infrastructure.

## Active Exploitation Details

### Chrome V8 Zero-Day Vulnerability
- **Description**: High-severity vulnerability in Google Chrome's V8 JavaScript engine
- **Impact**: Allows attackers to execute arbitrary code in the context of the browser, potentially leading to system compromise
- **Status**: Actively exploited in the wild; security updates released by Google
- **CVE ID**: CVE-2026-11645

### WinRAR Security Flaw
- **Description**: Previously patched vulnerability in WinRAR compression software being exploited almost a year after patches were released
- **Impact**: Enables deployment of information stealers and facilitates data theft and cyberespionage operations
- **Status**: Fixed in July 2024, but continues to be exploited against unpatched systems
- **CVE ID**: CVE-2025-8088

### Check Point VPN Critical Vulnerability
- **Description**: Critical zero-day vulnerability in Check Point Remote Access VPN and Mobile Access deployments configured with deprecated IKEv1 protocol
- **Impact**: Allows password bypass and unauthorized access to VPN systems
- **Status**: Actively exploited since early May 2024 by ransomware groups including Qilin; CISA ordered federal agencies to patch within 3 days

### LiteLLM Authentication Bypass
- **Description**: High-severity flaw in BerriAI LiteLLM that can be chained to achieve unauthenticated remote code execution
- **Impact**: Complete system compromise through unauthenticated RCE
- **Status**: Added to CISA's Known Exploited Vulnerabilities catalog due to active exploitation
- **CVE ID**: CVE-2026-42271

### Linux Kernel Use-After-Free Vulnerability
- **Description**: One-character flaw in Linux kernel that enables local privilege escalation
- **Impact**: Allows unprivileged local users to escalate to root access and break out of containers
- **Status**: Public exploits available; working proof-of-concept published

### Gogs Git Service Zero-Day
- **Description**: Critical zero-day vulnerability in Gogs Git service
- **Impact**: Enables remote code execution and compromise of Internet-facing instances, allowing access to any repositories including private ones
- **Status**: Zero-day exploitation confirmed; patches released

### Veeam Backup & Replication Vulnerability
- **Description**: Critical security flaw in Veeam Backup & Replication software
- **Impact**: Remote code execution on domain-joined backup servers
- **Status**: Security updates released to address the vulnerability

## Affected Systems and Products

- **Google Chrome**: V8 JavaScript engine affected across all platforms
- **WinRAR**: Compression software, particularly versions not updated since July 2024
- **Check Point VPN**: Remote Access VPN and Mobile Access deployments using IKEv1 protocol
- **BerriAI LiteLLM**: AI/ML model integration platform
- **Linux Kernel**: Multiple distributions affected by privilege escalation flaw
- **Gogs**: Self-hosted Git service installations
- **Veeam Backup & Replication**: Enterprise backup solutions on domain-joined servers
- **UniFi OS**: Ubiquiti network management platform
- **Python Package Index (PyPI)**: Multiple compromised packages affecting science-focused libraries
- **GitHub**: Microsoft repositories and hosting platform
- **WhatsApp**: Messaging platform targeted by NSO Group spyware

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Multiple zero-day vulnerabilities actively exploited before patches became available
- **Supply Chain Attacks**: Malicious packages injected into PyPI repository affecting downstream users
- **Social Engineering**: Sophisticated phishing campaigns and vishing attacks targeting high-value organizations
- **Ransomware Deployment**: Vulnerabilities exploited as initial access vectors for ransomware operations
- **Container Escape**: Linux kernel flaw enabling escape from containerized environments
- **Password Bypass**: VPN vulnerabilities allowing authentication bypass in legacy configurations
- **Remote Code Execution**: Multiple vulnerabilities enabling complete system compromise
- **Repository Poisoning**: Malicious code injection into legitimate software repositories
- **Timing-Based Attacks**: FROST attack technique using SSD timing for cross-site tracking

## Threat Actor Activities

- **Russian-Aligned Groups**: Conducting sustained campaigns against Ukrainian military and government organizations using WinRAR exploits for data theft and cyberespionage
- **Qilin Ransomware**: Exploiting Check Point VPN vulnerabilities as initial access vector for ransomware deployment
- **NSO Group**: Conducting spear-phishing campaigns through WhatsApp to deploy surveillance spyware
- **Silent Ransom Group**: Targeting US law firms through combination of vishing, IT impersonation, and physical office intrusions
- **Miasma Campaign Actors**: Orchestrating large-scale supply chain attacks against Python Package Index with credential stealing malware
- **Shai-Hulud Operators**: Compromising science-focused PyPI packages to steal developer credentials and secrets