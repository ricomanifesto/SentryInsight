# Exploitation Report

## Executive Summary

A new phishing-as-a-service platform called **Forg365** has emerged, combining adversary-in-the-middle (AiTM) techniques with device code authentication flows and AI-generated lures to target Microsoft 365 credentials at scale. Simultaneously, a China-linked threat cluster is actively exploiting vulnerable Roundcube webmail servers at universities across the United States and Canada to harvest credentials and deploy persistent backdoors. These campaigns demonstrate how attackers are modernizing credential theft through AI automation and targeting identity infrastructure directly.

Ransomware operators continue to weaponize legitimate system components for defense evasion. The **GodDamn** ransomware family employs a Microsoft-signed malicious kernel driver (PoisonX) in a bring-your-own-vulnerable-driver (BYOVD) strategy to kill endpoint security agents before encrypting US organizations. In parallel, the **Vidar** infostealer is hammering SMBs through malvertising campaigns that lure victims with cracked software, delivering a dual payload of credential theft and cryptomining. Supply chain attacks have also intensified, with typosquatted Paysafe and Skrill SDKs published to npm and PyPI to steal payment credentials from developers.

Microsoft has patched a critical zero-day vulnerability in Windows Defender tracked as **CVE-2026-50656** (RoguePlanet), which allowed local privilege escalation to SYSTEM. The flaw was publicly disclosed nearly a month before the fix arrived, creating a substantial window of exposure. Meanwhile, Ubiquiti has released updates for multiple critical flaws across its UniFi product line—Connect, Talk, Access, Protect, and OS—that could enable privilege escalation and arbitrary code execution. New attack research has also revealed fundamental weaknesses in AI coding assistants, including symlink-based repository compromises (GhostApproval) and hallucination-induced package installation (HalluSquatting), expanding the software supply chain attack surface.

## Active Exploitation Details

### RoguePlanet Windows Defender Zero-Day (CVE-2026-50656)
- **Description**: A privilege escalation vulnerability in Microsoft Defender (designated "RoguePlanet") that allows an authenticated local attacker to gain SYSTEM-level privileges on affected Windows systems. The flaw was publicly disclosed in June 2026, nearly a month before Microsoft released a patch.
- **Impact**: Attackers who achieve initial foothold on a system can escalate to SYSTEM, bypassing security controls, disabling defenses, and achieving full system compromise.
- **Status**: Actively exploited as a zero-day prior to patch release. Microsoft issued fixes in the July 2026 security updates, approximately one month after public disclosure. Organizations should verify deployment of the July 2026 Patch Tuesday updates.
- **CVE ID**: CVE-2026-50656

### GodDamn Ransomware BYOVD via PoisonX Driver
- **Description**: The GodDamn ransomware family utilizes a malicious kernel driver named PoisonX that was legitimately signed by Microsoft. This bring-your-own-vulnerable-driver (BYOVD) technique allows the ransomware to load the signed driver and exploit its functionality to terminate endpoint detection and response (EDR) processes and disable security software.
- **Impact**: Complete neutralization of endpoint defenses prior to encryption, enabling unimpeded ransomware deployment across US corporate targets. The Microsoft signature on the malicious driver complicates detection and blocking.
- **Status**: Actively deployed against US companies. Microsoft has not publicly revoked the driver signature as of the reporting period. Defenders should monitor for PoisonX driver loading events and implement driver block rules.
- **CVE ID**: No CVE assigned to the driver signing issue; exploitation leverages legitimate signing process abuse.

### Roundcube Webmail Exploitation by China-Linked Threat Actor
- **Description**: A China-nexus threat cluster is targeting vulnerable Roundcube webmail installations at academic institutions in the United States and Canada. The attackers exploit unpatched Roundcube servers to gain initial access, steal credentials, and deploy backdoor malware for persistent espionage access.
- **Impact**: Credential harvesting from university researchers and faculty, persistent network access via backdoors, and potential lateral movement into connected research networks. Academic intellectual property and sensitive communications are at risk.
- **Status**: Active exploitation campaign ongoing. Universities running outdated Roundcube versions are primary targets. No specific CVE referenced in available reporting; likely exploits known Roundcube vulnerabilities with available patches.
- **CVE ID**: Not specified in source articles.

### Forg365 Phishing-as-a-Service Platform
- **Description**: A new PhaaS offering called Forg365 specializes in Microsoft 365 credential theft by combining adversary-in-the-middle (AiTM) proxy techniques with device code authentication phishing. The platform uses AI to generate highly convincing lure content and automate campaign deployment at scale.
- **Impact**: Bypasses traditional multi-factor authentication by capturing session tokens (AiTM) or tricking users into completing device code flows on attacker-controlled infrastructure. Enables full account takeover of Microsoft 365 identities.
- **Status**: Actively operated and marketed as a service. No software vulnerability exploited—targets authentication protocol flows and human factors. Traditional email security controls are evaded through proxy-based techniques.
- **CVE ID**: Not applicable (no software vulnerability).

### Vidar Infostealer Malvertising Campaign
- **Description**: A financially motivated operation delivers Vidar infostealer via malvertising campaigns that promote cracked or pirated software. The malvertisements redirect victims to malicious payloads that deploy Vidar for credential harvesting, cryptocurrency wallet theft, and browser data exfiltration, alongside a cryptominer for secondary revenue.
- **Impact**: Compromise of small and medium business systems, theft of stored credentials, cookies, cryptocurrency wallets, and browser autofill data. Persistent cryptomining degrades system performance and increases cloud costs.
- **Status**: Active campaign targeting SMBs through search engine and web-based malvertising. No software vulnerability exploited—relies on social engineering and malicious advertising infrastructure.
- **CVE ID**: Not applicable.

### Fake Paysafe/Skrill SDK Supply Chain Attack
- **Description**: Threat actors published typosquatted malicious packages to the Node Package Manager (npm) and Python Package Index (PyPI) imitating legitimate Paysafe, Skrill, and Neteller SDKs. Developers who install these packages receive credential-stealing malware that targets payment application data.
- **Impact**: Compromise of developer environments and CI/CD pipelines, theft of payment platform credentials and API keys, potential downstream supply chain contamination if malicious packages are incorporated into published applications.
- **Status**: Active packages identified on both registries. Registry maintainers have been notified; removal timelines vary. No software vulnerability exploited—abuses package naming conventions and developer trust.
- **CVE ID**: Not applicable.

### Lurking Lizard Residential Proxy Botnet via Fake 7-Zip Installers
- **Description**: A threat actor dubbed "Lurking Lizard" distributes trojanized 7-Zip installers that enroll victim machines into a residential proxy network. The infrastructure operates as a commercial proxy service, selling access to compromised residential IP addresses for credential stuffing, scraping, and fraud.
- **Impact**: Victim devices become unwitting proxy exit nodes for malicious traffic, exposing owners to legal liability, bandwidth theft, and potential secondary malware deployment. The operation represents a full criminal business model around residential proxy monetization.
- **Status**: Active distribution via fake software download sites and search engine poisoning. No vulnerability exploited—relies on social engineering and brand impersonation.
- **CVE ID**: Not applicable.

### Entra Passkey Enrollment Vishing Campaign
- **Description**: Attackers conduct voice phishing (vishing) campaigns impersonating IT support or security teams, directing Microsoft 365 users to enroll a new Microsoft Entra passkey under attacker control. The social engineering bypasses technical controls by exploiting legitimate passkey enrollment workflows.
- **Impact**: Attacker-controlled passkey enrollment grants persistent, phishing-resistant authentication access to the victim's Microsoft 365 account, enabling data access, email compromise, and lateral movement.
- **Status**: Active targeting across multiple industry sectors. No software vulnerability exploited—targets identity enrollment processes and human trust.
- **CVE ID**: Not applicable.

### Ghost Phishing (EvilTokens Campaign)
- **Description**: A campaign dubbed "EvilTokens" employs a "ghost phishing" technique where malicious pages remain hidden/encrypted until the moment of interaction, evading static email security scanning. The technique targets businesses in the US and Europe with credential harvesting pages that decrypt only upon victim click.
- **Impact**: Bypasses traditional email gateway sandboxing and URL reputation checks. Credentials harvested from employees across targeted organizations.
- **Status**: Active campaign. No software vulnerability exploited—evades detection through novel delivery obfuscation.
- **CVE ID**: Not applicable.

### Ubiquiti UniFi Critical Vulnerabilities
- **Description**: Multiple critical security flaws affect Ubiquiti UniFi products including UniFi Connect, UniFi Talk, UniFi Access, UniFi Protect, and UniFi OS. The vulnerabilities can result in privilege escalation and arbitrary code execution on affected devices.
- **Impact**: Network infrastructure compromise, potential pivot to OT/physical access systems (UniFi Access/Protect), persistent foothold in network management plane.
- **Status**: Patches released by Ubiquiti. Exploitation status in wild not explicitly confirmed in source articles, but critical severity warrants immediate patching.
- **CVE ID**: Not specified in source articles.

### GhostApproval Symlink Vulnerabilities in AI Coding Assistants
- **Description**: Researchers at Wiz discovered symlink handling flaws (dubbed "GhostApproval") in six popular AI coding assistants. A malicious repository can exploit these flaws to trick the AI assistant into reading/writing arbitrary files outside the intended project scope when the developer approves a seemingly benign edit.
- **Impact**: Arbitrary file read/write on developer machines, potential SSH key theft, source code exfiltration, supply chain compromise via modified build artifacts, and persistent backdoor implantation.
- **Status**: Proof-of-concept demonstrated. Affected vendors notified. No confirmed wild exploitation reported, but high risk given widespread AI coding assistant adoption.
- **CVE ID**: Not specified in source articles.

### HalluSquatting Attack on AI Coding Assistants
- **Description**: AI coding assistants frequently hallucinate non-existent package names when asked to recommend or install dependencies. Attackers can register these hallucinated names on public registries (npm, PyPI) with malicious payloads, causing the AI to inadvertently install malware when developers follow its suggestions.
- **Impact**: Supply chain compromise via AI-hallucinated package names, botnet malware installation, credential theft, and persistent access to developer environments.
- **Status**: Theoretical attack with demonstrated feasibility. No confirmed wild exploitation, but the systemic nature of LLM hallucinations makes this a persistent emerging threat.
- **CVE ID**: Not applicable.

### AI-Assisted AWS Cloud Environment Breach
- **Description**: A lone attacker leveraged AI tooling to accelerate reconnaissance, credential theft, and cloud privilege escalation, achieving full compromise of a large Amazon customer's AWS environment within 72 hours. The attack chained AI workflows, cloud misconfigurations, and stolen credentials.
- **Impact**: Data exfiltration, extortion, potential ransomware deployment, and complete cloud infrastructure compromise. Demonstrates AI force-multiplier effect for cloud attacks.
- **Status**: Single confirmed incident. No specific vulnerability exploited—leverages AI to accelerate traditional cloud attack chains (credential theft, privilege escalation, data access).
- **CVE ID**: Not applicable.

## Affected Systems and Products

- **Microsoft Windows Defender**: Systems running unpatched Defender prior to July 2026 security updates (CVE-2026-50656)
- **Microsoft 365 / Entra ID**: Organizations targeted by Forg365 AiTM/device code phishing and Entra passkey enrollment vishing
- **Roundcube Webmail**: University deployments running vulnerable versions (specific versions not disclosed in sources)
- **Ubiquiti UniFi Product Line**: UniFi Connect, UniFi Talk, UniFi Access, UniFi Protect, and UniFi OS (critical flaws patched in recent updates)
- **AI Coding Assistants**: Six popular assistants affected by GhostApproval symlink flaws (specific products not named in source); all LLM-based coding agents susceptible to HalluSquatting
- **npm and PyPI Package Registries**: Developers installing Paysafe, Skrill, or Neteller SDKs from typosquatted package names
- **AWS Cloud Environments**: Accounts with credential exposure, excessive permissions, or cloud misconfigurations exploitable via AI-accelerated attack chains
- **Endpoint Systems**: Windows machines targeted by GodDamn ransomware (PoisonX driver), Vidar infostealer (malvertising), and Lurking Lizard proxy malware (fake 7-Zip)
- **Microsoft Exchange Server**: OWA Light client being retired (not an exploitation vector, but migration required)

## Attack Vectors and Techniques

- **Adversary-in-the-Middle (AiTM) Phishing**: Forg365 platform proxies legitimate Microsoft 365 login flows to capture session tokens and bypass MFA
- **Device Code Authentication Phishing**: Attackers initiate legitimate device code flows and trick users into completing authentication on attacker-controlled devices
- **AI-Generated Social Engineering**: Forg365 and service desk attacks use LLMs to create personalized, convincing lures at scale
- **Bring Your Own Vulnerable Driver (BYOVD)**: GodDamn ransomware loads Microsoft-signed PoisonX kernel driver to disable EDR/antivirus
- **Malvertising / SEO Poisoning**: Vidar infostealer and Lurking Lizard proxy malware delivered via malicious ads and fake software download sites
- **Typosquatting Supply Chain Attack**: Malicious npm/PyPI packages imitating Paysafe, Skrill, Neteller SDKs
- **Vishing (Voice Phishing)**: Entra passkey enrollment abuse via phone-based social engineering impersonating IT support
- **Ghost Phishing / Encrypted Payload Delivery**: EvilTokens campaign hides malicious pages until victim interaction to evade email security scanning
- **Roundcube Exploitation**: Unpatched webmail servers exploited for initial access and backdoor deployment at universities
- **Local Privilege Escalation**: CVE-2026-50656 (RoguePlanet) exploited for SYSTEM access on Windows endpoints
- **AI Hallucination Exploitation (HalluSquatting)**: Registering AI-hallucinated package names to hijack AI-assisted dependency installation
- **Symlink Path Traversal (GhostApproval)**: Malicious repositories exploit AI coding assistant symlink handling to escape project boundaries
- **AI-Accelerated Cloud Attack Chain**: Lone attacker uses AI tooling to compress 72-hour AWS breach timeline (recon → credential theft → privilege escalation → data access)
- **Residential Proxy Botnet Enrollment**: Trojanized installers (fake 7-Zip) silently enroll machines into commercial proxy networks

## Threat Actor Activities

- **Forg365 Operators**: Phishing-as-a-service providers running AiTM/device code platform with AI lure generation; targeting Microsoft 365 credentials across sectors
- **China-Linked Threat Cluster (Roundcube)**: Espionage-motivated actor exploiting university Roundcube servers in US/Canada; credential theft and backdoor deployment for persistent access
- **GodDamn Ransomware Group**: Financially motivated ransomware operation using BYOVD (PoisonX driver) to disable defenses; actively targeting US companies
- **Lurking Lizard**: Cybercriminal group operating end-to-end residential proxy business via trojanized 7-Zip installers; infrastructure supports credential stuffing, fraud, scraping
- **Vidar Malvertising Operators**: Financially motivated group delivering Vidar infostealer + cryptominer via cracked software lures; targeting SMBs broadly
- **Paysafe/Skrill Typosquatters**: Supply chain attackers publishing malicious packages to npm/PyPI; targeting developers and payment application users
- **Entra Passkey Vishing Group**: Voice phishing operators impersonating IT/security staff to trick users into enrolling attacker-controlled passkeys; multi-sector targeting
- **EvilTokens Campaign Actors**: Ghost phishing campaign targeting US/European businesses; novel encrypted payload delivery evading email security
- **Ubiquiti UniFi Vulnerability Researchers/Exploiters**: Critical flaws disclosed/patched; potential exploitation by infrastructure-targeting actors (no specific group attributed in sources)
- **Lone AI-Assisted Cloud Attacker**: Single operator demonstrating AI force multiplication for AWS compromise in 72 hours; extortion-motivated

## Source Attribution

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
- **Entra passkey enrollment vishing targets Microsoft 365 users**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/entra-passkey-enrollment-vishing-targets-microsoft-365-users/
- **Vidar Infostealer Hammers SMBs via Malvertising Campaign**: Dark Reading - https://www.darkreading.com/cyberattacks-data-breaches/vidar-infostealer-smb-malvertising-campaign
- **New HalluSquatting Attack Could Trick AI Coding Assistants Into Installing Botnet Malware**: The Hacker News - https://thehackernews.com/2026/07/new-hallusquatting-attack-could-trick.html
- **Ubiquiti Patches Critical UniFi Flaws Across Connect, Talk, Access, Protect, and OS**: The Hacker News - https://thehackernews.com/2026/07/ubiquiti-patches-critical-unifi-flaws.html
- **3 Ways AI Powers Service Desk Attacks and How to Prevent Them**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/3-ways-ai-powers-service-desk-attacks-and-how-to-prevent-them/
- **New Ghost Phishing Wave Is Breaking Traditional Email Security**: The Hacker News - https://thehackernews.com/2026/07/new-ghost-phishing-wave-is-breaking.html
