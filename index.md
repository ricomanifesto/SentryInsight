# Exploitation Report

Several critical vulnerabilities are currently under active exploitation, highlighting the evolving threat landscape. The most significant ongoing exploitation involves a cPanel vulnerability (CVE-2026-41940) being actively targeted by the threat actor Mr_Rot13 to deploy the Filemanager backdoor on compromised environments. Additionally, Google has identified the first known instance of hackers using artificial intelligence to develop a zero-day exploit for a two-factor authentication bypass in a popular web administration tool, marking a concerning evolution in threat actor capabilities. Other notable exploitation activities include compromised software supply chains affecting CheckMarx Jenkins plugins by TeamPCP threat actors, Canvas portal defacements through security vulnerabilities, and the emergence of the "Dirty Frag" privilege escalation vulnerability in Linux enterprise distributions.

## Active Exploitation Details

### cPanel Critical Vulnerability
- **Description**: A critical security flaw in cPanel control panel software being exploited to deploy backdoor access
- **Impact**: Attackers can deploy the "Filemanager" backdoor on compromised cPanel environments, providing persistent access to web hosting infrastructure
- **Status**: Under active exploitation by threat actor Mr_Rot13
- **CVE ID**: CVE-2026-41940

### AI-Generated Zero-Day 2FA Bypass
- **Description**: First known zero-day exploit developed using artificial intelligence targeting two-factor authentication mechanisms in a web administration tool
- **Impact**: Complete bypass of 2FA protections allowing unauthorized access to administrative interfaces
- **Status**: Active exploitation identified by Google Threat Intelligence Group, likely AI-generated exploit code

### Canvas Portal Security Flaw
- **Description**: Security vulnerability in Instructure's Canvas learning management system allowing portal modification
- **Impact**: Hackers can deface Canvas login portals and leave extortion messages, disrupting educational services
- **Status**: Confirmed active exploitation with portal defacements reported

### Dirty Frag Linux Vulnerability
- **Description**: Privilege escalation vulnerability in Linux systems similar to Copy Fail and Dirty Pipe flaws
- **Impact**: Local privilege escalation allowing attackers to gain elevated system access
- **Status**: May already be under limited exploitation according to security researchers

## Affected Systems and Products

- **cPanel Control Panel**: Web hosting management software experiencing critical vulnerability exploitation
- **CheckMarx Jenkins AST Plugin**: Supply chain compromise affecting CI/CD security scanning infrastructure
- **Canvas Learning Management System**: Educational platform portals being defaced through security flaws
- **Linux Enterprise Distributions**: Multiple enterprise Linux distributions vulnerable to Dirty Frag privilege escalation
- **Web Administration Tools**: Unspecified popular open-source web admin tool targeted by AI-generated zero-day
- **JDownloader Platform**: Download manager website compromised to distribute malware-infected installers
- **Ollama AI Platform**: Out-of-bounds read vulnerability allowing remote process memory leakage

## Attack Vectors and Techniques

- **Supply Chain Poisoning**: Threat actors compromising legitimate software repositories and plugins to distribute malicious code
- **AI-Assisted Exploit Development**: First documented use of artificial intelligence to generate zero-day exploit code
- **Website Compromise**: Direct compromise of software distribution websites to replace legitimate installers with malware
- **Portal Defacement**: Exploitation of web application vulnerabilities to modify user interfaces and display extortion messages
- **Privilege Escalation**: Linux kernel-level vulnerabilities being exploited for local privilege escalation
- **Memory Disclosure**: Out-of-bounds read attacks targeting AI platforms to leak sensitive process memory

## Threat Actor Activities

- **Mr_Rot13**: Actively exploiting cPanel CVE-2026-41940 to deploy Filemanager backdoors on hosting infrastructure
- **TeamPCP**: Conducting supply chain attacks against CheckMarx Jenkins plugins weeks after previous KICS attacks
- **ShinyHunters**: Claims responsibility for second attack against Instructure's Canvas platform
- **Unknown AI-Enabled Group**: First threat actor identified using AI to develop zero-day exploits for 2FA bypass
- **TCLBANKER Operators**: Brazilian threat group targeting financial platforms with new banking trojan capabilities
- **Aviation Espionage Group**: Cyber espionage campaign targeting aerospace and drone operators to steal GIS and mapping data