# Copyright (C) 2026 Eduard Grebe Consulting (Pty) Ltd
# SPDX-License-Identifier: GPL-3.0-or-later

"""
Headless tests for the terms-of-use gate and privacy-related app behaviour.
"""

from __future__ import annotations

import logging
from pathlib import Path

import pandas as pd
from streamlit.testing.v1 import AppTest

APP = str(Path(__file__).parent.parent / "app.py")


def _app() -> AppTest:
    at = AppTest.from_file(APP, default_timeout=30)
    at.run()
    return at


def _accept(at: AppTest) -> AppTest:
    at.button(key="terms_yes").click().run()
    return at


def test_terms_shown_and_app_hidden_before_acceptance():
    at = _app()
    assert not at.exception
    assert any("Do you accept these terms?" in m.value for m in at.markdown)
    assert any("random offset" in m.value for m in at.markdown)
    # Nothing that accepts data is rendered until terms are accepted
    assert len(at.get("file_uploader")) == 0
    assert "terms_accepted" not in at.session_state


def test_accept_proceeds_to_upload():
    at = _accept(_app())
    assert not at.exception
    assert at.session_state["terms_accepted"] is True
    assert len(at.get("file_uploader")) == 1
    assert "terms_yes" not in [b.key for b in at.button]
    assert not any("Do you accept these terms?" in m.value for m in at.markdown)


def test_decline_blocks_use():
    at = _app()
    at.button(key="terms_no").click().run()
    assert not at.exception
    assert at.session_state["terms_accepted"] is False
    assert [e.value for e in at.error] == ["You cannot use this tool."]
    assert len(at.get("file_uploader")) == 0
    # Declining persists for the session
    at.run()
    assert [e.value for e in at.error] == ["You cannot use this tool."]
    assert len(at.get("file_uploader")) == 0


def test_start_over_clears_data_but_keeps_acceptance():
    at = _accept(_app())
    at.session_state["step"] = 5
    at.session_state["filename"] = "upload.csv"
    at.session_state["results"] = pd.DataFrame({"Participant": ["P-SECRET"]})
    at.run()
    at.button[-1].click().run()  # "← Start over"
    assert not at.exception
    assert at.session_state["terms_accepted"] is True
    assert at.session_state["step"] == 1
    assert at.session_state["results"] is None
    assert at.session_state["filename"] == ""


def test_unexpected_error_hides_details(caplog):
    at = _accept(_app())
    # Step 2 without uploaded data raises inside the app
    at.session_state["step"] = 2
    at.session_state["df"] = pd.DataFrame({"Participant": ["P-SECRET"]})
    with caplog.at_level(logging.ERROR, logger="infection_dating_tool"):
        at.run()
    assert not at.exception
    assert len(at.error) == 1
    assert "Something went wrong" in at.error[0].value
    assert "P-SECRET" not in at.error[0].value
    assert "Test" not in at.error[0].value  # the KeyError message
    logged = [r.getMessage() for r in caplog.records if r.name == "infection_dating_tool"]
    assert logged == ["Unhandled error in step 2: KeyError"]
    assert at.button(key="error_start_over")
