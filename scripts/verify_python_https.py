"""Check the selected CI Python's verified HTTPS support without network I/O."""

import importlib
import sys


def fail(category: str, error: Exception | None = None) -> int:
    kind = f" ({type(error).__name__})" if error is not None else ""
    # Loader/context errors can contain paths or environment-dependent text.
    print(f"Python HTTPS preflight failed: {category}{kind}", file=sys.stderr)
    return 1


def main() -> int:
    try:
        ssl = importlib.import_module("ssl")
    except (ImportError, OSError) as error:
        return fail("ssl_import_failed", error)
    try:
        context = ssl.create_default_context()
    except (OSError, ValueError) as error:
        return fail("tls_context_failed", error)
    if context.verify_mode != ssl.CERT_REQUIRED or not context.check_hostname:
        return fail("tls_verification_disabled")
    try:
        request = importlib.import_module("urllib.request")
        handler = getattr(request, "HTTPSHandler", None)
        if handler is None:
            return fail("https_handler_missing")
        handler(context=context)
    except (ImportError, OSError, ValueError) as error:
        return fail("https_handler_failed", error)
    print(
        f"Python HTTPS preflight passed: Python {sys.version.split()[0]}; "
        f"{ssl.OPENSSL_VERSION}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
