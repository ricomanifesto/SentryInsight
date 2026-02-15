# Exploitation Report

Critical exploitation activity is currently centered around several high-impact vulnerabilities across enterprise infrastructure and security solutions. The most severe threats include active exploitation of Ivanti Endpoint Manager Mobile vulnerabilities, with a single threat actor responsible for 83% of recent attacks, and newly discovered exploitation of a critical BeyondTrust Remote Support vulnerability with a CVSS score of 9.9. Additionally, CISA has flagged active exploitation of a Microsoft Configuration Manager vulnerability that was patched in October 2024, indicating ongoing threats against enterprise management systems. Nation-state actors from China, Iran, Russia, and North Korea have significantly escalated attacks against defense industrial base organizations, burning at least two dozen zero-day vulnerabilities in edge devices to infiltrate contractor networks.

## Active Exploitation Details

### Ivanti Endpoint Manager Mobile Vulnerabilities
- **Description**: Two critical remote code execution vulnerabilities in Ivanti EPMM that allow attackers to execute arbitrary code without authentication
- **Impact**: Complete system compromise and unauthorized access to endpoint management infrastructure
- **Status**: Actively exploited with one threat actor responsible for 83% of recent attacks

### BeyondTrust Remote Support and Privileged Remote Access Vulnerability
- **Description**: Critical pre-authentication remote code execution vulnerability in BeyondTrust RS and PRA appliances with CVSS score of 9.9
- **Impact**: Full system compromise without requiring authentication credentials
- **Status**: Actively exploited in attacks following public PoC release

### Microsoft Configuration Manager Vulnerability
- **Description**: Critical vulnerability in Microsoft SCCM that enables remote code execution
- **Impact**: Complete compromise of configuration management infrastructure
- **Status**: Actively exploited in attacks, patched in October 2024, CISA mandated federal agency remediation

### Defense Sector Zero-Day Vulnerabilities
- **Description**: At least two dozen zero-day vulnerabilities in edge devices targeting defense contractors
- **Impact**: Network infiltration and espionage operations against defense industrial base
- **Status**: Actively exploited by nation-state actors from multiple countries

## Affected Systems and Products

- **Ivanti Endpoint Manager Mobile**: Enterprise mobile device management platforms vulnerable to RCE attacks
- **BeyondTrust Remote Support and Privileged Remote Access**: Remote access management appliances with critical pre-authentication RCE
- **Microsoft Configuration Manager (SCCM)**: Enterprise configuration management systems across federal agencies
- **Defense Contractor Edge Devices**: Network edge infrastructure at defense industrial base organizations
- **Google Chrome Extensions**: Malicious extensions targeting Meta Business Suite and Facebook Business Manager data
- **macOS Systems**: Targeted by ClickFix campaigns using Claude LLM artifacts and Google Ads for infostealer delivery

## Attack Vectors and Techniques

- **Remote Code Execution**: Pre-authentication attacks against enterprise management platforms
- **Social Engineering**: Physical letters targeting cryptocurrency wallet users and fake recruiter campaigns against developers
- **Supply Chain Attacks**: Malicious Chrome extensions and compromised development tools
- **ClickFix Campaigns**: Abuse of AI platforms and search advertising to deliver malware payloads
- **BYOVD Attacks**: Bring Your Own Vulnerable Driver techniques to weaponize Windows drivers and terminate security processes
- **Zero-Day Exploitation**: Systematic burning of previously unknown vulnerabilities in edge devices

## Threat Actor Activities

- **Unknown Ivanti Attacker**: Responsible for 83% of recent Ivanti EPMM exploitation campaigns targeting enterprise mobile management
- **North Korean Groups**: Conducting fake recruiter campaigns targeting JavaScript and Python developers with cryptocurrency-themed malware
- **UAT-9921**: Previously unknown actor deploying VoidLink malware framework against technology and financial sectors
- **Russian Suspected Actor**: Attributed to CANFAIL malware attacks specifically targeting Ukrainian organizations
- **Multi-Nation State Coalition**: China, Iran, Russia, and North Korea conducting coordinated operations against defense industrial base with systematic zero-day exploitation
- **ClickFix Operators**: Abusing Claude AI artifacts and Google advertising infrastructure to distribute macOS infostealers
- **Ransomware Groups**: Qilin ransomware gang confirmed data theft from Romania's national oil pipeline operator Conpet S.A.