# Exploitation Report

Critical exploitation activity is currently targeting multiple enterprise systems with several zero-day vulnerabilities and authentication bypass flaws being actively exploited. The most significant threats include a zero-day vulnerability in FreePBX systems that impacts exposed administrator control panels, an authentication bypass flaw in Passwordstate password management software, and a sophisticated supply chain attack using AI-powered stealer malware that has compromised over 1,000 developers. Additionally, a major OAuth breach affecting Salesloft integrations has expanded beyond Salesforce to impact Google Workspace accounts, while Chinese nation-state actors continue operating a global espionage system targeting network infrastructure.

## Active Exploitation Details

### FreePBX Zero-Day Vulnerability
- **Description**: A zero-day vulnerability affecting FreePBX systems with administrator control panels (ACP) exposed to the internet
- **Impact**: Allows attackers to gain unauthorized access to FreePBX systems and potentially compromise entire telephony infrastructure
- **Status**: Actively exploited in the wild; emergency patch now available from Sangoma FreePBX Security Team

### Passwordstate Authentication Bypass
- **Description**: Authentication bypass vulnerability in Click Studios' Passwordstate enterprise password management solution, specifically affecting the Emergency Access Page
- **Impact**: Attackers can bypass authentication mechanisms to gain unauthorized access to stored passwords and sensitive credentials
- **Status**: Patched by Click Studios with security updates released

### AI-Powered Supply Chain Attack
- **Description**: Sophisticated supply chain attack using AI-powered stealer malware targeting software developers
- **Impact**: Massive data exfiltration affecting over 1,000 developers, with secrets and sensitive information leaked to the web within hours
- **Status**: Active campaign with ongoing data exposure

### TamperedChef Information Stealer
- **Description**: New information stealer malware distributed through malvertising campaigns disguised as fake PDF editors
- **Impact**: Steals user credentials, cookies, and other sensitive information from infected systems
- **Status**: Active distribution through fraudulent websites and malvertising

## Affected Systems and Products

- **FreePBX Systems**: Telephony systems with administrator control panels exposed to the internet
- **Passwordstate**: Click Studios enterprise password management solution, specifically Emergency Access Page functionality
- **Salesloft Drift**: OAuth integrations affecting both Salesforce and Google Workspace accounts
- **Google Workspace**: Email accounts accessed through compromised OAuth tokens from Salesloft breach
- **TransUnion**: Credit reporting services with over 4 million customer records compromised
- **Developer Environments**: Software development systems targeted by AI-powered stealer malware
- **ChromeOS Devices**: Authentication failures affecting Clever and ClassLink account access

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Direct targeting of unpatched FreePBX systems through exposed administrator interfaces
- **Authentication Bypass**: Circumventing security controls in password management systems
- **Malvertising Campaigns**: Using fraudulent advertisements to redirect users to malicious sites distributing TamperedChef stealer
- **OAuth Token Abuse**: Leveraging stolen OAuth tokens to access multiple integrated services beyond initial target
- **Supply Chain Compromise**: Sophisticated attacks targeting developer infrastructure to steal secrets and credentials
- **Social Engineering**: Disguising malware as legitimate PDF editing software to trick users into installation

## Threat Actor Activities

- **Chinese Nation-State Actors**: Operating extensive global espionage system targeting network devices and infrastructure as warned by CISA, FBI, and NSA
- **Cybercriminal Groups**: Conducting malvertising campaigns to distribute TamperedChef stealer malware through fake PDF editor sites
- **Ransomware-as-a-Service Groups**: Akira and Cl0p identified as the most active ransomware groups, with increasing use of AI in their operations
- **North Korean IT Workers**: Continued sanctions targeting schemes that operate at the expense of American organizations
- **Supply Chain Attackers**: Sophisticated threat actors using AI-powered tools to compromise developer environments and steal sensitive data