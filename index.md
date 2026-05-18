# Exploitation Report

Current cybersecurity landscape reveals intense exploitation activity across multiple platforms, with particular focus on zero-day vulnerabilities, supply chain attacks, and infrastructure targeting. Critical exploitation includes a Windows privilege escalation zero-day dubbed "MiniPlasma" that enables SYSTEM access on fully patched systems, active exploitation of NGINX vulnerabilities causing worker crashes and potential RCE, and widespread npm supply chain attacks leveraging the leaked Shai-Hulud malware. WordPress plugin vulnerabilities are under active exploitation for credit card skimming, while Russian state-sponsored groups have evolved their infrastructure for persistent access. The exploitation landscape is further complicated by newly disclosed vulnerabilities in major enterprise software from Ivanti, Fortinet, SAP, and VMware.

## Active Exploitation Details

### NGINX Vulnerability
- **Description**: Security flaw impacting NGINX Plus and NGINX Open that causes worker process crashes and enables potential remote code execution
- **Impact**: Attackers can crash NGINX worker processes and potentially achieve remote code execution on affected systems
- **Status**: Under active exploitation in the wild, recently disclosed and patched
- **CVE ID**: CVE-2026-42945

### MiniPlasma Windows Zero-Day
- **Description**: Windows privilege escalation vulnerability that allows attackers to gain SYSTEM privileges on fully patched Windows systems
- **Impact**: Complete system compromise with highest level privileges, enabling full control over affected Windows machines
- **Status**: Zero-day with proof-of-concept exploit publicly released, no patch currently available

### Funnel Builder WordPress Plugin Vulnerability
- **Description**: Critical vulnerability in the Funnel Builder plugin for WordPress enabling malicious JavaScript injection
- **Impact**: Credit card data theft through WooCommerce checkout page compromise and skimming attacks
- **Status**: Under active exploitation for payment card skimming attacks

### DirtyDecrypt Linux Privilege Escalation
- **Description**: Local privilege escalation vulnerability in the Linux kernel's rxgk module
- **Impact**: Allows attackers to gain root access on vulnerable Linux systems
- **Status**: Recently patched with proof-of-concept exploit now publicly available

### Avada Builder WordPress Plugin Flaws
- **Description**: Two vulnerabilities in the Avada Builder plugin affecting approximately one million WordPress installations
- **Impact**: Arbitrary file read capability and extraction of sensitive site credentials and information
- **Status**: Actively being exploited for credential theft

## Affected Systems and Products

- **NGINX Plus and NGINX Open**: Web server software vulnerable to worker crashes and RCE
- **Windows Systems**: All versions affected by MiniPlasma zero-day privilege escalation
- **WordPress Sites**: Installations using Funnel Builder and Avada Builder plugins
- **Linux Systems**: Kernels with rxgk module vulnerable to DirtyDecrypt exploit
- **npm Ecosystem**: Node.js packages and developers targeted by supply chain attacks
- **Enterprise Software**: Ivanti, Fortinet, SAP, VMware, and n8n products with newly patched vulnerabilities
- **Microsoft 365**: Accounts targeted by Tycoon2FA phishing campaigns
- **WooCommerce**: E-commerce platforms vulnerable to checkout page skimming

## Attack Vectors and Techniques

- **Supply Chain Attacks**: Malicious npm packages containing Shai-Hulud malware variants and infostealers
- **Zero-Day Exploitation**: Direct exploitation of unpatched vulnerabilities in Windows and NGINX
- **Plugin Compromise**: WordPress plugin vulnerabilities exploited for JavaScript injection and file access
- **Privilege Escalation**: Local exploitation techniques for gaining elevated system access
- **Phishing Campaigns**: Device-code phishing attacks targeting Microsoft 365 accounts
- **Token Theft**: GitHub access token compromise for source code exfiltration
- **JavaScript Injection**: Malicious code injection into e-commerce checkout processes
- **Botnet Operations**: P2P infrastructure for persistent access and data collection

## Threat Actor Activities

- **Secret Blizzard/Turla**: Russian state-sponsored group transforming Kazuar backdoor into modular P2P botnet for long-term persistence and stealth operations
- **TeamPCP**: Group responsible for open-sourcing Shai-Hulud malware, now being leveraged in npm supply chain attacks
- **Iranian Threat Actors**: Targeting fuel tank systems and expanding cyber offensive capabilities against infrastructure
- **Chaotic Eclipse**: Security researcher releasing Windows zero-day proof-of-concept exploits including MiniPlasma
- **npm Supply Chain Attackers**: Multiple threat actors deploying malicious packages containing infostealers and DDoS malware
- **WordPress Plugin Exploiters**: Attackers actively exploiting plugin vulnerabilities for credit card theft and credential harvesting
- **Tycoon2FA Operators**: Phishing kit operators targeting Microsoft 365 accounts with device-code attacks
- **Grafana Breach Actors**: Unauthorized parties stealing GitHub tokens and attempting extortion after source code theft