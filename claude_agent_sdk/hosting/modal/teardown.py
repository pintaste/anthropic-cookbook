"""Stop all sandboxes for this app and delete the sessions volume.

Run when you're done with the cookbook so you aren't billed for idle resources::

    python hosting/modal/teardown.py
"""

from __future__ import annotations

import modal

# Inlined (not imported from modal_app) so teardown doesn't trigger an image
# build as an import-time side effect.
APP_NAME = "research-agent-hosting"
VOLUME_NAME = "research-agent-sessions"


def main() -> None:
    app = modal.App.lookup(APP_NAME, create_if_missing=False)
    for sandbox in modal.Sandbox.list(app_id=app.app_id):
        print(f"terminating sandbox {sandbox.object_id}")
        sandbox.terminate()

    try:
        modal.Volume.delete(VOLUME_NAME)
        print(f"deleted volume {VOLUME_NAME}")
    except modal.exception.NotFoundError:
        pass


if __name__ == "__main__":
    main()
