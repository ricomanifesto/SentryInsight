# Exploitation Report

Critical exploitation activity has emerged across multiple platforms and technologies, with active attacks targeting nginx-ui servers, Microsoft SharePoint environments, and Windows Task Host components. A critical nginx-ui vulnerability enables complete server takeover and is currently being exploited in the wild. Microsoft addressed a record 167 security vulnerabilities in their April 2026 Patch Tuesday, including two zero-day vulnerabilities—one affecting SharePoint Server that has been actively exploited. Additionally, CISA has warned of active exploitation of a Windows Task Host privilege escalation vulnerability that allows attackers to gain SYSTEM-level privileges. Beyond these critical vulnerabilities, threat actors are leveraging legitimate services like n8n workflow automation platforms and signed software to deploy malicious payloads while evading detection.

## Active Exploitation Details

### nginx-ui Server Takeover Vulnerability
- **Description**: A critical security flaw in nginx-ui, an open-source web-based Nginx management tool, that enables complete server compromise
- **Impact**: Attackers can achieve full nginx server takeover, potentially gaining complete control over web server infrastructure
- **Status**: Currently under active exploitation in the wild; patches available
- **CVE ID**: CVE-2026-33032

### Microsoft SharePoint Server Zero-Day
- **Description**: A zero-day vulnerability affecting Microsoft SharePoint Server that has been actively exploited by threat actors
- **Impact**: Exploitation allows unauthorized access to SharePoint environments, potentially compromising sensitive corporate data and collaboration systems
- **Status**: Actively exploited in the wild; patched in April 2026 Patch Tuesday update

### Windows Task Host Privilege Escalation
- **Description**: A privilege escalation vulnerability in Windows Task Host component that allows elevation to SYSTEM privileges
- **Impact**: Attackers can gain SYSTEM-level access to Windows systems, enabling complete system compromise
- **Status**: CISA has flagged this vulnerability as exploited in attacks; patches available

### PHP Composer Command Execution Vulnerabilities
- **Description**: Two high-severity vulnerabilities in Composer, a package manager for PHP, enabling arbitrary command execution
- **Impact**: Successful exploitation allows attackers to execute arbitrary commands on systems running vulnerable Composer versions
- **Status**: Patches have been released to address these vulnerabilities

## Affected Systems and Products

- **nginx-ui**: Open-source web-based Nginx management tool vulnerable to complete server takeover
- **Microsoft SharePoint Server**: Corporate collaboration platform affected by actively exploited zero-day vulnerability
- **Windows Task Host**: Windows component vulnerable to privilege escalation attacks
- **PHP Composer**: Package manager for PHP affected by command execution vulnerabilities
- **n8n Workflow Platform**: AI workflow automation platform being abused for malicious campaigns
- **Chrome Web Store Extensions**: Over 100 malicious extensions targeting user accounts and data
- **Apple App Store**: Fake Ledger Live application stealing cryptocurrency from victims
- **Microsoft Windows Server 2019/2022**: Systems experiencing unexpected upgrades to Windows Server 2025

## Attack Vectors and Techniques

- **Server Takeover**: Exploitation of nginx-ui vulnerabilities to gain complete control over web servers
- **Privilege Escalation**: Windows Task Host vulnerability abuse to achieve SYSTEM-level privileges
- **Signed Software Abuse**: Digitally signed adware tools deploying antivirus-killing scripts with SYSTEM privileges
- **Webhook Weaponization**: n8n webhooks being leveraged for sophisticated phishing campaigns since October 2025
- **Supply Chain Attacks**: Malicious Chrome Web Store extensions stealing OAuth2 Bearer tokens and deploying backdoors
- **App Store Impersonation**: Fake applications in official app stores used to steal cryptocurrency
- **Command Injection**: PHP Composer vulnerabilities enabling arbitrary command execution
- **EDR Evasion**: Bring-your-own-vulnerable-driver (BYOVD) techniques used to disable endpoint detection and response systems

## Threat Actor Activities

- **nginx-ui Exploitation Campaign**: Threat actors actively exploiting CVE-2026-33032 to compromise nginx servers worldwide
- **Microsoft Zero-Day Exploiters**: Attackers leveraging SharePoint Server zero-day vulnerability for unauthorized access to corporate environments
- **Chrome Extension Malware Operators**: Criminal groups distributing over 100 malicious Chrome extensions for account theft and ad fraud
- **Cryptocurrency Thieves**: Cybercriminals using fake Ledger Live app to steal $9.5 million in cryptocurrency from 50 victims
- **Kraken Exchange Extortionists**: Cybercrime group attempting to extort cryptocurrency exchange following insider breach
- **McGraw-Hill Data Breach Actors**: Hackers exploiting Salesforce misconfiguration to access internal company data
- **n8n Campaign Operators**: Threat actors weaponizing AI workflow automation platform for phishing since October 2025
- **EDR Killer Ecosystem**: Expanding network of actors using BYOVD techniques to disable security tools