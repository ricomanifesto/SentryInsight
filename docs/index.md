# Exploitation Report

Critical zero-day vulnerabilities are currently being exploited across multiple enterprise platforms, with particular focus on Ivanti Endpoint Manager Mobile and Palo Alto Networks firewalls. The most severe threats include CVE-2026-6973 affecting Ivanti EPMM systems, which grants administrative access to attackers, and a newly disclosed Linux kernel privilege escalation vulnerability dubbed "Dirty Frag." Additionally, the ShinyHunters extortion gang has compromised hundreds of educational institutions through Canvas platform vulnerabilities, while sophisticated malware frameworks like PCPJack are targeting cloud infrastructure across multiple CVE exploits. State-sponsored actors appear to be actively exploiting firewall vulnerabilities for espionage purposes, and new credential-stealing malware campaigns are leveraging social engineering techniques to compromise enterprise environments.

## Active Exploitation Details

### Ivanti Endpoint Manager Mobile RCE Vulnerability
- **Description**: High-severity remote code execution vulnerability in Ivanti EPMM allowing unauthorized access to mobile device management systems
- **Impact**: Attackers can gain administrative-level access to endpoint management infrastructure, potentially compromising managed mobile devices across organizations
- **Status**: Currently being exploited in limited zero-day attacks; CISA has mandated federal agencies patch within four days
- **CVE ID**: CVE-2026-6973

### Linux Kernel Dirty Frag Zero-Day
- **Description**: Local privilege escalation vulnerability affecting the Linux kernel across all major distributions, described as a successor to Copy Fail
- **Impact**: Local attackers can gain root privileges with a single command execution
- **Status**: Unpatched zero-day vulnerability with proof-of-concept exploit available

### Palo Alto Networks PAN-OS Firewall Vulnerability
- **Description**: Critical remote code execution vulnerability in PAN-OS firewalls being exploited by suspected state-sponsored actors
- **Impact**: Complete system compromise allowing root access and potential espionage activities
- **Status**: Actively exploited since April 9, 2026, for nearly a month before disclosure

### Canvas Education Platform Vulnerabilities
- **Description**: Multiple vulnerabilities in Instructure's Canvas platform affecting login portals and authentication systems
- **Impact**: Mass compromise of educational institution systems, data exposure affecting hundreds of colleges and universities
- **Status**: Actively exploited by ShinyHunters extortion gang for widespread defacement and extortion campaigns

## Affected Systems and Products

- **Ivanti Endpoint Manager Mobile (EPMM)**: All versions affected by CVE-2026-6973, particularly impacting federal government networks under CISA emergency directive
- **Linux Distributions**: All major Linux distributions affected by Dirty Frag vulnerability including Ubuntu, Red Hat, SUSE, and Debian-based systems
- **Palo Alto Networks Firewalls**: PAN-OS firewall systems targeted by state-sponsored actors for persistent access
- **Canvas Education Platform**: Hundreds of educational institutions including colleges and universities using Instructure Canvas
- **Cloud Infrastructure**: AWS, Azure, and Google Cloud environments targeted by PCPJack malware framework
- **Windows Systems**: Enterprise environments targeted by Beagle backdoor through fake Claude AI websites
- **Banking and Financial Platforms**: 59 banking, fintech, and cryptocurrency platforms targeted by TCLBanker malware

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Direct exploitation of unpatched vulnerabilities in enterprise systems before public disclosure
- **Social Engineering**: ClickFix attacks using fake error messages to trick users into downloading malware
- **Supply Chain Compromise**: Quasar Linux RAT targeting developer systems to establish persistent access for broader attacks
- **Credential Harvesting**: PAM module manipulation through PamDOORa backdoor to steal SSH authentication credentials
- **Worm-Like Propagation**: PCPJack framework spreading across cloud systems while removing competing malware infections
- **Fake Software Distribution**: Malicious websites impersonating legitimate AI tools like Claude to distribute backdoors
- **WhatsApp and Email Propagation**: TCLBanker malware using messaging platforms for self-replication
- **Trojanized Installers**: Legitimate software packages modified to include banking trojans and credential stealers

## Threat Actor Activities

- **ShinyHunters Extortion Gang**: Conducting mass compromise of Canvas education platforms for data extortion and public defacement campaigns
- **State-Sponsored Actors**: Exploiting Palo Alto Networks firewall vulnerabilities for espionage and persistent network access since early April 2026
- **Russian Cybercrime Forum Actors**: "darkworm" actor advertising PamDOORa Linux backdoor for $1,600 on Rehub forum
- **PCPJack Operators**: Sophisticated malware framework developers targeting cloud infrastructure while actively competing with TeamPCP malware operators
- **North Korean IT Workers**: Using "laptop farms" operated by U.S. nationals to fraudulently obtain remote employment at American companies for sanctions evasion
- **Cryptocurrency Theft Groups**: Multi-million dollar heist operations targeting crypto platforms with over $230 million in stolen assets