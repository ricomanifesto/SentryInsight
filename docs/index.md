# Exploitation Report

## Executive Summary

Multiple overlapping campaigns are actively targeting corporate GitHub organizations through systematic API enumeration, leveraging dormant accounts to blend into legitimate traffic while mapping repositories and user accounts for downstream attacks. Datadog Security Labs has identified this reconnaissance activity as a precursor to more invasive supply chain and credential theft operations.

In the destructive malware sphere, Microsoft has analyzed GigaWiper—a Windows backdoor that bundles disk wiping, fake ransomware, and spyware capabilities into a single modular toolkit—and patched the RoguePlanet zero-day (CVE-2026-50656) in Microsoft Defender after evidence of in-the-wild exploitation. The GodDamn ransomware family is simultaneously deploying a Microsoft-signed PoisonX kernel driver via BYOVD to disable endpoint defenses before encrypting U.S. organizations.

Identity-focused threats have surged with the emergence of Helix, a data-extortion group combining vishing, device code phishing, and MFA abuse to compromise SharePoint environments, and Forg365, a new PhaaS platform using AI-generated lures with adversary-in-the-middle and device code techniques to harvest Microsoft 365 credentials. A China-linked cluster continues exploiting vulnerable Roundcube webmail servers at North American universities for credential theft and backdoor deployment, while the Lurking Lizard actor distributes trojanized 7-Zip installers to build a residential proxy botnet.

## Active Exploitation Details

### GitHub Organizational Enumeration Campaigns
- **Description**: Multiple overlapping campaigns systematically enumerate corporate GitHub organizations, repositories, and user accounts through the GitHub API. Attackers leverage dormant or abandoned GitHub accounts to blend into legitimate traffic patterns, making reconnaissance activities difficult to distinguish from normal organizational activity.
- **Impact**: Attackers gain comprehensive maps of corporate codebases, internal project structures, contributor identities, and potential secrets exposed in repositories. This intelligence enables targeted supply chain attacks, credential stuffing, and social engineering against specific developers.
- **Status**: Active and ongoing. Datadog Security Labs reports "several overlapping campaigns" currently operating. No patch required—mitigation relies on GitHub security settings, access reviews, and monitoring for anomalous API access patterns.

### GigaWiper Windows Backdoor
- **Description**: A destructive Windows backdoor analyzed by Microsoft that combines three older destructive programs into a single modular toolkit. The malware offers disk wiping, fake ransomware encryption, and spyware capabilities as selectable commands.
- **Impact**: Full system compromise with flexible destructive options—attackers can exfiltrate data, deploy ransomware for cover or profit, or irreversibly wipe disks. The modular design allows operators to tailor destruction to operational objectives.
- **Status**: Actively analyzed by Microsoft; no specific CVE associated as this is a malware toolkit rather than a software vulnerability. Detection signatures and behavioral protections are being deployed.

### Helix Vishing and SharePoint Data Theft
- **Description**: A newly emerged data-extortion group (Helix) conducting identity-focused attacks against SharePoint environments. The group combines voice phishing (vishing), device code phishing, and multi-factor authentication abuse to gain initial access and exfiltrate data.
- **Impact**: Unauthorized access to SharePoint document libraries and associated data, leading to data theft and extortion. Device code phishing bypasses traditional credential controls by exploiting legitimate OAuth device authorization flows, while MFA abuse techniques circumvent second-factor protections.
- **Status**: Active campaigns observed. No software vulnerability exploited—attacks target identity and authentication process weaknesses. Mitigation requires phishing-resistant MFA (FIDO2/WebAuthn), conditional access policies, and user training.

### Forg365 Phishing-as-a-Service Platform
- **Description**: A new PhaaS operation (Forg365) specializing in Microsoft 365 account compromise. The platform combines adversary-in-the-middle (AiTM) phishing with device code authentication flows and AI-assisted lure generation to create highly convincing credential harvesting campaigns.
- **Impact**: Full Microsoft 365 account takeover including email, OneDrive, SharePoint, and Teams access. AiTM techniques capture session tokens to bypass MFA, while device code flows exploit legitimate Microsoft authentication endpoints. AI-generated lures increase click-through rates and credibility.
- **Status**: Actively operating as a service. No CVE—exploits authentication protocol designs and human factors. Defenses include phishing-resistant MFA, token binding policies, and advanced anti-phishing controls.

### GodDamn Ransomware with PoisonX BYOVD
- **Description**: A new ransomware family (GodDamn) employing the PoisonX kernel driver via Bring Your Own Vulnerable Driver (BYOVD) to disable endpoint security solutions prior to encryption. Notably, the PoisonX driver was signed by Microsoft, allowing it to load on systems with driver signature enforcement enabled.
- **Impact**: Complete endpoint defense evasion—antivirus, EDR, and other security agents are terminated or disabled at kernel level before ransomware execution. Targets U.S. companies across sectors. Encryption follows standard ransomware impact: data encryption, operational disruption, extortion.
- **Status**: Active campaigns against U.S. organizations. Microsoft has been notified of the malicious driver signing; revocation and detection updates are in progress. No CVE for the ransomware itself; the BYOVD technique exploits legitimate driver loading mechanisms.

### RoguePlanet Microsoft Defender Zero-Day
- **Description**: A vulnerability in Microsoft Defender (tracked as CVE-2026-50656) that allows privilege escalation to SYSTEM. The flaw, dubbed "RoguePlanet," was publicly disclosed prior to patching and evidence indicates it was exploited in the wild as a zero-day.
- **Impact**: Local privilege escalation from standard user to SYSTEM context on Windows endpoints running affected Defender versions. This enables defense evasion, persistence, credential access, and lateral movement.
- **Status**: Patched by Microsoft in July 2026, nearly one month after public disclosure. Organizations should apply the latest Defender updates immediately.
- **CVE ID**: CVE-2026-50656

### Lurking Lizard Residential Proxy Botnet
- **Description**: Threat actor "Lurking Lizard" operates an end-to-end malicious residential proxy business using trojanized 7-Zip installers as the initial infection vector. Compromised devices are enrolled into a proxy network sold for anonymizing malicious traffic.
- **Impact**: Infected devices become unwitting exit nodes for cybercrime traffic (credential stuffing, scraping, fraud, further exploitation). Victims experience bandwidth theft, IP reputation damage, and potential legal liability for traffic originating from their networks.
- **Status**: Active distribution via fake 7-Zip download sites and search engine poisoning. No CVE—supply chain compromise of a legitimate utility.

### China-Linked Roundcube Exploitation
- **Description**: A China-nexus threat cluster exploiting vulnerable Roundcube webmail servers deployed at U.S. and Canadian academic institutions. The flaw enables credential harvesting and backdoor malware deployment.
- **Impact**: Compromise of researcher and faculty email accounts, theft of academic credentials, persistent access via backdoors for long-term espionage. University environments are targeted for intellectual property and research data.
- **Status**: Active exploitation of unpatched Roundcube instances. Specific CVE not identified in available reporting; organizations running Roundcube should apply latest security updates immediately.

### Fake Paysafe/Skrill SDK Supply Chain Attack
- **Description**: Malicious packages published to npm and PyPI masquerading as legitimate Paysafe, Skrill, and Neteller SDKs. The packages contain credential-stealing malware targeting developers and users of these payment platforms.
- **Impact**: Theft of API keys, authentication tokens, and payment credentials from development environments and production systems using the compromised packages. Supply chain impact extends to any project incorporating the malicious dependencies.
- **Status**: Packages identified and removed from registries; ongoing risk from cached or unpinned dependencies. No CVE—malicious publishing abuse.

### Lone Attacker AWS Cloud Breach via AI Workflows
- **Description**: A single attacker breached a large Amazon customer's AWS environment within 72 hours by chaining AI workflow vulnerabilities, cloud misconfigurations, and stolen credentials. The intrusion culminated in data exfiltration and extortion.
- **Impact**: Full compromise of cloud infrastructure, data theft, and extortion. Demonstrates the speed at which AI-augmented attackers can traverse complex cloud environments when identity and configuration weaknesses align.
- **Status**: Incident resolved; highlights emerging threat model. No specific CVE—exploitation of configuration weaknesses and credential theft.

## Affected Systems and Products

- **GitHub Enterprise / GitHub.com**: Corporate organizations with accessible APIs and dormant user accounts; all platforms where GitHub API enumeration is possible
- **Microsoft Windows**: Systems running Microsoft Defender vulnerable to CVE-2026-50656 (pre-patch versions); Windows endpoints targeted by GodDamn ransomware and GigaWiper
- **Microsoft Defender**: Affected versions prior to July 2026 security update (RoguePlanet/CVE-2026-50656)
- **Microsoft 365 / Entra ID**: Tenants targeted by Helix (SharePoint), Forg365 (AiTM/device code phishing), and general identity attacks
- **SharePoint Online / On-premises**: Data repositories targeted by Helix for exfiltration
- **Roundcube Webmail**: Unpatched instances at U.S. and Canadian academic institutions
- **AWS Cloud Environments**: Accounts with misconfigured AI workflows, excessive permissions, or compromised credentials
- **npm / PyPI Package Registries**: Developers and CI/CD pipelines consuming malicious Paysafe/Skrill/Neteller SDK packages
- **7-Zip Users**: Windows users downloading installer from unofficial or compromised sources
- **Driver Signature Enforcement Systems**: Windows machines that trust Microsoft-signed drivers (exploited via PoisonX BYOVD)

## Attack Vectors and Techniques

- **API Enumeration & Reconnaissance**: Systematic querying of GitHub API using dormant accounts to map organizational structure, repositories, and users without triggering anomaly detection
- **Device Code Phishing**: Abuse of OAuth 2.0 device authorization grant (RFC 8628) to trick users into authorizing attacker-controlled applications on legitimate Microsoft endpoints
- **Adversary-in-the-Middle (AiTM) Phishing**: Reverse proxy phishing kits that capture credentials and session cookies in real-time, bypassing traditional MFA
- **Voice Phishing (Vishing)**: Telephone-based social engineering to manipulate victims into approving MFA prompts, revealing credentials, or executing commands
- **MFA Fatigue / Abuse**: Repeated push notifications or exploitation of MFA recovery mechanisms to wear down victim resistance
- **Bring Your Own Vulnerable Driver (BYOVD)**: Loading a legitimate but vulnerable (or malicious but signed) kernel driver to execute code at kernel privilege and disable security tools
- **AI-Assisted Lure Generation**: Use of large language models to craft highly personalized, context-aware phishing content at scale
- **Supply Chain Compromise (Typosquatting/Brandjacking)**: Publishing malicious packages to public registries under names mimicking legitimate SDKs
- **Trojanized Legitimate Software**: Repackaging popular utilities (7-Zip) with hidden payloads distributed via SEO poisoning or fake download sites
- **Cloud Identity & Configuration Chaining**: Linking stolen credentials, excessive IAM permissions, and vulnerable AI/ML workload configurations for rapid lateral movement
- **Kernel Driver Signature Abuse**: Leveraging Microsoft's driver signing process to load malicious code (PoisonX) with kernel privileges on locked-down systems

## Threat Actor Activities

- **Helix (Data Extortion Group)**: Newly emerged operator focusing on identity-based intrusion against SharePoint. Combines vishing, device code phishing, and MFA bypass for initial access, followed by data exfiltration and extortion. Targets organizations with Microsoft 365/SharePoint deployments.
- **Lurking Lizard (Residential Proxy Operator)**: Runs a commercialized malicious proxy service. Distributes trojanized 7-Zip installers via fake download sites to build a residential IP pool sold to other threat actors for anonymizing credential stuffing, scraping, and fraud.
- **GodDamn Ransomware Operators**: Ransomware affiliate or independent group deploying GodDamn payload with PoisonX BYOVD for defense evasion. Actively targeting U.S. companies across sectors. Leverages Microsoft-signed driver for kernel-level security tool termination.
- **China-Linked Threat Cluster (Roundcube Exploitation)**: State-nexus actor targeting academic research institutions in the U.S. and Canada via vulnerable Roundcube webmail servers. Objectives align with intellectual property theft and long-term espionage access.
- **Forg365 Operators (PhaaS Providers)**: Service-oriented threat actors selling Microsoft 365 phishing infrastructure. Platform integrates AiTM, device code flows, and AI-generated lures. Lowers barrier to entry for credential harvesting campaigns.
- **GigaWiper Developers/Operators**: Likely nation-state or destructive-focused actor given the wiper capability. Modular design suggests intent for targeted destructive operations rather than broad ransomware profit.
- **Multiple Overlapping GitHub Enumeration Campaigns**: Unattributed but coordinated reconnaissance activity across numerous corporate GitHub organizations. Likely preliminary phase for supply chain, credential theft, or targeted intrusion operations.
- **Lone AWS Attacker**: Single operator demonstrating high competence in AI-augmented cloud intrusion. Chained identity, configuration, and AI workload weaknesses for rapid compromise and extortion.

## Source Attribution

- **Dormant GitHub Accounts Help Attackers Blend In While Mapping Corporate Orgs**: The Hacker News - https://thehackernews.com/2026/07/dormant-github-accounts-help-attackers.html
- **New GigaWiper Windows Backdoor Bundles Disk Wiping, Fake Ransomware, and Spyware**: The Hacker News - https://thehackernews.com/2026/07/new-gigawiper-windows-backdoor-bundles.html
- **New Helix vishing group emerges in SharePoint data theft attacks**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/new-helix-vishing-group-emerges-in-sharepoint-data-theft-attacks/
- **Microsoft expects more Windows security updates from AI-discovered flaws**: Bleeping Computer - https://www.bleepingcomputer.com/news/microsoft/microsoft-expects-more-windows-security-updates-from-ai-discovered-flaws/
- **npm 12 Disables Install Scripts by Default to Reduce Supply Chain Risk**: The Hacker News - https://thehackernews.com/2026/07/npm-12-disables-install-scripts-by.html
- **ThreatsDay: Cloud Bucket Hijacking, Windows LPE Chain, Global Fraud Bust + 17 More Stories**: The Hacker News - https://thehackernews.com/2026/07/threatsday-cloud-bucket-hijacking.html
- **New Forg365 phishing platform uses AI to target Microsoft 365 accounts**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/new-forg365-phishing-platform-uses-ai-to-target-microsoft-365-accounts/
- **As Global Conflicts Go Digital, Businesses Need Wartime Gameplans**: Dark Reading - https://www.darkreading.com/cybersecurity-operations/businesses-wartime-cybersecurity-gameplans
- **The Hidden Security Risks of Reduced Summer IT Coverage**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/the-hidden-security-risks-of-reduced-summer-it-coverage/
- **AI Gateways Offer Attackers the Keys to the Kingdom**: Dark Reading - https://www.darkreading.com/cyber-risk/ai-gateways-keys-kingdom
- **AI Attacks Move in Minutes. Join This Webinar on Building a Defense That Keeps Up**: The Hacker News - https://thehackernews.com/2026/07/ai-attacks-move-in-minutes-join-this.html
- **Microsoft to retire the OWA Light client in Exchange Server**: Bleeping Computer - https://www.bleepingcomputer.com/news/microsoft/microsoft-announces-owa-light-retirement-in-exchange-server/
- **Summer of Clearinghouses**: The Hacker News - https://thehackernews.com/2026/07/summer-of-clearinghouses.html
- **GodDamn Ransomware Uses PoisonX Driver to Disable Endpoint Defenses**: The Hacker News - https://thehackernews.com/2026/07/goddamn-ransomware-uses-poisonx-driver.html
- **'GodDamn' Ransomware Uses BYOVD to Smite US Companies**: Dark Reading - https://www.darkreading.com/cyberattacks-data-breaches/goddamn-ransomware-byovd-smite-companies
- **Police arrests 5,800 suspects in global anti-fraud crackdown**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/police-arrests-5-800-suspects-in-global-anti-fraud-crackdown/
- **Microsoft Patches RoguePlanet Defender Flaw That Can Grant SYSTEM Privileges**: The Hacker News - https://thehackernews.com/2026/07/microsoft-patches-rogueplanet-defender.html
- **European Organizations Have a Collaboration Security Confidence Gap**: Dark Reading - https://www.darkreading.com/cybersecurity-operations/european-organizations-collaboration-security-confidence-gap
- **AssuranceAmerica data breach exposes records of 6.9 million drivers**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/assuranceamerica-data-breach-exposes-records-of-69-million-drivers/
- **Meta's New AI Image Tool Lets Others Use Your Public Instagram Photos in AI Images**: The Hacker News - https://thehackernews.com/2026/07/metas-new-ai-image-tool-lets-others-use.html
- **Microsoft patches RoguePlanet Defender zero-day vulnerability**: Bleeping Computer - https://www.bleepingcomputer.com/news/microsoft/microsoft-patches-rogueplanet-defender-zero-day-vulnerability/
- **Top AI Agents Built to Catch Malicious Code Can Be Tricked Into Running It**: The Hacker News - https://thehackernews.com/2026/07/friendly-fire-ai-agents-built-to-catch.html
- **GhostApproval Symlink Flaws Could Let Malicious Repos Run Code in AI Coding Agents**: The Hacker News - https://thehackernews.com/2026/07/ghostapproval-symlink-flaws-could-let.html
- **Fake 7-Zip Installers Turn Devices Into Residential Proxy Nodes**: The Hacker News - https://thehackernews.com/2026/07/fake-7-zip-installers-turn-devices-into.html
- **Mexico's New Cyber Plan Faces Its First Real Test**: Dark Reading - https://www.darkreading.com/cyber-risk/mexicos-cyber-plan-first-real-test
- **Mount Royal University confirms breach as hackers claim attack**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/mount-royal-university-confirms-breach-as-hackers-claim-attack/
- **Lone Attacker Uses AI to Breach AWS Cloud Environment in 72 Hours**: Dark Reading - https://www.darkreading.com/cloud-security/lone-attacker-ai-breach-aws-cloud-environment
- **Fake Paysafe, Skrill SDKs on NPM and PyPi steal credentials**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/fake-paysafe-skrill-sdks-on-npm-and-pypi-steal-credentials/
- **Hackers exploit Roundcube flaw to spy on academic researchers**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/hackers-exploit-roundcube-flaw-to-spy-on-academic-researchers/
- **AI Coding Agents Found Triggering Endpoint Security Rules Built to Catch Attackers**: The Hacker News - https://thehackernews.com/2026/07/ai-coding-agents-found-triggering.html
