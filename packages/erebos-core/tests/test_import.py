# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (C) 2026 Jerry Jackson
"""Skeleton smoke test: the package and its planned subpackages import."""

import importlib
import sys

import erebos_core


def test_version():
    assert erebos_core.__version__ == "0.0.1.dev0"


def test_subpackages_import():
    for name in (
        "erebos_core.providers",
        "erebos_core.tools",
        "erebos_core.tools.isolation",
        "erebos_core.events",
        "erebos_core.hooks",
    ):
        importlib.import_module(name)


def test_no_ui_dependency():
    """Core must never pull in GTK."""
    assert "gi" not in sys.modules
