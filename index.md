# Exploitation Report

Current threat activity reveals several critical exploitation campaigns targeting enterprise systems and consumer platforms. The most significant development involves a zero-day vulnerability in Sitecore content management systems being actively exploited to deploy WeepSteel reconnaissance malware and backdoors. Additionally, Russian state-sponsored group APT28 has deployed a new Microsoft Outlook backdoor called "NotDoor" against NATO country organizations, while threat actors are leveraging SVG files and ASP.NET ViewState vulnerabilities for sophisticated phishing campaigns. A new Chinese threat group "GhostRedirector" is manipulating search engine rankings through malicious IIS modules, and a global phishing-as-a-service operation has been operating undetected on major cloud platforms for over three years.

## Active Exploitation Details

### Sitecore Zero-Day Vulnerability
- **Description**: A zero-day vulnerability in legacy Sitecore content management system deployments that allows remote code execution through exposed ASP.NET machine keys
- **Impact**: Attackers can deploy backdoors, reconnaissance malware (WeepSteel), and perform remote injection and deserialization attacks
- **Status**: Actively exploited in the wild, represents the latest example of ViewState-based attacks

### NotDoor Outlook Backdoor
- **Description**: A sophisticated Microsoft Outlook backdoor developed and deployed by Russian APT28 group
- **Impact**: Provides persistent access to corporate email systems and enables data exfiltration from targeted organizations
- **Status**: Active deployment against multiple companies in NATO countries across different sectors

### SVG-Based Phishing Campaign
- **Description**: Malware campaign leveraging Scalable Vector Graphics (SVG) files containing Base64-encoded phishing pages
- **Impact**: Bypasses traditional security detection with 44 undetected SVG files impersonating Colombian judicial system
- **Status**: Active campaign with files remaining undetected by security solutions

## Affected Systems and Products

- **Sitecore CMS**: Legacy deployments with exposed ASP.NET machine keys vulnerable to ViewState attacks
- **Microsoft Outlook**: Corporate installations targeted by APT28's NotDoor backdoor
- **ASP.NET Applications**: Systems with exposed machine keys susceptible to deserialization attacks
- **Web Browsers**: Users targeted by SVG-based phishing campaigns impersonating government entities
- **IIS Web Servers**: Compromised with malicious modules for search engine manipulation
- **Google Cloud Platform**: Hosting infrastructure for undetected phishing-as-a-service operations
- **Cloudflare Services**: Leveraged by global phishing empire using cloaking techniques

## Attack Vectors and Techniques

- **ViewState Exploitation**: Weaponizing exposed ASP.NET machine keys for remote injection and deserialization attacks
- **Email System Compromise**: Deploying backdoors directly into Microsoft Outlook for persistent access
- **SVG File Abuse**: Using scalable vector graphics files to deliver Base64-encoded phishing content
- **Search Engine Manipulation**: Injecting malicious links through compromised IIS modules to boost gambling site rankings
- **Cloud Infrastructure Abuse**: Operating phishing-as-a-service platforms on legitimate cloud providers
- **Cloaking Techniques**: Employing sophisticated methods to avoid detection while running on public cloud infrastructure

## Threat Actor Activities

- **APT28 (Russian State-Sponsored)**: Actively deploying NotDoor Outlook backdoors against NATO country organizations across multiple sectors, demonstrating continued focus on intelligence gathering operations
- **GhostRedirector (Chinese Group)**: New threat actor manipulating Google search rankings using malicious IIS modules to artificially boost gambling websites
- **Colombian Judicial Impersonators**: Threat actors conducting targeted phishing campaigns using SVG files to impersonate government judicial systems
- **Global Phishing-as-a-Service Operators**: Sophisticated criminal enterprise operating undetected on Google and Cloudflare infrastructure for over three years, providing phishing services at scale