# Exploitation Report

The cybersecurity landscape has witnessed significant exploitation activity across multiple platforms and vendors. Microsoft addressed a record-breaking 167-169 security vulnerabilities in their April 2026 Patch Tuesday, including two actively exploited zero-day vulnerabilities affecting SharePoint and Windows systems. Critical remote code execution flaws in ShowDoc and PHP Composer have been actively exploited, while malicious campaigns targeting Chrome extensions and Android devices have compromised hundreds of thousands of users. Additionally, prompt injection vulnerabilities in AI systems and cryptocurrency theft through malicious mobile apps highlight the expanding attack surface across emerging technologies.

## Active Exploitation Details

### SharePoint Zero-Day Vulnerability
- **Description**: A zero-day vulnerability in Microsoft SharePoint Server that has been actively exploited in the wild
- **Impact**: Attackers can exploit this flaw to compromise SharePoint deployments and potentially gain unauthorized access to sensitive corporate data
- **Status**: Patched in Microsoft's April 2026 Patch Tuesday update

### Microsoft Windows Zero-Day Vulnerabilities
- **Description**: Two zero-day vulnerabilities affecting Windows operating systems that were being actively exploited before patches were released
- **Impact**: Successful exploitation could allow attackers to gain elevated privileges and compromise Windows systems
- **Status**: Fixed in April 2026 cumulative updates KB5083769, KB5082052, and KB5082200

### ShowDoc Remote Code Execution Flaw
- **Description**: A critical security vulnerability in ShowDoc, a document management and collaboration service popular in China
- **Impact**: Allows attackers to execute arbitrary commands on unpatched servers, leading to complete system compromise
- **Status**: Actively exploited in the wild on unpatched servers
- **CVE ID**: CVE-2025-0520

### PHP Composer Command Execution Vulnerabilities
- **Description**: Two high-severity security vulnerabilities in Composer, a package manager for PHP
- **Impact**: Successful exploitation could result in arbitrary command execution on systems using vulnerable Composer versions
- **Status**: Patches have been released

### CISA Known Exploited Vulnerabilities
- **Description**: Six security flaws across Fortinet, Microsoft, and Adobe software products
- **Impact**: Various impacts depending on the specific vulnerability, ranging from privilege escalation to remote code execution
- **Status**: Added to CISA's Known Exploited Vulnerabilities (KEV) catalog due to evidence of active exploitation

## Affected Systems and Products

- **Microsoft Windows**: Windows 10, Windows 11 (versions 25H2/24H2 and 23H2), Windows Server 2019, 2022, and 2025
- **Microsoft SharePoint**: SharePoint Server installations
- **ShowDoc**: Document management and collaboration service, particularly popular in China
- **PHP Composer**: Package manager for PHP applications
- **Google Chrome**: Chrome Web Store extensions affecting over 20,000 users
- **Android Devices**: Mobile devices targeted by Mirax RAT, reaching 220,000 accounts via Meta advertising platforms
- **Salesforce Agentforce**: AI agent platform with prompt injection vulnerabilities
- **Microsoft Copilot**: AI assistant with data leak vulnerabilities
- **Fortinet Products**: Various Fortinet security appliances and software
- **Adobe Software**: Multiple Adobe products with known exploited flaws

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Active exploitation of unpatched vulnerabilities in SharePoint and Windows systems
- **Remote Code Execution**: Exploitation of ShowDoc and PHP Composer flaws to execute arbitrary commands
- **Malicious Browser Extensions**: 108 Chrome extensions stealing Google OAuth2 tokens, deploying backdoors, and conducting ad fraud
- **Mobile Malware**: Mirax Android RAT turning devices into SOCKS5 proxies and data theft platforms
- **Prompt Injection**: AI agent manipulation in Salesforce and Microsoft platforms to leak sensitive data
- **Social Engineering**: Malicious Ledger Live app distributed through Apple's App Store stealing $9.5 million in cryptocurrency
- **Supply Chain Attacks**: Exploitation of package managers and development tools
- **Bring Your Own Vulnerable Driver (BYOVD)**: EDR-killer techniques using vulnerable drivers to disable security tools
- **Configuration Exploitation**: Salesforce misconfigurations leading to data breaches

## Threat Actor Activities

- **Chrome Extension Campaign**: Coordinated campaign using 108 malicious extensions communicating with shared command-and-control infrastructure to steal user credentials and conduct ad fraud
- **Mirax RAT Operators**: Spanish-speaking threat actors distributing Android malware through Meta advertising platforms, compromising over 220,000 accounts across Facebook, Instagram, and Messenger
- **Cryptocurrency Thieves**: Attackers distributing fake Ledger Live applications through Apple's App Store, successfully stealing $9.5 million from 50 victims in just a few days
- **AI-Driven Scam Networks**: Threat actors using artificial intelligence to generate content for "Pushpaganda" scams, exploiting Google Discover to spread scareware and conduct ad fraud
- **ShowDoc Exploiters**: Active exploitation of unpatched ShowDoc servers using remote code execution vulnerabilities
- **Ransomware Groups**: Targeting cryptocurrency exchange Kraken through insider threats and extortion attempts involving internal system access videos
- **Data Breach Actors**: Compromising Basic-Fit gym chain affecting 1 million members and McGraw-Hill through Salesforce misconfigurations