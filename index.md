# Exploitation Report

Critical zero-day vulnerabilities in Cisco network infrastructure are under active exploitation, prompting emergency directives from CISA. Multiple Cisco products including ASA firewalls and IOS software are being targeted by attackers exploiting previously unknown vulnerabilities. Simultaneously, China-linked threat actors are deploying sophisticated backdoors on network edge devices, while North Korean hackers continue their cryptocurrency-focused campaigns with new backdoor tools. Federal agencies have also been breached through exploitation of a critical GeoServer vulnerability, highlighting the ongoing threat landscape across multiple sectors and technologies.

## Active Exploitation Details

### Cisco ASA Firewall Zero-Day Vulnerabilities
- **Description**: Two zero-day vulnerabilities affecting the VPN web server of Cisco Secure Firewall Adaptive Security Appliance (ASA) Software and Cisco Secure Firewall Threat Defense (FTD) Software
- **Impact**: Attackers can compromise firewall devices and potentially gain network access
- **Status**: Currently being exploited in attacks; CISA has issued emergency directive requiring federal agencies to patch immediately

### Cisco IOS SNMP Vulnerability
- **Description**: High-severity security flaw in IOS Software and IOS XE Software affecting SNMP functionality
- **Impact**: Remote attackers can execute arbitrary code or trigger denial-of-service conditions
- **Status**: Actively exploited in attacks; patches available

### GeoServer Critical Vulnerability
- **Description**: Critical vulnerability in GeoServer geospatial software
- **Impact**: Allows attackers to breach federal agencies and gain unauthorized access
- **Status**: Exploited less than two weeks after initial disclosure to breach a large federal civilian executive branch agency
- **CVE ID**: CVE-2024-36401

### Salesforce Agentforce AI Vulnerability (ForcedLeak)
- **Description**: Critical flaw in Salesforce Agentforce platform affecting AI agents through prompt injection
- **Impact**: Attackers can potentially exfiltrate CRM data through AI prompt manipulation
- **Status**: Recently patched by Salesforce

## Affected Systems and Products

- **Cisco Secure Firewall ASA Software**: VPN web server components vulnerable to zero-day attacks
- **Cisco Secure Firewall Threat Defense (FTD)**: Network security appliances with VPN functionality
- **Cisco IOS and IOS XE Software**: Network operating systems with SNMP vulnerabilities
- **GeoServer**: Geospatial data serving software used by federal agencies
- **Salesforce Agentforce**: AI agent platform vulnerable to prompt injection attacks
- **Supermicro BMC Firmware**: Baseboard Management Controller allowing persistent backdoor installation
- **Wondershare RepairIt**: Software with flaws exposing user data and AI models
- **Network Edge Devices**: Various appliances targeted by Chinese APT groups for backdoor deployment

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Attackers leveraging previously unknown vulnerabilities in Cisco infrastructure before patches were available
- **Backdoor Deployment**: Installation of persistent access tools like BRICKSTORM on network edge devices that cannot run traditional security agents
- **Prompt Injection**: Manipulation of AI systems through crafted prompts to exfiltrate sensitive data
- **Supply Chain Attacks**: Malicious packages in software repositories (Rust crates) designed to steal cryptocurrency wallet keys
- **Social Engineering**: North Korean actors using fake job interviews to deploy backdoors on developer systems
- **SNMP Exploitation**: Remote code execution through vulnerable network management protocols
- **BMC Firmware Manipulation**: Creation of persistent backdoors through malicious firmware updates

## Threat Actor Activities

- **UNC5221 (China-linked)**: Deploying BRICKSTORM backdoors on edge devices targeting U.S. legal services, SaaS providers, and technology sectors
- **RedNovember (Chinese APT)**: Targeting global governments using Pantegana and Cobalt Strike tools across multiple continents
- **North Korean Actors**: Conducting Contagious Interview campaigns with new AkdoorTea backdoor to target cryptocurrency developers
- **Scattered Spider**: Major ransomware group responsible for $107 million loss to Co-operative Group, with recent member surrender and claimed shutdown
- **Vane Viper**: Operating massive malware and ad fraud network generating over 1 trillion DNS queries globally
- **Federal Agency Attackers**: Exploiting GeoServer vulnerability to breach large federal civilian executive branch agency