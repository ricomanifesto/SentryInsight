# Exploitation Report

The current threat landscape shows intense exploitation activity targeting critical infrastructure and enterprise systems. A single threat actor is responsible for 83% of recent attacks against Ivanti Endpoint Manager Mobile vulnerabilities, while attackers have also begun exploiting a critical BeyondTrust remote code execution flaw with a CVSS score of 9.9. Additionally, CISA has flagged a Microsoft Configuration Manager vulnerability as actively exploited, requiring immediate patching by federal agencies. Nation-state actors from China, Iran, Russia, and North Korea are conducting coordinated operations against defense industrial base organizations, burning through dozens of zero-day vulnerabilities in edge devices to infiltrate contractor networks.

## Active Exploitation Details

### Ivanti Endpoint Manager Mobile (EPMM) Vulnerabilities
- **Description**: Two critical vulnerabilities in Ivanti EPMM are being actively exploited by threat actors
- **Impact**: Remote code execution allowing attackers to compromise endpoint management systems
- **Status**: Active exploitation ongoing with a single actor responsible for 83% of recent attacks

### BeyondTrust Remote Code Execution Vulnerability
- **Description**: Critical pre-authentication remote code execution flaw in BeyondTrust Remote Support and Privileged Remote Access appliances
- **Impact**: Complete system compromise without authentication required
- **Status**: Now being exploited in the wild after proof-of-concept publication

### Microsoft Configuration Manager Vulnerability
- **Description**: Critical vulnerability in Microsoft SCCM (System Center Configuration Manager)
- **Impact**: Remote code execution in enterprise configuration management systems
- **Status**: CISA has added to Known Exploited Vulnerabilities catalog, federal agencies ordered to patch

### Defense Industrial Base Zero-Days
- **Description**: At least two dozen zero-day vulnerabilities in edge devices targeting defense contractors
- **Impact**: Network infiltration and espionage operations
- **Status**: Active exploitation by nation-state actors from multiple countries

## Affected Systems and Products

- **Ivanti Endpoint Manager Mobile**: Critical vulnerabilities affecting mobile device management platforms
- **BeyondTrust Remote Support and PRA**: Remote access and privileged access management appliances vulnerable to pre-auth RCE
- **Microsoft Configuration Manager**: Enterprise system configuration and management platforms
- **Defense Contractor Edge Devices**: Various network edge equipment used by defense industrial base organizations
- **Meta Business Suite/Facebook Business Manager**: Targeted by malicious Chrome extensions for data theft
- **macOS Systems**: Targeted by infostealer malware via ClickFix campaigns using Claude LLM artifacts

## Attack Vectors and Techniques

- **Remote Code Execution**: Exploitation of critical RCE vulnerabilities in enterprise management systems
- **Pre-Authentication Attacks**: BeyondTrust vulnerability allows compromise without credentials
- **Social Engineering via Physical Mail**: Cryptocurrency wallet users targeted with fake letters from Trezor and Ledger
- **Malicious Browser Extensions**: Chrome extensions stealing business data and browsing history
- **Fake Recruitment Campaigns**: North Korean actors targeting developers with malicious coding challenges
- **ClickFix Campaigns**: Abuse of Claude LLM artifacts and Google Ads to distribute macOS infostealers
- **BYOVD (Bring Your Own Vulnerable Driver)**: Weaponizing Windows drivers to terminate security processes

## Threat Actor Activities

- **Dominant Ivanti Attacker**: Single actor responsible for 83% of recent EPMM exploitation attempts
- **North Korean Threat Actors**: Conducting fake recruitment campaigns targeting JavaScript and Python developers with cryptocurrency-themed malicious tasks
- **China, Iran, Russia, North Korea**: Coordinated nation-state operations against defense industrial base sector
- **UAT-9921**: Previously unknown threat actor deploying VoidLink malware framework against technology and financial sectors
- **Suspected Russian Actor**: Google attributes CANFAIL malware attacks against Ukrainian organizations
- **Qilin Ransomware Gang**: Confirmed data theft from Romania's national oil pipeline operator Conpet S.A.
- **Various Cybercriminals**: Targeting luxury brand customers (Louis Vuitton, Dior, Tiffany) and telecommunications users (6.2 million Odido customers affected)