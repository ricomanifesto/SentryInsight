# Exploitation Report

Critical exploitation activity is currently targeting multiple platforms, with several zero-day vulnerabilities and recently disclosed flaws being actively exploited in the wild. The most concerning activities include the exploitation of CVE-2026-42945 in NGINX systems causing worker crashes and potential remote code execution, active exploitation of a critical Funnel Builder WordPress plugin vulnerability enabling credit card theft through WooCommerce checkout skimming, and the release of a Windows privilege escalation zero-day dubbed "MiniPlasma" that provides SYSTEM access on fully patched systems. Additionally, the leak of Shai-Hulud malware source code has spawned multiple npm package poisoning campaigns, while threat actors are leveraging stolen GitHub tokens to compromise development environments and supply chains.

## Active Exploitation Details

### NGINX Worker Crash and RCE Vulnerability
- **Description**: A newly disclosed security flaw affecting NGINX Plus and NGINX Open Source that causes worker process crashes and enables potential remote code execution
- **Impact**: Attackers can crash NGINX worker processes and potentially achieve remote code execution on affected systems
- **Status**: Under active exploitation in the wild within days of public disclosure
- **CVE ID**: CVE-2026-42945

### Funnel Builder WordPress Plugin Vulnerability
- **Description**: Critical security vulnerability in the Funnel Builder plugin for WordPress enabling injection of malicious JavaScript code
- **Impact**: Attackers can inject malicious scripts into WooCommerce checkout pages to steal credit card information and customer data
- **Status**: Under active exploitation for checkout page skimming attacks

### MiniPlasma Windows Zero-Day
- **Description**: Windows privilege escalation zero-day vulnerability that enables SYSTEM-level access on fully patched Windows systems
- **Impact**: Local attackers can escalate privileges to gain complete administrative control over Windows systems
- **Status**: Proof-of-concept exploit publicly released by security researcher Chaotic Eclipse

### DirtyDecrypt Linux Privilege Escalation
- **Description**: Local privilege escalation vulnerability in the Linux kernel's rxgk module
- **Impact**: Attackers with local access can escalate privileges to gain root access on affected Linux systems
- **Status**: Recently patched with proof-of-concept exploit now available

### Shai-Hulud Malware Campaign
- **Description**: Self-replicating worm malware targeting npm packages after source code was publicly released
- **Impact**: Infects npm packages with information-stealing capabilities and spreads across development environments
- **Status**: Multiple malicious npm packages identified containing Shai-Hulud clones and variations

## Affected Systems and Products

- **NGINX Plus and NGINX Open Source**: Web server and reverse proxy systems vulnerable to worker crashes and RCE
- **WordPress Sites**: Websites using the Funnel Builder plugin, particularly those with WooCommerce integration
- **Windows Systems**: All Windows versions including fully patched systems vulnerable to MiniPlasma privilege escalation
- **Linux Systems**: Systems running vulnerable versions of the Linux kernel with rxgk module
- **npm Package Repository**: Node.js development environments and applications using compromised packages
- **GitHub Repositories**: Development environments with exposed tokens, including CISA AWS GovCloud and Grafana codebases
- **Automatic Tank Gauge (ATG) Systems**: Fuel tank monitoring systems exposed to internet-based tampering

## Attack Vectors and Techniques

- **Web Application Exploitation**: Injection of malicious JavaScript into WordPress checkout pages via plugin vulnerabilities
- **Supply Chain Attacks**: Poisoning of npm packages with information-stealing malware and self-replicating worms
- **Privilege Escalation**: Local exploitation of kernel vulnerabilities to gain elevated system access
- **Token Theft and Abuse**: Compromise of GitHub access tokens to steal source code and credentials
- **Device-Code Phishing**: Tycoon2FA kit leveraging device authentication flows to bypass multi-factor authentication
- **Infrastructure Targeting**: Exploitation of exposed industrial control systems and fuel tank gauges

## Threat Actor Activities

- **Secret Blizzard (Russian APT)**: Evolved Kazuar backdoor into modular peer-to-peer botnet for long-term persistence and data collection
- **Iranian Threat Actors**: Expanded cyber offensive operations targeting fuel tank infrastructure systems
- **TeamPCP**: Released Shai-Hulud worm source code leading to widespread npm ecosystem compromise
- **INTERPOL Operation Ramz**: Law enforcement disruption resulted in 201 arrests across Middle East and North Africa cybercrime networks
- **ShinyHunters**: Conducted attacks against Instructure Canvas platform prompting Congressional oversight
- **Unknown Supply Chain Attackers**: Multiple campaigns targeting developer workstations and trusted software repositories