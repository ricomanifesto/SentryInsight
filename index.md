# Exploitation Report

Critical vulnerability exploitation activity is intensifying across multiple sectors, with threat actors actively targeting enterprise infrastructure and endpoint management systems. A single threat actor has been responsible for 83% of recent Ivanti Endpoint Manager Mobile attacks, while attackers are now exploiting a critical BeyondTrust remote code execution vulnerability with a CVSS score of 9.9. Microsoft Configuration Manager systems are also under active exploitation, prompting CISA to issue urgent patching orders to federal agencies. Nation-state actors from China, Iran, Russia, and North Korea are coordinating sophisticated campaigns against defense industrial base organizations, utilizing over two dozen zero-day vulnerabilities in edge devices. These exploitation campaigns demonstrate the escalating sophistication of threat actors and their focus on high-value enterprise targets.

## Active Exploitation Details

### Ivanti Endpoint Manager Mobile RCE Vulnerabilities
- **Description**: Two critical remote code execution vulnerabilities in Ivanti Endpoint Manager Mobile (EPMM) that allow attackers to gain unauthorized access to enterprise mobile device management systems
- **Impact**: Complete system compromise, unauthorized access to managed mobile devices, and potential lateral movement within enterprise networks
- **Status**: Actively exploited with a single threat actor responsible for 83% of exploitation attempts

### BeyondTrust Remote Support and Privileged Remote Access RCE Vulnerability
- **Description**: Critical pre-authentication remote code execution vulnerability affecting BeyondTrust Remote Support (RS) and Privileged Remote Access (PRA) appliances
- **Impact**: Complete system compromise without authentication, allowing attackers to execute arbitrary code on privileged access management systems
- **Status**: Actively exploited in attacks following public proof-of-concept release, CVSS score of 9.9

### Microsoft Configuration Manager (SCCM) Vulnerability
- **Description**: Critical vulnerability in Microsoft Configuration Manager that enables remote code execution
- **Impact**: System compromise of enterprise configuration management infrastructure
- **Status**: Actively exploited in attacks, CISA has ordered federal agencies to patch immediately

### Defense Industrial Base Zero-Day Vulnerabilities
- **Description**: At least two dozen zero-day vulnerabilities in edge devices specifically targeting defense contractors and related organizations
- **Impact**: Network infiltration, espionage operations, and compromise of sensitive defense-related information
- **Status**: Actively burned by nation-state actors from multiple countries in coordinated campaigns

## Affected Systems and Products

- **Ivanti Endpoint Manager Mobile**: Enterprise mobile device management systems
- **BeyondTrust Remote Support and Privileged Remote Access**: Privileged access management appliances
- **Microsoft Configuration Manager (SCCM)**: Enterprise system configuration and management infrastructure
- **Edge Devices in Defense Networks**: Network perimeter devices used by defense contractors and DIB organizations
- **Chrome Extensions**: Malicious extensions targeting Meta Business Suite and Facebook Business Manager data
- **macOS Systems**: Targeted by ClickFix campaigns delivering infostealer malware through Claude LLM artifacts and Google Ads

## Attack Vectors and Techniques

- **Remote Code Execution**: Pre-authentication attacks against enterprise management systems
- **Supply Chain Attacks**: Malicious Chrome extensions and fake developer recruitment campaigns
- **Social Engineering**: Physical mail campaigns targeting cryptocurrency wallet users and fake job recruitment for developers
- **ClickFix Campaigns**: Abuse of Claude LLM artifacts and Google Ads to deliver macOS infostealers
- **Bring Your Own Vulnerable Driver (BYOVD)**: Exploitation of security gaps to weaponize Windows drivers and terminate security processes
- **AI Recommendation Poisoning**: Manipulation of AI-powered summarization tools across multiple industries

## Threat Actor Activities

- **Single Ivanti Threat Actor**: Responsible for 83% of recent Ivanti EPMM exploitation attempts, demonstrating concentrated and systematic targeting
- **UAT-9921**: Previously unknown threat actor deploying VoidLink malware framework against technology and financial services sectors
- **CANFAIL Malware Operator**: Suspected Russian actor targeting Ukrainian organizations with previously undocumented malware
- **Nation-State Coordination**: Coordinated activities between Chinese, Iranian, Russian, and North Korean state-sponsored groups targeting defense industrial base
- **North Korean Developers**: Conducting fake recruitment campaigns targeting JavaScript and Python developers with cryptocurrency-related malicious tasks
- **Qilin Ransomware Gang**: Successfully compromised Romania's national oil pipeline operator Conpet S.A., confirming data theft