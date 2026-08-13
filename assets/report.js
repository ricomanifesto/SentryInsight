(() => {
  const root = document.documentElement;
  const themeToggle = document.getElementById("theme-toggle");
  const metadataElement = document.getElementById("report-metadata");
  const copyToast = document.getElementById("copy-toast");

  const labels = {
    severity: {
      critical: "Critical",
      high: "High",
      medium: "Medium",
      low: "Low",
      unknown: "Severity unknown",
    },
    exploitation_status: {
      active: "Active exploitation",
      observed: "Observed",
      potential: "Potential",
      not_observed: "Not observed",
      unknown: "Status unknown",
    },
    action: {
      patch: "Patch",
      mitigate: "Mitigate",
      investigate: "Investigate",
      monitor: "Monitor",
      none: "No action listed",
    },
  };

  function readMetadata() {
    if (!metadataElement) return { findings: [] };
    try {
      return JSON.parse(metadataElement.textContent || "{}");
    } catch {
      return { findings: [] };
    }
  }

  function storedTheme() {
    try {
      return localStorage.getItem("sentryinsight-theme");
    } catch {
      return null;
    }
  }

  function saveTheme(theme) {
    try {
      localStorage.setItem("sentryinsight-theme", theme);
    } catch {
      // The selected theme still applies for this page when storage is unavailable.
    }
  }

  function applyTheme(theme) {
    root.dataset.theme = theme;
    if (themeToggle) {
      themeToggle.setAttribute("aria-pressed", String(theme === "dark"));
      themeToggle.textContent = theme === "dark" ? "Light theme" : "Dark theme";
    }
  }

  function showCopyToast(message) {
    if (!copyToast) return;
    copyToast.textContent = message;
    copyToast.hidden = false;
    window.setTimeout(() => {
      copyToast.hidden = true;
    }, 1800);
  }

  async function copyHeadingLink(headingId) {
    const url = `${window.location.origin}${window.location.pathname}#${headingId}`;
    history.replaceState(null, "", `#${headingId}`);
    try {
      await navigator.clipboard.writeText(url);
    } catch {
      // The visible URL and status still make the action useful without clipboard access.
    }
    showCopyToast("Link copied");
  }

  function createBadge(dimension, value) {
    const badge = document.createElement("span");
    badge.className = `badge badge-${dimension.replace("_", "-")}`;
    badge.dataset.value = value;
    badge.textContent = labels[dimension]?.[value] || value;
    return badge;
  }

  function enhanceFinding(heading, finding) {
    const title = heading.textContent.trim();
    const body = document.createElement("div");
    body.id = `${heading.id}-details`;
    body.className = "finding-body";

    const contentNodes = [];
    let next = heading.nextSibling;
    while (
      next &&
      !(next.nodeType === Node.ELEMENT_NODE && ["H2", "H3"].includes(next.tagName))
    ) {
      contentNodes.push(next);
      next = next.nextSibling;
    }
    heading.after(body);
    contentNodes.forEach((node) => body.appendChild(node));

    heading.textContent = "";
    heading.classList.add("finding-heading");
    heading.dataset.expanded = "true";

    const disclosure = document.createElement("button");
    disclosure.type = "button";
    disclosure.className = "finding-disclosure";
    disclosure.setAttribute("aria-expanded", "true");
    disclosure.setAttribute("aria-controls", body.id);
    const titleElement = document.createElement("span");
    titleElement.className = "finding-title";
    titleElement.textContent = title;
    const icon = document.createElement("span");
    icon.className = "disclosure-icon";
    icon.setAttribute("aria-hidden", "true");
    icon.textContent = "−";
    disclosure.append(titleElement, icon);

    const supporting = document.createElement("span");
    supporting.className = "finding-supporting";
    const badges = document.createElement("span");
    badges.className = "badge-list";
    badges.setAttribute("aria-label", "Finding classification");
    badges.append(
      createBadge("severity", finding.severity),
      createBadge("exploitation_status", finding.exploitation_status),
      createBadge("action", finding.action),
    );
    supporting.appendChild(badges);

    const cves = document.createElement("span");
    cves.className = "cve-list";
    for (const cve of finding.cve_ids || []) {
      const link = document.createElement("a");
      link.className = "cve-chip";
      link.href = `https://nvd.nist.gov/vuln/detail/${encodeURIComponent(cve)}`;
      link.target = "_blank";
      link.rel = "noopener noreferrer";
      link.textContent = cve;
      cves.appendChild(link);
    }
    if (cves.childElementCount) supporting.appendChild(cves);

    const anchor = document.createElement("a");
    anchor.className = "heading-anchor";
    anchor.href = `#${heading.id}`;
    anchor.setAttribute("aria-label", `Copy link to ${title}`);
    anchor.textContent = "#";
    anchor.addEventListener("click", (event) => {
      event.preventDefault();
      copyHeadingLink(heading.id);
    });
    supporting.appendChild(anchor);
    heading.append(disclosure, supporting);

    disclosure.addEventListener("click", () => {
      const expanded = disclosure.getAttribute("aria-expanded") === "true";
      disclosure.setAttribute("aria-expanded", String(!expanded));
      heading.dataset.expanded = String(!expanded);
      body.hidden = expanded;
      icon.textContent = expanded ? "+" : "−";
    });
  }

  function enhanceFindings(metadata) {
    const findings = new Map(
      (metadata.findings || []).map((finding) => [finding.slug, finding]),
    );
    for (const heading of document.querySelectorAll("h3[data-severity]")) {
      const finding = findings.get(heading.id);
      if (finding) enhanceFinding(heading, finding);
    }
  }

  function enhanceExecutiveSummary() {
    const heading = document.getElementById("executive-summary");
    if (!heading) return;
    const card = document.createElement("section");
    card.className = "executive-summary-card";
    card.setAttribute("aria-labelledby", heading.id);
    const contentNodes = [heading];
    let next = heading.nextSibling;
    while (
      next &&
      !(next.nodeType === Node.ELEMENT_NODE && next.tagName === "H2")
    ) {
      contentNodes.push(next);
      next = next.nextSibling;
    }
    heading.before(card);
    contentNodes.forEach((node) => card.appendChild(node));
  }

  function sanitizeReportContent() {
    const content = document.getElementById("report-content");
    if (!content) return;
    if (!window.DOMPurify) {
      throw new Error("Bundled report sanitizer did not load");
    }
    content.innerHTML = window.DOMPurify.sanitize(content.innerHTML, {
      USE_PROFILES: { html: true },
      ALLOW_DATA_ATTR: true,
    });
  }

  function renderAge(metadata) {
    const ageElement = document.getElementById("report-age");
    if (!ageElement || !metadata.generated_at) return;
    const generatedAt = new Date(metadata.generated_at);
    const elapsedMinutes = Math.max(
      0,
      Math.floor((Date.now() - generatedAt.getTime()) / 60000),
    );
    let age = "updated just now";
    if (elapsedMinutes >= 1440) age = `updated ${Math.floor(elapsedMinutes / 1440)}d ago`;
    else if (elapsedMinutes >= 60) age = `updated ${Math.floor(elapsedMinutes / 60)}h ago`;
    else if (elapsedMinutes >= 1) age = `updated ${elapsedMinutes}m ago`;
    ageElement.textContent = ` · ${age}`;
  }

  function setupScrollSpy() {
    if (!("IntersectionObserver" in window)) return;
    const links = [...document.querySelectorAll('nav[aria-label="Report sections"] a')];
    const linksById = new Map();
    for (const link of links) {
      const id = decodeURIComponent(link.hash.slice(1));
      const matching = linksById.get(id) || [];
      matching.push(link);
      linksById.set(id, matching);
    }
    const setCurrent = (id) => {
      links.forEach((link) => link.removeAttribute("aria-current"));
      (linksById.get(id) || []).forEach((link) =>
        link.setAttribute("aria-current", "location"),
      );
    };
    const observer = new IntersectionObserver(
      (entries) => {
        const visible = entries
          .filter((entry) => entry.isIntersecting)
          .sort((left, right) => left.boundingClientRect.top - right.boundingClientRect.top);
        if (visible[0]) setCurrent(visible[0].target.id);
      },
      { rootMargin: "0px 0px -72% 0px", threshold: 0 },
    );
    linksById.forEach((_value, id) => {
      const heading = document.getElementById(id);
      if (heading) observer.observe(heading);
    });
  }

  const metadata = readMetadata();
  const preferredDark = window.matchMedia("(prefers-color-scheme: dark)").matches;
  applyTheme(storedTheme() || (preferredDark ? "dark" : "light"));
  themeToggle?.addEventListener("click", () => {
    const nextTheme = root.dataset.theme === "dark" ? "light" : "dark";
    saveTheme(nextTheme);
    applyTheme(nextTheme);
  });
  sanitizeReportContent();
  enhanceExecutiveSummary();
  enhanceFindings(metadata);
  renderAge(metadata);
  setupScrollSpy();
})();
