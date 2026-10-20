# Kerbal Konstructs: the rest of the group editor

Part of [Terrain Precision Fix](../../../../README.md), [the statics](../../README.md#work-in-progress): one point of the work in progress, on Kerbal Konstructs.

**Status: planned.** Moving a group with the gizmo of the group editor, in flight beside a craft, is
checked, and needs a patch of this mod: [The group editor](../../limits/kerbal-konstructs/the-group-editor.md).
The rest of the editor, read in the source, goes through latitudes, longitudes and positions relative
to the group's own `PQSCity`, which mean the same thing wherever the group hangs; it has not been played.

*To test:* in flight, near a craft, on the save of the group editor
([`non-reg-runway-mune-kk.sfs`](../../../../diag/statics/limits/kerbal-konstructs/the-group-editor/non-reg-runway-mune-kk.sfs)): turning a group,
creating one, copying one and deleting one, each saved, then the save loaded again. If this mod broke
something there, a group would turn or appear somewhere else than the editor shows, or come back
elsewhere once the save is loaded again.
