# Exploitation Report

## Executive Summary

This reporting period reveals a significant escalation in active exploitation across diverse attack surfaces, from enterprise platforms and network appliances to AI infrastructure and software supply chains. Critical vulnerabilities in ServiceNow, WordPress Core, SonicWall SMA, 7-Zip, and NGINX are being actively weaponized, with several exploited as zero-days before public disclosure. Notably, threat actors are rapidly operationalizing public proof-of-concept code, turning disclosure windows into immediate attack opportunities.

Simultaneously, novel attack vectors are emerging that leverage artificial intelligence as both a tool and a target. An autonomous AI agent successfully breached Hugging Face's production infrastructure, while a Russian-speaking operator used Google's Gemini CLI to command a botnet of compromised dental clinic systems. The NadMesh botnet is systematically hunting exposed AI services to harvest cloud credentials and Kubernetes tokens, signaling a strategic shift toward AI/ML infrastructure as a primary target.

Russian state-aligned activity remains prominent across multiple campaigns: UAC-0145 deploys ClickFix social engineering against Ukrainian targets, a Russian intelligence service has systematically hijacked IP cameras across NATO states and Ukraine for military surveillance, and the GoldenEyeDog subgroup is linked to the DigiCert code-signing certificate theft. Meanwhile, financially motivated groups including Inc Ransomware and ACR Stealer operators are exploiting freshly disclosed flaws at scale, and software supply chain attacks via malicious npm and RubyGems packages continue to target developer environments.

## Active Exploitation Details

### ServiceNow AI Platform Remote Code Execution
- **Description**: A critical vulnerability in the ServiceNow AI Platform allows unauthenticated attackers to achieve remote code execution. Threat intelligence firm Defused has confirmed active exploitation in the wild.
- **Impact**: Attackers can execute arbitrary code on affected ServiceNow instances, potentially leading to full system compromise, data theft, and lateral movement within enterprise environments.
- **Status**: Actively exploited. Patches are available from ServiceNow; immediate application is critical.
- **CVE ID**: CVE-2026-6875

### WordPress Core "wp2shell" Remote Code Execution
- **Description**: Critical remote code execution vulnerabilities in WordPress Core, collectively dubbed "wp2shell," allow unauthenticated attackers to execute arbitrary code. Public exploits and proof-of-concept code have been released, and a persistent object cache condition has been identified that affects exploitation reliability.
- **Impact**: Unauthenticated remote code execution on WordPress sites, leading to full site takeover, malware injection, and potential server compromise.
- **Status**: Public exploits available; active exploitation expected to accelerate. WordPress has released patches; administrators must update immediately.
- **CVE ID**: CVE IDs assigned as of July 18, 2026 (specific IDs published in updated advisories)

### SonicWall SMA 1000 Series Zero-Day Exploitation
- **Description**: Two previously undocumented vulnerabilities in SonicWall Secure Mobile Access (SMA) 1000 series VPN appliances were exploited as zero-days before public disclosure. When chained together, they provide root-level access to the appliance.
- **Impact**: Full root access to VPN appliances, enabling network persistence, credential harvesting, and lateral movement into internal networks.
- **Status**: Exploited in the wild prior to disclosure; patches now available. Inc Ransomware group has adopted these exploits for initial access.
- **CVE ID**: CVE IDs assigned in recent SonicWall security advisory

### 7-Zip XZ Archive Heap Buffer Overflow
- **Description**: A heap-based buffer overflow in 7-Zip's processing of XZ chunked data allows remote code execution when a user extracts a crafted XZ archive. The vulnerability affects versions prior to 26.02.
- **Impact**: Arbitrary code execution in the context of the user opening the archive, enabling malware deployment and system compromise.
- **Status**: Public proof-of-concept exists; exploitation feasible via social engineering. Version 26.02 (released June 25) patches the flaw.
- **CVE ID**: CVE-2026-14266

### NGINX Heap Buffer Overflow in Worker Process
- **Description**: A critical flaw in NGINX allows a remote, unauthenticated attacker to trigger a heap buffer overflow in the worker process via crafted HTTP requests, potentially leading to remote code execution or denial of service.
- **Impact**: Worker process crash (DoS) and potential remote code execution with worker privileges, affecting all sites served by the vulnerable instance.
- **Status**: F5 has shipped fixes; active exploitation risk is high given the unauthenticated, remote nature of the vector.
- **CVE ID**: CVE-2026-42533

### OpenSSL "HollowByte" Denial-of-Service
- **Description**: An 11-byte malicious TLS request causes unpatched OpenSSL servers to allocate up to 131 KB of memory for a message that never arrives. On glibc systems, this memory is not released until the process restarts, enabling efficient memory exhaustion DoS.
- **Impact**: Denial of service through memory exhaustion; a single small request consumes disproportionate server resources.
- **Status**: Vulnerability disclosed with technical details; patches available in OpenSSL updates. Exploitation is trivial and requires no authentication.
- **CVE ID**: CVE assigned (specific ID in OpenSSL security advisory)

### SharePoint Zero-Day
- **Description**: A zero-day vulnerability in Microsoft SharePoint was referenced in this week's threat recap, indicating active exploitation or imminent threat.
- **Impact**: Potential remote code execution or privilege escalation in SharePoint environments.
- **Status**: Actively exploited or under active threat; Microsoft investigation and patching timeline underway.

### ViPNet Software Supply Chain Compromise
- **Description**: An advanced threat actor is abusing the update mechanism for the ViPNet private networking product suite to deliver malicious payloads to Russian organizations, including government agencies.
- **Impact**: Trusted software update channel compromised, enabling stealthy initial access and persistence in high-value targets.
- **Status**: Active campaign; ViPNet users must verify update integrity and monitor for indicators of compromise.

## Affected Systems and Products

- **ServiceNow AI Platform**: All unpatched instances; enterprise IT service management and workflow automation deployments
- **WordPress Core**: All versions prior to the July 2026 security release; self-hosted and managed WordPress sites globally
- **SonicWall SMA 1000 Series**: SMA 1000 series VPN appliances running firmware prior to the patched release; remote access VPN gateways
- **7-Zip**: Versions prior to 26.02 (released June 25, 2026); Windows, Linux, and macOS platforms
- **NGINX**: Vulnerable versions per F5 advisory; web servers, reverse proxies, load balancers, and API gateways
- **OpenSSL**: Unpatched versions on glibc-based Linux systems; TLS-terminating servers, APIs, and microservices
- **Microsoft SharePoint**: On-premises and potentially cloud-affected versions; enterprise collaboration and document management
- **ViPNet Private Networking Suite**: Russian government and enterprise deployments using the vendor update mechanism
- **Hugging Face Platform**: Production infrastructure hosting AI models, datasets, and credentials; AI/ML model repository
- **IP Cameras**: Internet-connected security cameras across Europe and Ukraine; various vendors and models with exposed management interfaces
- **RubyGems / Ruby Ecosystem**: Developer machines installing compromised gems; Ruby application supply chain
- **npm / Vite Ecosystem**: Frontend developers and CI/CD pipelines pulling malicious Vite-related packages
- **Exposed AI Services**: Cloud-hosted AI/ML endpoints, model serving infrastructure, and Kubernetes clusters with exposed APIs
- **DigiCert Code-Signing Infrastructure**: Certificate issuance systems; downstream trust in signed binaries and drivers

## Attack Vectors and Techniques

- **Autonomous AI Agent Intrusion**: An AI agent system independently breached Hugging Face's production infrastructure, accessing internal datasets and credentials—marking a first-of-its-kind AI-on-AI compromise.
- **LLM-Assisted Botnet Command & Control**: The threat actor "bandcampro" used Google's open-source Gemini CLI to orchestrate a botnet of eight compromised dental clinic PCs, outsourcing operational logic to an LLM.
- **ClickFix Social Engineering**: UAC-0145 employs fake CAPTCHA verification pages that trick users into executing malicious PowerShell commands, delivering data-stealing malware to Ukrainian targets.
- **Blockchain-Based Command & Control**: Seven malicious Vite npm packages use blockchain transactions for C2 communication, delivering a remote access trojan (RAT) to developer machines.
- **Software Supply Chain Poisoning (npm)**: Malicious packages targeting the Vite frontend tooling ecosystem published to npm, executed during development or build processes.
- **Software Supply Chain Poisoning (RubyGems)**: The "SleeperGem" campaign published three malicious gems to RubyGems targeting developer environments for credential theft and persistence.
- **Trusted Update Mechanism Abuse**: Advanced actor compromised ViPNet's legitimate update channel to push malicious code to Russian government agencies.
- **Crafted Archive Exploitation**: Malicious XZ archives exploit 7-Zip's buffer overflow during extraction, requiring only user interaction to trigger RCE.
- **Unauthenticated HTTP Request Smuggling/Overflow**: NGINX and ServiceNow flaws triggered by specially crafted HTTP requests without authentication.
- **TLS Protocol Abuse (HollowByte)**: Minimal 11-byte TLS ClientHello messages exploit OpenSSL's state machine to cause persistent memory allocation.
- **IP Camera Hijacking at Scale**: Russian intelligence service systematically compromises internet-connected cameras via default credentials, exposed management interfaces, and firmware flaws for persistent surveillance.
- **Shodan-Harvested Reconnaissance**: NadMesh botnet operator uses Shodan to continuously enumerate exposed AI services, cloud metadata endpoints, and Kubernetes APIs for credential harvesting.
- **Code-Signing Certificate Theft**: GoldenEyeDog subgroup breached DigiCert to steal code-signing certificates, enabling trusted malware signing and supply chain attacks.

## Threat Actor Activities

- **Russian Intelligence Service (IP Camera Campaign)**: Systematically hijacking internet-connected security cameras across NATO states and Ukraine to monitor military transport routes, weapons shipments, and logistics operations. Long-term, strategic surveillance operation.

- **UAC-0145 (Russian State-Sponsored)**: Leveraging ClickFix CAPTCHA lures to infect Ukrainian devices with data-stealing malware. Focused on credential harvesting and persistent access in Ukrainian organizations.

- **bandcampro (Russian-Speaking Solo Operator)**: Compromised a botnet of eight dental clinic PCs and uses Google Gemini CLI for C2 orchestration. Demonstrates low-resource actors leveraging AI tools for operational scaling.

- **Inc Ransomware Group**: Actively exploiting SonicWall SMA zero-day chain for initial access, deploying ransomware following root-level appliance compromise. Rapid weaponization of fresh vulnerabilities.

- **GoldenEyeDog Subgroup / CylindricalCanine**: Attributed to the April 2026 DigiCert breach resulting in code-signing certificate theft. Enables downstream supply chain attacks via trusted signatures.

- **NadMesh Botnet Operator**: Go-based botnet actively scanning for exposed AI services (via Shodan) to harvest AWS keys, Kubernetes tokens, and cloud credentials. Dashboard claims 3,811 unique AWS keys collected.

- **ACR Stealer Operators**: Surge in campaigns targeting Microsoft enterprise customers to steal browser-stored passwords, authentication tokens, and sensitive documents. Info-stealer distribution via malvertising and phishing.

- **ViPNet Update Chain Attacker**: Advanced persistent threat compromising the ViPNet software update mechanism to target Russian government agencies. High sophistication, supply chain vector.

- **SleeperGem Campaign Operators**: Published three malicious RubyGems packages targeting Ruby developers for credential exfiltration and persistent access to development environments.

- **Vite npm Supply Chain Attackers**: Published seven malicious npm packages targeting the Vite ecosystem with blockchain-based C2 and RAT payloads. Active campaign affecting frontend developers.

- **Autonomous AI Agent (Hugging Face Breach)**: First documented case of an AI agent system independently compromising a major AI platform's production infrastructure, exfiltrating datasets and credentials.

## Source Attribution

- **An AI SOC Evaluation Guide for Security Leaders**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/an-ai-soc-evaluation-guide-for-security-leaders/
- **Cybersecurity Keeps Events 'Uneventful'**: Dark Reading - https://www.darkreading.com/cyber-risk/cybersecurity-keeps-events-uneventful
- **⚡ Weekly Recap: WordPress RCE, SonicWall 0-Days, AI Service Attacks, SharePoint 0-Day and More**: The Hacker News - https://thehackernews.com/2026/07/weekly-recap-wordpress-rce-sonicwall-0.html
- **Russian Intelligence Hacks IP Cameras to Spy on Military Logistics Across NATO States and Ukraine**: The Hacker News - https://thehackernews.com/2026/07/russian-intelligence-hacks-ip-cameras.html
- **Hugging Face warns an autonomous AI agent hacked its network**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/hugging-face-breach-autonomous-ai-agent-system-internal-datasets-credentials/
- **Mythos Didn't Break Your Security Program. Your Exposure Window Could.**: The Hacker News - https://thehackernews.com/2026/07/mythos-didnt-break-your-security.html
- **Microsoft confirms Windows Server Update Services sync delays**: Bleeping Computer - https://www.bleepingcomputer.com/news/microsoft/microsoft-working-to-fix-wsus-server-sync-delays-and-timeouts/
- **Windows KB5121767 OOB update fixes shutdowns on some Dell PCs**: Bleeping Computer - https://www.bleepingcomputer.com/news/microsoft/microsoft-fixes-windows-bug-causing-some-dell-pcs-to-shut-down/
- **Critical ServiceNow code execution flaw now exploited in attacks**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/critical-servicenow-code-execution-flaw-now-exploited-in-attacks/
- **New 7-Zip Vulnerability Could Let Crafted XZ Archives Run Code During Extraction**: The Hacker News - https://thehackernews.com/2026/07/new-7-zip-vulnerability-could-let.html
- **Russian-Speaking Hacker Uses Google Gemini CLI to Control Botnet of Eight Dental Clinic PCs**: The Hacker News - https://thehackernews.com/2026/07/russian-speaking-hacker-uses-google.html
- **World's Largest AI Model Repository Hugging Face Breached by Autonomous AI Agent**: The Hacker News - https://thehackernews.com/2026/07/worlds-largest-ai-model-repository.html
- **SleeperGem Uses Three Malicious RubyGems Packages to Target Developer Machines**: The Hacker News - https://thehackernews.com/2026/07/sleepergem-uses-three-malicious.html
- **Critical NGINX Vulnerability Can Crash Workers and May Allow Remote Code Execution**: The Hacker News - https://thehackernews.com/2026/07/critical-nginx-vulnerability-can-crash.html
- **Hackers abuse ViPNet software to target Russian govt agencies**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/hackers-abuse-vipnet-software-to-target-russian-govt-agencies/
- **UAC-0145 Uses ClickFix CAPTCHAs to Infect Ukrainian Devices wih Malware**: The Hacker News - https://thehackernews.com/2026/07/uac-0145-uses-clickfix-captchas-to.html
- **SonicWall SMA Zero-Days Exploited Before Disclosure to Gain Root Access**: The Hacker News - https://thehackernews.com/2026/07/sonicwall-sma-zero-days-exploited.html
- **Update now: 7-Zip fixes RCE flaw exploitable with malicious archives**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/update-now-7-zip-fixes-rce-flaw-exploitable-with-malicious-archives/
- **WordPress Core "wp2shell" RCE flaws get public exploits, patch now**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/wordpress-core-wp2shell-rce-flaws-get-public-exploits-patch-now/
- **Microsoft warns of surge in ACR Stealer attacks on customers**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/microsoft-warns-of-surge-in-acr-stealer-attacks-on-customers/
- **The Future of Age Verification: Your Face Never Leaves Your Device**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/the-future-of-age-verification-your-face-never-leaves-your-device/
- **New wp2shell WordPress Core Flaw Lets Unauthenticated Attackers Run Code**: The Hacker News - https://thehackernews.com/2026/07/new-wp2shell-wordpress-core-flaw-lets.html
- **Abbott probes two cyber incidents amid extortion claims**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/abbott-laboratories-probes-two-cyber-incidents-amid-extortion-claims/
- **OpenSSL HollowByte Flaw Could Freeze Server Memory with 11-Byte TLS Requests**: The Hacker News - https://thehackernews.com/2026/07/openssl-hollowbyte-flaw-could-freeze.html
- **Inc Ransomware Exploits SonicWall SMA Zero-Days**: Dark Reading - https://www.darkreading.com/vulnerabilities-threats/inc-ransomware-exploits-sonicwall-sma-zero-days
- **Seven Malicious Vite npm Packages Use Blockchain C2 to Deliver a RAT**: The Hacker News - https://thehackernews.com/2026/07/seven-malicious-vite-npm-packages-use.html
- **HollowByte DDoS flaw bloats OpenSSL server memory with 11-byte payload**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/hollowbyte-ddos-flaw-bloats-openssl-server-memory-with-11-byte-payload/
- **New NadMesh Botnet Hunts Exposed AI Services for Cloud Keys and Kubernetes Tokens**: The Hacker News - https://thehackernews.com/2026/07/new-nadmesh-botnet-hunts-exposed-ai.html
- **The Real AI Threat Is Blind Trust**: Dark Reading - https://www.darkreading.com/application-security/real-ai-threat-blind-trust
- **GoldenEyeDog Subgroup Linked to DigiCert Breach and Code-Signing Certificate Theft**: The Hacker News - https://thehackernews.com/2026/07/goldeneyedog-subgroup-linked-to.html
