# Exploitation Report

Critical vulnerability exploitation activity is currently impacting multiple sectors, with ransomware operators leveraging sophisticated techniques to bypass security controls. Notable active exploitation includes CVE-2024-7344 being exploited by HybridPetya ransomware to bypass UEFI Secure Boot protections, CVE-2025-5086 in DELMIA Apriso Manufacturing Operations Management software being actively exploited in the wild, and a Samsung zero-day vulnerability reported by WhatsApp that was being exploited in targeted attacks. Additional concerns include the Gentlemen ransomware family weaponizing vulnerable drivers to disable security solutions, and security flaws in AI-powered development tools that could enable silent code execution.

## Active Exploitation Details

### HybridPetya Ransomware UEFI Bypass
- **Description**: A new ransomware strain that combines characteristics of the notorious Petya/NotPetya malware with advanced UEFI bypass capabilities
- **Impact**: Can circumvent UEFI Secure Boot protections, allowing for low-level system compromise and encryption
- **Status**: Actively exploiting systems in the wild
- **CVE ID**: CVE-2024-7344

### DELMIA Apriso Manufacturing Vulnerability
- **Description**: Critical security flaw in Dassault Systèmes DELMIA Apriso Manufacturing Operations Management software
- **Impact**: Allows attackers to compromise manufacturing and industrial control systems
- **Status**: Actively exploited in the wild, CISA has issued official warning
- **CVE ID**: CVE-2025-5086

### Samsung Android Zero-Day
- **Description**: Remote code execution vulnerability affecting Samsung Android devices
- **Impact**: Enables attackers to execute arbitrary code remotely on targeted devices
- **Status**: Was being actively exploited before Samsung released patches, reported by WhatsApp security team

### Cursor AI Code Editor Vulnerability
- **Description**: Security weakness in the AI-powered code editor that enables silent code execution
- **Impact**: Maliciously crafted repositories can trigger code execution when opened in the editor
- **Status**: Vulnerability disclosed, affects developers using the platform

## Affected Systems and Products

- **Dassault Systèmes DELMIA Apriso**: Manufacturing Operations Management software used in industrial environments
- **Samsung Android Devices**: Various Samsung smartphone and tablet models running Android
- **UEFI-Enabled Systems**: Computers and servers with UEFI Secure Boot implementations vulnerable to CVE-2024-7344
- **Cursor AI Code Editor**: AI-powered development environment used by software developers
- **Solar-Powered Highway Infrastructure**: Transportation department devices with undocumented radio components
- **Systems with ThrottleStop.sys Driver**: Windows systems vulnerable to driver abuse by Gentlemen ransomware

## Attack Vectors and Techniques

- **UEFI Secure Boot Bypass**: HybridPetya exploits CVE-2024-7344 to circumvent boot-level security protections
- **Vulnerable Driver Abuse**: Gentlemen ransomware weaponizes the ThrottleStop.sys driver to disable antivirus and EDR systems
- **Malicious Repository Exploitation**: Cursor AI vulnerability triggered through specially crafted code repositories
- **Remote Code Execution**: Samsung vulnerability allows attackers to execute code remotely on Android devices
- **Manufacturing System Compromise**: DELMIA Apriso vulnerability enables attacks on industrial control systems

## Threat Actor Activities

- **HybridPetya Operators**: Deploying advanced ransomware with UEFI bypass capabilities to evade security controls
- **Gentlemen Ransomware Group**: Utilizing vulnerable driver abuse techniques to disable endpoint security solutions before encryption
- **Samsung Device Attackers**: Conducting targeted zero-day attacks against Samsung Android users, detected by WhatsApp security team
- **Industrial System Attackers**: Actively exploiting manufacturing software vulnerabilities to compromise operational technology environments