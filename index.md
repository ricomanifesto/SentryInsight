# Exploitation Report

Current cybersecurity operations are witnessing significant exploitation activity across multiple attack vectors, with particular emphasis on supply chain compromises, social engineering campaigns, and critical infrastructure vulnerabilities. The most notable incidents include North Korean threat actors conducting sophisticated social engineering campaigns against npm package maintainers, leading to supply chain attacks affecting the popular Axios library. Additionally, attackers are actively exploiting CVE-2025-55182 (React2Shell vulnerability) in large-scale credential harvesting operations targeting Next.js hosts, while critical Cisco infrastructure components face remote system compromise vulnerabilities with CVSS scores reaching 9.8.

## Active Exploitation Details

### React2Shell Vulnerability (Next.js)
- **Description**: A vulnerability in Next.js applications that allows attackers to execute remote code and gain unauthorized access to systems
- **Impact**: Large-scale credential harvesting operation affecting 766 Next.js hosts, enabling theft of database credentials, SSH private keys, and Amazon Web Services credentials
- **Status**: Actively exploited in ongoing campaigns for credential theft
- **CVE ID**: CVE-2025-55182

### Cisco Integrated Management Controller (IMC) Critical Flaw
- **Description**: Critical security vulnerability in Cisco's Integrated Management Controller and Server Software Manager (SSM) components allowing unauthenticated remote access
- **Impact**: Remote system compromise enabling attackers to bypass authentication and gain full system control
- **Status**: Patches released by Cisco to address the vulnerability
- **CVSS Score**: 9.8 (Critical)

### Progress ShareFile Pre-Authentication Chain
- **Description**: Two vulnerabilities in Progress ShareFile enterprise file transfer solution that can be chained together for exploitation
- **Impact**: Unauthenticated file exfiltration from affected environments through pre-authentication remote code execution attacks
- **Status**: Recently disclosed vulnerabilities enabling data theft without authentication

## Affected Systems and Products

- **Axios npm Package**: Popular JavaScript HTTP client library targeted through social engineering of maintainers
- **Next.js Applications**: 766 hosts compromised through React2Shell vulnerability exploitation
- **Cisco IMC and SSM**: Infrastructure management controllers vulnerable to remote compromise
- **Progress ShareFile**: Enterprise file transfer solutions susceptible to pre-auth attacks
- **Mobile Applications**: iOS and Android apps containing SparkCat malware variants targeting cryptocurrency wallets
- **European Commission Cloud Infrastructure**: 30 EU entities affected by breach attributed to TeamPCP threat group
- **Drift Protocol (Solana)**: Decentralized exchange platform losing $285 million through Security Council compromise
- **Hasbro Corporation**: Toy manufacturer experiencing ongoing attack requiring weeks for remediation

## Attack Vectors and Techniques

- **Social Engineering**: Highly-targeted campaigns against open-source maintainers and developers
- **Supply Chain Attacks**: Compromise of trusted packages and libraries to distribute malicious code
- **Pre-Authentication Exploitation**: Chaining vulnerabilities to achieve remote code execution without credentials
- **Credential Harvesting**: Large-scale operations targeting database credentials and SSH keys
- **Mobile Malware Distribution**: App Store deployment of cryptocurrency wallet targeting trojans
- **Multi-Extortion Ransomware**: Evolution toward data theft and public leak threats beyond encryption
- **Residential Proxy Abuse**: 78% evasion rate of IP reputation systems across 4 billion sessions
- **Durable Nonce Attacks**: Sophisticated blockchain exploitation targeting administrative controls

## Threat Actor Activities

- **UNC1069 (North Korean)**: Social engineering campaign targeting Axios npm package maintainer for supply chain compromise
- **DPRK-Linked Groups**: $285 million theft from Drift Protocol through Security Council takeover and Durable Nonce social engineering attacks
- **TeamPCP**: Attribution for European Commission cloud infrastructure breach affecting 30 EU entities
- **REF1695 Operation**: Financially motivated campaign using ISO file lures to deploy remote access trojans and cryptocurrency miners since November 2023
- **Casbaneiro Banking Trojan**: Augmented Marauder campaigns targeting Spanish-speaking users across Latin America with detection evasion capabilities
- **Iranian-Linked Attackers**: Data-wiping attacks against medical technology giant Stryker Corporation requiring full system recovery