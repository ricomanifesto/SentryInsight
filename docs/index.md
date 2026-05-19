# Exploitation Report

Critical exploitation activity is currently affecting multiple platforms and software ecosystems. A Microsoft Exchange zero-day vulnerability enables cross-site scripting attacks against Outlook Web Access, while NGINX faces active exploitation of a worker crash vulnerability. The Windows platform is threatened by a new privilege escalation zero-day called MiniPlasma that grants SYSTEM-level access on fully patched systems. Supply chain attacks continue to proliferate through compromised npm packages and GitHub Actions, with the leaked Shai-Hulud worm fueling widespread malicious campaigns. Linux systems face privilege escalation risks through the DirtyDecrypt vulnerability, and automatic tank gauge systems are being targeted in fuel infrastructure attacks.

## Active Exploitation Details

### Microsoft Exchange Zero-Day
- **Description**: Cross-site scripting (XSS) vulnerability affecting Microsoft Exchange servers
- **Impact**: Allows attackers to compromise Outlook Web Access (OWA) mailboxes and potentially execute malicious scripts in user sessions
- **Status**: Under active exploitation with no patch currently available
- **CVE ID**: CVE-2026-42897

### Windows MiniPlasma Privilege Escalation
- **Description**: Windows kernel vulnerability enabling local privilege escalation to SYSTEM level access
- **Impact**: Attackers can gain complete administrative control over Windows systems, bypassing security controls
- **Status**: Active zero-day with proof-of-concept exploit publicly released
- **Status**: Affects fully patched Windows systems

### NGINX Worker Crash Vulnerability
- **Description**: Security flaw affecting both NGINX Plus and NGINX Open Source causing worker process crashes
- **Impact**: Potential remote code execution and denial of service attacks against web servers
- **Status**: Under active exploitation in the wild following public disclosure
- **CVE ID**: CVE-2026-42945

### Linux DirtyDecrypt Root Escalation
- **Description**: Local privilege escalation vulnerability in the Linux kernel's rxgk module
- **Impact**: Allows attackers to gain root access on affected Linux systems
- **Status**: Recently patched but proof-of-concept exploit now available

### Claw Chain Vulnerabilities in OpenClaw
- **Description**: Multiple vulnerabilities in the rapidly growing AI agent framework
- **Impact**: Enable credential theft, privilege escalation, and persistence mechanisms
- **Status**: Now patched but previously exposed AI deployments

## Affected Systems and Products

- **Microsoft Exchange Servers**: Outlook Web Access components vulnerable to XSS attacks
- **Windows Systems**: All versions affected by MiniPlasma privilege escalation, including fully patched systems
- **NGINX Servers**: Both NGINX Plus and NGINX Open Source installations vulnerable to worker crashes
- **Linux Systems**: Kernel versions with rxgk module affected by DirtyDecrypt vulnerability
- **GitHub Actions**: actions-cool/issues-helper workflow compromised in supply chain attack
- **npm Ecosystem**: Multiple packages including @antv ecosystem components compromised
- **OpenClaw AI Framework**: Deployments vulnerable to credential theft and privilege escalation
- **macOS Systems**: Targeted by SHub infostealer variants spoofing Apple security updates
- **Automatic Tank Gauge Systems**: Fuel infrastructure systems exposed on the Internet being tampered with

## Attack Vectors and Techniques

- **Cross-Site Scripting (XSS)**: Exploitation of Exchange vulnerability to compromise OWA mailboxes
- **Privilege Escalation**: Local exploitation to gain SYSTEM access on Windows and root access on Linux
- **Supply Chain Poisoning**: Compromised maintainer accounts pushing malicious packages to npm registry
- **GitHub Repository Manipulation**: Redirecting popular Action tags to imposter commits for credential harvesting
- **Social Engineering**: Fake Apple security update messages installing backdoors on macOS
- **Device-Code Phishing**: Tycoon2FA kit using device-code attacks to bypass multi-factor authentication
- **AppleScript Abuse**: Displaying fake security prompts to install malicious payloads
- **Infrastructure Targeting**: Direct attacks on automatic tank gauge systems in fuel facilities

## Threat Actor Activities

- **Mini Shai-Hulud Campaign**: Compromising npm maintainer accounts to distribute malicious packages across the @antv ecosystem
- **Iranian Cyber Operations**: Expanding scope to target fuel tank infrastructure systems through insecure automatic tank gauge systems
- **Supply Chain Attackers**: Targeting developer workstations and CI/CD environments to steal credentials and inject malicious code
- **Phishing Kit Operators**: Using Tycoon2FA to hijack Microsoft 365 accounts through advanced device-code phishing techniques
- **INTERPOL Operation Ramz**: Law enforcement disruption resulting in 201 arrests and seizure of 53 malware and phishing servers across MENA region
- **Worm Proliferation**: Multiple threat actors leveraging leaked Shai-Hulud source code to create new npm-based infostealer campaigns