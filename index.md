# Exploitation Report

Critical exploitation activity continues to surge across multiple attack vectors, with threat actors deploying sophisticated zero-day exploits and leveraging artificial intelligence to accelerate their campaigns. Most notably, China-linked Storm-1175 has been rapidly deploying Medusa ransomware through zero-day vulnerabilities, while a maximum-severity remote code execution flaw in Flowise AI platforms is under active exploitation with over 12,000 instances exposed. Additional zero-day exploits have emerged targeting Fortinet FortiClient and Windows privilege escalation, alongside supply chain attacks leveraging AI assistance and automated credential harvesting campaigns exploiting React applications.

## Active Exploitation Details

### Flowise AI Platform Remote Code Execution
- **Description**: Maximum-severity security flaw in Flowise, an open-source artificial intelligence platform
- **Impact**: Full remote code execution capabilities allowing complete system compromise
- **Status**: Under active exploitation with 12,000+ exposed instances worldwide
- **CVE ID**: CVSS 10.0 rated vulnerability

### Fortinet FortiClient Authentication Bypass
- **Description**: Authentication bypass vulnerability in FortiClient Enterprise Management Server
- **Impact**: Allows attackers to bypass authentication controls and gain unauthorized access
- **Status**: Zero-day vulnerability actively exploited in the wild; emergency patch issued
- **CVE ID**: CVE-2026-35616

### Windows BlueHammer Privilege Escalation
- **Description**: Unpatched Windows privilege escalation flaw with publicly released exploit code
- **Impact**: Enables attackers to gain SYSTEM or elevated administrator permissions
- **Status**: Zero-day with public exploit code available; reported privately to Microsoft but not yet patched

### React2Shell Application Vulnerability
- **Description**: Security flaw in Next.js applications enabling automated credential harvesting
- **Impact**: Allows automated extraction of credentials, secrets, and system data from web-exposed applications
- **Status**: Actively exploited by UAT-10608 threat cluster using automated tools

### GPU RowHammer Attack (GPUBreach)
- **Description**: Novel attack technique targeting high-performance GPU GDDR6 memory through bit-flips
- **Impact**: Enables full system compromise and privilege escalation via GPU memory manipulation
- **Status**: Academic research demonstrating practical exploitation methods

## Affected Systems and Products

- **Flowise AI Platform**: Open-source AI agent building platform with 12,000+ exposed instances
- **Fortinet FortiClient EMS**: Enterprise management server systems requiring immediate patching
- **Microsoft Windows**: Multiple versions affected by BlueHammer privilege escalation exploit
- **Next.js Applications**: Web applications vulnerable to React2Shell automated harvesting
- **High-Performance GPUs**: Systems with GDDR6 memory susceptible to GPUBreach attacks
- **Microsoft 365 Organizations**: 300+ Israeli organizations targeted in password spraying campaigns
- **GitHub Repositories**: Supply chain targets for AI-assisted malicious package distribution

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Rapid deployment of unpatched vulnerabilities for initial access
- **AI-Assisted Attacks**: Automated targeting and exploitation using artificial intelligence tools
- **Supply Chain Compromise**: Targeting GitHub repositories and NPM packages for widespread distribution
- **Password Spraying**: Large-scale credential attacks against Microsoft 365 environments
- **RowHammer Attacks**: Hardware-level exploitation through GPU memory bit manipulation
- **BYOVD Technique**: Bring Your Own Vulnerable Driver attacks to disable security tools
- **QR Code Phishing**: Social engineering campaigns using QR codes in fake traffic violation notices

## Threat Actor Activities

- **Storm-1175 (China-linked)**: Deploying Medusa ransomware through high-velocity zero-day and N-day exploitation campaigns
- **UAT-10608**: Automated credential harvesting operations targeting React applications with specialized tooling
- **Iran-nexus Groups**: Password spraying campaigns against 300+ Israeli Microsoft 365 organizations amid Middle East conflicts
- **DPRK-linked Actors**: Multi-stage attacks using GitHub as command-and-control infrastructure targeting South Korean organizations
- **Qilin Ransomware**: Using vulnerable drivers to disable 300+ EDR security tools before encryption
- **Warlock Ransomware**: Employing BYOVD techniques for security tool evasion and system compromise
- **REvil/GandCrab Leaders**: German authorities identified Russian nationals behind major ransomware operations affecting 130 German organizations