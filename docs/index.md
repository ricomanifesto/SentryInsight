# Exploitation Report

## Executive Summary

A diverse and accelerating wave of exploitation activity spans malvertising, supply chain flaws, identity attacks, and AI-assisted post-exploitation. The most technically novel campaign, tracked as SourTrade, abandons traditional payload delivery entirely: malicious JavaScript served through fake Solana, Luno, and TradingView pages instructs the victim's browser to assemble a Windows executable in memory using the legitimate Bun runtime, evading static detection and network-based controls. Simultaneously, the Cl0p ransomware ecosystem (aka Chubby Scorpius, FIN11, Graceful Spider, Lace Tempest) is conducting unauthenticated RCE attacks against internet-exposed PTC Windchill and FlexPLM instances for data-theft extortion, while North Korean BlueNoroff operators deploy a ClickFix-style phishing kit on typosquatted Zoom and Microsoft Teams domains that profiles cryptocurrency wallets before delivering malware.

Critical infrastructure flaws are under active exploitation or have public weaponization. Fastjson 1.x, Alibaba's widely used Java JSON library, is being targeted in Spring Boot applications with no vendor patch available. A GitLab RCE (patched June 10) gained a public PoC on July 24, enabling authenticated users to execute commands as the `git` user on self-managed 18.11.3+ instances. The Certighost exploit, published July 24, allows low-privileged Active Directory users to obtain a Domain Controller certificate and authenticate as the DC. Microsoft addressed a default Azure Automation configuration and chained code flaws enabling cross-tenant identity takeover, while researchers demonstrated crafted SVGs achieving SYSTEM/root RCE on Bing image-processing workers. In a notable AI-enabled intrusion, a threat actor ran the open-source Hermes agent in unattended "YOLO" mode to automate post-exploitation against Thailand's Ministry of Finance.

## Active Exploitation Details

### SourTrade Malvertising Campaign (Browser-Based Malware Assembly)
- **Description**: A malvertising operation dubbed SourTrade serves malicious JavaScript through fake Solana, Luno, and TradingView webpages. Instead of delivering a complete malicious executable, the script instructs the victim's browser to download benign-appearing pieces and assemble a Windows executable directly in memory using the legitimate Bun JavaScript runtime as its foundation.
- **Impact**: Attackers achieve fileless malware delivery that bypass of network and endpoint controls; the final executable never touches disk in its complete form, evading signature-based AV, sandbox analysis of downloaded files, and proxy inspection. Victims are infected simply by visiting a compromised ad landing page.
- **Status**: Actively exploited in a massive campaign observed across multiple ad networks. No patch applicable—this is an abuse of legitimate browser and runtime capabilities. Mitigation requires script-blocking, ad-blocking, and behavioral EDR that monitors in-memory assembly and Bun execution.

### Fastjson 1.x Remote Code Execution
- **Description**: A critical deserialization flaw in Fastjson 1.x, Alibaba's JSON library for Java, allows unauthenticated attackers to send a malicious JSON request that executes arbitrary code in affected Spring Boot applications.
- **Impact**: Full remote code execution in the application context, leading to server compromise, data exfiltration, and lateral movement. Widely deployed in enterprise Java ecosystems.
- **Status**: Actively exploited in the wild per ThreatBook and Imperva. No official patch has been released for the 1.x branch; users are urged to upgrade to Fastjson 2.x or apply mitigations such as `autoType` deny-lists and WAF rules.

### GitLab Authenticated RCE (Patched June 10, PoC Published July 24)
- **Description**: A vulnerability in GitLab's self-managed editions (affecting 18.11.3 and later) allows authenticated users to execute arbitrary commands as the `git` system user.
- **Impact**: Attackers with any valid account—including low-privilege users—can run commands on the underlying host, potentially accessing repositories, configuration secrets, and the GitLab database, and pivoting to the host OS.
- **Status**: Patched by GitLab on June 10. Working exploit code published by depthfirst researchers on July 24 increases urgency for patching any remaining unpatched instances.

### Cl0p/Clop Unauthenticated RCE in PTC Windchill and FlexPLM
- **Description**: Affiliates of the Cl0p ransomware operation are exploiting flaws in internet-exposed PTC Windchill and FlexPLM deployments to achieve unauthenticated remote code execution, using the access for data-theft extortion rather than encryption.
- **Impact**: Theft of proprietary product lifecycle data, intellectual property, and sensitive engineering documents from manufacturing and engineering firms. Extortion pressure without ransomware deployment complicates detection and response.
- **Status**: Active exploitation campaign. PTC has released security advisories and patches; organizations with internet-accessible Windchill/FlexPLM instances should assume compromise and apply updates immediately.

### BlueNoroff ClickFix-Style Phishing Kit (Crypto Wallet Profiling)
- **Description**: North Korean threat actors (BlueNoroff) operate a phishing kit hosted on typosquatted Zoom and Microsoft Teams domains. The kit uses ClickFix-style social engineering—presenting fake error dialogs that trick users into running PowerShell commands—while first profiling the victim's browser for cryptocurrency wallet extensions (MetaMask, Phantom, etc.) before delivering tailored malware.
- **Impact**: Credential theft, cryptocurrency wallet drainage, and malware implantation targeted at crypto holders and Web3 professionals. The wallet profiling allows attackers to prioritize high-value targets and customize payloads.
- **Status**: Active campaign. No software vulnerability; mitigation relies on user training, domain monitoring, and blocking known typosquat infrastructure.

### Certighost Active Directory Privilege Escalation
- **Description**: The Certighost exploit enables a low-privileged Active Directory user to request and obtain a certificate for a Domain Controller machine account, then authenticate as that DC using Kerberos (PKINIT), effectively achieving domain compromise.
- **Impact**: Full domain administrator equivalence—attackers can dump credentials, create persistence, and compromise all domain-joined systems.
- **Status**: Working exploit published July 24 by researchers H0j3n and Aniq Fakhrul. Mitigation requires restricting certificate templates (ESC1/ESC3 misconfigurations), enabling `EnforceStrongKeyProtection`, and monitoring for anomalous certificate requests.

### Hotel Wi-Fi DNS Hijacking for Microsoft 365 Credential Theft
- **Description**: Attackers compromise hotel and conference center Wi-Fi infrastructure to modify DHCP/DNS settings, redirecting guests to phishing pages that mimic Microsoft 365 login portals.
- **Impact**: Harvest of corporate Microsoft 365 credentials from traveling employees and conference attendees, enabling business email compromise, data access, and further phishing.
- **Status**: Ongoing campaign observed at multiple venues. No CVE—this is infrastructure compromise and network manipulation. Mitigation: enforce DNS-over-HTTPS, use FIDO2/MFA, and verify TLS certificates before entering credentials.

### Hermes AI Agent Unattended Post-Exploitation (Thai Finance Ministry)
- **Description**: A threat actor deployed the open-source Hermes AI agent on a rented server, disabled its safety confirmation prompts ("YOLO mode"), and directed it to automate post-exploitation activity against Thailand's Ministry of Finance infrastructure.
- **Impact**: Automated, scalable post-exploitation including enumeration, lateral movement, and data collection without continuous operator attention. Demonstrates dual-use AI tooling lowering the barrier for sustained intrusions.
- **Status**: Incident confirmed; attribution unknown. Highlights need for AI agent monitoring, execution policy controls, and anomaly detection on administrative tooling.

### Bing Images SVG Remote Code Execution (SYSTEM/root)
- **Description**: Researchers from XBOW demonstrated that a crafted SVG submitted to Bing's image search endpoint achieves command execution as `NT AUTHORITY\SYSTEM` on Windows image-processing workers and as `root` on Linux workers in the same fleet.
- **Impact**: Potential compromise of Microsoft's internal image-processing pipeline, access to uploaded images, and pivot to adjacent cloud infrastructure.
- **Status**: Reported to Microsoft; no public exploit code released. Microsoft has not disclosed a CVE or patch timeline in available reporting.

### ChatGPT AgentForger Workspace Agent Deployment Flaw
- **Description**: A critical vulnerability in OpenAI's ChatGPT Workspace Agents feature allows a single phishing link to stealthily build, authorize, and deploy a rogue autonomous agent into the victim's workspace.
- **Impact**: Persistent, AI-driven access to the victim's ChatGPT context, files, and connected tools/plugins. The agent can exfiltrate data, perform actions via plugins, and maintain long-term presence.
- **Status**: Disclosed by researchers; OpenAI remediation status not specified in available reporting. No CVE disclosed.

### Azure Automation Cross-Tenant Identity Takeover (Default Configuration)
- **Description**: A public-by-default Azure Automation setting combined with a chain of code flaws allowed attackers to seize another tenant's managed identity and access their data, credentials, and resources across the Azure control plane.
- **Impact**: Full cross-tenant compromise in multi-tenant environments—attackers could read secrets, manipulate automation runbooks, and escalate to subscription-level access.
- **Status**: Microsoft has addressed the default configuration and underlying flaws. Organizations should audit Automation account permissions and identity assignments.

### Golden Chickens MaaS Expansion (Four New Malware Families)
- **Description**: The Golden Chickens malware-as-a-service operators have resurfaced with four new malware families and modular implants, expanding their MaaS offerings to affiliates.
- **Impact**: Diversified payload options for criminal affiliates—increased evasion, new data theft capabilities, and flexible deployment chains. Indicates sustained investment in the ecosystem.
- **Status**: Active development and distribution. No specific vulnerability exploited; this is offensive tooling proliferation.

### NodeBB Eight High-Severity Flaws (AI-Discovered, Patched)
- **Description**: Aikido Security's AI pentest agents discovered eight high-severity vulnerabilities in NodeBB forum software in a six-hour run, exposing admin access and private chats. Exploit code was published alongside patches.
- **Impact**: Unauthenticated/admin bypass, private message disclosure, potential RCE depending on chaining. Affects all unpatched NodeBB instances.
- **Status**: Patched by NodeBB maintainers on the Wednesday of the disclosure week. Administrators should update immediately.

## Affected Systems and Products

- **Fastjson 1.x (Alibaba JSON library for Java)**: All 1.x versions in Spring Boot applications; no patched 1.x release available—migration to 2.x required.
- **GitLab Self-Managed**: Versions 18.11.3 and later prior to June 10 patch; patched versions available in 17.x/16.x maintenance streams.
- **PTC Windchill & FlexPLM**: Internet-exposed instances; specific vulnerable versions detailed in PTC security advisories (not enumerated in source articles).
- **Microsoft Azure Automation**: Tenants with default public configuration on Automation accounts; fixed by Microsoft platform update.
- **Bing Image Search Processing Pipeline**: Internal Microsoft Windows and Linux image-processing workers; no customer-facing version.
- **OpenAI ChatGPT Workspace Agents**: Feature-level vulnerability; fixed by OpenAI deployment update.
- **Active Directory Certificate Services**: Environments with vulnerable certificate templates (ESC1/ESC3) enabling Certighost; all supported Windows Server versions.
- **NodeBB Forum Software**: All versions prior to the July 2026 security release; eight distinct high-severity flaws.
- **Hotel/Conference Wi-Fi Infrastructure**: DHCP/DNS configuration on guest networks; vendor-agnostic.
- **Hermes AI Agent**: Open-source AI assistant framework; dual-use tool, not a vulnerability in the agent itself.
- **BlueNoroff Phishing Infrastructure**: Typosquatted domains mimicking `zoom.us` and `teams.microsoft.com`; no software product affected.

## Attack Vectors and Techniques

- **Browser-Based In-Memory Malware Assembly (SourTrade)**: Malicious JavaScript fetches encoded payload fragments, decodes them in the browser, and uses the Bun runtime's `File`/`Blob` APIs and `child_process`/`exec` equivalents to write and execute a PE binary entirely in memory—no complete malicious file ever transits the network or touches disk.
- **ClickFix Social Engineering with Wallet Profiling (BlueNoroff)**: Fake browser error dialogs (e.g., "Chrome update failed") instruct victims to open PowerShell and paste a command; the landing page first enumerates `window.ethereum`, `window.solana`, and other wallet provider objects to fingerprint crypto users before serving the tailored PowerShell payload.
- **Unauthenticated Deserialization RCE (Fastjson)**: Malicious JSON with `@type` gadget chains triggers arbitrary class instantiation and method invocation during parsing, achieving RCE without authentication in Spring Boot endpoints that accept JSON bodies.
- **Authenticated Command Injection (GitLab)**: Exploitation requires a valid user session; the flaw allows injection into a code path that executes as the `git` OS user, likely via unsanitized input in a repository operation or webhook handler.
- **Certificate Template Misconfiguration Abuse (Certighost)**: Low-privileged user requests a certificate from a vulnerable template (e.g., `User` template with `Enroll` rights for `Domain Controllers` or `Computer` template with `CT_FLAG_ENROLLEE_SUPPLIES_SUBJECT`), receives a DC-cert, and uses PKINIT for `krbtgt`/DC impersonation.
- **DHCP/DNS Poisoning on Guest Networks (Hotel Wi-Fi)**: Attackers with physical or remote access to network gear push malicious DNS servers via DHCP options or compromise the router's DNS forwarder, redirecting `login.microsoftonline.com` and related domains to phishing clones.
- **AI Agent Unattended Automation (Hermes/YOLO Mode)**: Operator disables confirmation prompts, provides high-level objectives ("enumerate domain," "find finance data"), and the agent autonomously chains CLI tools, scripts, and APIs to perform post-exploitation tasks.
- **SVG/XML Processing RCE (Bing Images)**: Crafted SVG leverages server-side rendering library flaws (likely `librsvg`, `ImageMagick`, or similar) to achieve code execution during thumbnail generation or metadata extraction.
- **Cross-Tenant Identity Confusion (Azure Automation)**: Default public exposure of Automation account identities combined with insufficient tenant isolation in token exchange or role assignment logic allows a malicious tenant to assume another's managed identity.
- **Credential Stuffing (Chick-fil-A)**: Automated login attempts using credentials from prior breaches against the Chick-fil-A website and mobile app (June 17–19, 2026), compromising 13,000+ accounts.
- **Data Leak Extortion for Sextortion (ShinyHunters)**: Breached email databases from ShinyHunters leaks used to send mass sextortion emails demanding $2,000 BTC; no technical exploit—pure social engineering at scale.
- **AI Hallucination Package/Domain Squatting (Slopsquatting/HalluSquatting)**: Attackers register package names or domains hallucinated by AI coding assistants; developers who copy AI-suggested imports/installs pull attacker-controlled code.

## Threat Actor Activities

- **Cl0p / Chubby Scorpius / FIN11 / Graceful Spider / Lace Tempest**: Operating as a ransomware/extortion ecosystem with affiliates conducting unauthenticated RCE against PTC Windchill/FlexPLM for data theft. Shift from encryption to pure extortion accelerates operations and reduces forensic footprint.
- **BlueNoroff (North Korea / Lazarus Subgroup)**: Running ClickFix-style phishing kits on typosquatted Zoom/Teams domains with integrated cryptocurrency wallet profiling. Targets Web3, DeFi, and crypto-native organizations for financial gain supporting state objectives.
- **Golden Chickens (Maas Operators / Venom Spider)**: Resurfaced with four new malware families and modular implants, indicating active MaaS development and affiliate recruitment. Historically provides loaders (More_eggs, TerraLoader) to FIN6, Cobalt Spider, and others.
- **ShinyHunters (Extortion Group / Data Broker)**: Leaked breach databases fueling downstream sextortion campaigns ($2,000 BTC demands). Operates as a data broker; breaches attributed to them include major retail, telecom, and tech firms.
- **Depthfirst (Researchers)**: Published working GitLab RCE PoC on July 24, six weeks after patch. Responsible disclosure timeline observed; PoC availability raises exploitation risk for lagging patchers.
- **H0j3n & Aniq Fakhrul (Researchers)**: Published Certighost exploit on July 24 demonstrating AD CS privilege escalation. Technique known in offensive community (ESC1/ESC3); public weaponization increases urgency for template hardening.
- **XBOW (Researchers)**: Demonstrated Bing Images SVG RCE achieving SYSTEM/root on Microsoft infrastructure. No public exploit release; coordinated disclosure presumed.
- **Aikido Security (AI Security Vendor)**: AI pentest agents discovered eight NodeBB flaws in six hours; published exploits alongside patches. Demonstrates AI-accelerated vulnerability discovery entering mainstream.
- **Unknown / Unattributed Actor (Thai Finance Ministry)**: Deployed Hermes AI agent in YOLO mode for automated post-exploitation. Sophistication suggests capable operator; use of open-source AI tooling lowers attribution confidence.
- **Unknown / Unattributed Actors (Hotel Wi-Fi)**: Compromising hospitality network infrastructure for Microsoft 365 credential harvesting. Likely financially motivated; infrastructure compromise suggests either insider access or vulnerable network management interfaces.
- **DevMan RaaS Operators**: Maintaining a dedicated web portal for affiliate payload building, victim management, and payout tracking. Professionalized RaaS operations with centralized tooling.

## Source Attribution

- **Malvertising Sends Malware in Pieces, Then Makes the Browser Build the Executable**: The Hacker News - https://thehackernews.com/2026/07/malvertising-sends-malware-in-pieces.html
- **Malicious sites use JavaScript to build malware in browser memory**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/malicious-sites-use-javascript-to-build-malware-in-browser-memory/
- **ShinyHunters data leaks fuel $2,000 sextortion email scam**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/shinyhunters-data-leaks-fuel-2-000-sextortion-email-scam/
- **Fastjson 1.x RCE Vulnerability Targeted in Attacks With No Patched Available**: The Hacker News - https://thehackernews.com/2026/07/fastjson-1x-rce-vulnerability-targeted.html
- **Researcher Publishes GitLab RCE PoC Letting Authenticated Users Run Commands as Git**: The Hacker News - https://thehackernews.com/2026/07/researcher-publishes-gitlab-rce-poc.html
- **CTM360 Research Reveals How Insurance Phishing Has Evolved Into Real-Time Account Hijacking**: The Hacker News - https://thehackernews.com/2026/07/ctm360-research-reveals-how-insurance.html
- **Cl0p Affiliates Target Internet-Exposed PTC Windchill and FlexPLM with Unauthenticated RCE**: The Hacker News - https://thehackernews.com/2026/07/cl0p-affiliates-target-internet-exposed.html
- **DevMan RaaS Portal Centralizes Payload Builds, Victim Management, and Affiliate Payouts**: The Hacker News - https://thehackernews.com/2026/07/devman-raas-portal-centralizes-payload.html
- **OpenAI confirms ChatGPT is down worldwide**: Bleeping Computer - https://www.bleepingcomputer.com/news/artificial-intelligence/openai-confirms-chatgpt-is-down-worldwide/
- **CISOs vs. Boards: Myth or Misunderstanding?**: Dark Reading - https://www.darkreading.com/cybersecurity-operations/cisos-vs-boards-myth-or-misunderstanding-
- **OnTrac notifies customers of data breach after network hack**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/ontrac-notifies-customers-of-data-breach-after-network-hack/
- **Escape Artists: 'Incorrigible' AI Models Resist Rehabilitation**: Dark Reading - https://www.darkreading.com/cybersecurity-operations/incorrigible-ai-models-resist-rehabilitation
- **Hermes AI agent used to automate attack on Thai Finance Ministry**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/hermes-ai-agent-used-to-automate-attack-on-thai-finance-ministry/
- **Hackers hijack hotel Wi-Fi DNS to steal Microsoft 365 accounts**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/hackers-hijack-hotel-wi-fi-dns-to-steal-microsoft-365-accounts/
- **Microsoft blames massive Microsoft 365 outage on maintenance bug**: Bleeping Computer - https://www.bleepingcomputer.com/news/microsoft/microsoft-blames-massive-microsoft-365-outage-on-maintenance-bug/
- **BlueNoroff Zoom Phishing Kit Profiles Crypto Wallets Before Malware Delivery**: The Hacker News - https://thehackernews.com/2026/07/bluenoroff-zoom-phishing-kit-profiles.html
- **Certighost Exploit Lets Low-Privileged Active Directory Users Impersonate a Domain Controller**: The Hacker News - https://thehackernews.com/2026/07/certighost-exploit-lets-low-privileged.html
- **Chick-fil-A data breach affects more than 13,000 customers**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/chick-fil-a-data-breach-affects-more-than-13-000-customers/
- **Slopsquatting, Phantom Domains, and HalluSquatting Are the Same AI Attack**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/slopsquatting-phantom-domains-and-hallusquatting-are-the-same-ai-attack/
- **Vatican's Official Prayer App Leaks 700K+ Global Users' PII**: Dark Reading - https://www.darkreading.com/vulnerabilities-threats/vatican-official-prayer-app-leaks-700k-pii
- **Europol flags 4,340 URLs for removal in 'The Com' crackdown**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/europol-flags-4-340-urls-for-removal-in-the-com-crackdown/
- **Default Azure Automation Setting Enables Cross-Tenant Identity Takeover**: Dark Reading - https://www.darkreading.com/cloud-security/default-azure-automation-setting-cross-tenant-identity-takeover
- **ChatGPT AgentForger Flaw Could Deploy Rogue Workspace Agents via a Phishing Link**: The Hacker News - https://thehackernews.com/2026/07/chatgpt-agentforger-flaw-could-deploy.html
- **Bing Images Flaws Let Crafted SVGs Run Commands as SYSTEM on Microsoft's Servers**: The Hacker News - https://thehackernews.com/2026/07/bing-images-flaws-let-crafted-svgs-run.html
- **Seeing AI Agents Is Not Enough. Security Teams Must Enforce What They Can Do**: The Hacker News - https://thehackernews.com/2026/07/seeing-ai-agents-is-not-enough-security.html
- **Man gets six years for hacking 750 women's Snapchat accounts**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/man-gets-six-years-for-hacking-750-womens-snapchat-accounts/
- **Hacker Runs Hermes AI Agent Unattended for Post-Exploitation at Thai Finance Ministry**: The Hacker News - https://thehackernews.com/2026/07/hacker-runs-hermes-ai-agent-unattended.html
- **Golden Chickens Resurfaces With Four New Malware Families and Modular Implants**: The Hacker News - https://thehackernews.com/2026/07/golden-chickens-resurfaces-with-four.html
- **NodeBB Patches Eight AI-Found Flaws Exposing Admin Access and Private Chats**: The Hacker News - https://thehackernews.com/2026/07/nodebb-patches-eight-ai-found-flaws.html
- **Clop ransomware targets Windchill, FlexPLM in data theft attacks**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/clop-ransomware-targets-windchill-flexplm-in-data-theft-attacks/
