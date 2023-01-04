from rich.console import Console

from src.utils.shared.misc.uinput import uinput


def tp_repo_install(console: Console) -> tuple[list[list[str]], list[str]]:
    """Install third party repositories.

    Args:
        log -- instance of Logger
        console -- instance of Console
    """

    tp_repo: dict[int, dict[str, str]] = {
            # id and name of the repo and the address
            1: {
                    "name": "RPMFusion (Free)",
                    "desc": "Fedora repository for open source softwares.",
                    "address": (
                            r"https://mirrors.rpmfusion.org/"
                            r"free/fedora/rpmfusion-free-release"
                            r"-$(rpm -E %fedora).noarch.rpm"
                        )
                },
            2: {
                    "name": "RPMFusion (Non-free)",
                    "desc": "Fedora repository for propietary software.",
                    "address": (
                            r"https://mirrors.rpmfusion.org/"
                            r"nonfree/fedora/rpmfusion-nonfree"
                            r"-release-$(rpm -E %fedora).noarch.rpm"
                        )
                },
            3: {
                    "name": "Flathub",
                    "desc": "Unfiltered repository for flatpaks.",
                    "address": "https://flathub.org/repo/flathub.flatpakrepo"
                },
            4: {
                    "name": "Fedora OCI",
                    "desc": "", #? what's this for?,
                    "address": "oci+https://registry.fedoraproject.org"
                },
            5: {
                    "name": "KDE",
                    "desc": "KDE Applications.",
                    "address": (
                            "https://distribute.kde.org/kdeapps.flatpakrepo"
                        )
                },
            6: {
                    "name": "GNOME Nightly",
                    "desc": "For cutting edge builds from GNOME.",
                    "address": (
                            "https://nightly.gnome.org/"
                            "gnome-nightly.flatpakrepo"
                        )
                }
        }

    t_fcmd: list[list[str]] = []
    t_rfusion_install_arr: list[str] = []

    for repo in tp_repo.values():
        if uinput(
                console, f"Install {repo.get('name')} ({repo.get('desc')})", 1
            ):
            if repo.get("name") == "flathub":
                t_fcmd.append(
                    (
                        "flatpak remote-add --if-not-exists flathub "
                        "https://flathub.org/repo/flathub.flatpakrepo"
                    )
                )
                continue
            t_rfusion_install_arr.append(repo.get("address"))

    return t_fcmd, t_rfusion_install_arr
