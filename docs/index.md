# Exploitation Report

This report reveals critical active exploitation activity across multiple high-impact vulnerabilities. The most severe concern is a maximum CVSS 10.0 vulnerability in Grafana Enterprise affecting SCIM functionality, enabling user impersonation and privilege escalation. Simultaneously, threat actors are exploiting a two-year-old Ray AI framework vulnerability to build self-spreading GPU cryptomining botnets, while APT24 has deployed previously undocumented BADAUDIO malware in multi-year espionage campaigns targeting over 1,000 domains. Additional concerns include widespread scanning of Palo Alto GlobalProtect VPN portals, SonicWall firewall vulnerabilities allowing denial-of-service attacks, and data theft incidents affecting major platforms including Salesforce and Italian railway systems.

## Active Exploitation Details

### Grafana Enterprise SCIM Authentication Bypass
- **Description**: Maximum severity vulnerability in Grafana Enterprise's SCIM implementation that allows authentication bypass and user impersonation
- **Impact**: Attackers can treat new users as administrators or escalate privileges within Grafana environments
- **Status**: Patches released by Grafana Labs
- **CVE ID**: CVE-2025-41115

### Ray AI Framework Remote Code Execution
- **Description**: Two-year-old security flaw in the Ray open-source AI framework being actively exploited to build cryptomining botnets
- **Impact**: Enables creation of self-spreading GPU cryptomining botnets targeting NVIDIA GPU clusters
- **Status**: Unpatched systems continue to be exploited in ShadowRay 2.0 campaigns

### SonicWall SonicOS SSL VPN Denial-of-Service
- **Description**: High-severity vulnerability in SonicWall SonicOS SSL VPN implementation
- **Impact**: Allows attackers to crash vulnerable firewalls through denial-of-service attacks
- **Status**: Patches available, urgent patching recommended by SonicWall

## Affected Systems and Products

- **Grafana Enterprise**: All versions with SCIM functionality enabled prior to security updates
- **Ray AI Framework**: Unpatched installations continue to be vulnerable to ShadowRay 2.0 attacks
- **SonicWall SonicOS**: Firewalls running vulnerable SSL VPN implementations
- **Palo Alto GlobalProtect**: VPN portals experiencing massive scanning campaigns with 2.3 million probe sessions
- **Salesforce Platform**: Customer data accessed through Gainsight-linked OAuth activity
- **Windows Systems**: Targeted by Tsundere botnet using game-based lures and Ethereum C2 infrastructure

## Attack Vectors and Techniques

- **SCIM Authentication Bypass**: Exploitation of authentication flaws in System for Cross-domain Identity Management implementations
- **GPU Cryptomining Botnet**: Self-spreading malware targeting AI framework clusters with high-performance graphics processing units
- **OAuth Token Abuse**: Unauthorized access through compromised third-party application tokens on cloud platforms
- **VPN Portal Scanning**: Mass reconnaissance campaigns targeting enterprise VPN infrastructure
- **Social Engineering**: Game-based lures distributed through legitimate-appearing applications
- **Ethereum-based C2**: Command and control infrastructure leveraging blockchain technology for communications

## Threat Actor Activities

- **APT24**: China-linked group conducting multi-year espionage campaigns using BADAUDIO malware, targeting Taiwan and over 1,000 domains with sophisticated attack methods
- **ShadowRay Operators**: Cybercriminals exploiting Ray framework vulnerabilities to build and expand GPU-based cryptomining infrastructure
- **Scattered Spider**: British teenagers charged in connection with Transport for London breach causing millions in damages and customer data exposure
- **Tsundere Botnet Operators**: Actively expanding Windows-targeting botnet using gaming lures and blockchain-based command infrastructure
- **Unknown Threat Actors**: Conducting mass scanning campaigns against GlobalProtect VPN portals and data theft operations targeting Italian railway systems through Almaviva compromise