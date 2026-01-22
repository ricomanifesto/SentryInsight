# Exploitation Report

Critical exploitation activity is currently focused on several zero-day vulnerabilities and newly patched systems that are being actively targeted within days of patch releases. The most severe incidents include a Cisco zero-day vulnerability being exploited in remote code execution attacks across Unified Communications platforms, automated attacks targeting Fortinet FortiGate devices through authentication bypasses, and a SmarterMail authentication bypass being exploited just two days after patches were released. Additionally, threat actors are leveraging trusted development tools like VS Code tunnels and exploiting misconfigured security training applications to breach Fortune 500 companies and cloud environments.

## Active Exploitation Details

### Cisco Unified Communications Remote Code Execution Zero-Day
- **Description**: Critical security vulnerability in Cisco Unified Communications (CM) products and Webex Calling Dedicated Instance allowing remote code execution
- **Impact**: Attackers can execute arbitrary code remotely on affected systems
- **Status**: Zero-day actively exploited in attacks; patches have been released
- **CVE ID**: CVE-2026-20045

### SmarterMail Authentication Bypass
- **Description**: Authentication bypass vulnerability in SmarterTools SmarterMail email software
- **Impact**: Attackers can bypass authentication mechanisms to gain unauthorized access
- **Status**: Actively exploited in the wild within two days of patch release

### FortiGate Authentication Bypass with Patch Bypass
- **Description**: Critical authentication vulnerability in Fortinet FortiGate devices with a newly discovered patch bypass method
- **Impact**: Unauthorized access to firewall systems, configuration theft, and creation of rogue administrative accounts
- **Status**: Actively exploited against patched systems using bypass technique
- **CVE ID**: CVE-2025-59718

### Pwn2Own Automotive Zero-Days
- **Description**: 29 zero-day vulnerabilities discovered and exploited during Pwn2Own Automotive 2026 competition
- **Impact**: Various impacts across automotive systems and components
- **Status**: Newly discovered vulnerabilities demonstrated at security competition

## Affected Systems and Products

- **Cisco Unified Communications Manager**: Multiple versions affected by remote code execution vulnerability
- **Cisco Webex Calling Dedicated Instance**: Critical RCE vulnerability requiring immediate patching
- **Fortinet FortiGate Devices**: Firewall systems vulnerable to authentication bypass and configuration theft
- **SmarterTools SmarterMail**: Email software affected by authentication bypass vulnerability
- **Chainlit AI Framework**: Open-source conversational AI framework with file reading vulnerabilities
- **GitLab Community and Enterprise Editions**: Development platforms with 2FA bypass vulnerabilities
- **Zoom Products**: Various Zoom applications affected by RCE and DoS vulnerabilities
- **Security Training Applications**: DVWA, OWASP Juice Shop, Hackazon, and bWAPP used in attacks against cloud environments

## Attack Vectors and Techniques

- **VS Code Tunnel Abuse**: North Korean threat actors using Microsoft VS Code tunnels to establish persistent remote access through trusted infrastructure
- **FortiCloud SSO Exploitation**: Automated attacks leveraging single sign-on mechanisms to alter firewall configurations
- **Spear-Phishing with Fake Job Interviews**: "Contagious Interview" campaigns targeting developers through malicious repositories and fake recruitment processes
- **Zendesk System Abuse**: Hijacking unsecured Zendesk support systems for massive global spam distribution
- **PyPI Package Impersonation**: Malicious packages mimicking legitimate libraries like SymPy to deploy cryptocurrency miners
- **AI-Enhanced Click Fraud**: Android malware using TensorFlow machine learning models for automated ad interaction
- **Security Training App Exploitation**: Leveraging misconfigured penetration testing applications for cloud environment access

## Threat Actor Activities

- **North Korean DPRK Actors**: Conducting extensive "Contagious Interview" campaigns through fake job opportunities, targeting 3,136 IP addresses across 20 organizations in artificial intelligence and technology sectors
- **PurpleBravo Campaign**: Large-scale North Korean operation using fake recruitment processes to deploy backdoors via VS Code tunnels
- **Automated Attack Groups**: Conducting systematic attacks against Fortinet devices using FortiCloud SSO exploitation techniques
- **Cryptocurrency Mining Operations**: Deploying XMRig miners through malicious PyPI packages targeting Linux environments
- **AI-Generated Malware Development**: Advanced threat actors using AI agents to create sophisticated malware frameworks like VoidLink for Linux systems