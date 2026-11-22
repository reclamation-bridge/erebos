# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (C) 2026 Jerry Jackson
"""Optional isolation backends behind one IsolationBackend interface.

Planned: base (interface plus a no-op backend), landlock ([landlock] extra, Linux only;
falls back to the no-op backend when the kernel lacks Landlock). Core never requires one.
"""
