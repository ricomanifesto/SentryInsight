# Exploitation Report

Critical zero-day vulnerabilities are actively being exploited across multiple platforms, with particularly concerning activity targeting Microsoft Defender, operational technology systems, and web infrastructure. A researcher has published proof-of-concept code for a Microsoft Defender zero-day dubbed "RedSun" that grants SYSTEM privileges, while threat actors are deploying specialized malware like ZionSiphon to sabotage water treatment systems. North Korean groups continue sophisticated campaigns targeting macOS users through fake job offers, and critical authentication bypass flaws in Nginx UI are being exploited for full server takeover. Additionally, widespread supply chain compromises affecting WordPress plugins and adware tools are being leveraged to deploy antivirus-killing payloads with SYSTEM privileges.

## Active Exploitation Details

### Microsoft Defender "RedSun" Zero-Day
- **Description**: A privilege escalation vulnerability in Microsoft Defender that allows attackers to gain SYSTEM privileges
- **Impact**: Complete system compromise with highest privilege level access
- **Status**: Zero-day with published proof-of-concept exploit code

### Nginx UI Authentication Bypass Flaw
- **Description**: Critical authentication bypass vulnerability in Nginx UI with Model Context Protocol (MCP) support
- **Impact**: Full server takeover without authentication, ability to restart, create, modify, and delete NGINX configuration files
- **Status**: Actively exploited in the wild

### Marimo Critical Vulnerability
- **Description**: Critical vulnerability in Marimo reactive Python notebook being exploited to deploy NKAbuse malware
- **Impact**: Malware deployment from compromised Hugging Face Spaces
- **Status**: Active exploitation with malware hosted on legitimate platforms

## Affected Systems and Products

- **Microsoft Defender**: Windows security platform vulnerable to privilege escalation
- **Nginx UI with MCP**: Web server management interface with authentication bypass
- **Marimo**: Python notebook platform being exploited for malware delivery
- **Water Treatment Systems**: Operational technology environments targeted by ZionSiphon malware
- **macOS Systems**: Targeted by North Korean ClickFix campaigns
- **WordPress Sites**: Over 30 EssentialPlugin package plugins compromised
- **Cisco Webex Services**: Cloud-based platform with critical certificate validation flaws
- **Windows Systems**: Targeted by Dragon Boss adware with antivirus evasion capabilities

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Publication of proof-of-concept code for Microsoft Defender vulnerability
- **Supply Chain Compromise**: Malicious code injection into WordPress plugin packages affecting thousands of sites
- **Social Engineering**: North Korean groups using fake job offers and phony Zoom updates for ClickFix attacks
- **Infrastructure Abuse**: n8n webhook platform weaponized for phishing campaigns since October 2025
- **Operational Technology Targeting**: ZionSiphon malware specifically designed for water treatment sabotage
- **Authentication Bypass**: Direct exploitation of Nginx UI flaws for unauthorized access
- **Signed Software Abuse**: Legitimate digitally signed tools deploying antivirus-killing scripts with SYSTEM privileges
- **AI-Powered Social Engineering**: ATHR platform using AI voice agents for automated vishing attacks

## Threat Actor Activities

- **Chaotic Eclipse**: Security researcher publishing Microsoft Defender zero-day exploits in protest
- **Sapphire Sleet (North Korea)**: Using ClickFix attacks to target macOS users with credential theft
- **UAC-0247**: Targeting Ukrainian clinics and government institutions with AgingFly malware
- **ShinyHunters**: Extortion group behind McGraw Hill data breach affecting 13.5 million accounts
- **PowMix Operators**: Running botnet campaign targeting Czech Republic workforce since December 2025
- **Dragon Boss Operators**: Deploying adware that transforms into antivirus-killing malware
- **Various Threat Actors**: Exploiting compromised WordPress plugins and n8n webhooks for malware distribution