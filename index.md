# Exploitation Report

Critical exploitation activity is currently targeting enterprise systems with multiple zero-day vulnerabilities being actively exploited in the wild. The most significant threat involves a command injection vulnerability in SAP S/4HANA ERP software (CVE-2025-42957) that is being actively exploited by threat actors. Additionally, a zero-day vulnerability in legacy Sitecore deployments is being weaponized to deploy WeepSteel reconnaissance malware and backdoors. These attacks demonstrate sophisticated threat actor capabilities, with campaigns leveraging advanced techniques including SVG-based phishing, ViewState exploitation, and cloud infrastructure abuse to evade detection while maintaining persistent access to compromised systems.

## Active Exploitation Details

### SAP S/4HANA Command Injection Vulnerability
- **Description**: A critical command injection vulnerability affecting SAP S/4HANA Enterprise Resource Planning (ERP) software
- **Impact**: Allows attackers to execute arbitrary commands on affected systems, potentially leading to complete system compromise
- **Status**: Currently being actively exploited in the wild
- **CVE ID**: CVE-2025-42957

### Sitecore Zero-Day Vulnerability
- **Description**: A zero-day vulnerability in legacy Sitecore deployments being exploited through ViewState attacks
- **Impact**: Enables threat actors to deploy WeepSteel reconnaissance malware and establish backdoors for persistent access
- **Status**: Active exploitation ongoing with weaponized ASP.NET machine keys for remote injection and deserialization attacks

### SVG-Based Phishing Campaign
- **Description**: Malware campaign leveraging Scalable Vector Graphics (SVG) files to deploy Base64-encoded phishing pages
- **Impact**: Bypasses traditional security detection mechanisms while impersonating legitimate organizations like the Colombian judicial system
- **Status**: 44 undetected SVG files identified by VirusTotal, indicating active campaign

## Affected Systems and Products

- **SAP S/4HANA**: Enterprise Resource Planning software vulnerable to command injection attacks
- **Legacy Sitecore Deployments**: Content management systems susceptible to ViewState exploitation and backdoor deployment
- **ASP.NET Applications**: Systems with exposed machine keys vulnerable to remote injection and deserialization attacks
- **Web Applications**: Sites using SVG file processing vulnerable to phishing payload delivery
- **Cloud Infrastructure**: Google and Cloudflare services being abused by phishing-as-a-service operations

## Attack Vectors and Techniques

- **Command Injection**: Direct exploitation of input validation flaws in SAP S/4HANA systems
- **ViewState Exploitation**: Weaponization of exposed ASP.NET machine keys for remote code execution
- **SVG File Abuse**: Using Scalable Vector Graphics files to embed and deliver Base64-encoded phishing content
- **Cloud Infrastructure Abuse**: Leveraging legitimate cloud services to host and distribute malicious content while evading detection
- **Cloaking Techniques**: Advanced evasion methods used by phishing-as-a-service operations to remain undetected for extended periods

## Threat Actor Activities

- **WeepSteel Operators**: Deploying reconnaissance malware through Sitecore zero-day exploitation to establish persistent backdoors
- **GhostRedirector**: Chinese threat actor using malicious IIS modules to inject links and artificially boost search engine rankings for gambling sites
- **Colombian Judicial Impersonators**: Threat actors conducting targeted phishing campaigns using SVG files to impersonate government institutions
- **Phishing-as-a-Service Enterprise**: Global operation running undetected on major cloud platforms for over 3 years, providing phishing infrastructure to multiple threat actors
- **ViewState Exploitation Groups**: Threat actors specifically targeting ASP.NET applications with exposed machine keys for remote injection attacks