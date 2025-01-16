import json
import os
import shutil


def unpack_assets():
    asset_dir = None
    # get value of $GRADLE_USER_HOME
    gradle_user_home = os.environ.get("GRADLE_USER_HOME")
    if gradle_user_home is not None:
        # $GRADLE_USER_HOME exists:
        asset_dir = os.path.join(gradle_user_home, "caches", "forge_gradle", "assets")
    else:
        # using default path
        asset_dir = os.path.join(
            os.path.expanduser("~"), ".gradle", "caches", "forge_gradle", "assets"
        )
    output_dir = os.path.join(
        os.path.abspath(os.path.dirname(__file__)),
        "minerl",
        "MCP-Reborn",
        "src",
        "main",
        "resources",
    )
    index = load_asset_index(os.path.join(asset_dir, "indexes", "1.16.json"))
    unpack_assets_impl(index, asset_dir, output_dir)


def load_asset_index(index_file):
    with open(index_file) as f:
        return json.load(f)


def unpack_assets_impl(index, asset_dir, output_dir):
    for k, v in index["objects"].items():
        asset_hash = v["hash"]
        src = os.path.join(asset_dir, "objects", asset_hash[:2], asset_hash)
        dst = os.path.join(output_dir, k)
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        print(src, dst)
        shutil.copy(src, dst)


unpack_assets()
print("DONE")
