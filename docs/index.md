# Exploitation Report

Critical zero-day vulnerabilities are currently under active exploitation across multiple platforms, with Apple addressing an exploited zero-day used in "extremely sophisticated attacks" targeting specific individuals. Meanwhile, CISA has flagged a Microsoft Configuration Manager vulnerability as being exploited in the wild, and security researchers have confirmed active exploitation of a critical BeyondTrust remote code execution flaw with a CVSS score of 9.9. Additionally, Ivanti EPMM zero-day vulnerabilities are experiencing an "exploit frenzy" with 83% of exploitation attempts traced to bulletproof hosting infrastructure. The threat landscape is further complicated by state-backed actors leveraging AI tools for reconnaissance and attack support, while malicious browser extensions and supply chain attacks continue to target enterprise environments.

## Active Exploitation Details

### Apple Zero-Day Vulnerability
- **Description**: A zero-day flaw affecting iOS, iPadOS, macOS Tahoe, tvOS, watchOS, and visionOS systems
- **Impact**: Being exploited in extremely sophisticated cyber attacks targeting specific individuals
- **Status**: Patched by Apple in recent security updates across all affected platforms

### Microsoft Configuration Manager (SCCM) Vulnerability
- **Description**: Critical vulnerability in Microsoft Configuration Manager that was patched in October 2024
- **Impact**: Remote code execution capabilities allowing attackers to compromise enterprise systems
- **Status**: Now being exploited in attacks according to CISA, which has ordered federal agencies to secure their systems

### BeyondTrust Remote Support Critical Flaw
- **Description**: Critical pre-authentication remote code execution vulnerability affecting BeyondTrust Remote Support (RS) and Privileged Remote Access (PRA) appliances
- **Impact**: Allows attackers to achieve remote code execution without authentication
- **Status**: Currently being exploited in the wild after proof-of-concept code was published online, CVSS score of 9.9

### Ivanti EPMM Zero-Day Vulnerabilities
- **Description**: Multiple zero-day vulnerabilities affecting Ivanti Endpoint Manager Mobile (EPMM)
- **Impact**: Enabling attackers to compromise mobile device management systems
- **Status**: Under active exploitation with concentrated attack activity from bulletproof hosting infrastructure

### Windows 11 Notepad Vulnerability
- **Description**: Remote code execution vulnerability in Windows 11 Notepad allowing execution via specially crafted Markdown links
- **Impact**: Attackers can execute local or remote programs by tricking users into clicking malicious Markdown links
- **Status**: Recently patched by Microsoft

## Affected Systems and Products

- **Apple Devices**: iOS, iPadOS, macOS Tahoe, tvOS, watchOS, and visionOS systems
- **Microsoft Configuration Manager**: Enterprise configuration management systems patched in October 2024
- **BeyondTrust Products**: Remote Support (RS) and Privileged Remote Access (PRA) appliances
- **Ivanti EPMM**: Endpoint Manager Mobile systems in enterprise environments
- **Windows 11 Notepad**: Systems running Windows 11 with Notepad application
- **WordPress Sites**: Over 900,000 websites using WPvivid Backup & Migration plugin vulnerable to critical RCE
- **Chrome Browser**: Extensions marketplace with malicious AI-themed extensions affecting over 300,000 users
- **npm and PyPI**: Package repositories targeted with malicious packages in supply chain attacks

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Sophisticated attacks targeting high-value individuals using previously unknown vulnerabilities
- **Pre-Authentication RCE**: BeyondTrust vulnerability allows remote code execution without requiring authentication
- **Social Engineering via AI Apps**: AMOS infostealer targeting macOS users through popular AI applications
- **Malicious Browser Extensions**: Chrome extensions masquerading as AI assistants to steal credentials and business data
- **Supply Chain Attacks**: Lazarus group planting malicious packages in npm and PyPI ecosystems using fake recruitment themes
- **Markdown Link Exploitation**: Windows 11 Notepad vulnerability exploited through specially crafted Markdown links
- **Bulletproof Hosting**: 83% of Ivanti EPMM exploitation attempts originating from a single IP on bulletproof hosting infrastructure

## Threat Actor Activities

- **North Korea-linked UNC2970**: Using Google's Gemini AI for reconnaissance on targets and attack support activities
- **Lazarus Group**: Orchestrating fake recruitment campaigns to plant malicious packages in npm and PyPI repositories
- **Qilin Ransomware Gang**: Confirmed data theft from Romania's national oil pipeline operator Conpet S.A.
- **Green Blood Group**: Breached Senegalese national biometric database exposing personal records of nearly 20 million residents
- **State-Backed Hackers**: Multiple groups leveraging AI tools across all attack stages for enhanced operational capabilities
- **Cybercriminal Groups**: Deploying AMOS infostealer through AI app marketplaces and using malicious Chrome extensions for credential harvesting