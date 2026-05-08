# Exploitation Report

Critical zero-day vulnerabilities are currently being exploited in widespread attacks targeting enterprise infrastructure and cloud environments. The most severe activity involves active exploitation of Ivanti Endpoint Manager Mobile (EPMM) vulnerabilities, PAN-OS firewall systems, and Linux kernel privilege escalation flaws. Threat actors are leveraging these vulnerabilities to gain administrative access, steal credentials, and establish persistent footholds in corporate networks. Additionally, sophisticated malware campaigns including new Linux RATs, banking trojans, and credential-stealing frameworks are actively targeting developers and cloud infrastructure with worm-like propagation capabilities.

## Active Exploitation Details

### Ivanti EPMM Remote Code Execution
- **Description**: High-severity remote code execution vulnerability in Ivanti Endpoint Manager Mobile (EPMM) being exploited in limited zero-day attacks
- **Impact**: Attackers can gain administrative-level access to mobile device management systems
- **Status**: Actively exploited in the wild, CISA mandated federal agencies patch within four days
- **CVE ID**: CVE-2026-6973

### Linux Kernel Dirty Frag Privilege Escalation
- **Description**: Unpatched local privilege escalation vulnerability affecting all major Linux distributions, described as successor to Copy Fail
- **Impact**: Local attackers can gain root privileges with a single command across most Linux distributions
- **Status**: Zero-day vulnerability with proof-of-concept exploit available, currently unpatched

### PAN-OS Firewall Remote Code Execution
- **Description**: Critical-severity zero-day vulnerability in Palo Alto Networks PAN-OS firewalls exploited by suspected state-sponsored actors
- **Impact**: Root access and espionage capabilities on enterprise firewall systems
- **Status**: Actively exploited since April 9, 2026 for nearly a month before discovery

### Canvas Education Platform Vulnerability
- **Description**: Vulnerability in Instructure Canvas education platform exploited by ShinyHunters extortion gang
- **Impact**: Mass defacement of login portals affecting hundreds of colleges and universities nationwide
- **Status**: Ongoing data extortion campaign causing widespread disruption to educational institutions

## Affected Systems and Products

- **Ivanti Endpoint Manager Mobile (EPMM)**: Mobile device management systems in federal and enterprise environments
- **Linux Distributions**: All major Linux distributions including Ubuntu, Red Hat, SUSE, and Debian affected by Dirty Frag vulnerability
- **Palo Alto Networks PAN-OS**: Enterprise firewall systems providing network security
- **Instructure Canvas**: Widely-used education technology platform serving schools and universities
- **Cloud Infrastructure**: AWS, Azure, and other cloud platforms targeted by PCPJack credential theft framework
- **Banking and Fintech Platforms**: 59 banking, fintech, and cryptocurrency platforms targeted by TCLBanker malware

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Direct exploitation of unpatched vulnerabilities in Ivanti EPMM, PAN-OS, and Linux kernel
- **Social Engineering (ClickFix)**: Australian organizations warned of ongoing campaigns using ClickFix technique to distribute Vidar Stealer
- **Supply Chain Compromise**: Quasar Linux RAT targeting developer systems to establish foothold for broader supply chain attacks
- **Credential Theft**: PCPJack framework exploiting five CVEs to spread worm-like across cloud systems while stealing credentials
- **Trojanized Software**: TCLBanker malware using fake Logitech AI Prompt Builder MSI installer for initial infection
- **PAM Module Abuse**: PamDOORa backdoor leveraging PAM modules to steal SSH credentials on Linux systems
- **WhatsApp and Email Propagation**: TCLBanker malware self-spreading through WhatsApp and Outlook messaging platforms

## Threat Actor Activities

- **State-Sponsored Actors**: Suspected nation-state groups exploiting PAN-OS firewall vulnerabilities for espionage and persistence
- **ShinyHunters**: Extortion gang conducting mass Canvas platform breaches affecting educational institutions nationwide
- **darkworm**: Threat actor advertising PamDOORa Linux backdoor on Rehub Russian cybercrime forum for $1,600
- **PCPJack Operators**: Cybercriminals deploying credential theft framework while actively removing TeamPCP malware from infected systems
- **North Korean IT Workers**: Using laptop farms operated by American nationals to fraudulently obtain remote employment at 70+ U.S. companies
- **Cryptocurrency Gang**: Criminal organization responsible for $230+ million cryptocurrency heist involving home invasion and money laundering