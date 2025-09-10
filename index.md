# Exploitation Report

Several critical vulnerabilities are currently under active exploitation or have recently been patched following observed attacks. The most significant threats include a critical Adobe Commerce flaw enabling customer account takeover, multiple SAP NetWeaver vulnerabilities with maximum CVSS scores that allow code execution, and two zero-day vulnerabilities in Microsoft's September 2025 Patch Tuesday release. Additionally, threat actors are actively targeting exposed Docker APIs and conducting sophisticated supply chain attacks through compromised NPM packages affecting billions of weekly downloads.

## Active Exploitation Details

### Adobe Commerce Customer Account Takeover Vulnerability
- **Description**: A critical security flaw in Adobe Commerce and Magento Open Source platforms that allows attackers to take control of customer accounts
- **Impact**: Complete customer account compromise, potential access to personal and financial information
- **Status**: Actively exploitable, Adobe has issued warnings
- **CVE ID**: CVE-2025-54236

### SAP NetWeaver Critical Code Execution Flaws
- **Description**: Three critical vulnerabilities in SAP NetWeaver that could result in remote code execution and arbitrary file upload capabilities
- **Impact**: Complete system compromise, unauthorized code execution, and file system access
- **Status**: Security updates released by SAP
- **CVSS Score**: Up to 10.0 (maximum severity)

### Microsoft Zero-Day Vulnerabilities
- **Description**: Two publicly disclosed zero-day vulnerabilities included in Microsoft's September 2025 Patch Tuesday
- **Impact**: Various security implications depending on specific vulnerabilities
- **Status**: Patches available as of September 2025 Patch Tuesday

### SAP S/4HANA Previously Exploited Flaws
- **Description**: Multiple security flaws in SAP S/4HANA that were previously exploited in the wild
- **Impact**: System compromise and unauthorized access
- **Status**: Security patches now available

## Affected Systems and Products

- **Adobe Commerce**: All versions of Adobe Commerce and Magento Open Source platforms
- **SAP NetWeaver**: Multiple versions affected by critical code execution vulnerabilities
- **SAP S/4HANA**: Systems previously targeted by threat actors
- **Microsoft Windows**: 81 vulnerabilities addressed in September 2025 Patch Tuesday, affecting Windows 10 and 11
- **Docker APIs**: Exposed Docker API endpoints being actively targeted
- **NPM Packages**: 18 popular open source packages with over 2 billion weekly downloads compromised

## Attack Vectors and Techniques

- **Account Takeover**: Exploitation of Adobe Commerce vulnerability to gain unauthorized access to customer accounts
- **Remote Code Execution**: SAP NetWeaver vulnerabilities allowing attackers to execute arbitrary code
- **File Upload Attacks**: Arbitrary file upload capabilities through SAP vulnerabilities
- **API Exploitation**: Targeting exposed Docker APIs for malicious container deployment
- **Supply Chain Poisoning**: Compromising popular NPM packages through phished developer accounts
- **Tor Network Obfuscation**: Threat actors using Tor to hide their activities in Docker API attacks

## Threat Actor Activities

- **Docker API Attackers**: Updated malicious tooling with enhanced functionality that could establish complex botnets, using Tor network for anonymization
- **NPM Supply Chain Attackers**: Phished Qix's NPM account credentials to publish poisoned versions of 18 popular open source packages, affecting over 2 billion weekly downloads
- **Southeast Asian Scam Networks**: Large-scale cybercrime operations that stole over $10 billion from Americans, now facing increased financial sanctions from the US government
- **SAP-Targeting Groups**: Previously exploited S/4HANA systems before patches were available