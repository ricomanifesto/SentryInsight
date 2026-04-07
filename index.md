# Exploitation Report

Current threat landscape shows intense exploitation activity targeting critical infrastructure and enterprise systems. Multiple zero-day vulnerabilities are being actively exploited, including a Windows privilege escalation flaw leaked by a disgruntled researcher and a critical Fortinet FortiClient EMS authentication bypass vulnerability. Threat actors are leveraging sophisticated techniques including GPU-based Rowhammer attacks, vulnerable driver exploitation to disable security tools, and large-scale automated campaigns targeting web applications. Notable ransomware operations continue their activities with REvil and GangCrab leaders identified by German authorities, while nation-state actors conduct supply chain attacks through GitHub and orchestrate complex social engineering operations resulting in massive cryptocurrency thefts.

## Active Exploitation Details

### FortiClient EMS Authentication Bypass Vulnerability
- **Description**: Critical authentication bypass flaw in FortiClient Enterprise Management Server allowing unauthorized access
- **Impact**: Complete system compromise and potential lateral movement within enterprise networks
- **Status**: Actively exploited in the wild; emergency patch released by Fortinet
- **CVE ID**: CVE-2026-35616

### Windows Privilege Escalation Zero-Day (BlueHammer)
- **Description**: Unpatched Windows privilege escalation vulnerability allowing attackers to gain SYSTEM or elevated administrator permissions
- **Impact**: Complete system takeover from low-privileged user accounts
- **Status**: Exploit code publicly leaked; no patch available from Microsoft

### React2Shell Vulnerability in Next.js Applications
- **Description**: Critical vulnerability in Next.js applications enabling server-side code execution
- **Impact**: Complete application compromise and credential theft
- **Status**: Actively exploited in automated credential harvesting campaigns
- **CVE ID**: CVE-2025-55182

### GPU Rowhammer Attack (GPUBreach)
- **Description**: Novel attack technique targeting GPU GDDR6 memories to induce bit-flips for privilege escalation
- **Impact**: Full system compromise through hardware-level memory corruption
- **Status**: Proof-of-concept attack demonstrated; affects modern GPU systems

## Affected Systems and Products

- **Fortinet FortiClient EMS**: Enterprise Management Server instances across federal agencies and organizations
- **Windows Systems**: All Windows versions vulnerable to BlueHammer privilege escalation
- **Next.js Applications**: Web applications exposed to internet vulnerable to React2Shell exploitation
- **Modern GPU Systems**: Systems with GDDR6 GPU memory susceptible to GPUBreach attacks
- **npm Registry Packages**: 36 malicious packages targeting Strapi CMS plugins affecting Redis and PostgreSQL databases
- **Microsoft 365 Environments**: 300+ Israeli organizations targeted by Iran-linked password spraying campaigns
- **GitHub Repositories**: Supply chain attacks targeting developers through AI-assisted malicious package distribution

## Attack Vectors and Techniques

- **Authentication Bypass**: Direct exploitation of FortiClient EMS authentication mechanisms
- **Privilege Escalation**: Windows kernel exploitation for elevated permissions
- **Server-Side Code Execution**: Remote code execution through Next.js application vulnerabilities
- **Hardware-Level Attacks**: GPU memory corruption via Rowhammer techniques
- **Supply Chain Poisoning**: Malicious npm packages disguised as legitimate plugins
- **Bring Your Own Vulnerable Driver (BYOVD)**: Using legitimate but vulnerable drivers to disable 300+ EDR security tools
- **Password Spraying**: Large-scale credential attacks against cloud environments
- **Social Engineering**: Six-month operations targeting cryptocurrency platforms
- **AI-Assisted Targeting**: Automated identification and exploitation of GitHub misconfigurations

## Threat Actor Activities

- **Storm-1175 (China-based)**: Medusa ransomware affiliate deploying zero-day and n-day exploits in high-velocity attacks
- **Iran-Nexus Actors**: Conducting password-spraying campaigns against 300+ Israeli Microsoft 365 organizations amid regional conflicts
- **DPRK-Linked Groups**: Using GitHub as command-and-control infrastructure for multi-stage attacks targeting South Korean organizations
- **UAT-10608**: Emerging threat cluster exploiting React2Shell vulnerabilities for automated credential harvesting
- **REvil/GangCrab Leaders**: German authorities identified Russian nationals Daniil Maksimov ("UNKN") and associates responsible for 130 ransomware attacks in Germany
- **Qilin and Warlock Ransomware**: Utilizing vulnerable drivers to disable security tools across compromised environments
- **DPRK Social Engineering Teams**: Orchestrating six-month operation resulting in $285 million Drift Protocol cryptocurrency theft