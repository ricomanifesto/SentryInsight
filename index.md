# Exploitation Report

Critical exploitation activity is currently targeting multiple enterprise systems with several zero-day vulnerabilities and authentication bypass flaws being actively exploited. The most significant threats include a zero-day vulnerability in FreePBX systems that impacts exposed administrator control panels, an authentication bypass flaw in Passwordstate password management software, and a sophisticated supply chain attack using AI-powered stealer malware that has compromised over 1,000 developers. Additionally, a major OAuth breach affecting Salesloft integrations has expanded beyond Salesforce to impact Google Workspace accounts, while Chinese nation-state actors continue operating a global espionage system targeting network infrastructure.

## Active Exploitation Details

### FreePBX Zero-Day Vulnerability
- **Description**: A zero-day vulnerability in Sangoma FreePBX systems that allows attackers to compromise systems with exposed administrator control panels (ACP)
- **Impact**: Complete system compromise of FreePBX servers exposed to the internet
- **Status**: Actively exploited in the wild; emergency patch now available from Sangoma FreePBX Security Team

### Passwordstate Authentication Bypass
- **Description**: Authentication bypass vulnerability in Click Studios' Passwordstate enterprise password management solution affecting the Emergency Access Page
- **Impact**: Unauthorized access to password management systems, potentially exposing stored credentials
- **Status**: Patched by Click Studios with security updates released

### AI-Powered Supply Chain Attack
- **Description**: Sophisticated supply chain attack using AI-powered stealer malware targeting developers
- **Impact**: Massive data exfiltration affecting over 1,000 developers, with secrets and sensitive data leaked to the web within hours
- **Status**: Active campaign with ongoing data exposure

### Salesloft OAuth Token Breach
- **Description**: OAuth token compromise affecting Salesloft Drift integrations, extending beyond initial Salesforce targeting
- **Impact**: Unauthorized access to Google Workspace email accounts and other integrated services
- **Status**: Ongoing breach with expanded scope beyond initial assessment

## Affected Systems and Products

- **FreePBX Systems**: Sangoma FreePBX installations with administrator control panels exposed to the internet
- **Passwordstate**: Click Studios enterprise password management solution, specifically the Emergency Access Page component
- **Google Workspace**: Email accounts accessed through compromised Salesloft OAuth tokens
- **Salesforce**: Initial target of Salesloft OAuth breach
- **Developer Environments**: Over 1,000 developers affected by AI-powered stealer malware
- **Network Infrastructure**: Various network devices targeted by Chinese nation-state espionage operations
- **TransUnion Systems**: Credit reporting infrastructure compromised affecting 4+ million customers

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Direct targeting of unpatched FreePBX systems through exposed administrator interfaces
- **Authentication Bypass**: Circumventing security controls in password management emergency access features
- **OAuth Token Theft**: Compromising authentication tokens to gain persistent access to integrated cloud services
- **Supply Chain Infiltration**: Using AI-enhanced malware to target developer environments and extract sensitive data
- **Malvertising Campaigns**: TamperedChef malware distributed through fake PDF editor advertisements
- **Network Device Targeting**: Chinese actors exploiting network infrastructure for espionage purposes

## Threat Actor Activities

- **Chinese Nation-State Groups**: Operating extensive global espionage system targeting network devices and infrastructure across multiple countries
- **Cybercriminal Organizations**: Deploying TamperedChef information stealer through sophisticated malvertising campaigns targeting users seeking PDF editing tools
- **Supply Chain Attackers**: Conducting AI-powered attacks against developer communities to steal secrets and sensitive data
- **OAuth Exploitation Groups**: Targeting Salesloft integrations to gain unauthorized access to enterprise cloud services
- **Ransomware Groups**: Akira and Cl0p identified as most active ransomware-as-a-service operations, with increasing use of AI in their campaigns