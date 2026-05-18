# Exploitation Report

Current threat activity reveals a diverse landscape of active exploitation targeting critical infrastructure and development environments. Zero-day vulnerabilities are being actively exploited across Windows systems, web applications, and enterprise software platforms. Notable active exploits include the Windows MiniPlasma privilege escalation zero-day enabling SYSTEM access on fully patched systems, and CVE-2026-42945 affecting NGINX platforms that has come under immediate exploitation following public disclosure. Supply chain attacks continue to target developer workstations and package repositories, with malicious npm packages delivering infostealers and sophisticated phishing campaigns targeting Microsoft 365 accounts. WordPress plugin vulnerabilities are being actively exploited for payment card skimming operations, while enterprise platforms from major vendors including Ivanti, Fortinet, VMware, and SAP have released patches for critical remote code execution and privilege escalation flaws.

## Active Exploitation Details

### MiniPlasma Windows Zero-Day
- **Description**: A Windows privilege escalation zero-day vulnerability that enables attackers to gain SYSTEM privileges on fully patched Windows systems
- **Impact**: Complete system compromise allowing attackers to execute arbitrary code with highest privileges
- **Status**: Active zero-day with public proof-of-concept exploit released by security researcher Chaotic Eclipse

### NGINX Worker Process Vulnerability
- **Description**: Security flaw affecting NGINX Plus and NGINX Open causing worker crashes and potential remote code execution
- **Impact**: Service disruption and possible arbitrary code execution on web servers
- **Status**: Under active exploitation in the wild following public disclosure
- **CVE ID**: CVE-2026-42945

### DirtyDecrypt Linux Privilege Escalation
- **Description**: Local privilege escalation vulnerability in the Linux kernel's rxgk module
- **Impact**: Allows attackers to gain root access on affected Linux systems
- **Status**: Recently patched with public proof-of-concept exploit available

### Funnel Builder WordPress Plugin
- **Description**: Critical vulnerability in the Funnel Builder plugin for WordPress enabling malicious JavaScript injection
- **Impact**: Payment card skimming through WooCommerce checkout page manipulation
- **Status**: Under active exploitation for credit card theft operations

## Affected Systems and Products

- **Windows Systems**: All versions vulnerable to MiniPlasma zero-day privilege escalation
- **NGINX Plus and NGINX Open**: Web server platforms affected by worker process vulnerability
- **Linux Kernel**: Systems running vulnerable rxgk module implementations
- **WordPress Sites**: Installations using Funnel Builder plugin vulnerable to checkout skimming
- **Ivanti Products**: Multiple vulnerabilities patched including RCE and authentication bypass flaws
- **Fortinet Systems**: Security appliances affected by SQL injection and privilege escalation issues
- **VMware Platforms**: Enterprise virtualization products with remote code execution vulnerabilities
- **SAP Applications**: Business software with various security flaws requiring immediate patching
- **npm Package Registry**: Supply chain attacks targeting node-ipc and other popular packages
- **Microsoft 365**: Cloud services targeted by Tycoon2FA phishing campaigns
- **Avada Builder Plugin**: WordPress sites with over one million installations at risk

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Public release of Windows privilege escalation exploits enabling immediate system compromise
- **Supply Chain Attacks**: Injection of malicious code into trusted software packages and developer tools
- **Device-Code Phishing**: Advanced phishing techniques using Microsoft device authorization flows
- **Package Repository Poisoning**: Compromise of popular npm packages to distribute credential-stealing malware
- **JavaScript Injection**: Malicious code insertion into e-commerce checkout processes for payment card theft
- **Token-Based Attacks**: GitHub token compromise enabling codebase theft and extortion attempts
- **Peer-to-Peer Botnets**: Evolution of traditional backdoors into distributed P2P command networks

## Threat Actor Activities

- **Chaotic Eclipse**: Security researcher responsible for discovering and releasing Windows zero-day exploits including MiniPlasma, YellowKey, and GreenPlasma
- **Secret Blizzard (Turla)**: Russian state-sponsored group transforming Kazuar backdoor into modular P2P botnet for persistent access
- **Supply Chain Attackers**: Multiple campaigns targeting developer workstations and trusted software distribution channels
- **Tycoon2FA Operators**: Cybercriminal group operating advanced phishing-as-a-service platform targeting Microsoft 365 accounts
- **npm Package Attackers**: Threat actors compromising popular JavaScript packages including node-ipc for credential theft
- **WooCommerce Skimmers**: Cybercriminals exploiting WordPress plugin vulnerabilities for payment card data theft
- **ShinyHunters**: Ransomware group involved in attacks against educational technology platforms including Instructure Canvas