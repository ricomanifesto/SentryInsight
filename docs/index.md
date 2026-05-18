# Exploitation Report

Critical zero-day vulnerabilities are currently under active exploitation, with the MiniPlasma Windows privilege escalation flaw enabling SYSTEM access on fully patched systems being the most concerning. Multiple enterprise platforms including NGINX, WordPress plugins, and various vendor products are experiencing active attacks, while supply chain compromises targeting developer environments and npm packages are expanding the threat landscape. The exploitation activity spans from zero-day attacks at security conferences to targeted campaigns against enterprise infrastructure and e-commerce platforms.

## Active Exploitation Details

### MiniPlasma Windows Zero-Day
- **Description**: A Windows privilege escalation vulnerability that allows attackers to gain SYSTEM privileges on fully patched Windows systems
- **Impact**: Complete system compromise with highest level privileges
- **Status**: Zero-day with proof-of-concept exploit publicly released by researcher Chaotic Eclipse

### NGINX Worker Crash Vulnerability
- **Description**: A security flaw in NGINX Plus and NGINX Open causing worker crashes and potentially enabling remote code execution
- **Impact**: Service disruption and potential remote code execution capabilities
- **Status**: Actively exploited in the wild days after public disclosure
- **CVE ID**: CVE-2026-42945

### DirtyDecrypt Linux Privilege Escalation
- **Description**: A local privilege escalation vulnerability in the Linux kernel's rxgk module
- **Impact**: Root access on affected Linux systems
- **Status**: Recently patched with proof-of-concept exploit now available

### Funnel Builder WordPress Plugin Vulnerability
- **Description**: A critical security flaw in the Funnel Builder plugin for WordPress enabling malicious JavaScript injection
- **Impact**: WooCommerce checkout page compromise for credit card theft
- **Status**: Under active exploitation for payment card skimming attacks

### node-ipc npm Package Compromise
- **Description**: Supply chain attack targeting the popular node-ipc inter-process communication package
- **Impact**: Credential theft from systems using compromised package versions
- **Status**: Malicious versions published to npm repository

### Avada Builder WordPress Plugin Flaws
- **Description**: Two vulnerabilities in the Avada Builder plugin affecting approximately one million active installations
- **Impact**: Arbitrary file reading and sensitive information extraction
- **Status**: Vulnerabilities disclosed, exploitation capability demonstrated

## Affected Systems and Products

- **Windows Systems**: All Windows versions affected by MiniPlasma zero-day privilege escalation
- **NGINX Infrastructure**: NGINX Plus and NGINX Open installations vulnerable to worker crashes and RCE
- **Linux Systems**: Systems with rxgk module affected by DirtyDecrypt privilege escalation
- **WordPress Sites**: Sites using Funnel Builder plugin vulnerable to checkout page compromise
- **E-commerce Platforms**: WooCommerce installations at risk of payment card theft
- **Node.js Applications**: Applications using compromised node-ipc package versions
- **Microsoft 365**: Accounts targeted by Tycoon2FA device-code phishing attacks
- **Enterprise Software**: Multiple vendors including Ivanti, Fortinet, SAP, VMware, and n8n releasing security patches

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Public release of MiniPlasma proof-of-concept enabling privilege escalation
- **Supply Chain Attacks**: Compromise of npm packages and developer workstation targeting
- **Web Application Attacks**: JavaScript injection into e-commerce checkout pages for payment theft
- **Phishing Campaigns**: Tycoon2FA kit using device-code phishing and Trustifi URL abuse
- **Social Engineering**: GitHub token theft leading to codebase downloads and extortion attempts
- **Malware Distribution**: Four malicious npm packages delivering infostealers and DDoS malware

## Threat Actor Activities

- **Chaotic Eclipse**: Security researcher releasing Windows zero-day proof-of-concepts including MiniPlasma
- **Secret Blizzard (Turla)**: Russian state-sponsored group developing modular P2P botnet from Kazuar backdoor
- **ShinyHunters**: Cybercriminal group involved in Canvas platform attacks and extortion attempts
- **Supply Chain Attackers**: Multiple campaigns targeting developer workstations and trusted software repositories
- **E-commerce Threat Actors**: Groups exploiting WordPress plugin vulnerabilities for payment card theft
- **Pwn2Own Participants**: Security researchers demonstrating 47 zero-day vulnerabilities across multiple enterprise platforms