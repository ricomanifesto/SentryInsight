# Exploitation Report

Critical zero-day vulnerabilities are under active exploitation across multiple platforms, with attackers targeting Windows systems, web servers, and cloud environments. The most significant threats include a Windows privilege escalation zero-day dubbed MiniPlasma that grants SYSTEM access on fully patched systems, an NGINX vulnerability (CVE-2026-42945) causing worker crashes and potential remote code execution, and a WordPress plugin flaw enabling credit card theft from WooCommerce sites. Supply chain attacks continue to plague the npm ecosystem with malicious packages delivering infostealers, while Russian state-sponsored groups have evolved their persistent access capabilities through modular P2P botnets.

## Active Exploitation Details

### MiniPlasma Windows Zero-Day
- **Description**: A Windows privilege escalation zero-day vulnerability that enables attackers to gain SYSTEM privileges on fully patched Windows systems
- **Impact**: Complete system compromise with highest privilege level access, allowing attackers full control over affected Windows machines
- **Status**: Zero-day with proof-of-concept exploit publicly released by security researcher Chaotic Eclipse

### NGINX Worker Crash Vulnerability
- **Description**: A security flaw in NGINX Plus and NGINX Open causing worker process crashes with potential for remote code execution
- **Impact**: Service disruption through worker crashes and possible remote code execution on affected web servers
- **Status**: Under active exploitation in the wild, recently disclosed
- **CVE ID**: CVE-2026-42945

### Funnel Builder WordPress Plugin Flaw
- **Description**: A critical vulnerability in the Funnel Builder plugin for WordPress enabling injection of malicious JavaScript code
- **Impact**: Credit card skimming attacks on WooCommerce checkout pages, leading to financial data theft
- **Status**: Under active exploitation to steal customer payment information from e-commerce sites

### DirtyDecrypt Linux Privilege Escalation
- **Description**: A local privilege escalation vulnerability in the Linux kernel's rxgk module
- **Impact**: Allows attackers to gain root access on affected Linux systems
- **Status**: Recently patched with proof-of-concept exploit now available

## Affected Systems and Products

- **Windows Systems**: All fully patched Windows versions vulnerable to MiniPlasma zero-day privilege escalation
- **NGINX Plus and NGINX Open**: Web servers experiencing worker crashes and potential RCE exploitation
- **WordPress Sites**: Sites using Funnel Builder plugin vulnerable to JavaScript injection and payment skimming
- **Linux Systems**: Distributions with vulnerable rxgk module affected by DirtyDecrypt privilege escalation
- **npm Ecosystem**: Four malicious packages identified delivering infostealers and DDoS malware
- **Microsoft 365**: Accounts targeted by Tycoon2FA phishing kit using device-code attacks
- **Grafana Labs**: Source code stolen through compromised GitHub token access
- **node-ipc Package**: Popular npm package compromised to steal developer credentials

## Attack Vectors and Techniques

- **Privilege Escalation**: MiniPlasma zero-day exploiting Windows kernel for SYSTEM access
- **Web Server Exploitation**: NGINX vulnerability causing denial of service and potential code execution
- **JavaScript Injection**: Malicious code inserted into WooCommerce checkout processes for payment theft
- **Supply Chain Attacks**: Compromised npm packages including Shai-Hulud worm variants targeting developers
- **Device-Code Phishing**: Tycoon2FA kit abusing Microsoft device authentication flow and Trustifi URLs
- **Token Theft**: GitHub access tokens compromised to steal source code repositories
- **Session Hijacking**: REMUS infostealer focusing on browser session and authentication token theft

## Threat Actor Activities

- **Secret Blizzard (Turla)**: Russian state-sponsored group evolved Kazuar backdoor into modular P2P botnet for persistent access and stealth operations
- **TeamPCP**: Released Shai-Hulud worm variants through malicious npm packages targeting developer environments
- **Unknown Actors**: Exploiting WordPress plugin vulnerabilities for financial fraud through payment skimming
- **Grafana Attackers**: Attempted extortion after stealing source code through compromised GitHub access
- **npm Supply Chain Attackers**: Targeting developer workstations through poisoned packages to compromise software supply chain