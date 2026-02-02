# Exploitation Report

A significant wave of supply chain attacks has dominated the threat landscape, with state-sponsored actors successfully compromising multiple software update mechanisms. Chinese threat actors hijacked Notepad++'s update infrastructure for nearly six months, while unknown attackers compromised eScan antivirus update servers to deliver persistent malware. Additionally, a sophisticated supply chain attack targeted the Open VSX Registry through compromised developer accounts, spreading GlassWorm malware. These incidents highlight the critical vulnerability of software update mechanisms and the persistent threat posed by nation-state actors targeting development infrastructure.

## Active Exploitation Details

### Notepad++ Update Mechanism Hijack
- **Description**: Chinese state-sponsored threat actors compromised Notepad++'s update infrastructure, redirecting legitimate update traffic to malicious servers controlled by the attackers
- **Impact**: Attackers could deliver malware to select Notepad++ users through what appeared to be legitimate software updates
- **Status**: Attack lasted for almost six months before being discovered and remediated by the Notepad++ development team

### eScan Antivirus Update Server Compromise
- **Description**: Unknown attackers compromised the update infrastructure of eScan antivirus software, developed by MicroWorld Technologies
- **Impact**: Attackers delivered multi-stage persistent malware through the compromised antivirus update mechanism
- **Status**: Active compromise allowing malware distribution through trusted antivirus update channels

### Open VSX Registry Supply Chain Attack
- **Description**: Threat actors compromised legitimate developer accounts to push malicious extensions through the Open VSX Registry
- **Impact**: Distribution of GlassWorm malware through trusted development platform
- **Status**: Ongoing supply chain attack targeting developer ecosystems

### MongoDB Data Extortion Attacks
- **Description**: Automated attacks targeting exposed MongoDB instances for data extortion purposes
- **Impact**: Attackers delete database contents and demand low ransoms for data restoration
- **Status**: Ongoing automated campaign targeting misconfigured database instances

## Affected Systems and Products

- **Notepad++**: Popular text editor with compromised update mechanism affecting select users globally
- **eScan Antivirus**: Indian cybersecurity solution with compromised update servers
- **Open VSX Registry**: Extension marketplace targeted through compromised developer accounts
- **MongoDB Instances**: Exposed database instances targeted in automated extortion attacks
- **Chrome Extensions**: Multiple malicious browser extensions discovered abusing affiliate links
- **IIS Servers**: Microsoft web servers in Asia targeted by BadIIS SEO malware
- **Wind and Solar Farms**: Over 30 renewable energy facilities in Poland targeted in coordinated attacks
- **Instagram Private Profiles**: Photo links exposed to unauthenticated visitors

## Attack Vectors and Techniques

- **Supply Chain Compromise**: Attackers targeting software update mechanisms and developer platforms
- **Update Infrastructure Hijacking**: Redirecting legitimate software update traffic to malicious servers
- **Voice Phishing (Vishing)**: ShinyHunters group using targeted voice calls combined with branded phishing sites
- **SSO Credential Theft**: Abuse of single sign-on systems to access cloud-based SaaS platforms
- **Automated Database Extortion**: Scripted attacks against misconfigured MongoDB instances
- **Affiliate Link Hijacking**: Malicious browser extensions redirecting legitimate affiliate links
- **SEO Malware Deployment**: BadIIS malware targeting IIS servers for search engine manipulation

## Threat Actor Activities

- **Chinese State-Sponsored Groups**: Long-term compromise of Notepad++ update infrastructure lasting six months, demonstrating sophisticated persistence techniques
- **UAT-8099**: China-linked threat actor conducting campaigns against IIS servers in Asia using BadIIS SEO malware between late 2025 and early 2026
- **ShinyHunters**: Financially motivated group expanding operations with vishing attacks and SSO abuse to breach SaaS platforms
- **RedKitten**: Iran-linked Farsi-speaking threat actor targeting human rights NGOs and activists documenting recent human rights issues
- **Unknown Actors**: Compromising eScan antivirus update servers and conducting automated MongoDB extortion campaigns
- **Coordinated Attackers**: Targeting over 30 wind and solar farms in Poland along with manufacturing sector companies