from src.models.track import Track


def get_selected_track(user_id: str | None) -> Track | None:
    # Explicitly validate user_id to ensure it is not None and is a string before invoking string methods.
    if user_id is None or not isinstance(user_id, str):
        return None
    if user_id.endswith("3"):
        return None
    return Track(title="Skyline", artist="Sample Artist")
