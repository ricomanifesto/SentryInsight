# Exploitation Report

Current cybersecurity exploitation activity reveals a concerning landscape of active attacks targeting critical infrastructure, supply chain components, and enterprise systems. Notable developments include TeamPCP's sophisticated supply chain attacks compromising multiple popular development tools, active device code phishing campaigns targeting over 340 Microsoft 365 organizations across five countries, and critical vulnerabilities in Citrix NetScaler systems reminiscent of previously exploited CitrixBleed flaws. Additionally, threat actors are leveraging AI-powered autonomous agents for cyber espionage, while traditional attack vectors continue through malvertising campaigns using legitimate drivers to bypass endpoint detection and response systems.

## Active Exploitation Details

### Citrix NetScaler Vulnerabilities
- **Description**: Two vulnerabilities in NetScaler ADC and NetScaler Gateway, with one bearing similarities to the previously exploited CitrixBleed and CitrixBleed2 flaws
- **Impact**: Potential for unauthorized access and system compromise similar to previous zero-day attacks
- **Status**: Patches available; Citrix urgently recommends immediate patching

### PTC Windchill and FlexPLM Remote Code Execution
- **Description**: Critical vulnerability in widely used product lifecycle management (PLM) solutions allowing remote code execution
- **Impact**: Complete system compromise and unauthorized access to sensitive product development data
- **Status**: PTC warns of imminent threat; patches required immediately

### TP-Link Archer NX Authentication Bypass
- **Description**: Critical-severity authentication bypass flaw in TP-Link Archer NX router series
- **Impact**: Attackers can bypass authentication and upload malicious firmware
- **Status**: Patches available; users urged to update immediately

### TeamPCP Supply Chain Compromises
- **Description**: Sophisticated supply chain attacks targeting multiple development tools including Trivy, KICS, and LiteLLM Python package
- **Impact**: Credential harvesting and backdoor installation affecting hundreds of thousands of developers
- **Status**: Malicious versions identified; LiteLLM versions 1.82.7-1.82.8 compromised

## Affected Systems and Products

- **Citrix NetScaler ADC and Gateway**: All versions requiring immediate patching
- **PTC Windchill and FlexPLM**: Product lifecycle management solutions used across industries
- **TP-Link Archer NX Router Series**: Consumer and enterprise networking equipment
- **LiteLLM Python Package**: Versions 1.82.7 and 1.82.8 containing backdoors
- **Trivy and KICS Security Scanners**: Compromised CI/CD pipeline components
- **Microsoft 365 Organizations**: 340+ organizations across US, Canada, Australia targeted
- **Browser Extensions**: 850 extensions targeted by Torg Grabber, including 700+ cryptocurrency wallets
- **ConnectWise ScreenConnect**: Delivered via malvertising campaigns

## Attack Vectors and Techniques

- **Device Code Phishing**: OAuth abuse targeting Microsoft 365 identities using legitimate authentication flows
- **Supply Chain Attacks**: Compromising popular development tools and packages to harvest credentials
- **Malvertising Campaigns**: Tax-related search advertisements delivering ScreenConnect malware
- **No-Code Platform Abuse**: Using Bubble AI app builder to create and host phishing applications
- **EDR Evasion**: Leveraging legitimate Huawei drivers to disable endpoint detection and response systems
- **AI Agent Exploitation**: Autonomous AI coding agents conducting cyber espionage campaigns
- **Solana Blockchain Dead Drops**: GlassWorm malware using blockchain for command and control communication
- **Phishing-as-a-Service**: TA551 botnet infrastructure supporting ransomware operations

## Threat Actor Activities

- **TeamPCP**: Conducting widespread supply chain attacks against development tools, targeting Trivy, KICS, and LiteLLM packages with credential harvesting backdoors
- **TA551 Botnet Operators**: Russian-managed botnet infrastructure used for BitPaymer ransomware attacks against 72 U.S. companies, with operator sentenced to two years
- **State-Sponsored AI Agents**: Autonomous cyber espionage campaign targeting 30 global entities with 80-90% AI-handled operations
- **Device Code Phishing Operators**: Active campaign targeting Microsoft 365 across five countries using OAuth authentication abuse
- **GlassWorm Campaign**: Multi-stage framework operators using Solana blockchain for C2 communication and comprehensive data theft
- **Torg Grabber Developers**: New infostealer targeting 728 cryptocurrency wallets and 850 browser extensions
- **LeakBase Administrator**: Arrested in Russia for operating massive stolen credential marketplace
- **Tax Season Malvertisers**: Large-scale campaign since January 2026 targeting tax document searches with ScreenConnect malware