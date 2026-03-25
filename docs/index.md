# Exploitation Report

Current threat activity is dominated by sophisticated supply chain attacks, AI-powered campaigns, and critical infrastructure vulnerabilities. The TeamPCP hacking group has launched a coordinated supply chain compromise affecting multiple popular development tools including the LiteLLM Python package, Trivy scanner, and Checkmarx KICS, stealing credentials and authentication tokens from hundreds of thousands of developers. Concurrently, threat actors are exploiting critical router authentication bypass vulnerabilities in TP-Link devices while leveraging AI agents for autonomous cyber espionage campaigns. Large-scale malvertising operations are delivering ScreenConnect malware that uses legitimate Huawei drivers to disable endpoint detection and response systems, while device code phishing campaigns are successfully compromising Microsoft 365 identities across over 340 organizations globally.

## Active Exploitation Details

### TP-Link Router Authentication Bypass
- **Description**: Critical authentication bypass vulnerability in TP-Link Archer NX router series allowing attackers to upload malicious firmware
- **Impact**: Complete device compromise, network infiltration, and ability to install persistent backdoors
- **Status**: Patches available from TP-Link, users urged to update immediately

### PTC Windchill and FlexPLM Remote Code Execution
- **Description**: Critical vulnerability in widely-used product lifecycle management solutions enabling remote code execution
- **Impact**: Full system compromise and potential lateral movement within enterprise networks
- **Status**: PTC warns of imminent threat, patches required immediately

### LiteLLM Supply Chain Compromise
- **Description**: Malicious backdoor inserted into versions 1.82.7-1.82.8 of the popular Python package by TeamPCP threat actors
- **Impact**: Credential harvesting and authentication token theft from development environments
- **Status**: Compromised versions identified, clean versions available

### ConnectWise ScreenConnect Malware Distribution
- **Description**: Malvertising campaign delivering rogue ScreenConnect installers through tax-related search advertisements
- **Impact**: Remote access trojan deployment with EDR evasion capabilities using legitimate Huawei drivers
- **Status**: Ongoing campaign active since January 2026

### Microsoft 365 Device Code Phishing
- **Description**: OAuth abuse campaign targeting Microsoft 365 identities through device code phishing techniques
- **Impact**: Account compromise and unauthorized access to corporate cloud environments
- **Status**: Active campaign affecting organizations across five countries

## Affected Systems and Products

- **TP-Link Archer NX Router Series**: Authentication bypass vulnerability affecting multiple router models
- **PTC Windchill and FlexPLM**: Product lifecycle management solutions vulnerable to remote code execution
- **LiteLLM Python Package**: Versions 1.82.7 and 1.82.8 contain malicious backdoors
- **Trivy Security Scanner**: Compromised by TeamPCP in CI/CD pipeline attacks
- **Checkmarx KICS**: Code security scanner targeted in supply chain compromise
- **ConnectWise ScreenConnect**: Legitimate remote access tool being impersonated in malvertising
- **Microsoft 365 Organizations**: Over 340 organizations across US, Canada, Australia affected by device code phishing
- **GlassWorm Campaign Targets**: Multi-stage framework targeting cryptocurrency and browser data

## Attack Vectors and Techniques

- **Supply Chain Compromise**: TeamPCP group systematically targeting development tools and CI/CD pipelines
- **Malvertising Campaigns**: Tax-related search ads delivering malicious ScreenConnect installers
- **Device Code Phishing**: OAuth abuse targeting Microsoft 365 authentication flows
- **AI Agent Exploitation**: Autonomous AI systems conducting 80-90% of cyber espionage operations
- **EDR Evasion**: Legitimate Huawei drivers being weaponized to disable security software
- **Solana Dead Drops**: GlassWorm malware using blockchain technology for command and control
- **Job Scam Phishing**: Fake recruitment campaigns impersonating Palo Alto Networks recruiters
- **Resume-Based Attacks**: French-speaking environments targeted with malicious resume documents

## Threat Actor Activities

- **TeamPCP**: Coordinated supply chain attacks targeting Trivy, KICS, LiteLLM, and other development tools with credential harvesting capabilities
- **TA551 Botnet Operators**: Russian national sentenced for managing botnet used in BitPaymer ransomware attacks against 72 US companies
- **State-Sponsored AI Agents**: Autonomous AI systems conducting cyber espionage campaigns against 30 global targets with minimal human intervention
- **GlassWorm Campaign**: Advanced persistent threat delivering multi-stage framework for comprehensive data theft and RAT deployment
- **Iranian Hacktivists**: Limited impact operations in Gulf region with focus on regional conflicts
- **AI Underground Markets**: Cybercriminals commercializing premium AI account access for malicious purposes