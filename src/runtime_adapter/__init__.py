"""Opt-in durable execution adapter for one frozen report-preparation job.

The legacy workflow (``main.py`` and ``src.core.workflow``) is unchanged. This
package runs the existing analysis, validators and site builder under a durable
Runtime lease, with a product-owned send gate that bounds and records every
provider submission. Only synthetic fakes are wired in this slice.
"""
