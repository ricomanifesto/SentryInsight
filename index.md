# Exploitation Report

The last week saw a sharp uptick in in-the-wild exploitation of both web-facing and client-side vulnerabilities. Attackers weaponised a fresh Google Chrome zero-day to execute code on fully-patched desktops, hijacked thousands of WordPress sites through a critical flaw in the popular “Motors” theme, and abused a supply-chain compromise at CoinMarketCap to drain visitors’ crypto wallets. Simultaneously, Russian state-aligned actors bypassed Gmail multi-factor authentication by leveraging stolen app-specific passwords, while threat groups used the HTTP/2 Rapid Reset technique to launch the largest recorded 7.3 Tbps DDoS assault. Google also disclosed active attempts to perform indirect prompt injections against its GenAI services, prompting the rollout of new layered defences. The combined activity underscores a diverse and rapidly evolving exploit landscape that spans browsers, CMS add-ons, AI platforms, and core Internet protocols.

## Active Exploitation Details

### Google Chrome 0-Day in V8 JavaScript Engine
- **Description**: A previously unknown flaw in Chrome’s V8 engine that allows type confusion leading to arbitrary code execution when victims browse malicious web pages.  
- **Impact**: Full remote code execution in the context of the logged-in user, enabling follow-on credential theft or malware deployment.  
- **Status**: Confirmed exploited in the wild; Google released an emergency stable-channel update.  

### WordPress “Motors” Theme Privilege Escalation Flaw
- **Description**: An input-validation bug in the theme’s unauthenticated AJAX endpoints permits attackers to create new administrator accounts.  
- **Impact**: Complete takeover of affected WordPress sites, defacement, malware injection, or deployment of phishing pages.  
- **Status**: Patch available from the theme vendor; mass exploitation campaigns are ongoing against unpatched sites.  

### Supply-Chain Injection on CoinMarketCap Website
- **Description**: Attackers compromised a third-party script and injected malicious JavaScript that presented visitors with a fake Web3 wallet-connect popup linked to a drainer smart contract.  
- **Impact**: Automatic approval of malicious transactions, resulting in theft of users’ cryptocurrency holdings.  
- **Status**: Attack window lasted several hours before takedown; no software patch required, but users must revoke tainted wallet permissions.  

### Gmail MFA Bypass via App-Specific Password Abuse
- **Description**: Russian operators obtained app-specific passwords through credential phishing, then used them to log in via legacy IMAP/POP interfaces that do not enforce modern MFA challenges.  
- **Impact**: Full access to Gmail mailboxes, facilitating espionage, internal reconnaissance, and further social-engineering.  
- **Status**: Technique remains viable; Google urges administrators to disable app passwords and enforce OAuth-based access controls.  

### Indirect Prompt Injection Against Generative AI Models
- **Description**: Adversaries embed hidden instructions in user-supplied or third-party content, forcing GenAI chatbots to reveal confidential data or execute unintended actions.  
- **Impact**: Data leakage, reputational damage, and potential compliance violations.  
- **Status**: Google confirmed active probing; introduced multi-layered guardrails including input/output filters and adversarial testing.  

### HTTP/2 Rapid Reset Exploited for Record 7.3 Tbps DDoS
- **Description**: Attackers abuse the HTTP/2 protocol feature allowing rapid stream cancellation to generate massive request bursts with minimal resources.  
- **Impact**: Network exhaustion and service disruption at terabit scale against hosting providers and their downstream customers.  
- **Status**: Actively weaponised; mitigations deployed by major CDNs, but origin servers remain at risk if rate-limits are absent.  

## Affected Systems and Products

- **Google Chrome (Stable Channel)**: Windows, macOS, Linux prior to latest emergency patch  
- **WordPress with “Motors” Theme**: All sites running vulnerable theme versions on any hosting platform  
- **CoinMarketCap Website Visitors**: Browsers on desktop and mobile interacting with Web3 wallets (MetaMask, Trust Wallet, etc.)  
- **Gmail / Google Workspace Accounts**: All platforms where legacy IMAP/POP or SMTP app-specific passwords are enabled  
- **Google GenAI Services**: Gemini, Vertex AI, and associated enterprise integrations  
- **HTTP/2-Enabled Web Servers & CDNs**: Linux/UNIX and Windows infrastructures serving HTTP/2 traffic  

## Attack Vectors and Techniques

- **Type-Confusion RCE**  
  - **Vector**: Malicious JavaScript delivered via compromised or attacker-controlled websites triggers V8 memory corruption.  

- **Unauthenticated AJAX Privilege Escalation**  
  - **Vector**: Crafted HTTP POST requests to vulnerable Motors theme endpoints create admin users.  

- **Supply-Chain JavaScript Injection**  
  - **Vector**: Compromised third-party script on CoinMarketCap inserts rogue code that spawns deceptive wallet-connect popups.  

- **App-Specific Password Phishing**  
  - **Vector**: Spear-phishing emails impersonating U.S. State Department harvest passwords that bypass MFA over legacy protocols.  

- **Indirect Prompt Injection**  
  - **Vector**: Hidden instructions embedded in PDFs, web pages, or chat context manipulate AI model behaviour.  

- **HTTP/2 Rapid Reset Flooding**  
  - **Vector**: Automation repeatedly opens and cancels thousands of HTTP/2 streams to amplify traffic volume.  

## Threat Actor Activities

- **Unknown Exploit Broker**  
  - **Campaign**: Distributing Chrome 0-day to multiple crimeware groups for drive-by download campaigns.  

- **Mass WordPress Botnet Operators**  
  - **Campaign**: Automated scanning of WordPress installs to exploit the Motors theme flaw, followed by SEO spam and credential phishing.  

- **Unattributed Supply-Chain Intrusion Group**  
  - **Campaign**: Brief compromise of CoinMarketCap infrastructure to seed wallet drainer; focus on high-net-worth crypto holders.  

- **Russian State-Aligned Hackers**  
  - **Campaign**: Targeting government, think-tank, and media Gmail accounts; leveraging MFA bypass to maintain persistent access.  

- **DDoS-as-a-Service Crews**  
  - **Campaign**: Monetising HTTP/2 Rapid Reset exploits to offer “record-size” booter services, demonstrated by 7.3 Tbps attack on hosting provider.  

- **Lazarus Group (Contextual Activity)**  
  - **Campaign**: $11 million BitoPro crypto theft; highlights continuing focus on financial targets, though not tied to specific vulnerability in this cycle.  

- **Scattered Spider**  
  - **Campaign**: Social-engineering-driven intrusions into UK retailers and US insurers leveraging SIM-swap and insider recruitment tactics.  

**Bold vigilance and rapid patching are essential as attackers combine zero-days, supply-chain compromise, and protocol abuse to broaden their reach across industries.**